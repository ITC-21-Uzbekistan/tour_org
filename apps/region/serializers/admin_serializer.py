import traceback

from rest_framework.serializers import ModelSerializer, SerializerMethodField, raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from apps.region.models import ContentRegion, Region


class ContentRegionSerializer(ModelSerializer):
    class Meta:
        model = ContentRegion
        fields = "__all__"


class RegionSerializerWithContent(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Region
        fields = (
            'id',
            'region_name',
            'region_url',
            'region_meta_keywords',
            'country',
            'created_at',
            'created_by',
            'region_images',
            'contents',
        )

    def create(self, validated_data):
        raise_errors_on_nested_writes('create', self, validated_data)

        ModelClass = self.Meta.model

        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        try:
            instance = ModelClass._default_manager.create(**validated_data, created_by=self.context.get('created_by'))
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                    'Got a `TypeError` when calling `%s.%s.create()`. '
                    'This may be because you have a writable field on the '
                    'serializer class that is not a valid argument to '
                    '`%s.%s.create()`. You may need to make the field '
                    'read-only, or override the %s.create() method to handle '
                    'this correctly.\nOriginal exception was:\n %s' %
                    (
                        ModelClass.__name__,
                        ModelClass._default_manager.name,
                        ModelClass.__name__,
                        ModelClass._default_manager.name,
                        self.__class__.__name__,
                        tb
                    )
            )
            raise TypeError(msg)

        # Save many-to-many relationships after the instance is created.
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.created_by = self.context.get('created_by')
        instance.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

    def _get_contents(self, region):
        contents = ContentRegion.objects.filter(region=region)
        return ContentRegionSerializer(contents, many=True)

from rest_framework.renderers import JSONRenderer
import orjson as json


class CommonResultRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if "ErrorDetail" in str(data):
            if 'code' in data:
                if "token_not_valid" == data['code']:
                    return json.dumps(
                        {
                            "success": False,
                            "message": "Token is invalid or expired",
                            "data": None
                        }
                    )
            elif "detail" in data:
                return json.dumps(
                    {
                        "success": False,
                        "message": data['detail'],
                        "data": None
                    }
                )
            else:
                return json.dumps(
                    {
                        "success": False,
                        "message": "Form has been filled incorrectly",
                        "data": data
                    }
                )
        else:
            return json.dumps(
                {
                    "success": True,
                    "message": "SUCCESS",
                    "data": data
                }
            )

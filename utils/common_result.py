class CommonResult:
    __success = None
    __status_code = None
    __message = None
    __data = None

    def __init__(self):
        self.__success = None
        self.__status_code = None
        self.__message = None
        self.__data = None

    def set_response(self, success, status_code, message, data=None):
        self.__success = success
        self.__status_code = status_code
        self.__message = message
        self.__data = data

    @property
    def get_response(self):
        return {
            'success': self.__success,
            'status_code': self.__status_code,
            'message': self.__message,
            'data': self.__data
        }
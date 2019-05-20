class Result(object):
    @staticmethod
    def success(code, message, data):
        return {'code': code, 'message': message, 'data': data}

    @staticmethod
    def error(code, message):
        return {'code': code, 'message': message}

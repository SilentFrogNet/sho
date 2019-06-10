class BaseCustomException(Exception):

    def __init__(self, message=None, errors=None, *args, **kwargs):
        super(BaseCustomException, self).__init__(message, errors, args, kwargs)
        self.message = message
        self.errors = errors

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.__repr__()


class InvalidParameterError(BaseCustomException):
    """ Not a valid parameter """

    def __init__(self, message=None, errors=None, params: list = None, *args, **kwargs) -> None:
        self.params = params or []
        if not message:
            message = "Invalid parameters error."
        super(InvalidParameterError, self).__init__(message, errors, args, kwargs)


class InconsistentParametersError(InvalidParameterError):
    """ Parameters are not consistent with them """

    def __init__(self, message=None, errors=None, params: list = None, *args, **kwargs) -> None:
        if not message:
            message = "Inconsistent parameters error."
        super(InconsistentParametersError, self).__init__(message, errors, params, args, kwargs)


class AlreadyExistingShellError(BaseCustomException):
    """ Already existing shell """

    def __init__(self, message=None, errors=None, *args, **kwargs):
        if not message:
            message = "Shell already exists."
        super(AlreadyExistingShellError, self).__init__(message, errors, args, kwargs)


class ShellNotFoundError(BaseCustomException):
    """ Shell not found """

    def __init__(self, message=None, errors=None, *args, **kwargs):
        if not message:
            message = "Shell not found."
        super(ShellNotFoundError, self).__init__(message, errors, args, kwargs)

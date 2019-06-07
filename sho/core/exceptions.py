class InvalidParameterError(Exception):
    """ Not a valid parameter """

    def __init__(self, params: list = None, *args, **kwargs) -> None:
        self.params = params or []
        super(InvalidParameterError, self).__init__(args, kwargs)


class InconsistentParametersError(InvalidParameterError):
    """ Parameters are not consistent with them """

    def __init__(self, params: list = None, *args, **kwargs) -> None:
        super(InconsistentParametersError, self).__init__(params, args, kwargs)


class AlreadyExistingShellError(Exception):
    """ Already existing shell """

    def __init__(self, *args, **kwargs):
        if 'message' not in kwargs:
            kwargs['message'] = "Shell already exists."
        super(AlreadyExistingShellError, self).__init__(args, kwargs)


class ShellNotFoundError(Exception):
    """ Shell not found """

    def __init__(self, *args, **kwargs):
        if 'message' not in kwargs:
            kwargs['message'] = "Shell not found"
        super(ShellNotFoundError, self).__init__(args, kwargs)

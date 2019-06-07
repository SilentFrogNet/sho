class ShoTypes(object):
    SSH = "ssh"
    LOCAL = "local"

    REMOTE_TYPES = [SSH]
    SUPPORTED_TYPES = [SSH, LOCAL]

    @classmethod
    def type_to_string(cls, value):
        idx = cls.SUPPORTED_TYPES.index(value)
        if idx >= 0:
            return cls.SUPPORTED_TYPES[idx]
        else:
            return None

    @classmethod
    def to_string(cls):
        return ", ".join(cls.SUPPORTED_TYPES)

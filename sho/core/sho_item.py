from sho.core.sho_types import ShoTypes
from sho.core.exceptions import InconsistentParametersError


class ShoItem(object):
    """ Describes a shell item """

    def __init__(self, name: str, shell_type: ShoTypes = None, description: str = None, host: str = None) -> None:
        self.name = name
        self.shell_type = shell_type if shell_type in ShoTypes.SUPPORTED_TYPES else ShoTypes.LOCAL
        self.description = description
        if host and self.shell_type not in ShoTypes.REMOTE_TYPES:
            raise InconsistentParametersError(params=[shell_type, host], message="host is not supported with a non-remote shell_type")
        self.host = host

    @property
    def type(self):
        return self.shell_type

    def __repr__(self):
        out_str = "<Shell {name} - {type}".format(
            name=self.name,
            type="{}".format(self.shell_type)
        )
        if self.shell_type in ShoTypes.REMOTE_TYPES:
            out_str += "({})".format(self.host)
        return out_str

    def __str__(self):
        return self.__repr__()

from sho.core.sho_types import ShoTypes
from sho.core.sho_item import ShoItem
from sho.core.exceptions import (
    AlreadyExistingShellError,
    ShellNotFoundError
)


class Sho:
    """ Manages all the shells """

    configured_shells = None

    def __init__(self, verbose: bool = False) -> None:
        self.verbose = verbose
        self._setup()

    def _setup(self) -> None:
        """
        Performs all the setup operations to make the object ready.
        """
        self._load_shells()

    def _load_shells(self) -> None:
        """
        Loads all the configured shells.
        """
        self.shells = {}

    def list(self, shell_type: ShoTypes = None) -> list:
        """
        Lists the configured shells

        :param shell_type: an optional value of ShoTypes type to filter the results of a specific type
        :return: a list of objects representing the configured shells
        """
        if shell_type:
            return [s for s in self.shells.values() if s.type == shell_type]
        return [s for s in self.shells.values()]

    def strlist(self, shell_type: ShoTypes = None) -> list:
        """
        Lists the configured shells

        :param shell_type: an optional value of ShoTypes type to filter the results of a specific type

        :return: a list of strings representing the configured shells
        """
        shells = self.list(shell_type=shell_type)

        if not self.verbose:
            return [s.name for s in shells]

        out = []
        for s in shells:
            out_str = "{type}\t@ {name}".format(
                type=ShoTypes.type_to_string(s.type),
                name=s.name
            )
            if s.type in ShoTypes.REMOTE_TYPES:
                out_str += "({host})".format(
                    host=s.host
                )
            out.append(out_str)
        return out

    def add(self, item_name: str, item_type: ShoTypes, item_description: str, item_host: str) -> ShoItem:
        """
        Creates and adds a new shell item to the list

        :param item_name: the name of the shell
        :param item_type: the type of the shell
        :param item_description: the description of the shell
        :param item_host: the host of the shell, only if it's a remote shell

        :return: the added item

        :raises InconsistentParametersError: if the creation of the item fails for inconsistent parameters
        :raises AlreadyExistingShellError: if the shell to be added already exists in the list
        """
        item = ShoItem(item_name, item_type, description=item_description, host=item_host)
        self.add_item(item)
        return item

    def add_item(self, item: ShoItem) -> ShoItem:
        """
        Adds a new shell item to the list

        :param item: the shell item to add
        :return: the added item

        :raises AlreadyExistingShellError: if the shell to be added already exists in the list
        """
        if item.name in self.shells:
            raise AlreadyExistingShellError()

        self.shells[item.name] = item
        return item

    def get(self, item_name: str) -> ShoItem:
        """
        Retrieves the specified shell

        :param item_name: the name of the shell to retrieve

        :return: the selected shell

        :raises ShellNotFoundError: if the shell is not found
        """
        out = self.shells.get(item_name, None)
        if not out:
            raise ShellNotFoundError()
        return out

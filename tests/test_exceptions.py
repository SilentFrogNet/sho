import pytest

from sho.core.exceptions import (
    InvalidParameterError,
    InconsistentParametersError,
    AlreadyExistingShellError,
    ShellNotFoundError
)


# --- [TESTS] --- #
@pytest.mark.raises(exception=InvalidParameterError)
def test_invalid_parameter_error() -> None:
    """ Tests that raises an InvalidParameterError """
    raise InvalidParameterError()


@pytest.mark.raises(exception=InconsistentParametersError)
def test_inconsistent_parameter_error() -> None:
    """ Tests that raises an InconsistentParametersError """
    raise InconsistentParametersError()


@pytest.mark.raises(exception=AlreadyExistingShellError)
def test_already_existing_shell_error() -> None:
    """ Tests that raises an AlreadyExistingShellError """
    raise AlreadyExistingShellError()


@pytest.mark.raises(exception=ShellNotFoundError)
def test_shell_not_found_error() -> None:
    """ Tests that raises an ShellNotFoundError """
    raise ShellNotFoundError()
# --- [/TESTS] --- #

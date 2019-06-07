import pytest

from sho.core.sho import Sho
from sho.core.sho_types import ShoTypes
from sho.core.sho_item import ShoItem

sho_items_data = [
    {
        'name': 'demo',
        'description': 'Demo server',
        'host': '192.168.1.2',
        'shell_type': ShoTypes.SSH
    },
    {
        'name': 'zsh',
        'description': 'Oh My Zsh!',
        'shell_type': ShoTypes.LOCAL
    }
]


@pytest.fixture
def sho():
    return Sho()


@pytest.fixture(params=sho_items_data)
def sho_item(request, sho):
    return sho.add_item(ShoItem(**request.param))


def test_create_sho() -> None:
    sho = Sho()
    assert isinstance(sho, Sho), "no valid instance of Sho"


def test_get_list_of_shells_empty(sho: Sho) -> None:
    shells = sho.list()
    assert isinstance(shells, list), "should be a list"
    assert shells == [], "should be an empty list"


def test_create_sho_item(sho_item: ShoItem) -> None:
    assert isinstance(sho_item, ShoItem)


def test_get_sho_item(sho: Sho, sho_item: ShoItem) -> None:
    retrieved_item = sho.get(sho_item.name)

    assert retrieved_item.name == sho_item.name
    assert retrieved_item.type == sho_item.type
    assert retrieved_item.description == sho_item.description
    assert retrieved_item.host == sho_item.host

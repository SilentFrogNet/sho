from sho.core.sho import Sho


class TestSho(object):

    def test_create(self):
        sho = Sho()

        assert isinstance(sho, Sho)

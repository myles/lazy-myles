from lazymyles.__version__ import VERSION, __version__


def test___version__():
    assert VERSION == (1, 0, 0)
    assert __version__ == "1.0.0"

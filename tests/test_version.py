from lazymyles import __version__


def test___version__():
    assert __version__.VERSION == (1, 0, 0)
    assert __version__.__version__ == "1.0.0"

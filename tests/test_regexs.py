import pytest

from lazymyles import regexs


@pytest.mark.parametrize(
    "email", ("me@mylesbraithwaite.org", "me+lazy-myles@mylesbraithwaite.org")
)
def test_email_regex(email):
    assert regexs.EMAIL_REGEX.match(email)


@pytest.mark.parametrize(
    "url",
    (
        "https://mylesbraithwaite.org/",
        "http://mylesbraithwaite.org/",
        "http://www.mylesbraithwaite.org/",
    ),
)
def test_url_regex(url):
    assert regexs.URL_REGEX.match(url)

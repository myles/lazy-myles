import pytest

from lazymyles import regexs


@pytest.mark.parametrize(
    "email", ("me@mylesbraithwaite.org", "me+lazy-myles@mylesbraithwaite.org")
)
def test_email_regex(email):
    assert regexs.EMAIL_REGEX.match(email)


@pytest.mark.parametrize(
    "http_url",
    (
        "https://mylesbraithwaite.org/",
        "http://mylesbraithwaite.org/",
        "http://www.mylesbraithwaite.org/",
    ),
)
def test_http_url_regex(http_url):
    assert regexs.HTTP_URL_REGEX.match(http_url)

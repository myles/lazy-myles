import pytest
from pyquery import PyQuery as pq

from lazymyles.html.description_list import dl_to_dict

from . import fixtures


@pytest.mark.parametrize(
    "html,expected",
    (
        (fixtures.HTML_FIXTURE_ONE, fixtures.HTML_FIXTURE_ONE_OUTPUT),
        # TODO These two are valid HTML but a little difficult to implement.
        # (fixtures.HTML_FIXTURE_TWO, fixtures.HTML_FIXTURE_TWO_OUTPUT),
        # (fixtures.HTML_FIXTURE_THREE, fixtures.HTML_FIXTURE_THREE_OUTPUT),
    ),
)
def test_dl_to_dict(html, expected):
    doc = pq(html)
    output = dl_to_dict(doc("dl"))
    assert expected == output

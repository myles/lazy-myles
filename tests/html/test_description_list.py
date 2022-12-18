import pytest
from pyquery import PyQuery as pq

from lazymyles.html.description_list import dl_to_dict

from . import fixtures


@pytest.mark.parametrize(
    "html,expected",
    (
        pytest.param(fixtures.HTML_FIXTURE_ONE, fixtures.HTML_FIXTURE_ONE_OUTPUT),
        pytest.param(
            fixtures.HTML_FIXTURE_TWO,
            fixtures.HTML_FIXTURE_TWO_OUTPUT,
            marks=pytest.mark.xfail(
                reason="TODO ENG-2: The second fixture is vaild HTML but it's a little difficult to implement."
            ),
        ),
        pytest.param(
            fixtures.HTML_FIXTURE_THREE,
            fixtures.HTML_FIXTURE_THREE_OUTPUT,
            marks=pytest.mark.xfail(
                reason="TODO ENG-2: The third fixture is vaild HTML but it's a little difficult to implement."
            )
        ),
        pytest.param(fixtures.HTML_FIXTURE_FOUR, fixtures.HTML_FIXTURE_FOUR_OUTPUT),
    ),
)
def test_dl_to_dict(html, expected):
    doc = pq(html)
    output = dl_to_dict(doc("dl"))
    assert expected == output

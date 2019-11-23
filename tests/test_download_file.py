from pathlib import Path

import pytest
import responses

from lazymyles.download_file import download_file, get_file_name


@pytest.mark.parametrize(
    "url,expected_file_name",
    (
        ("https://example.com/test.csv", "test.csv"),
        ("https://example.com/test.csv?arg=1", "test.csv"),
    ),
)
def test_get_file_name(url, expected_file_name):
    assert get_file_name(url) == expected_file_name


@responses.activate
def test_download_file(monkeypatch):
    responses.add(
        responses.GET,
        "https://example.com/test.csv",
        status=200,
        body="name, birth_date\nMyles Braithwaite, 2019-09-19",
        content_type="text/csv",
    )

    path = Path(__file__).resolve().parent / "temp"

    if not path.exists():
        path.mkdir()

    file_path = download_file("https://example.com/test.csv", output_path=path)

    assert file_path.exists()

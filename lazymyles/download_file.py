import fnmatch
import re
from os.path import basename
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

import requests

from . import regexs


def get_file_name_from_content_disposition(content_disposition: str) -> Union[str, None]:
    """
    Get file name from the Content-Disposition HTTP header.

    Parameters
    ----------
    content_disposition : str

    Returns
    -------
    str
    """
    file_name = regexs.REGEX_CONTENT_DISPOSITION.findall(content_disposition, 0)

    if not file_name:
        file_name = regexs.REGEX_CONTENT_DISPOSITION_WITHOUT_QUOTES.findall(
            content_disposition, 0
        )

    if not file_name:
        return None

    return file_name[0]


def get_file_name_from_url(url: str) -> str:
    """
    Get the file name from the URL.

    Parameters
    ----------
    url : str

    Returns
    -------
    str
    """
    return basename(urlparse(url).path)


def download_file(
    url: str, output_path: Union[Path, str], file_name: str = None
) -> Path:
    """
    Download a file.

    Parameters
    ----------
    url : str
        The URL of the file you want to download.
    output_path : Path or str
        The directory you want to output the file to.
    file_name : str
        The name of the file you want the output to be.

    Returns
    -------
    Path
    """
    if isinstance(output_path, str):
        output_path = Path(output_path)

    response = requests.get(url, allow_redirects=True)

    response.raise_for_status()

    if file_name is None and response.headers.get("Content-Disposition"):
        file_name = get_file_name_from_content_disposition(
            response.headers["Content-Disposition"]
        )

    if file_name is None:
        file_name = get_file_name_from_url(url)

    output_file_path = output_path / file_name

    with output_file_path.open("wb") as file_obj:
        file_obj.write(response.content)

    return output_file_path

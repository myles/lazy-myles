from os.path import basename
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

import requests


def get_file_name(url: str):
    """
    Get the file name of the download.

    Parameters
    ----------
    url : str

    Returns
    -------
    str
    """
    return basename(urlparse(url).path)


def download_file(
    url: str, output_path: Union[Path, str], filename: str = None
):
    """
    Download a file.

    Parameters
    ----------
    url : str
        The URL of the file you want to download.
    output_path : Path or str
        The directory you want to output the file to.
    filename : str
        The name of the file you want the output to be.

    Returns
    -------
    Path
    """
    if isinstance(output_path, str):
        output_path = Path(output_path)

    if filename is None:
        filename = get_file_name(url)

    output_file_path = output_path / filename

    response = requests.get(url, allow_redirects=True)

    response.raise_for_status()

    with output_file_path.open("wb") as file_obj:
        file_obj.write(response.content)

    return output_file_path

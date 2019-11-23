from pyquery import PyQuery


def dl_to_dict(doc: PyQuery) -> dict:
    """
    HTML Description List to a Python dictionary.

    Parameters
    ----------
    doc : PyQuery

    Returns
    -------
    dict
    """
    data = {}

    for dt_el, dd_el in zip(*(iter(doc.find("dt, dd")),) * 2):
        data[dt_el.text] = dd_el.text

    return data

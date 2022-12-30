HTML_FIXTURE_ONE = """<!DOCTYPE html>
<dl>
    <dt>First name</dt>
    <dd>Dolores</dd>
    <dt>Last name</dt>
    <dd>Abernathy</dd>
    <dt>ID number</dt>
    <dd>CH465517080</dd>
    <dt>Status</dt>
    <dd>Conscious</dd>
    <dt>Park</dt>
    <dd>Westworld</dd>
    <dt>Narrative Role</dt>
    <dd>Rancher's daughter<dd>
</dl>"""

HTML_FIXTURE_ONE_OUTPUT = {
    "First name": "Dolores",
    "Last name": "Abernathy",
    "ID number": "CH465517080",
    "Status": "Conscious",
    "Park": "Westworld",
    "Narrative Role": "Rancher's daughter",
}

HTML_FIXTURE_TWO = """<!DOCTYPE html>
<dl>
    <dt>Firefox</dt>
    <dt>Mozilla Firefox</dt>
    <dt>Fx</dt>
    <dd>
        A free, open source, cross-platform,
        graphical web browser developed by the
        Mozilla Corporation and hundreds of
        volunteers.
    </dd>
</dl>"""

HTML_FIXTURE_TWO_OUTPUT = {
    "Firefox": (
        "A free, open source, cross-platform, graphical web browser developed "
        "by the Mozilla Corporation and hundreds of volunteers."
    ),
    "Mozilla Firefox": (
        "A free, open source, cross-platform, graphical web browser developed "
        "by the Mozilla Corporation and hundreds of volunteers. "
    ),
    "Fx": (
        "A free, open source, cross-platform, graphical web browser developed "
        "by the Mozilla Corporation and hundreds of volunteers. "
    ),
}

HTML_FIXTURE_THREE = """<!DOCTYPE html>
<dl>
    <dt>Firefox</dt>
    <dd>
        A free, open source, cross-platform,
        graphical web browser developed by the
        Mozilla Corporation and hundreds of
        volunteers.
    </dd>
    <dd>
        The Red Panda also known as the Lesser
        Panda, Wah, Bear Cat or Firefox, is a
        mostly herbivorous mammal, slightly larger
        than a domestic cat (60 cm long).
    </dd>
</dl>"""

HTML_FIXTURE_THREE_OUTPUT = {
    "Firefox": [
        (
            "A free, open source, cross-platform, graphical web browser "
            "developed by the Mozilla Corporation and hundreds of volunteers."
        ),
        (
            "The Red Panda also known as the Lesser Panda, Wah, Bear Cat or "
            "Firefox, is a mostly herbivorous mammal, slightly larger than a "
            "domestic cat (60 cm long)."
        ),
    ]
}

HTML_FIXTURE_FOUR = """<!DOCTYPE html>
<dl>
    <div>
        <dt>Name</dt>
        <dd>Godzilla</dd>
    </div>
    <div>
        <dt>Born</dt>
        <dd>1952</dd>
    </div>
    <div>
        <dt>Birthplace</dt>
        <dd>Japan</dd>
    </div>
    <div>
        <dt>Color</dt>
        <dd>Green</dd>
    </div>
</dl>"""

HTML_FIXTURE_FOUR_OUTPUT = {
    "Name": "Godzilla",
    "Born": "1952",
    "Birthplace": "Japan",
    "Color": "Green",
}

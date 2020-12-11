import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

HTTP_URL_REGEX = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)

CONTENT_DISPOSITION_REGEX = re.compile(r"filename=[\"|\']?(?P<file_name>.*)[\"|\']$")
CONTENT_DISPOSITION_WITHOUT_QUOTES_REGEX = re.compile(r"filename=(.*)")

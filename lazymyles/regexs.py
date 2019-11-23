import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

URL_REGEX = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)

REGEX_CONTENT_DISPOSITION = re.compile(
    r"filename=[\"|\']?(?P<file_name>.*)[\"|\']$"
)
REGEX_CONTENT_DISPOSITION_WITHOUT_QUOTES = re.compile(r"filename=(.*)")

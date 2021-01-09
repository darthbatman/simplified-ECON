import re

CONCEPT_TAGGED_PHRASE = re.compile(
    r'<c>(?P<phrase>[^<]*)</c>'
)

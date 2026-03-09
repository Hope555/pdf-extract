import re
from config import load_anchor_fields


ANCHOR_FIELDS = load_anchor_fields()


def normalize_text(text):

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    return text


def extract_value_after_anchor(text, anchor):

    pattern = rf"{anchor}\s*[:\-]?\s*([^\n\r]+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        value = match.group(1).strip()
        return value[:100]

    return None


def extract_fields(text):

    text = normalize_text(text)

    results = {}

    for field, anchors in ANCHOR_FIELDS.items():

        value = None

        for anchor in anchors:

            value = extract_value_after_anchor(text, anchor)

            if value:
                break

        results[field] = value

    return results
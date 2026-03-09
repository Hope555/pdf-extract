import json
import os


# Folder containing input PDFs
INPUT_FOLDER = "input"

# Folder containing output files
OUTPUT_FOLDER = "output"

# Anchor configuration file
ANCHOR_FILE = "anchors.json"


# OCR configuration
OCR_DPI = 300


def load_anchor_fields():
    """
    Load anchor definitions from configuration file
    """

    if not os.path.exists(ANCHOR_FILE):
        raise FileNotFoundError(f"Anchor config not found: {ANCHOR_FILE}")

    with open(ANCHOR_FILE, "r", encoding="utf-8") as f:
        anchors = json.load(f)

    return anchors
import fitz  # PyMuPDF


def is_scanned_pdf(pdf_path, min_text_threshold=30):
    """
    Determine whether a PDF is likely scanned (image-based)
    by checking if text can be extracted.
    """

    doc = fitz.open(pdf_path)

    total_text_length = 0

    for page in doc:
        text = page.get_text().strip()
        total_text_length += len(text)

    doc.close()

    return total_text_length < min_text_threshold


def extract_native_text(pdf_path):
    """
    Extract all text from a PDF using native text extraction.
    """

    doc = fitz.open(pdf_path)

    full_text = []

    for page in doc:
        text = page.get_text()
        full_text.append(text)

    doc.close()

    return "\n".join(full_text)


def extract_words_with_coordinates(pdf_path):
    """
    Extract words with positional coordinates.
    Useful for layout-aware anchor extraction.
    """

    doc = fitz.open(pdf_path)

    words_data = []

    for page_number, page in enumerate(doc):

        words = page.get_text("words")

        for word in words:

            x0, y0, x1, y1, text, block_no, line_no, word_no = word

            words_data.append({
                "page": page_number,
                "text": text,
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1,
                "block": block_no,
                "line": line_no,
                "word": word_no
            })

    doc.close()

    return words_data
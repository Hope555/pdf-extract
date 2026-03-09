import os

from pdf_reader import extract_native_text, is_scanned_pdf
from ocr_reader import extract_text_ocr
from anchor_extractor import extract_fields
from config import INPUT_FOLDER, OUTPUT_FOLDER


OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "final_report.txt")


def process_pdf(pdf_path):

    print(f"Processing: {pdf_path}")

    if is_scanned_pdf(pdf_path):
        print("Using OCR...")
        text = extract_text_ocr(pdf_path)
    else:
        print("Using native extraction...")
        text = extract_native_text(pdf_path)

    fields = extract_fields(text)

    fields["source_file"] = os.path.basename(pdf_path)

    return fields


def write_results_to_txt(results, output_file):

    with open(output_file, "w", encoding="utf-8") as f:

        for record in results:

            f.write("====================================\n")

            for key, value in record.items():
                f.write(f"{key}: {value}\n")

            f.write("\n")


def main():

    results = []

    for file in os.listdir(INPUT_FOLDER):

        if file.lower().endswith(".pdf"):

            path = os.path.join(INPUT_FOLDER, file)

            data = process_pdf(path)

            results.append(data)

    write_results_to_txt(results, OUTPUT_FILE)

    print("TXT report generated:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
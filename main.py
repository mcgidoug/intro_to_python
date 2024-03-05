import os
import pytesseract
from pdf2image import convert_from_path


def pdf_to_markdown(pdf_path, output_dir):
  # Create output directory if it doesn't exist
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # Convert PDF to images
  images = convert_from_path(pdf_path)

  # Iterate over each page image and extract text using OCR
  for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)

    # Write text to markdown file
    markdown_file = os.path.join(output_dir, f"page_{i+1}.md")
    with open(markdown_file, "w") as f:
      f.write(text)

  print(f"PDF converted to markdown files in directory: {output_dir}")


# Example usage:
pdf_path = "example.pdf"
output_dir = "output"
pdf_to_markdown(pdf_path, output_dir)

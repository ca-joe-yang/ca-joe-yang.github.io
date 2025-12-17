#!/usr/bin/env python3
"""
Convert PDF files to high-quality PNG images.
Usage: python pdf2png.py input.pdf [output.png]
"""

import sys
from pathlib import Path

from pdf2image import convert_from_path


def pdf_to_png(pdf_path, output_path=None, dpi=300):
    """
    Convert PDF to high-quality PNG.

    Args:
        pdf_path: Path to input PDF file
        output_path: Path to output PNG file (optional)
        dpi: Resolution in dots per inch (default: 300 for high quality)
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"Error: File '{pdf_path}' not found.")
        sys.exit(1)

    # Generate output filename if not provided
    if output_path is None:
        output_path = pdf_path.with_suffix('.png')
    else:
        output_path = Path(output_path)

    print(f"Converting {pdf_path} to PNG at {dpi} DPI...")

    # Convert PDF to images (returns list of PIL Image objects)
    # use_cropbox=True respects PDF crop/trim settings
    images = convert_from_path(str(pdf_path), dpi=dpi, use_cropbox=True)

    # Save first page (or all pages if needed)
    if len(images) > 0:
        images[0].save(str(output_path), 'PNG', quality=95)
        print(f"✓ Saved: {output_path}")
        print(f"  Size: {images[0].size[0]}x{images[0].size[1]} pixels")

        # If PDF has multiple pages, save them separately
        if len(images) > 1:
            print(f"\nPDF has {len(images)} pages. Saving all pages...")
            for i, image in enumerate(images):
                page_output = output_path.with_stem(f"{output_path.stem}_page{i+1}")
                image.save(str(page_output), 'PNG', quality=95)
                print(f"✓ Saved: {page_output}")
    else:
        print("Error: No images extracted from PDF.")
        sys.exit(1)


if __name__ == "__main__":
    input_path = Path(sys.argv[1])
    dpi = 100
    # if is dir
    if input_path.is_dir():
        for input_pdf in input_path.glob('**/*.pdf'):
            pdf_to_png(input_pdf, dpi=dpi)
    elif input_path.is_file() and input_path.suffix.lower() == '.pdf':
        pdf_to_png(input_path, dpi=dpi)

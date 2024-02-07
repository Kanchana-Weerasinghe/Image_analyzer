from PIL import Image
import fitz
import os

def extract_pdf_first_page_and_convert_to_jpg(input_pdf_path, output_image_folder,image_name):
    pdf_document = fitz.open(input_pdf_path)

    # Extract the first page
    first_page = pdf_document[0]

    # Convert the first page to a pixmap
    pixmap = first_page.get_pixmap()

    # Convert the pixmap to a Pillow Image
    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

    # Save the image as a JPG file
    output_image_path = os.path.join(output_image_folder, image_name +'.jpg')
    image.save(output_image_path, 'JPEG')

    # Close the PDF document
    pdf_document.close()
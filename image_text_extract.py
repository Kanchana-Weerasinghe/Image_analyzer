# from PIL import Image
# import pytesseract
# import os

# def extract_pdf_first_page_and_convert_to_jpg(input_image_path,output_image_text_folder_path):
#     img = Image.open(input_image_path)
#     text = pytesseract.image_to_string(img)

#     if not os.path.exists(output_image_text_folder_path):
#         os.makedirs(output_image_text_folder_path)

#     text_file_path = os.path.join(output_image_text_folder_path, f'text.txt')
#     with open(text_file_path, 'w') as file:
#      for color in color_palette:
#         file.write(f"{color}\n")

#     return text
import os
from pdf_downloder import download_pdf_files 
from extract_pdf_images import extract_pdf_first_page_and_convert_to_jpg 
from image_color_picker import extract_main_colors_and_create_text_file 
from image_object_extract import extract_and_classify_objects_from_image 


#region - Download pdf file 
def main_download_pdf_files():
    download_pdf_files()
#endregion

#region - Extract Pdf And Convert to JPG
def main_extract_pdf_first_page_and_convert_to_jpg():
    input_image_folder  = 'download_file'  
    output_image_color_floder = 'extract_images'  

    input_image_folder_path = os.path.join(os.getcwd(), input_image_folder)
    output_image_color_folder_path = os.path.join(os.getcwd(), output_image_color_floder)

    for filename in os.listdir(input_image_folder_path):
        if filename.endswith('.pdf'):
            image_name = os.path.splitext(filename)[0]
            input_pdf_path = os.path.join(input_image_folder_path, filename)
            extract_pdf_first_page_and_convert_to_jpg(input_pdf_path, output_image_color_folder_path,image_name)
#endregion

#region - Extract main 5 colors from the image
def main_extract_main_colors_and_create_text_file():
    input_folder  = 'extract_images'  
    output_image_folder = 'images_color'  

    input_folder_path = os.path.join(os.getcwd(), input_folder)
    output_image_folder_path = os.path.join(os.getcwd(), output_image_folder)

    for filename in os.listdir(input_folder_path):
        if filename.endswith('.jpg'):
            image_name = os.path.splitext(filename)[0]
            input_image_path = os.path.join(input_folder_path, filename)
            extract_main_colors_and_create_text_file(input_image_path, output_image_folder_path,image_name)
#endregion

#region - Extract object and clasify 
def main_extract_and_clisify_objects_from_image():
    input_folder  = 'extract_images'  

    input_folder_path = os.path.join(os.getcwd(), input_folder)

    for filename in os.listdir(input_folder_path):
        if filename.endswith('.jpg'):
            image_name = os.path.splitext(filename)[0]
            input_image_path = os.path.join(input_folder_path, filename)
            extract_and_classify_objects_from_image(input_image_path)
#endregion


if __name__ == "__main__":

    main_download_pdf_files()
    main_extract_pdf_first_page_and_convert_to_jpg()
    main_extract_main_colors_and_create_text_file()
    main_extract_and_clisify_objects_from_image()

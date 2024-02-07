from  colorthief import ColorThief
import matplotlib.pyplot as plt 
import colorsys
import os


def extract_main_colors_and_create_text_file(input_image_path, output_image_color_folder_path,image_name):
    ct= ColorThief(input_image_path)
    color_palette=ct.get_palette(color_count=5)
    plt.imshow([[color_palette[i] for i in range(5)]])
    plt.axis('off')
    color_palette_image_path = os.path.join(output_image_color_folder_path, f'color_palette_{image_name}.png')
    plt.savefig(color_palette_image_path, bbox_inches='tight')

    color_palette_txt_path = os.path.join(output_image_color_folder_path, f'color_palette_{image_name}.txt')
    with open(color_palette_txt_path, 'w') as file:
     for color in color_palette:
        file.write(f"{color}\n")
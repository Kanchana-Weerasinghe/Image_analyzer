import os
import pandas as pd
from image_object_extract import extract_and_classify_objects_from_image



#region - Extract object and clasify
def main_extract_and_clisify_objects_from_image(object_class_df,object_class_field_names):
    input_folder  = 'extract_images'
    # output_folder  = 'clasified_images'

    input_folder_path = os.path.join(os.getcwd(), input_folder)
    i=0
    for filename in os.listdir(input_folder_path):
        if filename.endswith('.png'):
            image_name = os.path.splitext(filename)[0]
            input_image_path = os.path.join(input_folder_path, filename)
            document_id=image_name.rstrip('.png')
            object_class_df.loc[i] = [None] * len(object_class_field_names)
            object_class_df.at[i, "report_name"] =document_id
            extract_and_classify_objects_from_image(input_image_path,object_class_df,i)
            i +=1

    return object_class_df

#endregion


if __name__ == "__main__":
    object_class_field_names = ["report_name","person_count","vehicle_count","animal_count","all_object_class_lsit"]
    object_class_df = pd.DataFrame(columns=object_class_field_names)
    object_class_df=main_extract_and_clisify_objects_from_image(object_class_df,object_class_field_names)

    data_folder_path = os.path.join(os.getcwd(), "data")
    object_class_df.to_csv(f"{data_folder_path}/summary.csv", index=False)


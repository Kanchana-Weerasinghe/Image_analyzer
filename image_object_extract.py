from ultralytics import YOLO

def extract_and_classify_objects_from_image(image_path,object_class_df,row_index):
    model =YOLO("yolov8m-seg.pt")
    object_list=model.predict(source=image_path, conf=0.5)
    names = model.names
    class_names_str=""
    for r in object_list:
        for c in r.boxes.cls:
            class_names_str += "," + names[int(c)]

    object_class_df.at[row_index, "all_object_class_lsit"] = class_names_str

    person_count=0
    vehicle_count=0
    animal_count=0

    person_count= class_names_str.lower().count("person")
    vehicle_to_count = ["car", "bus","bicycle","motorcycle","airplane","train","truck","boat"]
    for word in vehicle_to_count:
        vehicle_count += class_names_str.lower().count(word.lower())

    animal_to_count = ["cat", "dog","horse","sheep","cow","elephant","bear","zebra","giraffe"]
    for word in animal_to_count:
        animal_count += class_names_str.lower().count(word.lower())

    object_class_df.at[row_index, "person_count"] = person_count
    object_class_df.at[row_index, "vehicle_count"] = vehicle_count
    object_class_df.at[row_index, "animal_count"] = animal_count

    return object_class_df



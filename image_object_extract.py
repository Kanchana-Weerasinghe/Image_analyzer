import cv2
import numpy as np
import tensorflow as tf

def extract_and_classify_objects_from_image(image_path):
    model_path = 'ssd_mobilenet_v2_coco_2017_11_17/frozen_inference_graph.pb'

    # Load your trained model
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        graph_def = tf.compat.v1.GraphDef()
        with open(model_path, 'rb') as fid:
            serialized_graph = fid.read()
            graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(graph_def, name='')

    # Load class labels
    label_map = {1: 'human', 2: 'animal', 3: 'tree'}  # Adjust based on your label map

    # Read the image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform object detection
    with detection_graph.as_default():
        with tf.compat.v1.Session(graph=detection_graph) as sess:
            # Get handles to input and output tensors
            ops = detection_graph.get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            tensor_dict = {}
            for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes']:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    tensor_dict[key] = detection_graph.get_tensor_by_name(tensor_name)

            # Define the input tensor
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Run inference
            output_dict = sess.run(tensor_dict, feed_dict={image_tensor: np.expand_dims(image_rgb, 0)})

            # Extract information
            num_detections = int(output_dict['num_detections'][0])
            detection_classes = output_dict['detection_classes'][0].astype(np.uint8)
            detection_boxes = output_dict['detection_boxes'][0]
            detection_scores = output_dict['detection_scores'][0]

    # Classify and print results
    for i in range(num_detections):
        class_id = detection_classes[i]
        score = detection_scores[i]
        box = detection_boxes[i]

        # Optionally, you can use the label map to get the class name
        class_name = label_map.get(class_id, 'Unknown')

        print(f"Class Name: {class_name}, Score: {score}, Box: {box}")

# Example usage:
image_path = 'path/to/your/image.jpg'
extract_and_classify_objects_from_image(image_path)

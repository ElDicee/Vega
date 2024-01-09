import os.path

import integrations.VegaAPI as api
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks import python
import numpy as np
import cv2


def get_face_landmark_model(output_face_blendshapes: bool, output_facial_transmormation_matrixes: bool, num_faces: int):
    base_options = python.BaseOptions(model_asset_path=os.path.join("integrations", "Mediapipe", "face_landmarker_v2_with_blendshapes.task"))
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                           output_face_blendshapes=output_face_blendshapes,
                                           output_facial_transformation_matrixes=output_facial_transmormation_matrixes,
                                           num_faces=num_faces)

    return vision.FaceLandmarker.create_from_options(options)


def draw_landmarks_on_image(rgb_image, detection_result):
    face_landmarks_list = detection_result.face_landmarks
    annotated_image = np.copy(rgb_image)

    # Loop through the detected faces to visualize.
    for idx in range(len(face_landmarks_list)):
        face_landmarks = face_landmarks_list[idx]

        # Draw the face landmarks.
        face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        face_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
        ])

        solutions.drawing_utils.draw_landmarks(
            image=annotated_image,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles
            .get_default_face_mesh_tesselation_style())
        solutions.drawing_utils.draw_landmarks(
            image=annotated_image,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles
            .get_default_face_mesh_contours_style())
        solutions.drawing_utils.draw_landmarks(
            image=annotated_image,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_IRISES,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles
            .get_default_face_mesh_iris_connections_style())

    return annotated_image


def detect(model, image):
    return model.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.convertScaleAbs(image)))


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Mediapipe")
    vega.add_method(api.Method(get_face_landmark_model, api.EXECUTION, outputs={"Model": None}, formal_name="Create Face Landmark Model"))
    vega.add_method(api.Method(draw_landmarks_on_image, api.EXECUTION, outputs={"Image": None}, formal_name="Draw Landmarks"))
    vega.add_method(api.Method(detect, api.EXECUTION, outputs={"Detection": None}, formal_name="Detect"))
    return vega


if __name__ == "__main__":
    model = get_face_landmark_model(True, True, 1)
    cap = cv2.VideoCapture(0)
    while True:
        res, img = cap.read()
        d = model.detect(img)

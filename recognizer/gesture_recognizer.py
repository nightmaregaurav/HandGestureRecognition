from typing import Callable
from mediapipe import Image
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python.vision import HandLandmarker
from mediapipe.tasks.python.vision import HandLandmarkerOptions
from mediapipe.tasks.python.vision import HandLandmarkerResult

from recognizer.helpers.running_mode_helper import get_primitive_vision_running_mode
from recognizer.settings import MAX_NUM_OF_HANDS, MIN_HAND_DETECTION_CONFIDENCE, MIN_HAND_PRESENCE_CONFIDENCE, \
    MIN_HAND_LANDMARK_TRACKING_CONFIDENCE, MODEL_PATH
from recognizer.types.recognition_mode import RecognitionMode


def default_callback(result: HandLandmarkerResult, _: Image, timestamp_ms: int):
    print('[{}] Hand landmarker result: {}'.format(timestamp_ms, result))


def start_detection(
        mode: RecognitionMode,
        data_source: Image,
        frame_timestamp_ms: int,
        callback: Callable[[HandLandmarkerResult, Image, int], None] = default_callback
):
    options: HandLandmarkerOptions = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=MODEL_PATH),
        running_mode=get_primitive_vision_running_mode(mode),
        num_hands=MAX_NUM_OF_HANDS,
        min_hand_detection_confidence=MIN_HAND_DETECTION_CONFIDENCE,
        min_hand_presence_confidence=MIN_HAND_PRESENCE_CONFIDENCE,
        min_tracking_confidence=MIN_HAND_LANDMARK_TRACKING_CONFIDENCE,
        result_callback=callback
    )
    with HandLandmarker.create_from_options(options) as landmarker:
        if mode.current == RecognitionMode.IMAGE:
            landmarker.detect(data_source)
        elif mode.current == RecognitionMode.VIDEO:
            landmarker.detect_for_video(data_source, frame_timestamp_ms)
        elif mode.current == RecognitionMode.LIVE:
            landmarker.detect_async(data_source, frame_timestamp_ms)
        else:
            raise ValueError("Invalid recognition mode: {}".format(mode.current))

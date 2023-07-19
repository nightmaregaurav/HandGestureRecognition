from mediapipe.tasks.python.vision import RunningMode

from recognizer.types.recognition_mode import RecognitionMode


def get_primitive_vision_running_mode(mode: RecognitionMode) -> RunningMode:
    if mode.current == RecognitionMode.IMAGE:
        return RunningMode.IMAGE
    elif mode.current == RecognitionMode.VIDEO:
        return RunningMode.VIDEO
    elif mode.current == RecognitionMode.LIVE:
        return RunningMode.LIVE_STREAM
    else:
        raise ValueError("Invalid recognition mode: {}".format(mode.current))

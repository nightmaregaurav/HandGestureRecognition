class RecognitionMode:
    IMAGE: str = "Image"
    VIDEO: str = "Video"
    LIVE: str = "Live"

    ValidModes = [IMAGE, VIDEO, LIVE]

    current: str = None

    def __init__(self, value: str):
        if value not in RecognitionMode.ValidModes:
            raise ValueError("Invalid recognition mode: {}".format(value))
        self.current = value

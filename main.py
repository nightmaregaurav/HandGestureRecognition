from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.centralwidget = QWidget(self)

        self.main_layout = QWidget(self.centralwidget)
        self.main_layout.setGeometry(QRect(9, 9, 781, 581))

        self.main_vertical_layout = QVBoxLayout(self.main_layout)
        self.main_vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.qt_vision_horizontal_layout = QHBoxLayout()

        self.qt_vision_group_label = QLabel(self.main_layout)
        self.qt_vision_group_label.setStyleSheet(u"")
        self.qt_vision_group_label.setTextFormat(Qt.RichText)
        self.qt_vision_horizontal_layout.addWidget(self.qt_vision_group_label)

        self.main_vertical_layout.addLayout(self.qt_vision_horizontal_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.verticalLayout_2 = QVBoxLayout()
        self.qt_image_from_file_button = QPushButton(self.main_layout)

        self.verticalLayout_2.addWidget(self.qt_image_from_file_button)

        self.qt_image_capture_button = QPushButton(self.main_layout)

        self.verticalLayout_2.addWidget(self.qt_image_capture_button)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.qt_video_from_file_button = QPushButton(self.main_layout)

        self.verticalLayout_3.addWidget(self.qt_video_from_file_button)

        self.qt_video_stream_button = QPushButton(self.main_layout)

        self.verticalLayout_3.addWidget(self.qt_video_stream_button)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.qt_preview_checkbox = QCheckBox(self.main_layout)

        self.verticalLayout_4.addWidget(self.qt_preview_checkbox)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.main_vertical_layout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.web_vision_group_label = QLabel(self.main_layout)

        self.horizontalLayout_3.addWidget(self.web_vision_group_label)

        self.main_vertical_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5 = QVBoxLayout()
        self.web_image_upload_checkbox = QCheckBox(self.main_layout)

        self.verticalLayout_5.addWidget(self.web_image_upload_checkbox)

        self.web_image_base64_upload_checkbox = QCheckBox(self.main_layout)

        self.verticalLayout_5.addWidget(self.web_image_base64_upload_checkbox)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.web_video_upload_checkbox = QCheckBox(self.main_layout)

        self.verticalLayout_6.addWidget(self.web_video_upload_checkbox)

        self.web_video_stream_checkbox = QCheckBox(self.main_layout)

        self.verticalLayout_6.addWidget(self.web_video_stream_checkbox)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.web_preview_checkbox = QCheckBox(self.main_layout)

        self.verticalLayout_7.addWidget(self.web_preview_checkbox)

        self.web_vision_action_button = QPushButton(self.main_layout)

        self.verticalLayout_7.addWidget(self.web_vision_action_button)

        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.main_vertical_layout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.plainTextEdit = QPlainTextEdit(self.main_layout)

        self.horizontalLayout_5.addWidget(self.plainTextEdit)

        self.main_vertical_layout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.status_bar_label = QLabel(self.main_layout)

        self.horizontalLayout_6.addWidget(self.status_bar_label)

        self.main_vertical_layout.addLayout(self.horizontalLayout_6)

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle(u"Hand Gesture Recognition")
        self.qt_vision_group_label.setText(u"<b>QT Vision</b>")
        self.qt_image_from_file_button.setText(u"Image From File")
        self.qt_image_capture_button.setText(u"Image Capture")
        self.qt_video_from_file_button.setText(u"Video From File")
        self.qt_video_stream_button.setText(u"Video Stream")
        self.qt_preview_checkbox.setText(u"Show Result Preview")
        self.web_vision_group_label.setText(u"<b>Web Vision</b>")
        self.web_image_upload_checkbox.setText(u"Image file upload")
        self.web_image_base64_upload_checkbox.setText(u"Image from base64")
        self.web_video_upload_checkbox.setText(u"Video Upload")
        self.web_video_stream_checkbox.setText(u"Video Stream")
        self.web_preview_checkbox.setText(u"Send Result Preview")
        self.web_vision_action_button.setText(u"PushButton")
        self.status_bar_label.setText(u"<i>Warning Text</i>")

        QMetaObject.connectSlotsByName(self)

def start():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()

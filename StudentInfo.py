from PySide2 import QtWidgets, QtCore
from os import listdir

import loginSis
from save_data import save_transcript_to_db
from transcript import parse_transcript_data


class StudentInfo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(StudentInfo, self).__init__(parent)

        self.user_name = ""
        self.path = ""
        self.transcript_data = {}

        self.setFixedSize(350, 180)
        self.setWindowTitle("Transcript Seç")

        self.button_box = QtWidgets.QDialogButtonBox()
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.button_box2 = QtWidgets.QDialogButtonBox()
        self.button_box2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.existing_user_button = QtWidgets.QPushButton("Var Olan Transkrip Seç")
        self.new_user_button = QtWidgets.QPushButton("Yeni Transkrip Seç")

        user_name_label = QtWidgets.QLabel("İTU Kullanıcı Adı")
        password_label = QtWidgets.QLabel("Sifre")
        student_number_label = QtWidgets.QLabel("Öğrenci Numarası")
        student_pin_label = QtWidgets.QLabel("Pin")
        self.user_name_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_number_line_edit = QtWidgets.QLineEdit()
        self.student_pin_line_edit = QtWidgets.QLineEdit()
        self.student_pin_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.grid_layout1_widget = QtWidgets.QWidget()

        self.grid_layout1 = QtWidgets.QGridLayout(self.grid_layout1_widget)
        self.grid_layout1.addWidget(user_name_label, 0, 0)
        self.grid_layout1.addWidget(self.user_name_line_edit, 0, 1)
        self.grid_layout1.addWidget(password_label, 1, 0)
        self.grid_layout1.addWidget(self.password_line_edit, 1, 1)
        self.grid_layout1.addWidget(student_number_label, 2, 0)
        self.grid_layout1.addWidget(self.student_number_line_edit, 2, 1)
        self.grid_layout1.addWidget(student_pin_label, 3, 0)
        self.grid_layout1.addWidget(self.student_pin_line_edit, 3, 1)
        self.grid_layout1.addWidget(self.button_box, 4, 1)

        transcript_sec_label = QtWidgets.QLabel("Transkript Seç")
        self.transcript_sec_cbox = QtWidgets.QComboBox()
        self.open_button = QtWidgets.QPushButton("Transcript Aç")

        self.grid_layout2_widget = QtWidgets.QWidget()

        self.grid_layout2 = QtWidgets.QGridLayout(self.grid_layout2_widget)
        self.grid_layout2.addWidget(transcript_sec_label, 0, 0)
        self.grid_layout2.addWidget(self.transcript_sec_cbox, 0, 1)
        self.grid_layout2.addWidget(self.open_button, 1, 1)
        self.grid_layout2.addWidget(self.button_box2, 2, 1)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.existing_user_button, 0)
        self.main_layout.addWidget(self.new_user_button, 1)
        self.main_layout.addWidget(self.grid_layout1_widget, 2)
        self.main_layout.addWidget(self.grid_layout2_widget, 3)
        self.grid_layout1_widget.setVisible(False)
        self.grid_layout2_widget.setVisible(False)

        self.setLayout(self.main_layout)

        QtCore.QObject.connect(self.existing_user_button, QtCore.SIGNAL("clicked()"), self.set_existing_user_button)
        QtCore.QObject.connect(self.new_user_button, QtCore.SIGNAL("clicked()"), self.set_new_user_button)
        QtCore.QObject.connect(self.open_button, QtCore.SIGNAL("clicked()"), self.open_transcript)
        QtCore.QObject.connect(self.transcript_sec_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.set_user_name_by_transcript_cbox)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("accepted()"), self.set_new_user_accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("rejected()"), self.reset_student_info)
        QtCore.QObject.connect(self.button_box2, QtCore.SIGNAL("accepted()"), self.set_existing_user_accept)
        QtCore.QObject.connect(self.button_box2, QtCore.SIGNAL("rejected()"), self.reset_student_info)

        self.file_dialog = QtWidgets.QFileDialog()
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.file_dialog.setNameFilter("*.db")

    def set_new_user_button(self):
        self.existing_user_button.hide()
        self.new_user_button.hide()
        self.grid_layout2_widget.setVisible(False)

        self.grid_layout1_widget.setVisible(True)

    def set_existing_user_button(self):
        self.existing_user_button.hide()
        self.new_user_button.hide()
        self.grid_layout1_widget.setVisible(False)

        transcripts = listdir("Data/Transcripts")

        for trans in transcripts:
            self.transcript_sec_cbox.addItem(trans.split(".")[0])

        self.grid_layout2_widget.setVisible(True)

    def set_user_name_by_transcript_cbox(self):
        self.user_name = self.transcript_sec_cbox.currentText()

    def set_new_user_accept(self):
        self.get_transcript_data()
        self.accept()

    def set_existing_user_accept(self):
        self.user_name = self.transcript_sec_cbox.currentText()
        self.path = "Data/Transcripts/" + self.user_name + ".dp"
        self.accept()

    def open_transcript(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Transcript", '', "(*.dp)")
        self.user_name = file_name.split("/")[-1].split(".")[0]
        self.path = file_name

        if not file_name:
            return None

        self.accept()

    def get_transcript_data(self):
        user_name = self.user_name_line_edit.text()
        password = self.password_line_edit.text()
        student_number = self.student_number_line_edit.text()
        pin = self.student_pin_line_edit.text()

        transcript_data = loginSis.get_transcript_html(user_name, password, student_number, pin)

        if transcript_data == 1:
            return 1
        elif transcript_data == 2:
            return 2

        save_transcript_to_db(parse_transcript_data(transcript_data.text), user_name)

        self.user_name = user_name
        self.path = "Data/Transcripts/" + user_name + ".dp"

    def reset_student_info(self):
        self.user_name = ""
        self.transcript_data = {}
        self.existing_user_button.show()
        self.new_user_button.show()
        self.grid_layout1_widget.setVisible(False)
        self.grid_layout2_widget.setVisible(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    student_info = StudentInfo()
    student_info.show()

    sys.exit(app.exec_())

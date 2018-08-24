from PySide2 import QtWidgets, QtCore
from os import  listdir

import loginSis
from save_data import save_transcript
from transcript import edit_transcript_data, parse_transcript_data


class StudentInfo(QtWidgets.QDialog):
    def __init__(self, patent=None):
        super(StudentInfo, self).__init__(patent)

        self.user_name = ""

        self.setFixedSize(350, 180)

        self.button_box = QtWidgets.QDialogButtonBox()
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.var_olan_button = QtWidgets.QPushButton("Var Olan Transkrip Seç")
        self.yeni_button = QtWidgets.QPushButton("Yeni Transkrip Seç")

        kullanici_adi_label = QtWidgets.QLabel("İTU Kullanıcı Adı")
        sifre_label = QtWidgets.QLabel("Sifre")
        student_number_label = QtWidgets.QLabel("Öğrenci Numarası")
        student_pin_label = QtWidgets.QLabel("Pin")
        self.kullanici_adi_line_edit = QtWidgets.QLineEdit()
        self.sifre_line_edit = QtWidgets.QLineEdit()
        self.sifre_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_number_line_edit = QtWidgets.QLineEdit()
        self.student_pin_line_edit = QtWidgets.QLineEdit()
        self.student_pin_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.grid_layout1 = QtWidgets.QGridLayout()
        self.grid_layout1.addWidget(kullanici_adi_label, 0, 0)
        self.grid_layout1.addWidget(self.kullanici_adi_line_edit, 0, 1)
        self.grid_layout1.addWidget(sifre_label, 1, 0)
        self.grid_layout1.addWidget(self.sifre_line_edit, 1, 1)
        self.grid_layout1.addWidget(student_number_label, 2, 0)
        self.grid_layout1.addWidget(self.student_number_line_edit, 2, 1)
        self.grid_layout1.addWidget(student_pin_label, 3, 0)
        self.grid_layout1.addWidget(self.student_pin_line_edit, 3, 1)

        transkript_sec_label = QtWidgets.QLabel("Transkript Seç")
        self.transkript_sec_cbox = QtWidgets.QComboBox()
        self.disa_aktar_button = QtWidgets.QPushButton("Dışa Aktar")
        self.ice_aktar_button = QtWidgets.QPushButton("İçe Aktar")

        self.grid_layout2 = QtWidgets.QGridLayout()
        self.grid_layout2.addWidget(transkript_sec_label, 0, 0)
        self.grid_layout2.addWidget(self.transkript_sec_cbox, 0, 1)
        self.grid_layout2.addWidget(self.disa_aktar_button, 1, 0)
        self.grid_layout2.addWidget(self.ice_aktar_button, 1, 1)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.var_olan_button, 0)
        self.main_layout.addWidget(self.yeni_button, 1)

        self.setLayout(self.main_layout)

        QtCore.QObject.connect(self.var_olan_button, QtCore.SIGNAL("clicked()"), self.set_var_olan_button)
        QtCore.QObject.connect(self.yeni_button, QtCore.SIGNAL("clicked()"), self.set_yeni_button)
        QtCore.QObject.connect(self.disa_aktar_button, QtCore.SIGNAL("clicked()"), self.set_disa_aktar)
        QtCore.QObject.connect(self.ice_aktar_button, QtCore.SIGNAL("clicked()"), self.set_ice_aktar)
        QtCore.QObject.connect(self.transkript_sec_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.set_user_name_by_transcript_cbox)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("rejected()"), self.reject)

        self.file_dialog = QtWidgets.QFileDialog()
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.file_dialog.setNameFilter("*.json")

    def set_yeni_button(self):
        self.var_olan_button.hide()
        self.yeni_button.hide()

        self.main_layout.addLayout(self.grid_layout1, 3)
        self.main_layout.addWidget(self.button_box, 4)

    def set_var_olan_button(self):
        self.var_olan_button.hide()
        self.yeni_button.hide()

        transcripts = listdir("Data/Transcripts")

        for trans in transcripts:
            self.transkript_sec_cbox.addItem(trans.split(".")[0])

        self.main_layout.addLayout(self.grid_layout2, 3)
        self.main_layout.addWidget(self.button_box, 4)

    def set_user_name_by_transcript_cbox(self):
        self.user_name = self.transkript_sec_cbox.currentText()

    def set_disa_aktar(self):
        pass

    def set_ice_aktar(self):
        self.file_dialog.show()
        pass

    def get_transcript_data(self):
        kullanici_adi = self.kullanici_adi_line_edit.text()
        sifre = self.sifre_line_edit.text()
        student_number = self.student_number_line_edit.text()
        pin = self.student_pin_line_edit.text()
        transcript_data = loginSis.get_transcript_html(kullanici_adi, sifre, student_number, pin)

        if transcript_data == 1:
            return 1
        elif transcript_data == 2:
            return 2

        save_transcript(kullanici_adi, edit_transcript_data(*parse_transcript_data(transcript_data.text)))

        self.user_name = kullanici_adi


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    student_info = StudentInfo()
    student_info.show()

    sys.exit(app.exec_())

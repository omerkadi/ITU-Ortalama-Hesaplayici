from PySide2 import QtWidgets, QtCore


class StudentInfo(QtWidgets.QDialog):
    def __init__(self, patent=None):
        super(StudentInfo, self).__init__(patent)

        self.setFixedSize(350, 180)

        self.button_box = QtWidgets.QDialogButtonBox()
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
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

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(kullanici_adi_label, 0, 0)
        grid_layout.addWidget(self.kullanici_adi_line_edit, 0, 1)
        grid_layout.addWidget(sifre_label, 1, 0)
        grid_layout.addWidget(self.sifre_line_edit, 1, 1)
        grid_layout.addWidget(student_number_label, 2, 0)
        grid_layout.addWidget(self.student_number_line_edit, 2, 1)
        grid_layout.addWidget(student_pin_label, 3, 0)
        grid_layout.addWidget(self.student_pin_line_edit, 3, 1)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(grid_layout, 0)
        main_layout.addWidget(self.button_box, 1)

        self.setLayout(main_layout)

        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("rejected()"), self.reject)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    student_info = StudentInfo()
    student_info.show()

    sys.exit(app.exec_())

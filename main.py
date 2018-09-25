from PySide2 import QtCore, QtWidgets, QtGui
from sys import exit

import save_data
import curriculums
from StudentInfo import StudentInfo
from Transcript import Transcript
from sqlite3 import IntegrityError


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.transcript = Transcript()
        self.student_info = StudentInfo()

        self.selected_department = ""
        self.selectable_courses = {}
        self.current_season = ""
        self.destroy_app = 0

        self.resize(510, 700)
        self.setFixedWidth(510)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.menu_bar = QtWidgets.QMenuBar()

        self.file_menu = QtWidgets.QMenu("Dosya")
        self.open = self.file_menu.addAction("Aç")
        self.save = self.file_menu.addAction("Kaydet")
        self.save_as = self.file_menu.addAction("Farklı Kaydet")

        self.menu_bar.addMenu(self.file_menu)
        self.setMenuBar(self.menu_bar)

        user_name_label = QtWidgets.QLabel("Kullanıcı adı:")
        self.user_name_show_label = QtWidgets.QLabel("")
        self.user_select_button = QtWidgets.QPushButton("Transcript Yükle")

        user_layout = QtWidgets.QHBoxLayout()
        user_layout.addWidget(user_name_label, 0)
        user_layout.addWidget(self.user_name_show_label, 1)
        user_layout.addWidget(self.user_select_button, 2)

        code_select_label = QtWidgets.QLabel("Bölüm Kodu Seç")
        code_select_label.setMaximumSize(110, 25)
        education_year_label = QtWidgets.QLabel("Eğitim Yılını Seç")
        education_season_label = QtWidgets.QLabel("Eğitim Dönemini Seç")
        education_season_label.setMaximumSize(150, 25)
        self.code_select_cbox = QtWidgets.QComboBox()
        self.code_select_cbox.addItem("Seç")
        self.code_select_cbox.setFixedSize(100, 25)
        self.education_season_cbox = QtWidgets.QComboBox()
        self.education_year_cbox = QtWidgets.QComboBox()
        self.season_select = QtWidgets.QPushButton("Seç")
        hor_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding)

        top_grid_layout = QtWidgets.QGridLayout()
        top_grid_layout.addWidget(code_select_label, 0, 0)
        top_grid_layout.addWidget(self.code_select_cbox, 0, 1)
        top_grid_layout.addItem(hor_spacer, 0, 2)
        top_grid_layout.addWidget(education_year_label, 0, 3)
        top_grid_layout.addWidget(self.education_year_cbox, 0, 4)
        top_grid_layout.addWidget(education_season_label, 1, 3)
        top_grid_layout.addWidget(self.education_season_cbox, 1, 4)
        top_grid_layout.addWidget(self.season_select, 2, 4)

        self.course_table = QtWidgets.QTableWidget()
        self.course_table.setColumnCount(8)
        self.course_table.setFixedWidth(438)

        self.course_table.setColumnHidden(4, True)
        self.course_table.setColumnHidden(5, True)
        self.course_table.setColumnHidden(6, True)
        self.course_table.setColumnHidden(7, True)

        course_code_label = QtWidgets.QLabel("Ders Kodu")
        course_num_label = QtWidgets.QLabel("Ders Numarası")
        not_label = QtWidgets.QLabel("Not")
        gen_not_ort_label = QtWidgets.QLabel("Genel Not Ortalaması:")
        self.gpa_show_label = QtWidgets.QLabel()
        self.course_code_cbox = QtWidgets.QComboBox()
        self.course_code_cbox.addItem("Seç")
        self.course_num_cbox = QtWidgets.QComboBox()
        self.course_num_cbox.addItem("Seç")
        self.grade_cbox = QtWidgets.QComboBox()
        self.grade_cbox.addItem("Seç")
        self.gpa_show_label = QtWidgets.QLabel()
        self.remove_course_button = QtWidgets.QPushButton("Seçilen Dersi Çıkar")

        bottom_grid_layout = QtWidgets.QGridLayout()
        bottom_grid_layout.addWidget(course_code_label, 0, 0)
        bottom_grid_layout.addWidget(self.course_code_cbox, 0, 1)
        bottom_grid_layout.addWidget(self.remove_course_button, 0, 3)
        bottom_grid_layout.addWidget(course_num_label, 1, 0)
        bottom_grid_layout.addWidget(self.course_num_cbox, 1, 1)
        bottom_grid_layout.addWidget(gen_not_ort_label, 1, 2)
        bottom_grid_layout.addWidget(self.gpa_show_label, 1, 3)
        bottom_grid_layout.addWidget(not_label, 2, 0)
        bottom_grid_layout.addWidget(self.grade_cbox, 2, 1)

        self.add = QtWidgets.QPushButton("Ders Ekle")

        bottom_hor_layout = QtWidgets.QHBoxLayout()
        bottom_hor_layout.addWidget(self.add)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(user_layout, 0)
        main_layout.addLayout(top_grid_layout, 1)
        main_layout.addWidget(self.course_table, 2)
        main_layout.addLayout(bottom_grid_layout, 3)
        main_layout.addLayout(bottom_hor_layout, 4)

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("İTÜ Ortalama Hesaplayıcı")

        QtCore.QObject.connect(self.code_select_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.read_selected_department)
        QtCore.QObject.connect(self.course_code_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.set_course_num_cbox)
        QtCore.QObject.connect(self.education_year_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.set_education_season_cbox)
        QtCore.QObject.connect(self.season_select, QtCore.SIGNAL("clicked()"), self.add_season)
        QtCore.QObject.connect(self.add, QtCore.SIGNAL("clicked()"), self.add_course)
        QtCore.QObject.connect(self.remove_course_button, QtCore.SIGNAL("clicked()"), self.remove_row)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL("triggered()"), self.transcript.save_connection)

        if self.get_transcript_data():
            self.write_transcript_table()
            self.set_education_year_cbox()
            self.set_gpa_show_label()
            self.set_code_select_cbox(save_data.read_verify_departments_code())
            self.set_grade_cbox()
            self.set_user_name_label()
        else:
            exit()

    def closeEvent(self, event):
        replay = QtWidgets.QMessageBox.question(self, "Exit", "Kaydetmek ister misiniz?",
                                                QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.No |
                                                QtWidgets.QMessageBox.Yes)

        if replay == QtWidgets.QMessageBox.Yes:
            self.transcript.save_connection()
            self.transcript.close_connection()
        elif replay == QtWidgets.QMessageBox.No:
            self.transcript.close_connection()
        else:
            event.ignore()

    def set_code_select_cbox(self, departments: dict):
        for code in sorted(list(departments.values())):
            self.code_select_cbox.addItem(code)

    def set_course_code_cbox(self):
        self.course_code_cbox.clear()
        self.course_code_cbox.addItem("Seç")
        for code in sorted(self.selectable_courses.keys()):
            self.course_code_cbox.addItem(code)

    def set_course_num_cbox(self):
        department_code = self.course_code_cbox.currentText()
        self.course_num_cbox.clear()
        self.course_num_cbox.addItem("Seç")
        if department_code not in ["", "Seç"]:
            for code in sorted(set(self.selectable_courses[department_code])):
                self.course_num_cbox.addItem(code)

    def set_grade_cbox(self):
        for grades in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "VF"]:
            self.grade_cbox.addItem(grades)

    def set_education_year_cbox(self):
        years = self.calculate_years()

        for year in years:
            self.education_year_cbox.addItem(year)

    def set_education_season_cbox(self):
        self.education_season_cbox.clear()
        seasons = ["Güz", "Bahar", "Yaz Öğretimi"]
        education_year = self.education_year_cbox.currentText()
        last_season = self.transcript.get_last_season()
        last_year = last_season[:9]

        if education_year == last_year:
            for i in range(seasons.index(last_season[12:])+1, 3):
                self.education_season_cbox.addItem(seasons[i])
        else:
            for season in seasons:
                self.education_season_cbox.addItem(season)

    def set_gpa_show_label(self):
        self.gpa_show_label.setText(str(round(self.transcript.get_gpa(), 2)))

    def set_rows_header(self):
        course_counter = 1
        for i in range(self.course_table.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            if self.course_table.item(i, 5).text() == "Course":
                item.setText(str(course_counter))
                course_counter += 1
            else:
                item.setBackgroundColor(QtGui.QColor(QtCore.Qt.gray))
                item.setText("")
            self.course_table.setVerticalHeaderItem(i, item)

    def set_user_name_label(self):
        self.user_name_show_label.setText(self.transcript.user_name)

    def calculate_years(self):
        last_season = self.transcript.get_last_season()

        years = []
        if last_season[12:] != "Yaz Öğretimi":
            first_ind = 0
        else:
            first_ind = 1

        for i in range(first_ind, 5):
            years.append(str(int(last_season[:4]) + i) + "-" + str(int(last_season[5:9]) + i))
        return years

    def read_selected_department(self):
        self.selected_department = self.code_select_cbox.currentText()
        self.selectable_courses = curriculums.parse_courses_code(self.selected_department)
        self.set_course_code_cbox()

    def read_course_code_cbox(self):
        return self.course_code_cbox.currentText()

    def read_course_num_cbox(self):
        return self.course_num_cbox.currentText()

    def read_grade_cbox(self):
        return self.grade_cbox.currentText()

    def add_row(self, row_data, row_number=None):
        if not row_number:
            row_number = self.course_table.rowCount()

        if row_data[5] == "Course":
            self.add_course_row(row_data, row_number)
        elif row_data[5] == "Season":
            self.add_season_row(row_data, row_number)

    def add_season_row(self, row_data, row_number):
        self.course_table.insertRow(row_number)

        for i, data in enumerate(row_data):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setBackgroundColor(QtGui.QColor(QtCore.Qt.gray))
            self.course_table.setItem(row_number, i, item)

    def add_course_row(self, row_data, row_number):
        self.course_table.insertRow(row_number)

        for i, data in enumerate(row_data):
            if row_data[4] and i == 3:
                grade_cbox = QtWidgets.QComboBox()
                if row_data[7]:
                    grade_cbox.setEnabled(False)
                    grade_cbox.addItem(data)
                else:
                    if int(row_data[2]):
                        for grades in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "VF"]:
                            grade_cbox.addItem(grades)
                    else:
                        for grades in ["BZ", "BL"]:
                            grade_cbox.addItem(grades)
                    grade_cbox.setCurrentText(data.strip())
                self.course_table.setCellWidget(row_number, i, grade_cbox)

                QtCore.QObject.connect(self.course_table.cellWidget(row_number, i),
                                       QtCore.SIGNAL("currentIndexChanged(QString)"),
                                       self.update_course_data)

            else:
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.course_table.setItem(row_number, i, item)

    def add_season(self):
        education_year = self.education_year_cbox.currentText()
        education_season = self.education_season_cbox.currentText()
        season = education_year + " / " + education_season
        self.current_season = season

        try:
            self.transcript.add_season(season)
            self.write_transcript_table()
        except IntegrityError:
            pass

    def add_course(self):
        if not self.current_season:
            QtWidgets.QMessageBox.information(self, "Hata", "Önce Dönem Seçin!", QtWidgets.QMessageBox.Ok)
        else:
            course_code = self.read_course_code_cbox()
            if course_code == "Seç":
                QtWidgets.QMessageBox.information(self, "Hata", "Ders Kodu Seçin", QtWidgets.QMessageBox.Ok)
                return False

            course_num = self.read_course_num_cbox()
            if course_num == "Seç":
                QtWidgets.QMessageBox.information(self, "Hata", "Ders No Seçin", QtWidgets.QMessageBox.Ok)
                return False

            course_grade = self.read_grade_cbox()
            if course_grade == "Seç":
                QtWidgets.QMessageBox.information(self, "Hata", "Ders Notu Seçin", QtWidgets.QMessageBox.Ok)
                return False

            course_data = self.find_course_data(course_code + " " + course_num)
            data = [course_data["Ders Kodu"], course_data["Ders Adı"], course_data["Kredi"], course_grade, 0,
                    self.current_season]

            try:
                self.transcript.check_course_before_added(data[0])
                self.transcript.add_course(data)
                self.write_transcript_table()
                self.set_gpa_show_label()
            except IntegrityError:
                QtWidgets.QMessageBox.information(self, "Hata", "Bir Döneme Aynı Dersten İki Tane Eklenemez",
                                                  QtWidgets.QMessageBox.Ok)

    def write_transcript_table(self):
        self.course_table.clear()
        self.course_table.setRowCount(0)
        transcript_data = self.transcript.get_transcript_data()

        for row in transcript_data:
            self.add_row(row)

        self.set_rows_header()

        self.course_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Ders Kodu"))
        self.course_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Ders İsmi"))
        self.course_table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Kredi"))
        self.course_table.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Not"))
        self.course_table.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Editable"))
        self.course_table.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Tag"))
        self.course_table.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("Season Name"))
        self.course_table.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("Passive"))

    def find_course_data(self, course_code):
        department_code = self.code_select_cbox.currentText()

        courses = save_data.read_elective_courses(department_code) + save_data.read_departments_curriculum(
            department_code)

        for item in courses:
            key = item["Ders Kodu"]
            if course_code == key or course_code[:-1] == key or course_code == key[:-1]:
                item["Ders Kodu"] = course_code
                return item
        return {}

    def update_course_data(self):
        table_data = []
        for row in reversed(range(self.course_table.rowCount())):
            if self.course_table.item(row, 4).text() == '0':
                break
            elif self.course_table.item(row, 5).text() == "Season":
                continue
            table_data.append([self.course_table.cellWidget(row, 3).currentText(),
                               self.course_table.item(row, 6).text()])

        db_data = self.transcript.get_editable_data()

        for i, course in enumerate(reversed(db_data)):
            if table_data[i][0] != course[1].strip():
                self.transcript.update_course(table_data[i][1], course[0], table_data[i][0])
                self.transcript.update_season_gpa(table_data[i][1])
                self.update_season_gpa(table_data[i][1])
                break

        self.set_gpa_show_label()

    def update_season_gpa(self, season_name):
        gpa = self.transcript.get_season_gpa(season_name)

        for row in reversed(range(self.course_table.rowCount())):
            if self.course_table.item(row, 5).text() == "Season" \
               and self.course_table.item(row, 0).text() == season_name[:9] \
               and self.course_table.item(row, 1).text() == season_name[12:]:
                item = self.course_table.takeItem(row, 3)
                item.setText(str(gpa))
                self.course_table.setItem(row, 3, item)

    def remove_row(self):
        current_row = self.course_table.currentRow()
        if self.course_table.item(current_row, 4).text() == "0":
            QtWidgets.QMessageBox.information(self, "Hata", "Bu Satırı Silemezsiniz.", QtWidgets.QMessageBox.Ok)
            return

        if self.course_table.item(current_row, 5).text() == "Course":
            self.transcript.delete_course(self.course_table.item(current_row, 6).text(),
                                          self.course_table.item(current_row, 0).text())
            self.transcript.update_season_gpa(self.course_table.item(current_row, 6).text())
            self.transcript.update_season_credit(self.course_table.item(current_row, 6).text())
            self.write_transcript_table()
            self.set_gpa_show_label()
        else:
            self.transcript.delete_season(self.course_table.item(current_row, 6).text())
            self.write_transcript_table()
            self.set_gpa_show_label()

    def get_transcript_data(self):
        self.student_info.reset_student_info()
        self.student_info.show()

        replay = self.student_info.exec_()

        if replay == QtWidgets.QDialog.Accepted:
            self.transcript.set_user_name(self.student_info.user_name)
            self.transcript.set_path(self.student_info.path)
            self.user_name_show_label.setText(self.transcript.user_name)
            return 1
        else:
            return 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

from PySide2 import QtCore, QtWidgets, QtGui

import transcript
import save_data
import curriculums
import calculations
from StudentInfo import StudentInfo


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.selected_department = ""
        self.selectable_courses = {}
        self.data_course_table = {}
        self.last_season_data = ""
        self.current_season_data = []
        self.number_of_courses = 0
        self.seasons_index = {}
        self.banned_row_number = 0
        self.old_courses = save_data.read_old_courses()
        self.user_name = ""
        self.student_info = None
        self.file_directory = None

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
        self.course_table.setColumnCount(4)
        self.course_table.setFixedWidth(438)

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
        self.remove_course = QtWidgets.QPushButton("Seçilen Dersi Çıkar")

        bottom_grid_layout = QtWidgets.QGridLayout()
        bottom_grid_layout.addWidget(course_code_label, 0, 0)
        bottom_grid_layout.addWidget(self.course_code_cbox, 0, 1)
        bottom_grid_layout.addWidget(self.remove_course, 0, 3)
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
        QtCore.QObject.connect(self.add, QtCore.SIGNAL("clicked()"), self.add_course)
        QtCore.QObject.connect(self.season_select, QtCore.SIGNAL("clicked()"), self.set_current_season_data)
        QtCore.QObject.connect(self.remove_course, QtCore.SIGNAL("clicked()"), self.delete_course)
        QtCore.QObject.connect(self.user_select_button, QtCore.SIGNAL("clicked()"), self.get_transcript_data)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL("triggered()"), self.save_transcript)
        QtCore.QObject.connect(self.save_as, QtCore.SIGNAL("triggered()"), self.save_as_transcript)
        QtCore.QObject.connect(self.open, QtCore.SIGNAL("triggered()"), self.open_transcript)

        if not self.data_course_table:
            self.get_transcript_data()
        else:
            self.write_transcript_table()
            self.set_seasons_ort()
            self.set_education_year_cbox()
            self.set_education_season_cbox()
            self.set_gpa_show_label()

        for grades in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "VF"]:
            self.grade_cbox.addItem(grades)

        self.set_code_select_cbox(save_data.read_verify_departments_code())

    def read_course_code_cbox(self):
        return self.course_code_cbox.currentText()

    def read_course_num_cbox(self):
        return self.course_num_cbox.currentText()

    def read_grade_cbox(self):
        return self.grade_cbox.currentText()

    def read_selected_department(self):
        self.selected_department = self.code_select_cbox.currentText()
        self.selectable_courses = curriculums.parse_courses_code(self.selected_department)
        self.set_course_code_cbox()

    def read_courses_data(self):
        courses_data = []
        for courses in self.data_course_table.values():
            for course in courses:
                course_grade = course["Not"]
                if course_grade[-1] == "*" or course_grade == "M " or course_grade == "T ":
                    continue
                courses_data.append({"Kredi": course["Kredi"], "Not": course["Not"]})
        return courses_data

    def set_course_num_cbox(self):
        department_code = self.course_code_cbox.currentText()
        self.course_num_cbox.clear()
        self.course_num_cbox.addItem("Seç")
        if department_code not in ["", "Seç"]:
            for code in sorted(set(self.selectable_courses[department_code])):
                self.course_num_cbox.addItem(code)

    def set_course_code_cbox(self):
        self.course_code_cbox.clear()
        self.course_code_cbox.addItem("Seç")
        for code in sorted(self.selectable_courses.keys()):
            self.course_code_cbox.addItem(code)

    def set_code_select_cbox(self, departments: dict):
        for code in sorted(list(departments.values())):
            self.code_select_cbox.addItem(code)

    def set_education_year_cbox(self):
        years = self.calculate_years()

        for year in years:
            self.education_year_cbox.addItem(year)

    def set_education_season_cbox(self):
        self.education_season_cbox.clear()
        seasons = ["Güz", "Bahar", "Yaz Öğretimi"]
        education_year = self.education_year_cbox.currentText()
        last_year = str(self.last_season_data[0][0]) + "-" + str(self.last_season_data[0][1])

        if education_year == last_year:
            for i in range(seasons.index(self.last_season_data[1])+1, 3):
                self.education_season_cbox.addItem(seasons[i])
        else:
            for season in seasons:
                self.education_season_cbox.addItem(season)

    def set_current_season_data(self):
        year_data = self.education_year_cbox.currentText().split("-")
        season_data = self.education_season_cbox.currentText()
        seasons = list(self.seasons_index.keys())

        self.current_season_data = [year_data, season_data]
        if not self.convert_to_string_season_data(self.current_season_data) in seasons:
            self.add_season_table(self.current_season_data)
            self.data_course_table[self.convert_to_string_season_data(self.current_season_data)] = []

    def set_rows_header(self):
        course_counter = 1
        for i in range(self.course_table.rowCount()):
            item = self.course_table.takeVerticalHeaderItem(i)
            if item.text() != "":
                item.setText(str(course_counter))
                course_counter += 1
            self.course_table.setVerticalHeaderItem(i, item)

    def set_gpa_show_label(self):
        self.gpa_show_label.setText(str(calculations.calculate_gpa(self.read_courses_data())))

    def set_seasons_index(self):
        for i in range(self.course_table.rowCount()):
            try:
                float(self.course_table.item(i, 3).text())
                season = self.course_table.item(i, 0).text() + " / " + self.course_table.item(i, 1).text()
                self.seasons_index[season] = i
            except ValueError:
                pass
            except AttributeError:
                pass

        copy_seasons_index = dict(self.seasons_index)
        for season in self.seasons_index.keys():
            if season not in self.data_course_table.keys():
                copy_seasons_index.pop(season)
        self.seasons_index = copy_seasons_index

    def set_seasons_ort(self):
        for name, index in self.seasons_index.items():
            data = []
            for course in self.data_course_table[name]:
                data.append({"Kredi": course["Kredi"], "Not": course["Not"]})
            gpa_calculations = calculations.calculate_gpa(data, credit=True)

            item = self.course_table.takeItem(index, 2)
            item.setText(str(gpa_calculations[1]))
            self.course_table.setItem(index, 2, item)

            item = self.course_table.takeItem(index, 3)
            item.setText(str(gpa_calculations[0]))
            self.course_table.setItem(index, 3, item)

    def get_transcript_data(self):
        self.student_info = StudentInfo()
        self.student_info.reset_student_info()
        self.student_info.show()

        if self.student_info.exec_() == QtWidgets.QDialog.Accepted:
            self.user_name = self.student_info.user_name
            self.user_name_show_label.setText(self.user_name)
            self.file_directory = "./Data/Transcripts/" + self.user_name + ".json"
            if self.student_info.transcript_data:
                self.data_course_table = self.student_info.transcript_data
            else:
                self.data_course_table = save_data.read_transcript(self.user_name)
            self.last_season_data = self.parse_season_name_to_data(list(self.data_course_table.keys())[-1])

            self.write_transcript_table()
            self.set_seasons_ort()
            self.set_education_year_cbox()
            self.set_education_season_cbox()
            self.set_gpa_show_label()

    def add_course_table(self, courses, user_edit=False):
        for course in courses:
            row_count = self.calculate_row_number()
            self.course_table.insertRow(row_count)
            self.number_of_courses += 1
            self.course_table.setVerticalHeaderItem(row_count, QtWidgets.QTableWidgetItem(str(self.number_of_courses)))
            for i, course_data in enumerate(course.values()):
                if (user_edit is True) and (i == 3):
                    note_combo_box = QtWidgets.QComboBox()
                    if not int(self.course_table.item(row_count, 2).text()):
                        for grades in ["BZ", "BL"]:
                            note_combo_box.addItem(grades)
                    else:
                        for grades in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "VF"]:
                            note_combo_box.addItem(grades)
                    note_combo_box.setCurrentText(course_data)
                    self.course_table.setCellWidget(row_count, i, note_combo_box)
                    QtCore.QObject.connect(self.course_table.cellWidget(row_count, i),
                                           QtCore.SIGNAL("currentIndexChanged(QString)"),
                                           self.update_courses_data_from_note_cbox)
                else:
                    item = QtWidgets.QTableWidgetItem(course_data)
                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    self.course_table.setItem(row_count, i, item)

    def add_course(self):
        if not self.current_season_data:
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

            season = self.convert_to_string_season_data(self.current_season_data)
            course_data = self.find_course_data(course_code + " " + course_num)
            course_data["Not"] = course_grade

            if self.check_course_before_added_current_season(course_data):
                QtWidgets.QMessageBox.information(self, "Hata", "Bir Dersi Aynı Döneme İki Kere Ekleyemezsiniz",
                                                  QtWidgets.QMessageBox.Ok)
                return False

            self.add_course_table([course_data], user_edit=True)
            self.data_course_table[season].append(course_data)
            self.check_course_before_added(course_data)
            self.set_seasons_index()
            self.set_gpa_show_label()
            self.set_seasons_ort()
        return True

    def add_season_table(self, season_data):
        row_count = self.course_table.rowCount()
        self.seasons_index[self.convert_to_string_season_data(season_data)] = row_count
        column_count = self.course_table.columnCount()
        year = str(season_data[0][0]) + "-" + str(season_data[0][1])

        self.course_table.insertRow(row_count)
        self.course_table.setVerticalHeaderItem(row_count, QtWidgets.QTableWidgetItem(""))
        self.course_table.verticalHeaderItem(row_count).setBackgroundColor(QtGui.QColor(QtCore.Qt.gray))

        self.course_table.setItem(row_count, 0, QtWidgets.QTableWidgetItem(year))
        self.course_table.setItem(row_count, 1, QtWidgets.QTableWidgetItem(season_data[1]))
        for column in range(2, column_count):
            self.course_table.setItem(row_count, column, QtWidgets.QTableWidgetItem(""))

        for column in range(column_count):
            self.course_table.item(row_count, column).setBackgroundColor(QtGui.QColor(QtCore.Qt.gray))
            self.course_table.item(row_count, column).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

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

    def calculate_years(self):
        current_year = self.last_season_data[0]
        years = []

        if self.last_season_data[1] != "Yaz Öğretimi":
            first_ind = 0
        else:
            first_ind = 1

        for i in range(first_ind, 5):
            years.append(str(current_year[0] + i) + "-" + str(current_year[1] + i))
        return years

    def calculate_row_number(self):
        if not self.current_season_data:
            return self.course_table.rowCount()

        current_season = self.convert_to_string_season_data(self.current_season_data)
        seasons = list(self.seasons_index.keys())
        index = list(self.seasons_index.values())

        if current_season == seasons[-1]:
            return self.course_table.rowCount()
        for i, season in enumerate(seasons):
            if current_season == season:
                return index[i+1]
        return False

    def write_transcript_table(self):
        self.course_table.clear()

        self.number_of_courses = 0
        self.seasons_index = {}
        self.banned_row_number = 0

        self.course_table.setRowCount(0)

        self.course_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Ders Kodu"))
        self.course_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Ders İsmi"))
        self.course_table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Kredi"))
        self.course_table.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Not"))

        for season, season_courses in self.data_course_table.items():
            self.add_season_table(transcript.parse_season_name(season))
            self.add_course_table(season_courses)
        self.banned_row_number = self.number_of_courses + len(self.data_course_table) - 1

    @staticmethod
    def convert_to_string_season_data(season_data):
        return str(season_data[0][0]) + "-" + str(season_data[0][1]) + " / " + season_data[1]

    def check_course_before_added(self, course_data):
        if course_data["Ders Kodu"][-1] == "E":
            course_codes = [course_data["Ders Kodu"], course_data["Ders Kodu"][:-1]]
        else:
            course_codes = [course_data["Ders Kodu"], course_data["Ders Kodu"] + "E"]
        try:
            course_codes.append(self.old_courses[course_codes[0]])
        except KeyError:
            pass
        try:
            course_codes.append(self.old_courses[course_codes[1]])
        except KeyError:
            pass

        index = self.course_table.rowCount() - 1
        for season_data in reversed(list(self.data_course_table.items())):
            for j, course in reversed(list(enumerate(season_data[1]))):
                if course["Ders Kodu"] in course_codes and season_data[0] !=\
                        self.convert_to_string_season_data(self.current_season_data):
                    self.update_course_note(index, course["Not"], season_data[0], j)
                    return True
                index -= 1
            index -= 1
        return False

    def check_course_before_added_current_season(self, course_data):
        if course_data["Ders Kodu"][-1] == "E":
            course_codes = [course_data["Ders Kodu"], course_data["Ders Kodu"][:-1]]
        else:
            course_codes = [course_data["Ders Kodu"], course_data["Ders Kodu"] + "E"]

        current_season_name = self.convert_to_string_season_data(self.current_season_data)

        for course in self.data_course_table[current_season_name]:
            if course["Ders Kodu"] in course_codes:
                return True
        return False

    def delete_course(self, current_row=None):
        if current_row is None:
            current_row = self.course_table.currentRow()

        course_data = []
        if current_row > self.banned_row_number:
            courses_data = dict(self.data_course_table)
            counter = -1
            for season, courses in self.data_course_table.items():
                counter += 1
                if counter == current_row:
                    for i in range(len(self.data_course_table[season])):
                        self.course_table.removeRow(counter + 1)
                        self.number_of_courses -= 1
                        if season == self.convert_to_string_season_data(self.current_season_data):
                            self.current_season_data = []
                    courses_data.pop(season)
                for i in range(len(courses)):
                    counter += 1
                    if counter == current_row:
                        course_data = courses_data[season].pop(i)
                        self.number_of_courses -= 1

            self.course_table.removeRow(current_row)
            self.data_course_table = courses_data
            self.set_rows_header()
            if not course_data == []:
                self.check_course_before_added(course_data)
            self.set_gpa_show_label()
            self.set_seasons_index()
            self.set_seasons_ort()
        else:
            QtWidgets.QMessageBox.information(self, "Hata", "Bu Satırı Kaldıramazsınız",
                                              QtWidgets.QMessageBox.Ok)

    def update_courses_data_from_note_cbox(self):
        self.update_data_course_table()
        self.set_gpa_show_label()
        self.set_seasons_ort()

    def update_data_course_table(self):
        course_counter = 0
        season = ""
        for i in range(self.course_table.rowCount()):
            if i in self.seasons_index.values():
                season = self.course_table.item(i, 0).text() + " / " + self.course_table.item(i, 1).text()
                course_counter = 0
                continue
            try:
                item_text = self.course_table.cellWidget(i, 3).currentText()
                if item_text != self.data_course_table[season][course_counter]["Not"]:
                    self.data_course_table[season][course_counter]["Not"] = item_text
            except AttributeError:
                pass
            course_counter += 1

    def update_course_note(self, table_index, note, season, season_index):
        if note[-1] == "*":
            new_note = note[:-1]
            self.data_course_table[season][season_index]["Not"] = new_note
            try:
                item = self.course_table.takeItem(table_index, 3)
                item.setText(new_note)
                self.course_table.setItem(table_index, 3, item)
            except AttributeError:
                item = self.course_table.cellWidget(table_index, 3)
                item.setItemText(item.currentIndex(), new_note)
                item.setEnabled(True)
                self.course_table.setCellWidget(table_index, 3, item)
        else:
            new_note = note + "*"
            self.data_course_table[season][season_index]["Not"] = new_note
            try:
                item = self.course_table.takeItem(table_index, 3)
                item.setText(new_note)
                self.course_table.setItem(table_index, 3, item)
            except AttributeError:
                item = self.course_table.cellWidget(table_index, 3)
                item.setItemText(item.currentIndex(), new_note)
                item.setEnabled(False)
                self.course_table.setCellWidget(table_index, 3, item)

    @staticmethod
    def parse_season_name_to_data(season_name):
        parsed = season_name.split(" / ")

        years = parsed[0].split("-")
        years = [int(years[0]), int(years[1])]

        season = parsed[1]
        return [years, season]

    def save_transcript(self):
        if self.file_directory is None:
            file_directory, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Transcript Kaydet",
                                                                           "./Data/Transcripts", "(*.json)")
            if file_directory is None:
                return

            self.file_directory = file_directory
            if self.file_directory[-5:] != ".json":
                self.file_directory = self.file_directory + ".json"

    def save_as_transcript(self):
        file_directory, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Transcript Kaydet",
                                                                  QtCore.QDir.homePath(), "(*.json)")

        if file_directory is "":
            return

        self.file_directory = file_directory
        if self.file_directory[-5:] != ".json":
            self.file_directory = self.file_directory + ".json"

        save_data.save_transcript(self.data_course_table, directory=self.file_directory)

        self.user_name = self.file_directory.split("/")[-1].split(".")[0]
        self.user_name_show_label.setText(self.user_name)

    def open_transcript(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Transcript",
                                                             "./Data/Transcripts", "(*.json)")

        if not file_name:
            return None

        data = save_data.read_transcript(directory=file_name)

        if not transcript.is_transcript(data):
            QtWidgets.QMessageBox.information(self, "Hata", "Bu dosya bir transcript değil.", QtWidgets.QMessageBox.Ok)
            return

        self.file_directory = file_name
        self.data_course_table = data
        self.user_name = file_name.split("/")[-1].split(".")[0]
        self.last_season_data = self.parse_season_name_to_data(list(self.data_course_table.keys())[-1])

        self.write_transcript_table()
        self.set_seasons_ort()
        self.set_education_year_cbox()
        self.set_education_season_cbox()
        self.set_gpa_show_label()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

from PySide2 import QtCore, QtWidgets, QtGui

from not_hesaplama import Ui_MainWindow
import transcript
import data
import save_data
import curriculums
import hesaplamalar


class CustomWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.secilen_bolum = ""
        self.secilecek_dersler = {}
        self.data_lesson_table = transcript.edit_transcript_data(*transcript.parse_transcript_data(data.site_data))
        self.last_season_data = transcript.get_last_season()
        self.current_season_data = []
        self.number_of_courses = 0
        self.seasons_index = {}
        self.yasak_row_number = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.write_transcript_table()
        self.set_seasons_ort()
        self.set_egitim_yili_cbox()
        self.set_egitim_donemi_cbox()

        for notlar in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "VF"]:
            self.not_cbox.addItem(notlar)

        self.set_kod_sec_cbox(save_data.read_verify_departments_code())
        self.set_gen_not_ort_gos()

        QtCore.QObject.connect(self.kod_sec_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.read_secilen_bolum)
        QtCore.QObject.connect(self.ders_kodu_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.set_ders_no_cbox)
        QtCore.QObject.connect(self.egitim_yili_cbox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.set_egitim_donemi_cbox)
        QtCore.QObject.connect(self.add, QtCore.SIGNAL("clicked()"), self.add_lesson)
        QtCore.QObject.connect(self.season_select, QtCore.SIGNAL("clicked()"), self.set_current_season_data)
        QtCore.QObject.connect(self.ders_cikar, QtCore.SIGNAL("clicked()"), self.delete_course)

    def read_ders_kodu_cbox(self):
        return self.ders_kodu_cbox.currentText()

    def read_ders_no_cbox(self):
        return self.ders_no_cbox.currentText()

    def read_not_cbox(self):
        return self.not_cbox.currentText()

    def read_secilen_bolum(self):
        self.secilen_bolum = self.kod_sec_cbox.currentText()
        self.secilecek_dersler = curriculums.parse_lessons_code(self.secilen_bolum)
        self.set_ders_kodu_cbox()

    def read_courses_data(self):
        courses_data = []
        for couses in self.data_lesson_table.values():
            for course in couses:
                ders_not = course["Not"]
                if ders_not[-1] == "*" or ders_not == "M " or ders_not == "T ":
                    continue
                courses_data.append({"Kredi": course["Kredi"], "Not": course["Not"]})
        return courses_data

    def set_ders_no_cbox(self):
        bolum_code = self.ders_kodu_cbox.currentText()
        self.ders_no_cbox.clear()
        self.ders_no_cbox.addItem("Seç")
        if bolum_code not in ["", "Seç"]:
            for code in sorted(set(self.secilecek_dersler[bolum_code])):
                self.ders_no_cbox.addItem(code)

    def set_ders_kodu_cbox(self):
        self.ders_kodu_cbox.clear()
        self.ders_kodu_cbox.addItem("Seç")
        for code in sorted(self.secilecek_dersler.keys()):
            self.ders_kodu_cbox.addItem(code)

    def set_kod_sec_cbox(self, departments: dict):
        for code in sorted(list(departments.values())):
            self.kod_sec_cbox.addItem(code)

    def set_egitim_yili_cbox(self):
        years = self.calculate_years()

        for year in years:
            self.egitim_yili_cbox.addItem(year)

    def set_egitim_donemi_cbox(self):
        self.egitim_donemi_cbox.clear()
        seasons = ["Güz", "Bahar", "Yaz Öğretimi"]
        egitim_yili = self.egitim_yili_cbox.currentText()
        last_year = str(self.last_season_data[0][0]) + "-" + str(self.last_season_data[0][1])

        if egitim_yili == last_year:
            for i in range(seasons.index(self.last_season_data[1])+1, 3):
                self.egitim_donemi_cbox.addItem(seasons[i])
        else:
            for season in seasons:
                self.egitim_donemi_cbox.addItem(season)

    def set_current_season_data(self):
        year_data = self.egitim_yili_cbox.currentText().split("-")
        donem_data = self.egitim_donemi_cbox.currentText()
        seasons = list(self.seasons_index.keys())

        self.current_season_data = [year_data, donem_data]
        if not self.convert_to_string_season_data(self.current_season_data) in seasons:
            self.add_season_table(self.current_season_data)
            self.data_lesson_table[self.convert_to_string_season_data(self.current_season_data)] = []

    def set_rows_header(self):
        course_counter = 1
        for i in range(self.lesson_table.rowCount()):
            item = self.lesson_table.takeVerticalHeaderItem(i)
            if item.text() != "":
                item.setText(str(course_counter))
                course_counter += 1
            self.lesson_table.setVerticalHeaderItem(i, item)

    def set_gen_not_ort_gos(self):
        self.gen_not_ort_gos.setText(str(hesaplamalar.genel_ort_hesapla(self.read_courses_data())))

    def set_seasons_index(self):
        for i in range(self.lesson_table.rowCount()):
            try:
                float(self.lesson_table.item(i, 3).text())
                season = self.lesson_table.item(i, 0).text() + " / " + self.lesson_table.item(i, 1).text()
                self.seasons_index[season] = i
            except ValueError:
                pass
            except AttributeError:
                pass

        copy_seasons_index = dict(self.seasons_index)
        for season in self.seasons_index.keys():
            if season not in self.data_lesson_table.keys():
                copy_seasons_index.pop(season)
        self.seasons_index = copy_seasons_index

    def set_seasons_ort(self):
        for name, index in self.seasons_index.items():
            veri = []
            for course in self.data_lesson_table[name]:
                veri.append({"Kredi": course["Kredi"], "Not": course["Not"]})
            hesaplama = hesaplamalar.genel_ort_hesapla(veri, kredi=True)

            item = self.lesson_table.takeItem(index, 2)
            item.setText(str(hesaplama[1]))
            self.lesson_table.setItem(index, 2, item)

            item = self.lesson_table.takeItem(index, 3)
            item.setText(str(hesaplama[0]))
            self.lesson_table.setItem(index, 3, item)

    def add_lesson_table(self, dersler, user_edit=False):
        for ders in dersler:
            row_count = self.calculate_row_number()
            self.lesson_table.insertRow(row_count)
            self.number_of_courses += 1
            self.lesson_table.setVerticalHeaderItem(row_count, QtWidgets.QTableWidgetItem(str(self.number_of_courses)))
            for i, ders_data in enumerate(ders.values()):
                if (user_edit is True) and (i == 3):
                    note_combo_box = QtWidgets.QComboBox()
                    if not int(self.lesson_table.item(row_count, 2).text()):
                        for notlar in ["BZ", "BL"]:
                            note_combo_box.addItem(notlar)
                    else:
                        for notlar in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "VF"]:
                            note_combo_box.addItem(notlar)
                    note_combo_box.setCurrentText(ders_data)
                    self.lesson_table.setCellWidget(row_count, i, note_combo_box)
                    QtCore.QObject.connect(self.lesson_table.cellWidget(row_count, i),
                                           QtCore.SIGNAL("currentIndexChanged(QString)"),
                                           self.update_couses_data_from_note_cbox)
                else:
                    item = QtWidgets.QTableWidgetItem(ders_data)
                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    self.lesson_table.setItem(row_count, i, item)

    def add_lesson(self):
        if not self.current_season_data:
            self.create_message_box("Önce Dönem Seçin!")
        else:
            ders_kodu = self.read_ders_kodu_cbox()
            if ders_kodu == "Seç":
                self.create_message_box("Ders Kodu Seçin")
                return False

            ders_no = self.read_ders_no_cbox()
            if ders_no == "Seç":
                self.create_message_box("Ders No Seçin")
                return False

            ders_not = self.read_not_cbox()
            if ders_not == "Seç":
                self.create_message_box("Ders Notu Seçin")
                return False

            season = self.convert_to_string_season_data(self.current_season_data)
            ders_bigi = self.find_lesson_data(ders_kodu + " " + ders_no)
            ders_bigi["Not"] = ders_not

            if self.check_course_before_added_current_season(ders_bigi):
                self.create_message_box("Bir Dersi Aynı Döneme İki Kere Ekleyemezsiniz")
                return False

            self.add_lesson_table([ders_bigi], user_edit=True)
            self.data_lesson_table[season].append(ders_bigi)
            self.check_lessen_before_added(ders_bigi)
            self.set_seasons_index()
            self.set_gen_not_ort_gos()
            self.set_seasons_ort()
        return True

    def add_season_table(self, season_data):
        row_count = self.lesson_table.rowCount()
        self.seasons_index[self.convert_to_string_season_data(season_data)] = row_count
        column_count = self.lesson_table.columnCount()
        year = str(season_data[0][0]) + "-" + str(season_data[0][1])

        self.lesson_table.insertRow(row_count)
        self.lesson_table.setVerticalHeaderItem(row_count, QtWidgets.QTableWidgetItem(""))
        self.lesson_table.verticalHeaderItem(row_count).setBackgroundColor(QtGui.QColor(QtCore.Qt.gray))

        self.lesson_table.setItem(row_count, 0, QtWidgets.QTableWidgetItem(year))
        self.lesson_table.setItem(row_count, 1, QtWidgets.QTableWidgetItem(season_data[1]))
        for column in range(2, column_count):
            self.lesson_table.setItem(row_count, column, QtWidgets.QTableWidgetItem(""))

        for column in range(column_count):
            self.lesson_table.item(row_count, column).setBackgroundColor(QtGui.QColor(QtCore.Qt.gray))
            self.lesson_table.item(row_count, column).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

    def find_lesson_data(self, lesson_code):
        bolum_code = self.kod_sec_cbox.currentText()

        dersler = save_data.read_secmeli_ders(bolum_code) + save_data.read_depatments_cirriculum(bolum_code)

        for item in dersler:
            key = item["Ders Kodu"]
            if lesson_code == key or lesson_code[:-1] == key or lesson_code == key[:-1]:
                item["Ders Kodu"] = lesson_code
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
            return self.lesson_table.rowCount()

        current_season = self.convert_to_string_season_data(self.current_season_data)
        seasons = list(self.seasons_index.keys())
        index = list(self.seasons_index.values())

        if current_season == seasons[-1]:
            return self.lesson_table.rowCount()
        for i, season in enumerate(seasons):
            if current_season == season:
                return index[i+1]
        return False

    def write_transcript_table(self):
        for donem, donem_dersleri in self.data_lesson_table.items():
            self.add_season_table(transcript.parse_season_name(donem))
            self.add_lesson_table(donem_dersleri)
        self.yasak_row_number = self.number_of_courses + len(self.data_lesson_table) - 1

    def convert_to_string_season_data(self, season_data):
        return str(season_data[0][0]) + "-" + str(season_data[0][1]) + " / " + season_data[1]

    def check_lessen_before_added(self, course_data):
        if course_data["Ders Kodu"][-1] == "E":
            course_codes = [course_data["Ders Kodu"], course_data["Ders Kodu"][:-1]]
        else:
            course_codes = [course_data["Ders Kodu"], course_data["Ders Kodu"] + "E"]

        index = self.lesson_table.rowCount()-1
        for season_data in reversed(list(self.data_lesson_table.items())):
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

        for course in self.data_lesson_table[current_season_name]:
            if course["Ders Kodu"] in course_codes:
                return True
        return False

    def delete_course(self, current_row=None):
        if current_row is None:
            current_row = self.lesson_table.currentRow()

        course_data = []
        if current_row > self.yasak_row_number:
            courses_data = dict(self.data_lesson_table)
            counter = -1
            for season, courses in self.data_lesson_table.items():
                counter += 1
                if counter == current_row:
                    for i in range(len(self.data_lesson_table[season])):
                        self.lesson_table.removeRow(counter+1)
                        self.number_of_courses -= 1
                        if season == self.convert_to_string_season_data(self.current_season_data):
                            self.current_season_data = []
                    courses_data.pop(season)
                for i in range(len(courses)):
                    counter += 1
                    if counter == current_row:
                        course_data = courses_data[season].pop(i)
                        self.number_of_courses -= 1

            self.lesson_table.removeRow(current_row)
            self.data_lesson_table = courses_data
            self.set_rows_header()
            if not course_data == []:
                self.check_lessen_before_added(course_data)
            self.set_gen_not_ort_gos()
            self.set_seasons_index()
            self.set_seasons_ort()
        else:
            self.create_message_box("Bu Satırı Kaldıramzsınız")

    def create_message_box(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(str(message))
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def update_couses_data_from_note_cbox(self):
        self.update_data_lesson_table()
        self.set_gen_not_ort_gos()
        self.set_seasons_ort()

    def update_data_lesson_table(self):
        course_counter = 0
        season = ""
        for i in range(self.lesson_table.rowCount()):
            if i in self.seasons_index.values():
                season = self.lesson_table.item(i, 0).text() + " / " + self.lesson_table.item(i, 1).text()
                course_counter = 0
                continue
            try:
                item_text = self.lesson_table.cellWidget(i, 3).currentText()
                if item_text != self.data_lesson_table[season][course_counter]["Not"]:
                    self.data_lesson_table[season][course_counter]["Not"] = item_text
            except AttributeError:
                pass
            course_counter += 1

    def update_course_note(self, table_index, note, season, season_index):
        if note[-1] == "*":
            new_note = note[:-1]
            self.data_lesson_table[season][season_index]["Not"] = new_note
            try:
                item = self.lesson_table.takeItem(table_index, 3)
                item.setText(new_note)
                self.lesson_table.setItem(table_index, 3, item)
            except AttributeError:
                item = self.lesson_table.cellWidget(table_index, 3)
                item.setItemText(item.currentIndex(), new_note)
                item.setEnabled(True)
                self.lesson_table.setCellWidget(table_index, 3, item)
        else:
            new_note = note + "*"
            self.data_lesson_table[season][season_index]["Not"] = new_note
            try:
                item = self.lesson_table.takeItem(table_index, 3)
                item.setText(new_note)
                self.lesson_table.setItem(table_index, 3, item)
            except AttributeError:
                item = self.lesson_table.cellWidget(table_index, 3)
                item.setItemText(item.currentIndex(), new_note)
                item.setEnabled(False)
                self.lesson_table.setCellWidget(table_index, 3, item)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CustomWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

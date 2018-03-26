# encoding=utf-8

from PyQt5 import QtCore, QtWidgets
from constants import Constants


class DuplicationDialog(QtWidgets.QDialog):

    def __init__(self, duplication_dict=None):
        QtWidgets.QWidget.__init__(self)
        self.duplication_dict = duplication_dict
        self.check_box_dict = dict()
        self.create_main_ui()
        self.setWindowTitle('筛选重复文献')
        self.resize(800, 600)
        self.show()

    def create_main_ui(self):
        main_v_layout = QtWidgets.QVBoxLayout()
        scroll = self.create_scroll_ui()
        main_v_layout.addWidget(scroll)
        button_box = QtWidgets.QDialogButtonBox(parent=self)
        button_box.setOrientation(QtCore.Qt.Horizontal)
        button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        main_v_layout.addWidget(button_box)
        self.setLayout(main_v_layout)

    def create_scroll_ui(self):
        scroll_v_layout = QtWidgets.QVBoxLayout()
        for category, duplication_list in self.duplication_dict.items():
            if not duplication_list:
                continue
            for duplication_publish_list in duplication_list:
                box_group, check_box_list = self.create_check_box_group(duplication_publish_list, category)
                scroll_v_layout.addWidget(box_group)
                self.check_box_dict.setdefault(category, []).append(check_box_list)
        scroll = QtWidgets.QScrollArea()
        scroll_widget = QtWidgets.QWidget()
        scroll_widget.setMinimumSize(800, 600)
        scroll_widget.setLayout(scroll_v_layout)
        scroll.setWidget(scroll_widget)
        return scroll

    def create_check_box_group(self, duplication_publish_list, category):
        group_box = QtWidgets.QGroupBox()
        group_box.setTitle(Constants.ARTICLE_CLASS_DESC.get(category, ''))
        layout = QtWidgets.QVBoxLayout()
        check_box_list = list()
        for publish in duplication_publish_list:
            check_box = QtWidgets.QCheckBox(publish.export(), self)
            check_box_list.append(check_box)
            layout.addWidget(check_box)
        group_box.setLayout(layout)
        return group_box, check_box_list

    def get_selected_publish(self):
        result_dict = dict()
        for category, check_box_list in self.check_box_dict.items():
            for i, check_box_group in enumerate(check_box_list):
                for j, check_box in enumerate(check_box_group):
                    if check_box.isChecked():
                        result_dict.setdefault(category, []).append(self.duplication_dict[category][i][j])
        return result_dict

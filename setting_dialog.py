# -*- coding:utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from common.constants import Constants
from parser import MetadataBase
from parser import default_metadata_filename
from record import save_format, default_format_file


class SettingDialog(QtWidgets.QDialog):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.begin_label_input = QtWidgets.QLineEdit()
        self.label_input_dict = dict()
        self.class_tag_dict = dict()
        self.class_format_dict = dict()
        self.create_main_ui()
        self.setWindowTitle('设置')
        self.resize(1024, 768)
        self.show()

    def create_main_ui(self):
        main_v_layout = QtWidgets.QVBoxLayout()
        button_box = QtWidgets.QDialogButtonBox(parent=self)
        button_box.setOrientation(QtCore.Qt.Horizontal)
        button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_v_layout.addLayout(self.create_begin_label_config())
        main_v_layout.addLayout(self.create_label_config_layout())
        main_v_layout.addLayout(self.create_class_tag_layout())
        main_v_layout.addLayout(self.create_output_format_layout())
        main_v_layout.addWidget(button_box)
        self.setLayout(main_v_layout)

    def create_begin_label_config(self):
        main_v_layout = QtWidgets.QVBoxLayout()
        main_v_layout.addWidget(QtWidgets.QLabel('文献起始标签设置'))
        main_v_layout.addWidget(self.begin_label_input)
        self.begin_label_input.setText(MetadataBase.separator.join(MetadataBase.begin_labels))
        return main_v_layout

    def create_label_config_layout(self):
        max_num_per_row = 4
        count_in_row = 0
        main_v_layout = QtWidgets.QVBoxLayout()
        main_v_layout.addWidget(QtWidgets.QLabel('标识符设置'))
        labels_v_layout = QtWidgets.QVBoxLayout()
        row_h_layout = QtWidgets.QHBoxLayout()
        for label in MetadataBase.type_desc_dict:
            if count_in_row >= max_num_per_row:
                labels_v_layout.addLayout(row_h_layout)
                row_h_layout = QtWidgets.QHBoxLayout()
                count_in_row = 0
            input_h_layout = QtWidgets.QHBoxLayout()
            label_desc = MetadataBase.type_desc_dict[label]
            q_label_name = '%s\r\n(%s)' % (label_desc, label)
            label_input = QtWidgets.QLineEdit()
            label_input.setText(MetadataBase.get_label_string(label))
            input_h_layout.addWidget(QtWidgets.QLabel(q_label_name))
            input_h_layout.addWidget(label_input)
            self.label_input_dict[label] = label_input
            row_h_layout.addLayout(input_h_layout)
            count_in_row += 1
        labels_v_layout.addLayout(row_h_layout)
        main_v_layout.addLayout(labels_v_layout)
        return main_v_layout

    def create_output_format_layout(self):
        main_v_layout = QtWidgets.QVBoxLayout()
        main_v_layout.addWidget(QtWidgets.QLabel('输出格式设置'))
        for article_class, desc in Constants.ARTICLE_CLASS_DESC.items():
            class_h_layout = QtWidgets.QHBoxLayout()
            publish_class = MetadataBase.article_class_dict[article_class]
            class_input = QtWidgets.QLineEdit()
            class_input.setText(publish_class.export_format)
            self.class_format_dict[article_class] = class_input
            class_h_layout.addWidget(QtWidgets.QLabel(desc))
            class_h_layout.addWidget(class_input)
            main_v_layout.addLayout(class_h_layout)
        return main_v_layout

    def create_class_tag_layout(self):
        main_v_layout = QtWidgets.QVBoxLayout()
        main_v_layout.addWidget(QtWidgets.QLabel('文献类型标识设置'))
        for article_class, desc in Constants.ARTICLE_CLASS_DESC.items():
            class_h_layout = QtWidgets.QHBoxLayout()
            class_tags = MetadataBase.get_class_string(article_class)
            class_input = QtWidgets.QLineEdit()
            class_input.setText(class_tags)
            self.class_tag_dict[article_class] = class_input
            class_h_layout.addWidget(QtWidgets.QLabel(desc))
            class_h_layout.addWidget(class_input)
            main_v_layout.addLayout(class_h_layout)
        return main_v_layout

    def config_mata_data_base(self):
        # set begin labels
        MetadataBase.set_begin_labels(self.begin_label_input.text())
        # set labels
        for label, input_widget in self.label_input_dict.items():
            MetadataBase.set_label(label, input_widget.text())
        # set tags
        for article_class, input_widget in self.class_tag_dict.items():
            MetadataBase.set_class_tag(article_class, input_widget.text())
        # set output format
        for article_class, input_widget in self.class_format_dict.items():
            publish_type = MetadataBase.article_class_dict.get(article_class)
            if publish_type is None:
                continue
            publish_type.export_format = input_widget.text()
        # save to file
        MetadataBase.save(default_metadata_filename)
        save_format(default_format_file)


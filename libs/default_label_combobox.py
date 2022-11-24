# coding=utf-8

from qtpy.QtWidgets import QWidget, QHBoxLayout, QComboBox


class DefaultLabelComboBox(QWidget):
    def __init__(self, parent=None, items=None):
        super(DefaultLabelComboBox, self).__init__(parent)

        if items is None:
            items = []
        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.items = items
        self.cb.addItems(self.items)

        self.cb.currentIndexChanged.connect(
            parent.default_label_combo_selection_changed
        )

        layout.addWidget(self.cb)
        self.setLayout(layout)

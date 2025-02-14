# coding=utf-8
from qtpy.QtWidgets import QColorDialog, QDialogButtonBox

BB = QDialogButtonBox


class ColorDialog(QColorDialog):
    def __init__(self, parent=None):
        super(ColorDialog, self).__init__(parent)
        self.setOption(QColorDialog.ColorDialogOption.ShowAlphaChannel)
        # The Mac native dialog does not support our restore button.
        self.setOption(QColorDialog.ColorDialogOption.DontUseNativeDialog)
        # Add a restore defaults button.
        # The default is set at invocation time, so that it
        # works across dialogs for different elements.
        self.default = None
        self.bb = self.layout().itemAt(1).widget()
        self.bb.addButton(QDialogButtonBox.StandardButton.RestoreDefaults)
        self.bb.clicked.connect(self.check_restore)

    def getColor(self, value=None, title=None, default=None):
        self.default = default
        if title:
            self.setWindowTitle(title)
        if value:
            self.setCurrentColor(value)
        return self.currentColor() if self.exec_() else None

    def check_restore(self, button):
        if self.bb.buttonRole(button) & BB.ButtonRole.ResetRole and self.default:
            self.setCurrentColor(self.default)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qtpy.QtWidgets import *


# PyQt5: TypeError: unhashable type: 'QListWidgetItem'


class HashableQListWidgetItem(QListWidgetItem):
    def __init__(self, *args):
        super(HashableQListWidgetItem, self).__init__(*args)

    def __hash__(self):
        return hash(id(self))

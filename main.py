# pyside6-uic main.ui > main_window.py

import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QItemSelection
from PySide6.QtGui import Qt, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow

from main_window import Ui_MainWindow
from database import Recipe
from models import RecipeModel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.recipeModel = RecipeModel()
        self.ui.tableView.setModel(self.recipeModel)
        self.ui.tableView.hideColumn(0)

        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.ui.tableView.selectionModel().selectionChanged.connect(self.recipeChanged)
        self.ui.tableView.selectRow(0)

        self.ui.lineEdit.returnPressed.connect(self.doSearch)

        listStyle = 'QListView { background: transparent; }'
        self.ui.recipeInstructionList.setStyleSheet(listStyle)
        self.ui.recipeIngredientList.setStyleSheet(listStyle)

    def recipeChanged(self, selection: QItemSelection):
        if selection.isEmpty():
            return
        indices = selection.takeAt(0).indexes()
        if not indices:
            return
        row = indices[0].row()
        recipe_id = self.recipeModel.data(self.recipeModel.createIndex(row, 0), Qt.ItemDataRole.DisplayRole)
        recipe = Recipe.get(Recipe.id == recipe_id)
        self.showRecipe(recipe)

    def showRecipe(self, recipe):
        self.ui.recipeTitle.setText(recipe.title)

        if recipe.description:
            self.ui.recipeDescription.setText(recipe.description)
            self.ui.recipeDescription.show()
        else:
            self.ui.recipeDescription.hide()

        if recipe.author:
            self.ui.recipeAuthor.setText(recipe.author)
            self.ui.recipeAuthor.show()
        else:
            self.ui.recipeAuthor.setText('Anonymous')

        ingredientModel = QStandardItemModel()
        instructionModel = QStandardItemModel()

        for i in recipe.ingredients:
            item = QStandardItem(f"• {i.value}")
            ingredientModel.appendRow(item)

        c = 1
        for i in recipe.instructions:
            item = QStandardItem(f"{c}. {i.value}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignTop)
            instructionModel.appendRow(item)
            c += 1

        self.ui.recipeIngredientList.setModel(ingredientModel)
        self.ui.recipeInstructionList.setModel(instructionModel)

        width = self.ui.recipeIngredientList.sizeHintForColumn(0) + 20
        if width > 350:
            width = 350
        if width < 200:
            width = 200
        self.ui.recipeIngredientList.setMinimumWidth(width)
        self.ui.recipeIngredientList.setMaximumWidth(width)

    def doSearch(self):
        term = self.ui.lineEdit.text()
        self.ui.tableView.selectionModel().selectionChanged.disconnect()
        self.recipeModel = RecipeModel(term)
        self.ui.tableView.setModel(self.recipeModel)
        self.ui.tableView.selectionModel().selectionChanged.connect(self.recipeChanged)
        self.ui.tableView.selectRow(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

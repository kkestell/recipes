import typing

from PySide6 import QtCore
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import Qt

from database import Recipe


class RecipeModel(QtCore.QAbstractTableModel):
    def __init__(self, term=''):
        super(RecipeModel, self).__init__()
        q = Recipe.select()
        q = q.where(Recipe.title.contains(term))
        q = q.order_by(Recipe.rating_value.desc())
        self.recipes = q

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            recipe = self.recipes[index.row()]
            col = index.column()
            if col == 0:
                return recipe.id
            if col == 1:
                return recipe.title
            elif col == 2:
                return '%.2f' % recipe.rating_value

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> typing.Any:
        if orientation != QtCore.Qt.Orientation.Horizontal or role != Qt.ItemDataRole.DisplayRole:
            return
        return ['ID', 'Title', 'Rating'][section]

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.recipes)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return 3

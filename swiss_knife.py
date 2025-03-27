# main.py
"""Название: swiss_knife

Автор: hwpy
Дата: 2025-03-28
Описание: Универсальное приложение для работы с файлами
"""
import sys

import qdarktheme
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from archiver.controller.swiss_knife_controller import SwissKnifeController
from archiver.model.archiver_manager import ArchiveManager
from archiver.view.swiss_knife_view import SwissKnifeView
from config.swiss_knife_config import SwissKnifeConfig


class SwissKnifeApp:
    """Класс приложения

    Methods:
        - run: запускает приложение

    """

    def __init__(self) -> None:
        """Конструктор

        Args:
            - self: SwissKnifeApp - экземпляр

        Returns:
            None

        """
        self.app = QApplication(sys.argv)
        qdarktheme.setup_theme("auto")
        self.config = SwissKnifeConfig()
        self.view = SwissKnifeView()
        self.model = ArchiveManager()
        self.controller = SwissKnifeController(self.view, self.model)

        self.view.setWindowIcon(QIcon(self.config.icon_path))
        self.view.show()

    def run(self) -> None:
        """Запустить приложение

        Args:
            - self: SwissKnifeApp - экземпляр

        Returns:
            None

        """
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = SwissKnifeApp()
    app.run()

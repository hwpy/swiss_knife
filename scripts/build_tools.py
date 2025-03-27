"""Название: build_tools

Автор: hwpy
Дата: 2025-03-28
Описание: Функционал сборки приложения под разные системы
"""

import ast
import subprocess
import sys
from os import getcwd
from pathlib import Path

from jinja2 import Template

current_dir = Path(getcwd())  # noqa: PTH109
sys.path.append(str(current_dir))

from config.swiss_knife_config import JinjaTemplates, SwissKnifeConfig
from utils.platform_settings import Platform


def pick_builder_template_by_os(config: SwissKnifeConfig) -> dict:
    """Выбрать шаблон сборки для ОС

    Args:
        config: SwissKnifeConfig - конфиг приложения

    Returns:
       dict[str: dict[str: str]] - {строка сборки: параметры сборки}

    """
    if Platform.Windows == Platform.OS:
        params = {
            "app_name": config.build_params["app_name"],
            "win_icon_path": config.build_params["win_icon_path"],
            "app_py": config.build_params["app_py"],
        }
        return {"builder": JinjaTemplates.pyinstaller_win, "params": params}
    if Platform.macOS == Platform.OS:
        params = {
            "app_name": config.build_params["app_name"],
            "mac_icon_path": config.build_params["mac_icon_path"],
            "app_py": config.build_params["app_py"],
        }
        return {"builder": JinjaTemplates.pyinstaller_mac, "params": params}
    raise SystemError("Данная ОС на текущий момент не поддерживается!")


def build_with_pyinstaller(config: SwissKnifeConfig) -> None:
    """Собрать приложение с помощью pyinstaller

    Args:
        config: SwissKnifeConfig - конфиг приложения

    Returns:
       None

    """
    builder_template = pick_builder_template_by_os(config)
    with open(builder_template["builder"]) as f:
        template_str = f.read()
        template = Template(template_str)
        command = template.render(builder_template["params"])
        try:
            output = subprocess.check_output(ast.literal_eval(command))
            print(output.decode("utf-8"))
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")


def build_readme(config: SwissKnifeConfig) -> None:
    """Собрать readme

    Args:
        config: SwissKnifeConfig - конфиг приложения

    Returns:
        None

    """
    with open(JinjaTemplates.readme) as f:
        template_str = f.read()

        template = Template(template_str)
        rendered_md_content = template.render(
            app_name=config.build_params["app_name"],
            app_version=config.build_params["app_version"],
            screenshot_mac=config.build_params["screenshot_mac"],
            screenshot_win=config.build_params["screenshot_win"],
        )

    with open("README.md", "w") as file:
        file.write(rendered_md_content)


if __name__ == "__main__":
    build_readme(SwissKnifeConfig)
    # build_with_pyinstaller(SwissKnifeConfig)

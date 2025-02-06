# Swiss knife
Версия: 0.1.2

<p align="center">
    <img src="media/screenshots/screenshot_mac.png">
</p>
<p align="center">
    <img src="media/screenshots/screenshot_win.png">
</p>

## На данный момент поддерживается
1. Разархивировать .7z, .zip, .rar (требуется установка brew install rar)
2. Архивировать .7z, .zip, .rar (требуется установка brew install unrar) с паролем и без пароля

## Сборка с помощью pyinstaller:
macOS:
* pyinstaller --windowed --name="Swiss knife" --icon="media/icons/mac/appicon-sk.icns" swiss_knife.py

Windows:
* pyinstaller --onefile --windowed --name="Swiss knife" --add-data="media/icons/windows/appicon-sk.ico;." --icon="media/icons/windows/appicon-sk.ico" swiss_knife.py
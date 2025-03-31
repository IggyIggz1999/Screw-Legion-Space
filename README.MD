# ScrewLegionSpace
ScrewLegionSpace is a simple Python-based program that allows you to remap or disable the dedicated Legion Space button on the Legion Go, as there is currently no native way to do this.

## How does ScrewLegionSpace work?
When running, the program intercepts all attempts to open Legion Space and immediately terminates the process. Instead, it launches the desired program specified in the configuration file.
Due to the way this script functions, **Legion Space cannot be launched by any means**, whether through the dedicated button or a shortcut. However, the overlay and Quick Settings will remain functional as usual. To access Legion Space, ScrewLegionSpace has to be closed first.

## Installation & Usage instructions
1. Download the ScrewLegionGo executable from the [Releases page](https://github.com/IggyIggz1999/Screw-Legion-Space/releases) [here](https://github.com/IggyIggz1999/Screw-Legion-Space/releases/download/V1/ScrewLegionSpace.exe).
2. Move the executable to any desired folder on your device.
3. Run the executable. It will create a configuration file in the same folder. Most settings can be left as default, **but be sure to edit the path of the program you want to launch when pressing the Legion Space button!**
4. _(Optional)_ Right-clicking the system tray icon allows you to enable automatic startup with Windows. This requires administrator privileges. Alternatively, you can manually place the executable and its configuration file in:
 - C:\Users\(Your sytem name)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

ScrewLegionSpace runs in the background without any visible windows. You can close it via the system tray icon.

## Build the script yourself
A prebuilt executable is available in this repository, but if you prefer, you can modify and compile your own version using PyInstaller with the following command:
 - pyinstaller --onefile --noconsole --add-data "src/icon.ico;." --icon "src/icon.ico" --name "ScrewLegionSpace" "src/ScrewLegionSpace.pyw"

## Disclaimer
This script is a janky and probably inefficient solution to the problem, but it works! It was originally created for personal use. Use at your own risk.














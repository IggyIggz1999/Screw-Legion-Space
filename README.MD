# ScrewLegionSpace Readme
ScrewLegionSpace is a very basic Python script that I created to remap (Or disable) the Legion Space button on the Lenovo Legion Go, as there is no native way to do this.

## How does this script work?
When the script is active, it will intercept **any** attempt to start Legion Space, and kill the task immediately. It will then run the desired executable, as chosen by the user.
**This means Legion Space cannot be started through any means**, whether that is the dedicated Legion Space button or clicking any shortcut. It won't however inpact the overlay and quick settings, these will remain functional as before.

## Installation
1. Download the ScrewLegionGo executable from the release page [here]().
2. Move the executable to the location you'd like 

## Build the script
If you prefer, you can download the repository and build an executable file yourself using PyInstaller using the following command: pyinstaller --onefile --noconsole --add-data "src/icon.ico;." --icon "src/icon.ico" --name "ScrewLegionSpace" "src/ScrewLegionSpace.pyw"

## Disclaimer
This is a _very_ janky script and was originally made just for my own personal use. Use at your own risk!
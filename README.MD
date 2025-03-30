# ScrewLegionSpace Readme
ScrewLegionSpace is a very basic Python script that I created to remap (Or disable) the Legion Space button on the Lenovo Legion Go, as there is no native way to do this.

## How does this script work?
When the script is active, it will intercept **any** attempt to start Legion Space, and kill the task immediately. It will then run the desired executable/file, as chosen by the user.
**This means Legion Space cannot be started through any means**, whether that is the dedicated Legion Space button or clicking any shortcut. It won't however inpact the overlay and quick settings, these will remain functional as before.

## Easy Installation
1. Download the executable from the release page [here]()
2. Move the executable to the following folder, so it starts automatically when your system boots: "C:\Users\(Your username)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
3. Configure the desired settings in the configuration file located on your Documents folder.

## Python Installation
1. Download the ScrewLegionGo script ([screw-legion-space.pyw](https://github.com/IggyIggz1999/Screw-Legion-Space/blob/main/src/screw-legion-space.pyw)) from the 'src' folder in this reposity.
2. Install the latest version of Python from [here](https://www.python.org/downloads/).
3. Make sure .pyw files, such as this script, are associated with Python. You can easily do this by opening the ScrewLegionGo script after you download it. It should already be accosiated with Python, else Windows will promot you how to open .pyw files in the future.
4. Move the script to the following folder, so it starts automatically when your system boots: "C:\Users\(Your username)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
3. Configure the desired settings in the script.

## Build the executable yourself
If you prefer, you can build the executable file yourself using PyInstaller using the following command: pyinstaller --onefile --noconsole screw-legion-space-exe.pyw

## Disclaimer
This is a _very_ janky script and was originally made just for my own personal use. Use at your own risk!
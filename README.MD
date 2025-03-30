# ScrewLegionSpace Readme
ScrewLegionSpace is a very basic Python script that I created to remap (Or disable) the Legion Space button on the Lenovo Legion Go, as there is no native way to do this.

## How does this script work?
When the script is active, it will intercept **any** attempt to start Legion Space, and kill the task immediately. It will then run the desired executable/file, as chosen by the user.
**This means Legion Space cannot be started through any means**, whether that is the dedicated Legion Space button or clicking any shortcut. It won't however inpact the overlay and quick settings, these will remain functional as before.

## Installation
1. Download the ScrewLegionGo script [here]() or from the 'src' folder in this reposity.
2. Install the latest version of Python from [here](https://www.python.org/downloads/).
3. Make sure .pyw files, such as this script, are associated with Python. You can easily do this by opening the ScrewLegionGo script after you download it. It should already be accosiated with Python, else Windows will promot you how to open .pyw files in the future.
4. Move the script to the following folder, so it starts automatically when your system boots: "C:\Users\(Your username)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
# ------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------
import logging
import time
import os
import sys
import configparser
import threading
import subprocess

import psutil
from pystray import Icon, MenuItem, Menu
from PIL import Image

# ------------------------------------------------------------------------
# Hardcoded Paths
# ------------------------------------------------------------------------
LOGS_PATH: str = f"{os.getcwd()}\\ScrewLegionSpace-Logs.txt"
CONFIG_PATH: str = f"{os.getcwd()}\\ScrewLegionSpace-Config.ini"
CURRENT_EXE_PATH: str = f"{os.getcwd()}\\ScrewLegionSpace.exe"

# ------------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------------
logging.basicConfig(filename=LOGS_PATH, level=logging.INFO, format="%(asctime)s - %(levelname)s : %(message)s")

# ------------------------------------------------------------------------
# Config Functions
# ------------------------------------------------------------------------
config = configparser.ConfigParser()

def create_config() -> None:
    """create_config Function will create the configuration file with the default values.
    """
    config['ScrewLegionSpace'] = {'script_enabled': 'true', 'check_process_fequency': 1.0, 'legion_space_exe_name': 'LegionSpace.exe', 'start_replacement_exe': 'true', 'replacement_exe_path': 'C:\\Program Files\\Playnite\\Playnite.FullscreenApp.exe'}
    try:
        with open(CONFIG_PATH, 'w') as cf:
            config.write(cf)
    except Exception as e:
        logging.error(f"There was an error creating the configuration file, as a result ScrewLegionSpace will close!:\n    {e}")
        sys.exit()
        
def read_config() -> tuple[bool, float, str, bool, str]:
    """read_config Function will read an existing configuration file, convert the values into variables and return them.

    Returns:
        tuple[bool, float, str, bool, str]: Returns the various configuration options: 'script_enabled' / 'check_process_fequency' / 'legion_space_exe_name' / 'start_replacement_exe' / 'replacement_exe_path'
    """
    config.read(CONFIG_PATH)
    try:
        SCRIPT_ENABLED: bool = config.getboolean('ScrewLegionSpace', 'script_enabled')
        CHECK_PROCESS_FREQUENCY: float = config.getfloat('ScrewLegionSpace', 'check_process_fequency')
        LEGION_SPACE_EXE_NAME: str = config.get('ScrewLegionSpace', 'legion_space_exe_name')
        START_REPLACEMENT_EXE: bool = config.getboolean('ScrewLegionSpace', 'start_replacement_exe')
        REPLACEMENT_EXE_PATH: str = config.get('ScrewLegionSpace', 'replacement_exe_path')
    except Exception as e:
        logging.error(f"There was an error reading the configuration file, as a result ScrewLegionSpace will close!:\n    {e}")
        sys.exit()
        
    if len(LEGION_SPACE_EXE_NAME) < 5:
        logging.error(f"'legion_space_exe_name' Cannot be empty, as a result ScrewLegionSpace will close!")
        sys.exit()
    if len(REPLACEMENT_EXE_PATH) < 5:
        logging.error(f"'replacement_exe_path' Cannot be empty, as a result ScrewLegionSpace will close!")
        sys.exit()
        
    return SCRIPT_ENABLED, CHECK_PROCESS_FREQUENCY, LEGION_SPACE_EXE_NAME, START_REPLACEMENT_EXE, REPLACEMENT_EXE_PATH

# ------------------------------------------------------------------------
# Main Functiions
# ------------------------------------------------------------------------
def run_process_check() -> None:
    """run_process_check Function will be executed by a new thread to continuously check for any instances of Legion Space.
    """
    logging.info(f"Process scanning thread started successfully!")
    while not stop_event.is_set():
        # Read the config file or create one if one does not exist
        if not os.path.isfile(CONFIG_PATH):
            create_config()
            logging.info(f"No Configuration file found! New Configuration file created at: {CONFIG_PATH}")
        SCRIPT_ENABLED, CHECK_PROCESS_FREQUENCY, LEGION_SPACE_EXE_NAME, START_REPLACEMENT_EXE, REPLACEMENT_EXE_PATH = read_config()
            
        # If the script is enabled, look for instances of a Legion Space process and kill it, then start the replacement executable if desired.
        if SCRIPT_ENABLED is True:
            try:
                for process in psutil.process_iter():
                    if LEGION_SPACE_EXE_NAME.lower() == process.name().lower():
                        try:
                            process.kill()
                            logging.info(f"Successfully terminated process '{LEGION_SPACE_EXE_NAME}'")
                        except Exception as e:
                            logging.error(f"There was an error killing the active process!:\n    {e}")
                        if START_REPLACEMENT_EXE is True:
                            try:
                                os.startfile(REPLACEMENT_EXE_PATH)
                                logging.info(f"Successfully started executable '{REPLACEMENT_EXE_PATH}'")
                            except Exception as e:
                                logging.error(f"There was an error starting the desired executable!:\n    {e}")

            except Exception as e:
                logging.error(f"There was an error reading the configuration file, as a result ScrewLegionSpace will close!:\n    {e}")
                sys.exit()
        
        time.sleep(CHECK_PROCESS_FREQUENCY)

def open_config_file(icon, _) -> None:
    """open_config_file Function will simply open the configuration file in the default text editor.

    Args:
        icon (_type_): The tray icon this function is a part of.
    """
    logging.info(f"[Tray Icon] Opening configuration file at: {CONFIG_PATH}!")
    os.startfile(CONFIG_PATH)

def run_at_startup(icon, _) -> None:
    """run_at_startup Function that will add a task to thge Windows Task Scheduler to run this program on boot.

    Args:
        icon (_type_): The tray icon this function is a part of.
    """
    cmd = (f'powershell -Command "Start-Process schtasks -ArgumentList \'/create /tn \"ScrewLegionSpace\" /tr \"{CURRENT_EXE_PATH}\" /sc ONLOGON /f\' -Verb RunAs"')
    subprocess.run(cmd, shell=True)
    logging.info(f"[Tray Icon] Set executable to run on boot: {os.getcwd()}")

def exit_program(icon, _) -> None:
    """exit_program Function will end the task and close the tray icon, resulting in the software exiting

    Args:
        icon (_type_): The tray icon this function is a part of.
    """
    logging.info(f"[Tray Icon] Exitting program!")
    stop_event.set()
    icon.stop()
    
# ------------------------------------------------------------------------
# Program Flow
# ------------------------------------------------------------------------
if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        icon_path = os.path.join(sys._MEIPASS, "icon.ico")
        image = Image.open(icon_path)
    else:
        image = Image.new("RGB", (32, 32), (79, 81, 175))
    menu = Menu(MenuItem("Open Configuration File", open_config_file), MenuItem("Run Program at Startup", run_at_startup), MenuItem("Quit Program", exit_program))
    icon = Icon("icon", image, "ScrewLegionSpace", menu)
    
    stop_event = threading.Event()
    
    thread = threading.Thread(target=run_process_check, daemon=True)
    thread.start()
    logging.info(f"ScrewLegionSpace Successfully started at: {os.getcwd()}")
    icon.run()
    thread.join()

    
        
    
    
    
    
    
    
        
    
    




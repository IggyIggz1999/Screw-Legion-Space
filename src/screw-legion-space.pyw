# ------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------
import logging
import time
import os
import sys
import signal
import subprocess

# ------------------------------------------------------------------------
# Settings & Config
# ------------------------------------------------------------------------
SCRIPT_ENABLED: bool = True                                                                             # True/False decides whether this script is active.

LOGS_PATH: str = r"ScrewLegionSpace-Logs.txt"                                                           # The (full or relative) filepath where logs should be saved, by default this is in the same location as this script.
LEGION_SPACE_EXECUTABLE_NAME: str = r"LegionSpace.exe"                                                  # The name of the Legion Space executable.
REPLACEMENT_EXECUTABLE_PATH: None | str = r"C:\\Program Files\\Playnite\\Playnite.FullscreenApp.exe"    # The full filepath to the executable that should be launched instead of Legion Space. If you only want to disable Legion Space, change this to None.
CHECK_FOR_PROCESS_FREQUENCY: float = 1.0                                                                # The frequency in seconds how often the script should check for an active Legion Space process

# ------------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------------
logging.basicConfig(filename=LOGS_PATH, level=logging.INFO, format="%(asctime)s - %(levelname)s : %(message)s")

# ------------------------------------------------------------------------
# Functionality
# ------------------------------------------------------------------------
if __name__ == "__main__":
    logging.info("ScrewLegionSpace V1 Successfully started!")

    # Check all user input in the settings and log errors
    if not isinstance(SCRIPT_ENABLED, bool):
        logging.error(f"There was an error with the 'SCRIPT_ENABLED' option: Needs to be True or False! Due to this error the script has closed.")
        sys.exit()
    if not isinstance(CHECK_FOR_PROCESS_FREQUENCY, (float, int)):
        logging.error(f"There was an error with the 'CHECK_FOR_PROCESS_FREQUENCY' option: Needs to be a valid number of seconds! Due to this error the script has closed.")
        sys.exit()
        
    if len(LOGS_PATH) < 5 :
        logging.error(f"There was an error with the 'LOGS_PATH' option: Needs to be a valid filepath and cannot be empty! Due to this error the script has closed.")
        sys.exit()
    if len(LEGION_SPACE_EXECUTABLE_NAME) < 5:
        logging.error(f"There was an error with the 'LEGION_SPACE_EXECUTABLE_NAME' option: Needs to be a valid executable name and cannot be empty! Due to this error the script has closed.")
        sys.exit()
        
    if not isinstance(REPLACEMENT_EXECUTABLE_PATH, (None, str)):
        logging.error(f"There was an error with the 'REPLACEMENT_EXECUTABLE_PATH' option: Needs to be a valid executable name or be set to None! Due to this error the script has closed.")
        sys.exit()
    if REPLACEMENT_EXECUTABLE_PATH is not None:
        if len(REPLACEMENT_EXECUTABLE_PATH) < 5:
            logging.error(f"There was an error with the 'REPLACEMENT_EXECUTABLE_PATH' setting: Needs to be a valid filepath and cannot be empty! Due to this error the script has closed.")
            sys.exit()

    # Start checking at the given frequency if Legion Space is in the active tasklist, and if it kill it and start the replacement executable
    while SCRIPT_ENABLED is True:
        try:
            result = subprocess.run(["tasklist"], capture_output=True, text=True, check=True)
        except Exception as e:
            logging.error(f"There was an error getting the active tasklist ↓:\n{e}")
        
        try:
            for line in result.stdout.splitlines():
                if LEGION_SPACE_EXECUTABLE_NAME.lower() in line.lower():
                    pid = int(line.split()[1])
                    try:
                        os.kill(pid, signal.SIGTERM)
                        logging.info(f"Successfully terminated process '{LEGION_SPACE_EXECUTABLE_NAME}' with PID: {pid}")
                    except Exception as e:
                        logging.error(f"There was an error killing the active process ↓:\n{e}")
                    try:
                        if REPLACEMENT_EXECUTABLE_PATH is not None:
                            os.startfile(REPLACEMENT_EXECUTABLE_PATH)
                            logging.info(f"Successfully started executable '{REPLACEMENT_EXECUTABLE_PATH}'")
                    except Exception as e:
                        logging.error(f"There was an error starting the desired executable ↓:\n{e}")                   
        except Exception as e:
            logging.error(f"There was an error reading the tasklist ↓:\n{e}")

        time.sleep(CHECK_FOR_PROCESS_FREQUENCY)
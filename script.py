# script.py
# Contains reusable helper functions for PyAutoGUI automation.
# Modified so functions return True/False instead of exiting on image not found.

import pyautogui
import time
import sys # Still needed for other potential exit reasons or manual interrupt

# --- Configuration Constants ---
# These configure the behavior of the helper functions.

# Confidence level for image matching (requires opencv-python).
CONFIDENCE_LEVEL = 0.75 # Resetting to default, adjust if needed
# Timeout (in seconds) for image searching.
SEARCH_TIMEOUT = 10 # Default timeout for finding images to click
WAIT_TIMEOUT = 15 # Default timeout for waiting for screens
# Timeout (in seconds) for checking optional screens/dialogs. Use a shorter timeout.
OPTIONAL_CHECK_TIMEOUT = 5

# --- Helper Functions ---

def find_image(image_path, description, confidence=CONFIDENCE_LEVEL, timeout=SEARCH_TIMEOUT):
    """
    Searches the screen for a given image file until timeout. Internal use.

    Args:
        image_path (str): The filename of the image to search for.
        description (str): A human-readable description of the image for logging.
        confidence (float): The confidence level required for the match.
        timeout (int): How many seconds to keep searching before failing.

    Returns:
        tuple or None: The coordinates (left, top, width, height) of the found image, or None if not found within timeout.
    """
    # This internal function doesn't print start/found messages, caller does.
    start_time = time.time()
    location = None
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                return location # Return the location box
        except pyautogui.ImageNotFoundException:
            pass # Keep searching
        except Exception as e:
             # Catch other potential errors (e.g., file not found for the image itself)
             # This might still be a reason to exit, as it's not just "not found on screen"
             print(f"CRITICAL ERROR searching for '{description}' ({image_path}): {e}")
             sys.exit(f"Exiting due to critical error finding image file for {description}.")
        time.sleep(0.5)
    return None # Return None if not found

def check_optional_image(image_path, description, confidence=CONFIDENCE_LEVEL, timeout=OPTIONAL_CHECK_TIMEOUT):
    """
    Checks if an optional image appears on screen within a short timeout.

    Args:
        image_path (str): The filename of the image to check for.
        description (str): A human-readable description of the image for logging.
        confidence (float): The confidence level required for the match.
        timeout (int): How many seconds to keep searching before returning False.

    Returns:
        bool: True if the image was found within the timeout, False otherwise.
    """
    print(f"Checking for optional '{description}' ({image_path}) for up to {timeout} seconds...")
    location = find_image(image_path, description, confidence, timeout)
    if location:
        print(f"Found optional '{description}'.")
        return True
    else:
        print(f"Optional '{description}' not found.")
        return False


def wait_for_image(image_path, description, confidence=CONFIDENCE_LEVEL, timeout=WAIT_TIMEOUT):
    """
    Waits for a specific image to appear on the screen within the timeout.
    Returns True if found, False otherwise. Does NOT exit script.

    Args:
        image_path (str): The filename of the image to wait for.
        description (str): A human-readable description of the image for logging.
        confidence (float): The confidence level required for the match.
        timeout (int): How many seconds to keep searching before failing.

    Returns:
        bool: True if the image was found, False otherwise.
    """
    print(f"Waiting for '{description}' ({image_path}) to appear with confidence {confidence} for up to {timeout} seconds...")
    location = find_image(image_path, description, confidence, timeout)
    if location:
        print(f"Found '{description}'.")
        return True
    else:
        print(f"SKIPPING subsequent steps: '{description}' did not appear within {timeout} seconds.")
        return False


def find_and_click(image_path, description, confidence=CONFIDENCE_LEVEL, timeout=SEARCH_TIMEOUT):
    """
    Searches the screen for a given image file and clicks its center if found within the timeout.
    Returns True if found and clicked, False otherwise. Does NOT exit script.

    Args:
        image_path (str): The filename of the image to search for.
        description (str): A human-readable description of the image for logging.
        confidence (float): The confidence level required for the match.
        timeout (int): How many seconds to keep searching before failing.

    Returns:
        bool: True if the image was found and clicked, False otherwise.
    """
    print(f"Attempting to find and click '{description}' ({image_path}) with confidence {confidence}...")
    location = find_image(image_path, description, confidence, timeout)
    if location:
        try:
            center_location = pyautogui.center(location)
            print(f"Clicking center of '{description}' at coordinates: {center_location}.")
            # Adding moveTo for potential reliability increase
            pyautogui.moveTo(center_location, duration=0.1)
            pyautogui.click(center_location)
            time.sleep(0.5) # Brief pause after clicking
            return True # Indicate success
        except Exception as e:
            print(f"Error clicking found image '{description}': {e}")
            print(f"SKIPPING click for '{description}' due to error.")
            return False # Indicate failure to click, even if found
    else:
        print(f"SKIPPING click: '{description}' ({image_path}) was not found.")
        return False # Indicate image not found


def type_text(text_to_type, description):
    """
    Types the given text using pyautogui with a small delay between characters.
    (This function is kept for potential future use)

    Args:
        text_to_type (str): The string to type.
        description (str): A human-readable description of what's being typed for logging.
    """
    print(f"Typing '{description}': {text_to_type[:15]}...") # Log truncated text
    pyautogui.typewrite(text_to_type, interval=0.05)
    time.sleep(0.5) # Brief pause after typing

# You can add more reusable automation functions here if needed.

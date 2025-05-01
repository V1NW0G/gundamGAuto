# main.py
# Main script to run the PyAutoGUI automation sequence using functions from script.py
# Modified so that each step attempts to run, skipping only if its own image isn't found.
# All 'check' steps now use 'wait_for_image' for a longer timeout.

# Import necessary functions from our script module
# Make sure script.py contains the version of functions that return True/False
# Import find_image separately as we need its return value
from script import find_and_click, type_text, wait_for_image, check_optional_image, find_image # Keep check_optional_image import just in case, though not used below
import pyautogui # Import pyautogui directly for keyboard presses like 'enter' and direct clicks
import time
import sys # Import sys here too for handling KeyboardInterrupt in main
import os # Import os to construct platform-independent paths

# --- Configuration for this specific run ---

# Define the subfolder where images are stored
IMAGE_FOLDER = 'images'

# Define the image filenames to be used in this automation sequence.
# os.path.join creates a correct path regardless of operating system (Windows/Mac/Linux)
IMAGE_PATH_INGAME_OPTION = os.path.join(IMAGE_FOLDER, 'ingame_option.png')
IMAGE_PATH_BACK_TO_LOGIN = os.path.join(IMAGE_FOLDER, 'ingame_backToLogin.png')
IMAGE_PATH_CONFIRM_ACTION = os.path.join(IMAGE_FOLDER, 'ingame_confirmBackToLogin.png') # Confirmation after back to login
IMAGE_PATH_OUTGAME_LOGIN_CHECK = os.path.join(IMAGE_FOLDER, 'outgame_login.png') # Image to wait for after confirmation AND at the end

# Image paths for the delete user info steps
IMAGE_PATH_OUTGAME_OPTION = os.path.join(IMAGE_FOLDER, 'outgame_option.png')
IMAGE_PATH_DELETE_USER_INFO = os.path.join(IMAGE_FOLDER, 'outgame_option_deleteUserInfo.png')
IMAGE_PATH_CHECK_DELETE_CONFIRM = os.path.join(IMAGE_FOLDER, 'outgame_option_confirmDeleteUserInfo.png') # Check image
IMAGE_PATH_CONFIRM_DELETE_CHECKBOX = os.path.join(IMAGE_FOLDER, 'outgame_option_confirmDeleteUserInfo_checkbox.png') # Checkbox to click
IMAGE_PATH_CONFIRM_DELETE_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_option_confirmDeleteUserInfo_deleteButton.png') # Final delete button

# Image paths for the final confirmation steps
IMAGE_PATH_CHECK_FINAL_CONFIRM = os.path.join(IMAGE_FOLDER, 'outgame_confirmedDeleteUser.png') # Check image after delete
IMAGE_PATH_FINAL_CLOSE_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_confirmedDeleteUser_closeButton.png') # Close button

# Image path for entering the game
IMAGE_PATH_ENTER_GAME_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_login_enterGame.png') # Enter game button

# Image paths for terms agreement
IMAGE_PATH_CHECK_TERMS = os.path.join(IMAGE_FOLDER, 'outgame_terms.png') # Check for terms screen/dialog
IMAGE_PATH_TERMS_AGREE_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_termsAgree.png') # Agree button for terms

# Image paths for customer analytics
IMAGE_PATH_CHECK_ANALYTICS = os.path.join(IMAGE_FOLDER, 'outgame_customersAnalytics.png') # Check for analytics screen/dialog
IMAGE_PATH_ANALYTICS_DISAGREE_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_customersAnalytics_Disagree.png') # Disagree button

# Image paths for skipping newbie guide
IMAGE_PATH_CHECK_PASS_NEWBIE = os.path.join(IMAGE_FOLDER, 'outgame_passNewbie.png') # Check for pass newbie screen/dialog
IMAGE_PATH_PASS_NEWBIE_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_passNewbie_pass.png') # Pass newbie button

# Image paths for username input
IMAGE_PATH_CHECK_USERNAME_SCREEN = os.path.join(IMAGE_FOLDER, 'outgame_username.png') # Check for username screen/dialog
IMAGE_PATH_USERNAME_INPUT_FIELD = os.path.join(IMAGE_FOLDER, 'outgame_username_Input.png') # Username input field to click
IMAGE_PATH_USERNAME_CONFIRM_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_username_confirm.png') # Username confirm button
IMAGE_PATH_USERNAME_YES_BUTTON = os.path.join(IMAGE_FOLDER, 'outgame_username_Yes.png') # Username Yes button

# Image path for in-game skip button
IMAGE_PATH_INGAME_SKIP = os.path.join(IMAGE_FOLDER, 'ingame_skip.png') # In-game skip button

# Image path for new mission button
IMAGE_PATH_INGAME_NEW_MISSION = os.path.join(IMAGE_FOLDER, 'ingame_newMission.png') # New mission button

# Image paths for mission welcome
IMAGE_PATH_CHECK_MISSION_WELCOME = os.path.join(IMAGE_FOLDER, 'ingame_newMission_welcom.png') # Check for welcome dialog
IMAGE_PATH_MISSION_WELCOME_OK = os.path.join(IMAGE_FOLDER, 'ingame_newMission_welcom_ok.png') # OK button for welcome
IMAGE_PATH_MISSION_WELCOME_OK2 = os.path.join(IMAGE_FOLDER, 'ingame_newMission_welcom_ok2.png') # Second OK button

# Image path for collecting mission rewards
IMAGE_PATH_MISSION_COLLECT_ALL = os.path.join(IMAGE_FOLDER, 'ingame_newMission_welcom_collectAll.png') # Collect All button

# Image path for mission welcome close button
IMAGE_PATH_MISSION_WELCOME_CLOSE = os.path.join(IMAGE_FOLDER, 'ingame_newMission_welcom_close.png') # Close button after collecting

# Image paths for pop-up and gift
IMAGE_PATH_POPUP_CLOSE = os.path.join(IMAGE_FOLDER, 'ingame_popUp_close.png') # Optional pop-up close button
IMAGE_PATH_GIFT_BUTTON = os.path.join(IMAGE_FOLDER, 'ingame_gift.png') # Gift button

# Image path for gift collect all
IMAGE_PATH_GIFT_COLLECT_ALL = os.path.join(IMAGE_FOLDER, 'ingame_gift_collectAll.png') # Gift Collect All button

# Image path for gift OK button
IMAGE_PATH_GIFT_OK = os.path.join(IMAGE_FOLDER, 'ingame_gift_ok.png') # Gift OK button

# Image path for gift close button
IMAGE_PATH_GIFT_CLOSE = os.path.join(IMAGE_FOLDER, 'ingame_gift_close.png') # Gift Close button

# Image path for Gacha button
IMAGE_PATH_INGAME_GACHA = os.path.join(IMAGE_FOLDER, 'ingame_gacha.png') # Gacha button

# Image path for gift exit button
IMAGE_PATH_GIFT_EXIT = os.path.join(IMAGE_FOLDER, 'ingame_gift_exit.png') # Gift exit button

# Image path for gift next button
IMAGE_PATH_GIFT_NEXT = os.path.join(IMAGE_FOLDER, 'ingame_gift_next.png') # Gift Next button

# Image paths for Gacha sequence
IMAGE_PATH_GACHA_OPTION = os.path.join(IMAGE_FOLDER, 'ingame_gatcha_option.png') # Gacha option/banner
IMAGE_PATH_GACHA_PULL = os.path.join(IMAGE_FOLDER, 'ingame_gatcha_pull.png') # Gacha pull/confirm button
IMAGE_PATH_GACHA_CONFIRM = os.path.join(IMAGE_FOLDER, 'ingame_gatcha_confirm.png') # Gacha confirm button after pull
IMAGE_PATH_GACHA_SKIP = os.path.join(IMAGE_FOLDER, 'ingame_gatcha_skip.png') # Gacha skip button
IMAGE_PATH_GACHA_DONE = os.path.join(IMAGE_FOLDER, 'ingame_gatcha_done.png') # Gacha done button (replaces again)
# IMAGE_PATH_GACHA_AGAIN = os.path.join(IMAGE_FOLDER, 'ingame_gatch_again.png') # No longer needed
# IMAGE_PATH_GACHA_AGAIN_CONFIRM = os.path.join(IMAGE_FOLDER, 'ingame_gatcha_again_confirm.png') # No longer needed

# Add other image paths here if your sequence grows...
# IMAGE_PATH_ANOTHER_BUTTON = os.path.join(IMAGE_FOLDER, 'another_button.png')


# --- Main Execution Logic ---

if __name__ == "__main__":
    # This block runs only when main.py is executed directly
    print("Starting automation script...")
    print(f"Looking for images in the '{IMAGE_FOLDER}' subfolder.")
    print("Ensure the target window (e.g., NoxPlayer) is visible and unobstructed.")
    print("You have 3 seconds to switch focus if needed...")
    time.sleep(3) # Give user time to switch window focus

    # Removed the can_proceed flag. Each step will attempt to run.
    # Functions in script.py will print skip messages if their image isn't found.

    try:
        # --- Define Your Automation Sequence Here ---

        # Step 1: Wait for and click the 'ingame_option.png' image
        print("\n--- Step 1: Locating In-Game Option ---")
        if wait_for_image(IMAGE_PATH_INGAME_OPTION, "In-Game Option Wait"):
            find_and_click(IMAGE_PATH_INGAME_OPTION, "In-Game Option Click")
        # Script continues even if the above fails

        # Step 2: Wait for and click the 'ingame_backToLogin.png' image
        print("\n--- Step 2: Locating Back To Login ---")
        if wait_for_image(IMAGE_PATH_BACK_TO_LOGIN, "Back To Login Wait"):
            find_and_click(IMAGE_PATH_BACK_TO_LOGIN, "Back To Login Click")
        # Script continues even if the above fails

        # Step 3: Wait for and click the confirmation button (if needed)
        print("\n--- Step 3: Waiting for Confirmation Button ---")
        # Use wait_for_image with standard timeout, but click only if found
        if wait_for_image(IMAGE_PATH_CONFIRM_ACTION, "Confirm Back To Login Wait"):
            find_and_click(IMAGE_PATH_CONFIRM_ACTION, "Confirm Back To Login Click")
        else:
            print("\n--- Skipping Step 3 click as confirmation button did not appear ---")
        # Script continues regardless

        # Step 4: Wait for the out-of-game login screen
        print("\n--- Step 4: Waiting for Login Screen ---")
        wait_for_image(IMAGE_PATH_OUTGAME_LOGIN_CHECK, "Out-Game Login Screen Element")
        # Script continues even if the above fails

        # Step 5: Click the out-of-game option button
        print("\n--- Step 5: Clicking Out-Game Option ---")
        # Assuming this button should be present after login screen appears
        if wait_for_image(IMAGE_PATH_OUTGAME_OPTION, "Out-Game Option Wait"):
             find_and_click(IMAGE_PATH_OUTGAME_OPTION, "Out-Game Option Button Click")
        # Script continues even if the above fails

        # Step 6: Click the delete user info button
        print("\n--- Step 6: Clicking Delete User Info ---")
        if wait_for_image(IMAGE_PATH_DELETE_USER_INFO, "Delete User Info Wait"):
             find_and_click(IMAGE_PATH_DELETE_USER_INFO, "Delete User Info Click")
        # Script continues even if the above fails

        # Step 7: Wait for the delete confirmation dialog
        print("\n--- Step 7: Waiting for Delete Confirmation Dialog ---")
        delete_confirm_found = wait_for_image(IMAGE_PATH_CHECK_DELETE_CONFIRM, "Delete Confirmation Check Image")

        # Steps 8 & 9: Only run if the confirmation dialog appeared in Step 7
        if delete_confirm_found:
            print("\n--- Step 8: Clicking Delete Confirmation Checkbox ---")
            # If checkbox click fails, just skip step 9
            if find_and_click(IMAGE_PATH_CONFIRM_DELETE_CHECKBOX, "Delete Confirmation Checkbox"):
                print("\n--- Step 9: Clicking Final Delete Button ---")
                find_and_click(IMAGE_PATH_CONFIRM_DELETE_BUTTON, "Final Delete Button")
        else:
             print("\n--- Skipping Steps 8 & 9 as confirmation dialog did not appear ---")
        # Script continues regardless

        # Step 10: Wait for the final "Deleted User" confirmation message/dialog
        print("\n--- Step 10: Waiting for Final Deletion Confirmation ---")
        final_delete_confirm_found = wait_for_image(IMAGE_PATH_CHECK_FINAL_CONFIRM, "Final Deletion Confirmation Check")

        # Step 11: Only run if the final confirmation appeared in Step 10
        if final_delete_confirm_found:
            print("\n--- Step 11: Clicking Final Close Button ---")
            find_and_click(IMAGE_PATH_FINAL_CLOSE_BUTTON, "Final Deletion Close Button")
        else:
             print("\n--- Skipping Step 11 as final confirmation did not appear ---")
        # Script continues regardless

        # Step 12: Wait to confirm return to the login screen
        print("\n--- Step 12: Waiting for Login Screen (Post-Deletion) ---")
        wait_for_image(IMAGE_PATH_OUTGAME_LOGIN_CHECK, "Out-Game Login Screen Element (Post-Deletion)")
        # Script continues even if the above fails

        # Step 13: Click the Enter Game button
        print("\n--- Step 13: Clicking Enter Game Button ---")
        if wait_for_image(IMAGE_PATH_ENTER_GAME_BUTTON, "Enter Game Button Wait"):
             find_and_click(IMAGE_PATH_ENTER_GAME_BUTTON, "Enter Game Button Click")
        # Script continues even if the above fails

        # Step 14: Wait for the Terms screen/dialog
        print("\n--- Step 14: Waiting for Terms Screen ---")
        terms_found = wait_for_image(IMAGE_PATH_CHECK_TERMS, "Terms Screen Check Image")

        # Step 15: Only run if the Terms screen appeared in Step 14
        if terms_found:
            print("\n--- Step 15: Clicking Terms Agree Button ---")
            find_and_click(IMAGE_PATH_TERMS_AGREE_BUTTON, "Terms Agree Button")
        else:
             print("\n--- Skipping Step 15 as Terms screen did not appear ---")
        # Script continues regardless

        # Step 16: Wait for the Customer Analytics screen/dialog
        print("\n--- Step 16: Waiting for Customer Analytics Screen ---")
        analytics_found = wait_for_image(IMAGE_PATH_CHECK_ANALYTICS, "Customer Analytics Check Image")

        # Step 17: Only run if the Analytics screen appeared in Step 16
        if analytics_found:
            print("\n--- Step 17: Clicking Analytics Disagree Button ---")
            find_and_click(IMAGE_PATH_ANALYTICS_DISAGREE_BUTTON, "Analytics Disagree Button")
        else:
             print("\n--- Skipping Step 17 as Analytics screen did not appear ---")
        # Script continues regardless

        # Step 18: Wait for the Pass Newbie screen/dialog
        print("\n--- Step 18: Waiting for Pass Newbie Screen ---")
        pass_newbie_found = wait_for_image(IMAGE_PATH_CHECK_PASS_NEWBIE, "Pass Newbie Check Image")

        # Step 19: Only run if the Pass Newbie screen appeared in Step 18
        if pass_newbie_found:
            print("\n--- Step 19: Clicking Pass Newbie Button ---")
            find_and_click(IMAGE_PATH_PASS_NEWBIE_BUTTON, "Pass Newbie Button")
        else:
             print("\n--- Skipping Step 19 as Pass Newbie screen did not appear ---")
        # Script continues regardless

        # Step 20: Wait for the Username Input screen/dialog
        print("\n--- Step 20: Waiting for Username Input Screen ---")
        username_screen_found = wait_for_image(IMAGE_PATH_CHECK_USERNAME_SCREEN, "Username Screen Check Image")

        # Steps 21-25: Only run if the Username screen appeared in Step 20
        username_yes_location = None # Store location of Yes button if clicked
        if username_screen_found:
            print("\n--- Step 21: Clicking Username Input Field ---")
            if find_and_click(IMAGE_PATH_USERNAME_INPUT_FIELD, "Username Input Field"):
                # Only proceed if input field was clicked

                print("\n--- Step 22: Typing Username ---")
                username_to_type = "a"
                pyautogui.typewrite(username_to_type, interval=0.1)
                print(f"Typed: {username_to_type}")
                time.sleep(0.5)

                print("\n--- Step 23: Pressing Enter ---")
                pyautogui.press('enter')
                print("Pressed Enter key.")
                time.sleep(1)

                print("\n--- Step 24: Clicking Username Confirm Button ---")
                if find_and_click(IMAGE_PATH_USERNAME_CONFIRM_BUTTON, "Username Confirm Button"):
                    # Only proceed if confirm button was clicked

                    # Step 25: Wait for and click the Yes button
                    print("\n--- Step 25: Locating Username Yes Button ---")
                    # First wait for the 'Yes' button to appear
                    if wait_for_image(IMAGE_PATH_USERNAME_YES_BUTTON, "Username Yes Button Wait"):
                        # Find location again to store it
                        location = find_image(IMAGE_PATH_USERNAME_YES_BUTTON, "Username Yes Button Locate")
                        if location:
                             try:
                                 center_location = pyautogui.center(location)
                                 pyautogui.click(center_location)
                                 print("Clicked Username Yes Button.")
                                 username_yes_location = center_location # Store the click location
                                 time.sleep(0.5)
                             except Exception as click_error:
                                 print(f"Error clicking Username Yes Button: {click_error}")
                        else:
                            print("Could not locate Username Yes button again for clicking.")
                    # Script continues even if wait/click fails here

        else:
             print("\n--- Skipping Steps 21-25 as Username screen did not appear ---")
        # Script continues regardless

        # Step 26: Repeatedly click at Username Yes location until Skip button appears
        ingame_skip_found = False
        ingame_skip_location = None
        if username_yes_location: # Only proceed if Step 25 was successful and stored a location
            print("\n--- Step 26: Repeatedly Clicking at Username Yes Location until Skip appears---")
            click_count_yes = 0
            max_clicks_yes = 30 # Limit clicks
            while click_count_yes < max_clicks_yes:
                # Check if the Skip button is visible
                skip_location_check = find_image(IMAGE_PATH_INGAME_SKIP, "In-Game Skip Button Check", timeout=0.5) # Quick check
                if skip_location_check:
                    print("In-Game Skip Button found.")
                    ingame_skip_found = True
                    ingame_skip_location = pyautogui.center(skip_location_check) # Store center of skip button
                    break # Exit the clicking loop

                # Click at the stored location from Step 25
                try:
                    pyautogui.click(username_yes_location)
                    click_count_yes += 1
                    print(f"Clicked at Username Yes location ({click_count_yes} times).")
                    time.sleep(0.7) # Pause between clicks
                except Exception as click_error_yes:
                    print(f"Error during repeated click at Yes location: {click_error_yes}")
                    time.sleep(1)
                    # Optionally break if click error persists

            if not ingame_skip_found and click_count_yes >= max_clicks_yes:
                 print(f"Stopped repeated clicking after {max_clicks_yes} attempts, In-Game Skip button not found.")
        else:
            print("\n--- Skipping Step 26 as Username Yes Button location was not obtained ---")
        # Script continues regardless

        # Step 27: Repeatedly click at Skip location until Gift Exit appears
        gift_exit_found = False
        if ingame_skip_found and ingame_skip_location: # Only proceed if Step 26 found the skip button
            print("\n--- Step 27: Repeatedly Clicking at Skip Location until Gift Exit appears ---")
            click_count_skip = 0
            max_clicks_skip = 30 # Limit clicks
            while click_count_skip < max_clicks_skip:
                # Check if the Gift Exit button is visible
                if find_image(IMAGE_PATH_GIFT_EXIT, "Gift Exit Check", timeout=0.5): # Quick check
                    print("Gift Exit Button found.")
                    gift_exit_found = True
                    break # Exit the clicking loop

                # Click at the stored Skip button location
                try:
                    pyautogui.click(ingame_skip_location)
                    click_count_skip += 1
                    print(f"Clicked at In-Game Skip location ({click_count_skip} times).")
                    time.sleep(0.7) # Pause between clicks
                except Exception as click_error_skip:
                    print(f"Error during repeated click at Skip location: {click_error_skip}")
                    time.sleep(1)
                    # Optionally break if click error persists

            if not gift_exit_found and click_count_skip >= max_clicks_skip:
                 print(f"Stopped repeated clicking after {max_clicks_skip} attempts, Gift Exit button not found.")
        else:
             # Print skip message only if we got past step 25 but didn't find skip in 26
             if username_yes_location:
                 print("\n--- Skipping Step 27 as In-Game Skip button was not found ---")
        # Script continues regardless

        # Step 28: Click Gift Exit button if it was found
        if gift_exit_found:
            print("\n--- Step 28: Clicking Gift Exit Button ---")
            # Wait again to be sure
            if wait_for_image(IMAGE_PATH_GIFT_EXIT, "Gift Exit Button Wait"):
                find_and_click(IMAGE_PATH_GIFT_EXIT, "Gift Exit Button Click")
        else:
            # Only print skip if we tried the loop in step 27
            if ingame_skip_location:
                print("\n--- Skipping Step 28 as Gift Exit button was not found ---")
        # Script continues regardless


        # --- Original Steps after 26 are now shifted ---

        # Step 29: Repeatedly click the New Mission button until it's gone
        print("\n--- Step 29: Clicking New Mission Button Repeatedly ---")
        click_count_nm = 0
        while True:
            location_nm = find_image(IMAGE_PATH_INGAME_NEW_MISSION, "New Mission Button Check", timeout=1)
            if location_nm:
                try:
                    center_location_nm = pyautogui.center(location_nm)
                    pyautogui.click(center_location_nm)
                    click_count_nm += 1
                    print(f"Clicked New Mission Button ({click_count_nm} times).")
                    time.sleep(0.5)
                except Exception as click_error_nm:
                    print(f"Error clicking New Mission Button: {click_error_nm}")
                    time.sleep(1)
            else:
                print("New Mission Button no longer found.")
                break

        # Step 30: Wait for the New Mission Welcome dialog
        print("\n--- Step 30: Waiting for New Mission Welcome ---")
        welcome_found = wait_for_image(IMAGE_PATH_CHECK_MISSION_WELCOME, "New Mission Welcome Check")

        # Step 31: Only run if the Welcome dialog appeared in Step 30
        if welcome_found:
            print("\n--- Step 31: Clicking New Mission Welcome OK ---")
            find_and_click(IMAGE_PATH_MISSION_WELCOME_OK, "New Mission Welcome OK Button")
        else:
             print("\n--- Skipping Step 31 as Welcome dialog did not appear ---")

        # Step 32: Wait for the Collect All button after mission welcome/skip
        print("\n--- Step 32: Waiting for Collect All Button ---")
        collect_all_found = wait_for_image(IMAGE_PATH_MISSION_COLLECT_ALL, "Collect All Button Wait")

        # # Step 33: Click Collect All if it appeared
        # if collect_all_found:
        #     print("\n--- Step 33: Clicking Collect All Button ---")
        #     find_and_click(IMAGE_PATH_MISSION_COLLECT_ALL, "Collect All Button Click")
        # else:
        #     print("\n--- Skipping Step 33 as Collect All button did not appear ---")

        # # Step 34: Wait for the Second Mission Welcome OK button
        # print("\n--- Step 34: Waiting for Mission Welcome OK Button Again ---")
        # # Using the renamed image path
        # welcome_ok_found_again = wait_for_image(IMAGE_PATH_MISSION_WELCOME_OK2, "Mission Welcome OK Button 2 Wait")

        # # Step 35: Click Second Mission Welcome OK if it appeared
        # if welcome_ok_found_again:
        #     print("\n--- Step 35: Clicking Mission Welcome OK Button Again ---")
        #     find_and_click(IMAGE_PATH_MISSION_WELCOME_OK2, "Mission Welcome OK Button 2 Click")
        # else:
        #     print("\n--- Skipping Step 35 as Second Mission Welcome OK button did not appear ---")

        # Step 36: Wait for the Mission Welcome Close button (e.g., after rewards are shown)
        print("\n--- Step 36: Waiting for Mission Welcome Close Button ---")
        close_button_found = wait_for_image(IMAGE_PATH_MISSION_WELCOME_CLOSE, "Mission Welcome Close Button Wait")

        # Step 37: Click the Close button if it appeared
        if close_button_found:
            print("\n--- Step 37: Clicking Mission Welcome Close Button ---")
            find_and_click(IMAGE_PATH_MISSION_WELCOME_CLOSE, "Mission Welcome Close Button Click")
        else:
            print("\n--- Skipping Step 37 as Mission Welcome Close button did not appear ---")

        # Step 38: Wait for optional pop-up close button
        print("\n--- Step 38: Waiting for Optional Pop-up Close Button ---")
        popup_close_found = wait_for_image(IMAGE_PATH_POPUP_CLOSE, "Optional Pop-up Close Check")

        # Step 39: Click pop-up close if found
        if popup_close_found:
            print("\n--- Step 39: Clicking Optional Pop-up Close Button ---")
            find_and_click(IMAGE_PATH_POPUP_CLOSE, "Optional Pop-up Close Click")
        else:
            print("\n--- Skipping Step 39 as Pop-up Close button did not appear ---")

        # Step 40: Wait for Gift Button
        print("\n--- Step 40: Waiting for Gift Button ---")
        gift_button_found = wait_for_image(IMAGE_PATH_GIFT_BUTTON, "Gift Button Wait")

        # Step 41: Click Gift button if found
        if gift_button_found:
            print("\n--- Step 41: Clicking Gift Button ---")
            find_and_click(IMAGE_PATH_GIFT_BUTTON, "Gift Button Click")
        else:
            print("\n--- Skipping Step 41 as Gift button did not appear ---")

        # Step 42: Wait for Gift Collect All Button
        print("\n--- Step 42: Waiting for Gift Collect All Button ---")
        gift_collect_found = wait_for_image(IMAGE_PATH_GIFT_COLLECT_ALL, "Gift Collect All Button Wait")

        # Step 43: Click Gift Collect All button if found
        if gift_collect_found:
            print("\n--- Step 43: Clicking Gift Collect All Button ---")
            find_and_click(IMAGE_PATH_GIFT_COLLECT_ALL, "Gift Collect All Button Click")
        else:
            print("\n--- Skipping Step 43 and subsequent gift steps as Gift Collect All button did not appear ---")

        # Step 44: Wait for Gift Next Button
        print("\n--- Step 44: Waiting for Gift Next Button ---")
        gift_next_found = wait_for_image(IMAGE_PATH_GIFT_NEXT, "Gift Next Button Wait")

        # Step 45: Click Gift Next button if found
        if gift_next_found:
            print("\n--- Step 45: Clicking Gift Next Button ---")
            find_and_click(IMAGE_PATH_GIFT_NEXT, "Gift Next Button Click")
        else:
            print("\n--- Skipping Step 45 as Gift Next button did not appear ---")

        # Step 46: Wait for Gift OK Button
        print("\n--- Step 46: Waiting for Gift OK Button ---")
        gift_ok_found = wait_for_image(IMAGE_PATH_GIFT_OK, "Gift OK Button Wait")

        # Step 47: Click Gift OK button if found
        if gift_ok_found:
            print("\n--- Step 47: Clicking Gift OK Button ---")
            find_and_click(IMAGE_PATH_GIFT_OK, "Gift OK Button Click")
        else:
            print("\n--- Skipping Step 47 as Gift OK button did not appear ---")

        # Step 48: Wait for the Gift Close button
        print("\n--- Step 48: Waiting for Gift Close Button ---")
        gift_close_found = wait_for_image(IMAGE_PATH_GIFT_CLOSE, "Gift Close Button Wait")

        # Step 49: Click Gift Close button if found
        if gift_close_found:
            print("\n--- Step 49: Clicking Gift Close Button ---")
            find_and_click(IMAGE_PATH_GIFT_CLOSE, "Gift Close Button Click")
        else:
            print("\n--- Skipping Step 49 as Gift Close button did not appear ---")

        # Step 50: Wait for Gacha Button
        print("\n--- Step 50: Waiting for Gacha Button ---")
        gacha_button_found = wait_for_image(IMAGE_PATH_INGAME_GACHA, "Gacha Button Wait")

        # Step 51: Click Gacha button if found
        if gacha_button_found:
            print("\n--- Step 51: Clicking Gacha Button ---")
            find_and_click(IMAGE_PATH_INGAME_GACHA, "Gacha Button Click")
        else:
            print("\n--- Skipping Step 51 as Gacha button did not appear ---")

        # # Step 52: Wait for Gacha Option/Banner
        # print("\n--- Step 52: Waiting for Gacha Option/Banner ---")
        # gacha_option_found = wait_for_image(IMAGE_PATH_GACHA_OPTION, "Gacha Option Wait")

        # # Step 53: Click Gacha Option if found
        # if gacha_option_found:
        #     print("\n--- Step 53: Clicking Gacha Option/Banner ---")
        #     find_and_click(IMAGE_PATH_GACHA_OPTION, "Gacha Option Click")
        # else:
        #     print("\n--- Skipping Step 53 as Gacha Option did not appear ---")

        # # Step 54: Wait for Gacha Pull Button
        # print("\n--- Step 54: Waiting for Gacha Pull Button ---")
        # gacha_pull_found = wait_for_image(IMAGE_PATH_GACHA_PULL, "Gacha Pull Button Wait")

        # # Step 55: Click Gacha Pull button if found
        # if gacha_pull_found:
        #     print("\n--- Step 55: Clicking Gacha Pull Button ---")
        #     find_and_click(IMAGE_PATH_GACHA_PULL, "Gacha Pull Button Click")
        # else:
        #     print("\n--- Skipping Step 55 as Gacha Pull button did not appear ---")

        # # Step 56: Wait for Gacha Confirm Button
        # print("\n--- Step 56: Waiting for Gacha Confirm Button ---")
        # gacha_confirm_found = wait_for_image(IMAGE_PATH_GACHA_CONFIRM, "Gacha Confirm Button Wait")

        # # Step 57: Click Gacha Confirm button if found
        # if gacha_confirm_found:
        #     print("\n--- Step 57: Clicking Gacha Confirm Button ---")
        #     find_and_click(IMAGE_PATH_GACHA_CONFIRM, "Gacha Confirm Button Click")
        # else:
        #     print("\n--- Skipping Step 57 as Gacha Confirm button did not appear ---")

        # # Step 58: Wait for Gacha Skip button
        # print("\n--- Step 58: Waiting for Gacha Skip Button ---")
        # gacha_skip_found = wait_for_image(IMAGE_PATH_GACHA_SKIP, "Gacha Skip Button Wait")

        # # Step 59: Repeatedly click Gacha Skip until Gacha Done appears
        # gacha_done_found = False
        # gacha_skip_location = None # Store location of skip button
        # if gacha_skip_found:
        #     print("\n--- Step 59: Repeatedly Clicking Gacha Skip until Gacha Done appears ---")
        #     # Find location of skip button first
        #     skip_location = find_image(IMAGE_PATH_GACHA_SKIP, "Gacha Skip Button Locate")
        #     if skip_location:
        #         gacha_skip_location = pyautogui.center(skip_location)
        #         click_count_gacha_skip = 0
        #         max_clicks_gacha_skip = 30 # Limit clicks

        #         while click_count_gacha_skip < max_clicks_gacha_skip:
        #             # Check if the Gacha Done button is visible
        #             if find_image(IMAGE_PATH_GACHA_DONE, "Gacha Done Check", timeout=0.5): # Quick check
        #                 print("Gacha Done Button found.")
        #                 gacha_done_found = True
        #                 break # Exit the clicking loop

        #             # Click at the stored Gacha Skip button location
        #             try:
        #                 pyautogui.click(gacha_skip_location)
        #                 click_count_gacha_skip += 1
        #                 print(f"Clicked at Gacha Skip location ({click_count_gacha_skip} times).")
        #                 time.sleep(0.7) # Pause between clicks
        #             except Exception as click_error_gacha_skip:
        #                 print(f"Error during repeated click at Gacha Skip location: {click_error_gacha_skip}")
        #                 time.sleep(1)
        #                 # Optionally break if click error persists

        #         if not gacha_done_found and click_count_gacha_skip >= max_clicks_gacha_skip:
        #             print(f"Stopped repeated clicking after {max_clicks_gacha_skip} attempts, Gacha Done button not found.")
        #     else:
        #          print("Could not locate Gacha Skip button to click repeatedly.")
        # else:
        #     print("\n--- Skipping Step 59 as Gacha Skip button was not found in Step 58 ---")

        # # Step 60: Click Gacha Done button if it was found
        # if gacha_done_found:
        #     print("\n--- Step 60: Clicking Gacha Done Button ---")
        #     # Wait again to be sure
        #     if wait_for_image(IMAGE_PATH_GACHA_DONE, "Gacha Done Button Wait"):
        #         find_and_click(IMAGE_PATH_GACHA_DONE, "Gacha Done Button Click")
        # else:
        #     # Only print skip if we tried the loop in step 59
        #     if gacha_skip_found:
        #         print("\n--- Skipping Step 60 as Gacha Done button was not found ---")


        # --- Add more steps below if needed ---
        # Example: Wait for something after clicking gacha done
        # print("\n--- Step 61: Waiting for Something Else ---")
        # wait_for_image(os.path.join(IMAGE_FOLDER, 'something_else.png'), "Something Else")

        # --- End of Automation Sequence ---

        print("-" * 30)
        print("Automation sequence attempts completed.") # Updated message
        print("-" * 30)

    except KeyboardInterrupt:
        # Allows stopping the script manually with Ctrl+C
        print("\nScript execution stopped by user (Ctrl+C).")
    # Removed SystemExit catch as functions no longer exit this way for image not found
    # except SystemExit as e:
    #     print(f"\nScript exited unexpectedly: {e}") # Should only happen on critical errors now
    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn unexpected error occurred during the script: {e}")
    finally:
        # This block always runs at the end
        print("Script finished.")

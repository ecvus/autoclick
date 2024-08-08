import time
import pyautogui
import keyboard
from pynput.keyboard import Controller, Key

# Set the delay between hotkey presses (in seconds)
delay = 0.5

# Set the confidence level for image matching
confidence = 0.8

# Set the list of image paths to search for
image_paths = ['Screenshot_1.png', 'Screenshot_2.png']

def click_on_image():
    """
    Search for an image on the screen and click on it.
    """
    image_found = False
    for image_path in image_paths:
        try:
            # Search for the image on the screen with a timeout of 2 seconds
            image_location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            
            if image_location:
                # Move the mouse to the center of the image with a duration of 0.1 seconds
                x, y = pyautogui.center(image_location)
                pyautogui.moveTo(x, y, duration=0.1)
                
                # Click on the image
                if image_path == 'Screenshot_1.png':
                    pyautogui.click()
                    pyautogui.press('Enter')
                    time.sleep(0.4)
                    pyautogui.click()
                    pyautogui.press('Enter')
                    print(f"Clicked on {image_path} 2 times")
                elif image_path == 'Screenshot_2.png':
                    pyautogui.click()
                    time.sleep(0.4)
                    pyautogui.click()
                    print(f"Clicked on {image_path} 1 time")
                
                image_found = True
        except pyautogui.ImageNotFoundException as e:
            print(f"Could not find {image_path} on the screen: {e}")
        except pyautogui.FailSafeException as e:
            print(f"Failed to move the mouse: {e}")
    
    if image_found:
        time.sleep(0.5)
        # Use pynput to simulate keyboard presses
        kb = Controller()
        kb.press(Key.ctrl)
        kb.press('w')
        kb.release('w')
        kb.release(Key.ctrl)
    else:
        print("No image found")

def hotkey_function():
    """
    Call the click_on_image function after a delay.
    """
    time.sleep(delay)
    click_on_image()

# Bind hotkey to function
keyboard.add_hotkey('alt', hotkey_function)

print("Press 'alt' to click on one of the images")
keyboard.wait()
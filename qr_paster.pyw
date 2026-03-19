import platform
import pyperclip
from PIL import ImageGrab, Image
from pyzbar.pyzbar import decode
from pynput import keyboard

def process_qr_clipboard():
    try:
        img = ImageGrab.grabclipboard()
        
        if img is None:
            print("No image found in clipboard.")
            return

        decoded_objects = decode(img)
        if not decoded_objects:
            print("No QR code found in the image.")
            return

        qr_text = decoded_objects[0].data.decode('utf-8')
        pyperclip.copy(qr_text)
        print(f"Decoded and copied: {qr_text}")

        paste_text()

    except Exception as e:
        print(f"Error processing QR code: {e}")

def paste_text():
    controller = keyboard.Controller()
    controller.release('q')
    
    # Use Command for Mac, Control for Windows
    modifier = keyboard.Key.cmd if platform.system() == 'Darwin' else keyboard.Key.ctrl

    # TODO: add a small delay if pasting is buggy
    with controller.pressed(modifier):
        controller.press('v')
        controller.release('v')

def on_activate():
    process_qr_clipboard()

def main():
    hotkey = '<ctrl>+q' 
    print(f"QR Paster is running in the background. Press {hotkey} to decode and paste.")
    
    # Listen for the hotkey
    with keyboard.GlobalHotKeys({hotkey: on_activate}) as h:
        h.join()

if __name__ == '__main__':
    main()
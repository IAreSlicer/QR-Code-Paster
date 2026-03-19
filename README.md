# QR-Code-Paster
A background running python script, which which converts a copied qr-code to text on pasting using ctrl + q for Windows or command + q for mac.

## Prerequisites
You will need Python installed on your system. Once installed, you need to install the required libraries.
Open your terminal (mac) or command prompt (Windows) and run:
> pip install Pillow pyperclip pyzbar pynput

For macOS you must install the zbar library on your system for pyzbar to work. The easiest way is using Homebrew:
> brew install zbar

For Windows you'll need to have the  [Visual C++ Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=40784) installed.

## Setting up Run on Startup
To make this seamless, you'll want the script to run invisibly when you log into your computer.
### For Windows:
1.  Rename your script from qr_paster.py to qr_paster.pyw. The .pyw extension tells Windows to run Python in the background without opening a visible command prompt window.
2.  Press Win + R, type shell:startup, and press Enter. This opens your Startup folder.
3.  Right-click inside the Startup folder, select New > Shortcut.
4.  Browse to your qr_paster.pyw file, select it, and click Next/Finish.

### For macOS:

macOS requires a slightly different approach to run Python scripts silently in the background. We will use Automator.
1. Open Automator and create a new Application.
2. Search for the Run Shell Script action and drag it into the right pane.
3. Change the shell to /bin/bash (or /bin/zsh).
4. Enter the path to your Python executable and the script. It should look something like this:
> /usr/local/bin/python3 /path/to/your/qr_paster.py &

(You can find your python path by typing which python3 in the terminal).

5.  Save the Automator app (e.g., as "QRPaster").
6.  Go to System Settings > General > Login Items.
7.  Click the + button under "Open at Login" and select the Automator app you just created.

Crucial macOS Note: For pynput to detect global keystrokes like Command+Q on a Mac, your terminal (if running manually) or your Automator app (if running on startup) must be granted Accessibility permissions. macOS will likely prompt you the first time you run it, or you can go to System Settings > Privacy & Security > Accessibility to add it manually.

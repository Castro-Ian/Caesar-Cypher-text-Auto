import tkinter as tk
from tkinter import StringVar

# Function to apply Caesar Cipher logic
def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            result.append(char)
    return ''.join(result)

# Update function to handle automatic changes
def update_cipher(*args):
    try:
        text = entry_plain.get() if mode_var.get() == "Encode" else entry_cipher.get()
        shift = int(entry_key.get())
        if mode_var.get() == "Encode":
            result = caesar_cipher(text, shift)
            entry_cipher.delete(0, tk.END)
            entry_cipher.insert(0, result)
        else:
            result = caesar_cipher(text, shift, decode=True)
            entry_plain.delete(0, tk.END)
            entry_plain.insert(0, result)
    except ValueError:
        # Do not update if key is not a valid integer or fields are empty
        pass

# Initialize the main window
root = tk.Tk()
root.title("Automated Caesar Cipher Encoder/Decoder")

# Mode Selection (Encode/Decode)
mode_var = StringVar(value="Encode")
tk.Label(root, text="Mode").grid(row=0, column=0, padx=10, pady=10)
tk.OptionMenu(root, mode_var, "Encode", "Decode").grid(row=0, column=1, padx=10, pady=10)

# Plaintext Input
tk.Label(root, text="Plain Text").grid(row=1, column=0, padx=10, pady=10)
entry_plain = tk.Entry(root, width=50)
entry_plain.grid(row=1, column=1, padx=10, pady=10)

# Ciphertext Input
tk.Label(root, text="Cipher Text").grid(row=2, column=0, padx=10, pady=10)
entry_cipher = tk.Entry(root, width=50)
entry_cipher.grid(row=2, column=1, padx=10, pady=10)

# Key Input
tk.Label(root, text="Shift Key").grid(row=3, column=0, padx=10, pady=10)
entry_key = tk.Entry(root, width=10)
entry_key.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Trigger update when any input field or mode changes
mode_var.trace_add("write", update_cipher)
entry_plain.bind("<KeyRelease>", update_cipher)
entry_cipher.bind("<KeyRelease>", update_cipher)
entry_key.bind("<KeyRelease>", update_cipher)

# Start the Tkinter event loop
root.mainloop()


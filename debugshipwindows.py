import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

def start_debugging():
    output_text.delete(1.0, tk.END)
    threading.Thread(target=run_debugger).start()

def run_debugger():
    process = subprocess.Popen(["python", "./windows/debugshipwindows.ps1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        output_text.insert(tk.END, line)
    for line in process.stderr:
        output_text.insert(tk.END, line)

# Create the main window
root = tk.Tk()
root.title("DebugShip - GUI Debugger")

# Add a button to start debugging
start_button = tk.Button(root, text="Step into function, etc", command=stepInto)
start_button.pack(pady=10)
start_button = tk.Button(root, text="Quit operation and exit", command=q)
start_button.pack(pady=10)
start_button = tk.Button(root, text="Callstacks", command=k)
start_button.pack(pady=10)
start_button = tk.Button(root, text="Source code", command=l)
start_button.pack(pady=10)
start_button = tk.Button(root, text="Continue Operation", command=c)
start_button.pack(pady=10)
# Add a scrolled text area to show log/output
output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

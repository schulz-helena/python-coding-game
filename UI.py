import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Dictionary to store subprocesses
processes = {}

# List of status files
status_files = [
    "level_1.1.status", "level_1.2.status", "level_1.3.status",
    "level_2.1.status", "level_2.2.status", "level_2.3.status", "level_2.4.status",
    "level_3.1.status", "level_3.2.status",
    "level_4.1.status", "level_4.2.status", "level_5.1.status"
]

# Function to delete status files
def delete_status_files():
    for status_file in status_files:
        if os.path.exists(status_file):
            os.remove(status_file)

# Function to handle the completion of a script by checking the status file
def check_script_status(script_name, status_file, check_label):
    try:
        with open(status_file, "r") as f:
            status = f.read().strip()
            if status == "COMPLETED":
                check_label.config(text="✔")  # Update the label with a check mark
    except FileNotFoundError:
        # File does not exist yet, check again after a delay
        root.after(1000, lambda: check_script_status(script_name, status_file, check_label))

# Function to start a script
def start_script(script_name, status_file, check_label):
    if script_name not in processes or processes[script_name].poll() is not None:
        check_label.config(text="")  # Clear the check mark when restarting
        processes[script_name] = subprocess.Popen(["python", script_name])
        print("Info", f"Started {script_name}")
        # Start checking the script status
        root.after(1000, lambda: check_script_status(script_name, status_file, check_label))
    else:
        print("Warning", f"{script_name} is already running")

# Function to stop a script
def stop_script(script_name):
    if script_name in processes and processes[script_name].poll() is None:
        processes[script_name].kill()  # Forcefully terminate the process
        print("Info", f"Stopped {script_name}")
    else:
        print("Warning", f"{script_name} is not running")


# Create the main window
root = tk.Tk()
root.title("Python Learning UI")
root.geometry("400x700")  # Set the window size

# Function to create a script control frame
def create_script_control_frame(level_name, script_path, status_file):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    label = tk.Label(frame, text=level_name)
    label.pack(side=tk.LEFT, padx=10)

    start_button = tk.Button(frame, text="Start", command=lambda: start_script(script_path, status_file, check_label))
    start_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(frame, text="Stop", command=lambda: stop_script(script_path))
    stop_button.pack(side=tk.LEFT, padx=5)

    check_label = tk.Label(frame, text="", fg="green")
    check_label.pack(side=tk.LEFT, padx=10)

# Delete all status files at the start
delete_status_files()

# Create control frames for each level
create_script_control_frame("Level 1.1", "level1_1.py", "level_1.1.status")
create_script_control_frame("Level 1.2", "level1_2.py", "level_1.2.status")
create_script_control_frame("Level 1.3", "level1_3.py", "level_1.3.status")
create_script_control_frame("Level 2.1", "level2_1.py", "level_2.1.status")
create_script_control_frame("Level 2.2", "level2_2.py", "level_2.2.status")
create_script_control_frame("Level 2.3", "level2_3.py", "level_2.3.status")
create_script_control_frame("Level 2.4", "level2_4.py", "level_2.4.status")
create_script_control_frame("Level 3.1", "level3_1.py", "level_3.1.status")
create_script_control_frame("Level 3.2", "level3_2.py", "level_3.2.status")
create_script_control_frame("Level 4.1", "level4_1.py", "level_4.1.status")
create_script_control_frame("Level 4.2", "level4_2.py", "level_4.2.status")
create_script_control_frame("Level 5.1", "level5_1.py", "level_5.1.status")

# Run the Tkinter event loop
root.mainloop()

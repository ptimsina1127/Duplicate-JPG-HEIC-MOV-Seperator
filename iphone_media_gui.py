import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.ttk import Progressbar

# ---------------------------
# Utility Functions
# ---------------------------
def safe_move(src, dest, dry_run, status_box):
    """
    Moves file from src to dest.
    If dest exists, append a number to avoid overwrite.
    """
    dest = Path(dest)
    counter = 1
    new_dest = dest
    while new_dest.exists():
        new_dest = dest.with_name(f"{dest.stem}_{counter}{dest.suffix}")
        counter += 1

    if dry_run:
        status_box.insert(tk.END, f"DRY RUN: WOULD MOVE {src} -> {new_dest}\n")
    else:
        shutil.move(src, new_dest)
        status_box.insert(tk.END, f"MOVED: {src} -> {new_dest}\n")
    status_box.see(tk.END)

def move_files(main_folder, ext_move, ext_match, temp_folder_name, dry_run, status_box, progress=None):
    main_folder = Path(main_folder)
    temp_folder = main_folder / temp_folder_name
    temp_folder.mkdir(exist_ok=True)
    log_file = temp_folder / f"{temp_folder_name}_log.txt"

    all_files = []
    for root, dirs, files in os.walk(main_folder):
        files = [f for f in files if not f.startswith(".")]
        for file in files:
            if file.lower().endswith(ext_move.lower()):
                file_name = Path(file).stem
                if any((Path(root) / f"{file_name}{m_ext}").exists() for m_ext in ext_match):
                    all_files.append((Path(root) / file, temp_folder / file))

    total = len(all_files)
    if progress:
        progress['maximum'] = total
        progress['value'] = 0

    with open(log_file, "w") as log:
        log.write(f"{temp_folder_name.upper()} MOVE LOG\n")
        log.write("="*40 + "\n\n")
        for idx, (src, dest) in enumerate(all_files, 1):
            safe_move(src, dest, dry_run, status_box)
            if not dry_run:
                log.write(f"MOVED: {src.name}\nFROM: {src.parent}\n\n")
            if progress:
                progress['value'] = idx
                status_box.update_idletasks()

    status_box.insert(tk.END, f"Operation complete for {temp_folder_name}\n\n")
    status_box.see(tk.END)

def restore_files(temp_folder, dry_run, status_box, progress=None):
    temp_folder = Path(temp_folder)
    log_file = next(temp_folder.glob("*_log.txt"), None)
    if not log_file:
        status_box.insert(tk.END, f"No log file found in {temp_folder}\n")
        return

    with open(log_file, "r") as log:
        lines = log.readlines()

    restore_pairs = []
    file_name = ""
    folder_path = ""
    for line in lines:
        line = line.strip()
        if line.startswith("MOVED:"):
            file_name = line.replace("MOVED:", "").strip()
        elif line.startswith("FROM:"):
            folder_path = line.replace("FROM:", "").strip()
            restore_pairs.append((temp_folder / file_name, Path(folder_path) / file_name))

    total = len(restore_pairs)
    if progress:
        progress['maximum'] = total
        progress['value'] = 0

    for idx, (src, dest) in enumerate(restore_pairs, 1):
        safe_move(src, dest, dry_run, status_box)
        if progress:
            progress['value'] = idx
            status_box.update_idletasks()

# ---------------------------
# GUI Functions
# ---------------------------
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def run_move_mov_jpg():
    folder = folder_path.get()
    dry = dry_var.get()
    move_files(folder, ".mov", [".jpg"], "temporary MOV", dry, status_box, progress_bar)

def run_move_heic_jpg():
    folder = folder_path.get()
    dry = dry_var.get()
    move_files(folder, ".heic", [".jpg", ".jpeg"], "temporary HEIC", dry, status_box, progress_bar)

def run_separate_mov_heic():
    folder = folder_path.get()
    dry = dry_var.get()
    move_files(folder, ".mov", [".heic"], "temporary MOV", dry, status_box, progress_bar)

def run_restore():
    folder = folder_path.get()
    dry = dry_var.get()
    temp_mov = Path(folder) / "temporary MOV"
    temp_heic = Path(folder) / "temporary HEIC"
    restore_files(temp_mov, dry, status_box, progress_bar)
    restore_files(temp_heic, dry, status_box, progress_bar)

# ---------------------------
# GUI Setup
# ---------------------------
root = tk.Tk()
root.title("iPhone Media Organizer Tool")

folder_path = tk.StringVar()
dry_var = tk.BooleanVar(value=True)

tk.Label(root, text="Select iPhone Main Folder:").pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=60).pack(padx=5)
tk.Button(root, text="Browse Folder", command=select_folder).pack(pady=5)

tk.Checkbutton(root, text="Dry Run (do not move files)", variable=dry_var).pack()

# Buttons for each operation
tk.Button(root, text="Move MOV files matching JPG", command=run_move_mov_jpg, bg="lightgreen").pack(pady=2)
tk.Button(root, text="Move HEIC files matching JPG/JPEG", command=run_move_heic_jpg, bg="lightgreen").pack(pady=2)
tk.Button(root, text="Separate MOV files that match HEIC", command=run_separate_mov_heic, bg="lightgreen").pack(pady=2)
tk.Button(root, text="Restore Files from Logs", command=run_restore, bg="lightblue").pack(pady=5)

# Progress bar
progress_bar = Progressbar(root, orient=tk.HORIZONTAL, length=600, mode='determinate')
progress_bar.pack(pady=5)

# Status box
tk.Label(root, text="Status:").pack(pady=5)
status_box = scrolledtext.ScrolledText(root, width=80, height=20)
status_box.pack(padx=5, pady=5)

root.mainloop()

# iPhone Media Organizer Tool

**A Very Handy tool to separate same-named JPG, HEIC, and MOV files.**  

This tool is designed to help you **organize your photos and videos from iPhone** efficiently. If you've ever struggled with managing files in the Apple ecosystem, this is your **relief** — keeping all your media neat and easy to restore.  

---

## Features

- Move **MOV files** that have the same name as JPG files into a dedicated folder (`temporary MOV`).  
- Move **HEIC files** that have the same name as JPG/JPEG files into a dedicated folder (`temporary HEIC`).  
- Separate **MOV and HEIC files** with the same names to avoid clutter.  
- **Restore files** safely back to their original folders using log files.  
- **Dry run mode** to check what will happen without making changes.  
- **Handles duplicates safely**, automatically renaming files if needed.  
- **GUI interface** for easy one-click operations.  
- **Progress bar and status log** to track operations in real time.  
- Fully interactive — no hardcoded paths required.  

---

## How It Works

1. Select your **iPhone main folder** in the GUI.  
2. Use the buttons to:
   - Move MOV files matching JPG  
   - Move HEIC files matching JPG/JPEG  
   - Separate MOV files that match HEIC  
   - Restore files from logs  
3. Dry run first to preview actions, then run actual operations.  
4. All logs are saved in `temporary MOV` or `temporary HEIC` folders.  

---

## Requirements

- **Python 3.x**  
- Standard library only (no extra packages required)  
- Works on **Windows**  

---

## Usage

1. Download the script and save it as `iphone_media_gui.py`.  
2. Run the script:  
```bash
python iphone_media_gui.py ``

3. hello world

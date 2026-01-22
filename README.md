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
python iphone_media_gui.py

```

---
## Follow these steps in the GUI:

1. Browse and select your iPhone main folder.
2. Toggle Dry Run if you want to test the actions first.
3. Click the buttons to move, separate, or restore files.
4. Monitor the status box and progress bar to track progress.

5. Screenshots / GIFs
GUI Main Window:
<img width="674" height="633" alt="image" src="https://github.com/user-attachments/assets/a270d69b-114d-4e19-9fe6-a86ccc20062c" />


Dry Run Mode:
<img width="493" height="674" alt="image" src="https://github.com/user-attachments/assets/f8747227-ad24-461d-8f9a-6294890cdfa1" />


Restoring Files:
<img width="671" height="668" alt="image" src="https://github.com/user-attachments/assets/87c793ee-b333-467b-8bab-491cc53e66a4" />


GIF Example of Moving Files:

![python_qKTYCmQTDQ](https://github.com/user-attachments/assets/22c97a5e-6ad6-4bf2-8617-91146dfd04c9)

Benefits
1. Organizes all your iPhone media files in one place.
2. Eliminates confusion with duplicate names across formats.
3. Provides a safe and reversible workflow.
4. A relief to the Apple ecosystem, giving you control over your photos and videos.


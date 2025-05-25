# 🗂️ File Organizer Script

A simple and effective Python script to **automatically organize files** in a folder based on their file types — such as Documents, Images, Videos, Audio, Archives, and Scripts.

---

## 📌 Features
- Sorts and moves files into categorized folders.
- Supports multiple file extensions.
- Logs all actions to `file_organizer.log`.
- Simple command-line interface (CLI).

---

## 🛠 Technologies Used
- Python 3
- Built-in modules: `os`, `shutil`, `logging`

---

## 🚀 How to Use

1. Clone this repository or download the script.
2. Open Terminal / Command Prompt.
3. Run the script:
   ```bash
   python file_organizer.py
   ```
4. Enter the full path of the folder you want to organize.

---

## 📝 Example
```
Before:
📂 Downloads/
├── resume.pdf
├── song.mp3
├── script.py
├── image.png

After:
📂 Downloads/
├── Documents/resume.pdf
├── Audio/song.mp3
├── Scripts/script.py
├── Images/image.png
```

---

## 📂 Output Folders
The script creates and moves files into these:
- `Documents`
- `Images`
- `Videos`
- `Audio`
- `Archives`
- `Scripts`
- `Others` (for uncategorized file types)

---

## 📄 Files Included
| File | Description |
|------|-------------|
| `file_organizer.py` | Main Python script |
| `file_organizer.log` | Log file with all activity |
| `User_Guide.pdf` | Visual user guide with screenshots |
| `README.md` | GitHub project documentation |

---

import os
import sys
import shutil
from pathlib import Path
# Import the UI class we just created
from ui import OrganizerUI
from PySide6.QtWidgets import QApplication

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
}

# The logic now accepts a target directory and the ui log element
def organize_folder(target_dir, ui_logger):
    path = Path(target_dir)
    
    if not path.exists():
        ui_logger.append(f"Error: The directory '{target_dir}' does not exist.")
        return

    moved_count = 0

    for item in path.iterdir():
        # Prevent moving the code files themselves
        if item.is_dir() or item.name in ["fileorganiser.py", "ui.py"]:
            continue
            
        file_ext = item.suffix.lower()
        moved = False

        for folder_name, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                destination_folder = path / folder_name
                destination_folder.mkdir(exist_ok=True)
                destination_path = destination_folder / item.name
                
                if destination_path.exists():
                    ui_logger.append(f"Skipped (Exists): {item.name}")
                    continue

                shutil.move(str(item), str(destination_path))
                ui_logger.append(f"Moved: {item.name} -> {folder_name}/")
                moved_count += 1
                moved = True
                break
        
        if not moved and file_ext != "":
            others_folder = path / "Others"
            others_folder.mkdir(exist_ok=True)
            destination_path = others_folder / item.name
            
            if not destination_path.exists():
                shutil.move(str(item), str(destination_path))
                ui_logger.append(f"Moved: {item.name} -> Others/")
                moved_count += 1

    ui_logger.append(f"\nFinished! Successfully organized {moved_count} files.")


# The App Entry Point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # We pass the organize_folder function into the UI as a callback
    window = OrganizerUI(start_organizer_callback=organize_folder)
    window.show()
    
    sys.exit(app.exec())
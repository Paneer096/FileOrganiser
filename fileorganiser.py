import os
import shutil
from pathlib import Path

# Define your mapping of folders to extensions
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
}

def organize_folder(target_dir):
    path = Path(target_dir)
    
    if not path.exists():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Organizing files in: {path.resolve()}\n")
    moved_count = 0

    # Iterate through all items in the directory
    for item in path.iterdir():
        # Skip directories and the script itself if it's running inside the same folder
        if item.is_dir() or item.name == "organizer.py":
            continue
            
        file_ext = item.suffix.lower()
        moved = False

        # Look for a matching category in our map
        for folder_name, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                # Create the category folder if it doesn't exist yet
                destination_folder = path / folder_name
                destination_folder.mkdir(exist_ok=True)
                
                # Define the final path for the file
                destination_path = destination_folder / item.name
                
                # Handle potential naming conflicts (don't overwrite files)
                if destination_path.exists():
                    print(f"Skipped (File already exists in destination): {item.name}")
                    continue

                # Move the file
                shutil.move(str(item), str(destination_path))
                print(f"Moved: {item.name} -> {folder_name}/")
                moved_count += 1
                moved = True
                break
        
        # Optional: Handle unknown files by putting them in an 'Others' folder
        if not moved and file_ext != "": # Ignore files without an extension
            others_folder = path / "Others"
            others_folder.mkdir(exist_ok=True)
            destination_path = others_folder / item.name
            
            if not destination_path.exists():
                shutil.move(str(item), str(destination_path))
                print(f"Moved: {item.name} -> Others/")
                moved_count += 1

    print(f"\nDone! Successfully organized {moved_count} files.")

if __name__ == "__main__":
    # Prompt the user for the directory path
    user_input = input("Enter the full path of the folder to organize (e.g., C:\\Users\\Name\\Downloads): ").strip()
    # Remove surrounding quotes if the user dragged and dropped the folder into the terminal
    user_input = user_input.strip('"\'')
    
    organize_folder(user_input)
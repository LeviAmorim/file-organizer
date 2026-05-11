import os
import shutil

# Folder to organize
folder_path = "C:/Users/Levi/Downloads"

# File categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".html", ".css", ".js"]
}

# Organize files
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()

        for folder_name, extensions in file_types.items():
            if file_extension in extensions:

                destination_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, file_name))

                print(f"Moved: {file_name} → {folder_name}")

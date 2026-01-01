import os
import shutil


SOURCE_FOLDER = "C:/Users/Deb Lahiry/Downloads"


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
}

def create_folders():
    for folder in FILE_TYPES:
        folder_path = os.path.join(SOURCE_FOLDER, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files():
    for file_name in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file_name)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    destination = os.path.join(SOURCE_FOLDER, folder, file_name)
                    shutil.move(file_path, destination)
                    break

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("Files organized successfully!")

import os
import shutil
import logging

# Set up logging
logging.basicConfig(filename='file_organizer.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# File categories and their extensions
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"The path '{directory}' is not a valid directory.")

        for filename in os.listdir(directory):
            source_path = os.path.join(directory, filename)

            # Skip folders
            if os.path.isdir(source_path):
                continue

            _, extension = os.path.splitext(filename)
            category = get_category(extension)
            target_folder = os.path.join(directory, category)

            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(source_path, os.path.join(target_folder, filename))
                logging.info(f"Moved: {filename} --> {category}/")
                print(f"Moved: {filename} --> {category}/")
            except Exception as move_error:
                logging.error(f"Failed to move {filename}: {move_error}")
                print(f"❌ Failed to move {filename}. See log for details.")

    except Exception as e:
        logging.error(f"Error organizing files: {e}")
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    path = input("Enter the full path of the directory to organize: ").strip()
    organize_files(path)

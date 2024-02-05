import os
from mutagen.easyid3 import EasyID3

def list_files_by_subfolder(directory):
    files_by_subfolder = {}

    for root, _, files in os.walk(directory):
        subfolder_name = os.path.basename(root)
        for file in files:
            file_path = os.path.join(root, file)
            title, author = get_music_details(file_path)
            files_by_subfolder.setdefault(subfolder_name, []).append([file, title, author])

    for subfolder, files in files_by_subfolder.items():
        print(f"{subfolder}")
        for file_details in files:
            print(f"  - Filename: {file_details[0]}")
            print(f"    Title: {file_details[1]}")
            print(f"    Author: {file_details[2]}")



def get_music_details(file_path):
    try:
        audio = EasyID3(file_path)
        title = audio['title'][0]
        author = audio['albumartist'][0]
        # Add more fields as needed (e.g., album, genre)

        return title, author
    except Exception as e:
        print(f"Error: {e}")
        return None, None

directory_path = 'C:/Users/vandr/Downloads/Zenék'
list_files_by_subfolder(directory_path)

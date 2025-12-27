import os
import shutil

def file_sorter(base_path):
    base_path = r'C:\Users\ayush\gsoc-training\FileSorter\junk'
    files = os.listdir(base_path)
    for file in files:
        file_name, extension_name = os.path.splitext(file)
        if extension_name == '':
            continue

        destination_folder = ""
        if extension_name.lower() in ['.pdf', '.txt', '.docx', '']:
            # move to documents
            destination_folder = r"Documents"
            destination_folder = os.path.join(base_path, destination_folder)

        elif extension_name.lower() in ['.png', '.jpeg', '.jpg']:
            # move to images
            destination_folder = r"Images"
            destination_folder =os.path.join(base_path,destination_folder )
        else:
            destination_folder = r"Others"
            destination_folder = os.path.join(base_path, destination_folder)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        source_folder = os.path.join(base_path, file)
        shutil.move(source_folder, destination_folder)
        print(f'{file_name} moved to {destination_folder}')

    print("success")

file_sorter(r'C:\Users\ayush\gsoc-training\FileSorter\junk')

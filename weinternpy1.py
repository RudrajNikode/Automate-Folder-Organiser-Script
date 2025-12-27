import os
import shutil

def organize_files(base_folder):
    
    for item in os.listdir(base_folder):
        full_path = os.path.join(base_folder, item)

        
        if os.path.isfile(full_path):
            
            extension = item.split('.')[-1].lower()

            
            destination_folder = os.path.join(base_folder, extension)

            
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            
            shutil.move(full_path, os.path.join(destination_folder, item))


if __name__ == "__main__":
    folder_location = r"C:\Users\rudra\OneDrive\Desktop\test_folder"
    organize_files(folder_location)

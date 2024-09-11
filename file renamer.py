import os
import datetime
import random

def rename_files_in_folder(folder_path):
    # List all files in the folder
    file_list = os.listdir(folder_path)

    for old_name in file_list:
        # Split the filename into date and rest
        date_part, rest_part = old_name.split('-IMG_')

        # Parse the date in the original format
        date = datetime.datetime.strptime(date_part, '%d%m%Y')

        # Generate a random time between 10:00 and 13:00
        hours = random.randint(10, 12)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        milliseconds = random.randint(0, 99)

        time = datetime.time(hours, minutes, seconds, milliseconds * 10000)  # Convert milliseconds to microseconds

        # Combine date and time
        new_name = date.strftime('%Y-%m-%d_') + time.strftime('%H.%M.%S.%f')[:-4] + ".jpg"

        # Rename the file
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))

if __name__ == "__main__":
    folder_path = 'C:/Users/Hugo/Desktop/test'  # Replace with the path to your folder
    rename_files_in_folder(folder_path)

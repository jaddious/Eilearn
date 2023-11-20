# script that moves all the files in floders and alll subfolders that end with .xml to a new folder
# also moves all the files in the folder and all subfolders that end with .jpg to a new folder

import os
import shutil

layer_name = "etat_major"
zoom_level = 15

# path to the folder where the files are
path = r"map_layers\{}\images\tiles\\{}".format(
    layer_name, zoom_level)

# path to the folder where the files will be moved to
to_label = r"map_layers\{}\images\to_label\\{}".format(
    layer_name, zoom_level)

sub_folders = os.listdir(path)

if not os.path.exists(to_label):
    os.makedirs(to_label)

for sub_folder in sub_folders:
    print(f"Subfolder: {sub_folder}")
    jpgs = [jpg for jpg in os.listdir(os.path.join(
        path, sub_folder)) if jpg.endswith(".jpg")]
    print(f"Number of jpgs in {sub_folder}: {len(jpgs)}")
    for jpg in jpgs:
        # copy to to_be_labelled folder
        shutil.copy(os.path.join(path, sub_folder, jpg), to_label)
        # rename copied file
        os.rename(os.path.join(to_label, jpg), os.path.join(
            to_label, f"{zoom_level}_{sub_folder}_{jpg}"))

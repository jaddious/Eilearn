# script that moves all the files in floders and alll subfolders that end with .xml to a new folder
# also moves all the files in the folder and all subfolders that end with .jpg to a new folder

import os
import shutil

layer_name = "ign_france"
zoom_level = 15

# path to the folder where the files are
labeled = r"map_layers\{}\images\labeled".format(
    layer_name)

# path to the folder where the files will be moved to
to_label = r"map_layers\{}\images\to_label".format(
    layer_name)

if not os.path.exists(labeled):
    os.makedirs(labeled)

# move all the xml files to the new folder along with the jpg files
for file in os.listdir(to_label):
    if file.endswith(".xml"):
        shutil.move(os.path.join(to_label, file), os.path.join(labeled, file))
        shutil.move(os.path.join(
            to_label, file[:-4] + ".jpg"), os.path.join(labeled, file[:-4] + ".jpg"))
        print("moved " + file + " to " + to_label)

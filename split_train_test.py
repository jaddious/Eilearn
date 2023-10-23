# split the images in the labeled folder to train and test folders

import os
import shutil

layer_name = "popp_karte"

files = os.listdir("map_layers\{}\\labeled".format(layer_name))


# move 80% of the files to train folder and 20% to test folder
# it must be random 

# create train folder if it doesnt exist: 
if not os.path.exists("map_layers\{}\\train".format(layer_name)):
    os.makedirs("map_layers\{}\\train".format(layer_name))
if not os.path.exists("map_layers\{}\\test".format(layer_name)):
    os.makedirs("map_layers\{}\\test".format(layer_name))

# move the files to train folder
# MAKE IT RANDOM 
train_files = files[:int(len(files)*0.8)]

for file in train_files:
    shutil.move(os.path.join("map_layers\{}\\labeled".format(layer_name), file), os.path.join("map_layers\{}\\train".format(layer_name), file))
    print("moved " + file + " to train folder")

# remove them from the files list
for file in train_files:
    files.remove(file)
    
# move the files to test folder
for file in files:
    shutil.move(os.path.join("map_layers\{}\\labeled".format(layer_name), file), os.path.join("map_layers\{}\\test".format(layer_name), file))
    print("moved " + file + " to test folder")
    

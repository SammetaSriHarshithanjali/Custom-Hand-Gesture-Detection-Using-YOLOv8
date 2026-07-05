import os
import shutil
import random

# Source folders
image_folder = r"C:\Users\Saideepu Balaraju\Pictures\Images"
label_folder = r"C:\Users\Saideepu Balaraju\Desktop\HandGestureDataset\labels"

# Destination folders
dataset_root = r"C:\Users\Saideepu Balaraju\Desktop\HandGestureDataset"

train_img = os.path.join(dataset_root, "images", "train")
val_img = os.path.join(dataset_root, "images", "val")
test_img = os.path.join(dataset_root, "images", "test")

train_lbl = os.path.join(dataset_root, "labels", "train")
val_lbl = os.path.join(dataset_root, "labels", "val")
test_lbl = os.path.join(dataset_root, "labels", "test")

# Get all images
images = [f for f in os.listdir(image_folder)
          if f.lower().endswith((".jpg", ".jpeg", ".png"))]

print("Total Images Found:", len(images))

random.seed(42)
random.shuffle(images)

n = len(images)

train_count = int(0.8 * n)
val_count = int(0.1 * n)

train_set = images[:train_count]
val_set = images[train_count:train_count + val_count]
test_set = images[train_count + val_count:]

def copy_files(file_list, img_dest, lbl_dest):

    for img in file_list:

        shutil.copy(
            os.path.join(image_folder, img),
            os.path.join(img_dest, img)
        )

        txt = os.path.splitext(img)[0] + ".txt"

        txt_path = os.path.join(label_folder, txt)

        if os.path.exists(txt_path):
            shutil.copy(
                txt_path,
                os.path.join(lbl_dest, txt)
            )

copy_files(train_set, train_img, train_lbl)
copy_files(val_set, val_img, val_lbl)
copy_files(test_set, test_img, test_lbl)

print("\nDataset Split Completed")
print("Train:", len(train_set))
print("Val:", len(val_set))
print("Test:", len(test_set))
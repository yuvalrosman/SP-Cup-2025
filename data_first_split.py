import os
import shutil
import random

# Set the directories
base_dir = './datasets/'
train_dir = os.path.join(base_dir, 'DFWild/train')
validation_dir = os.path.join(base_dir, 'DFWild/validation')

# Create a new directory for the split
new_base_dir = os.path.join(base_dir, 'DFWild-FirstSplit')
os.makedirs(os.path.join(new_base_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(new_base_dir, 'test'), exist_ok=True)

# Load real images from the training set
real_images_train = [os.path.join(train_dir, 'real', f) for f in os.listdir(os.path.join(train_dir, 'real'))]
# Load real and fake images from the validation set
real_images_val = [os.path.join(validation_dir, 'real', f) for f in os.listdir(os.path.join(validation_dir, 'real'))]
fake_images_val = [os.path.join(validation_dir, 'fake', f) for f in os.listdir(os.path.join(validation_dir, 'fake'))]

# Combine all images
all_images = real_images_train + real_images_val + fake_images_val
random.shuffle(all_images)

# Define the split ratio
split_ratio = 0.8
split_index = int(len(all_images) * split_ratio)

# Split into training and testing
train_images = all_images[:split_index]
test_images = all_images[split_index:]

# Move images to the new directories
for img in train_images:
    shutil.copy(img, os.path.join(new_base_dir, 'train', os.path.basename(img)))

for img in test_images:
    shutil.copy(img, os.path.join(new_base_dir, 'test', os.path.basename(img)))

print(f'Train set created with {len(train_images)} images.')
print(f'Test set created with {len(test_images)} images.')

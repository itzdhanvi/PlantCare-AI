import os

train_path = "dataset/Our Dataset/Train"

classes = os.listdir(train_path)

print("Total Classes:", len(classes))
print("Class Names:", classes)

class_count = {}

for c in classes:
    class_path = os.path.join(train_path, c)
    
    if os.path.isdir(class_path):
        images = os.listdir(class_path)
        class_count[c] = len(images)

print("Images per class:")
print(class_count)

import matplotlib.pyplot as plt

names = list(class_count.keys())
values = list(class_count.values())

plt.figure(figsize=(10,5))
plt.bar(names, values)

plt.xticks(rotation=90)
plt.title("Class Distribution")
plt.xlabel("Plant Disease Classes")
plt.ylabel("Number of Images")

plt.show()
import random
import cv2
import matplotlib.pyplot as plt

# Random class choose
random_class = random.choice(classes)

class_path = os.path.join(train_path, random_class)

images = os.listdir(class_path)

# random image choose
img_name = random.choice(images)

img_path = os.path.join(class_path, img_name)

img = cv2.imread(img_path)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(random_class)
plt.axis("off")

plt.show()
from PIL import Image

sample_class = classes[0]

sample_path = os.path.join(train_path, sample_class)

sample_image = os.listdir(sample_path)[0]

img_path = os.path.join(sample_path, sample_image)

img = Image.open(img_path)

print("Image Size:", img.size)

total_images = sum(class_count.values())

print("Total Images in Dataset:", total_images)
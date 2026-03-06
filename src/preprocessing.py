from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# Training data generator with light augmentation
train_datagen = ImageDataGenerator(
preprocessing_function=preprocess_input, 
  horizontal_flip=True, 
  rotation_range=20, 
  zoom_range=0.15, 
  width_shift_range=0.1, 
  height_shift_range=0.1, 
  fill_mode='reflect'
)
# Validation data generator (no augmentation)
valid_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
# Create data generators
train_gen = train_datagen.flow_from_directory(
train_dir,
target_size=IMG_SIZE, 
  batch_size=BATCH_SIZE, 
  class_mode='categorical', 
  shuffle=True, 
  seed=SEED
)
valid_gen = valid_datagen.flow_from_directory(
valid_dir, 
  target_size=IMG_SIZE, 
  batch_size=BATCH_SIZE, 
  class_mode='categorical', 
  shuffle=False
)

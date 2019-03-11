from keras.models import load_model
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import img_to_array, load_img
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet import preprocess_input
import numpy as np

model = load_model('./bbq_model.h5')

test_data_generator = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

test_generator = test_data_generator.flow_from_directory(
    './images/test',
    target_size=(224, 224),
    color_mode='rgb',
    batch_size=1,
    class_mode='categorical'
)

labels = dict((v,k) for k,v in test_generator.class_indices.items())

for i in range(len(test_generator)):
    (img, category) = test_generator[i]
    probabilities = model.predict(img)
    label = labels[category.argmax(axis=-1)[0]]
    prediction = labels[probabilities.argmax(axis=-1)[0]]
    print(("FAIL", "OK")[label == prediction], ' label:', label, 'prediction: ', prediction)
    
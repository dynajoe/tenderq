from keras.models import load_model
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import img_to_array, load_img

bbq_model = load_model('./bbq_model.h5')

img = preprocess_input(img_to_array(
    load_img('./images/test/brisket/grey_oaks_brisket.jpg')))

formatted_image = img.reshape((1,) + img.shape)

probabilities = bbq_model.predict(formatted_image)

labels = sorted(['ribs', 'chicken', 'brisket', 'pork', 'other'])

print('prediction: ' + labels[probabilities.argmax(axis=-1)[0]])

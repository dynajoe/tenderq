import tensorflowjs as tfjs
from keras.models import load_model

tfjs_target_dir = './tfjs_out'

model = load_model('./bbq_model.h5')

tfjs.converters.save_keras_model(model, tfjs_target_dir)
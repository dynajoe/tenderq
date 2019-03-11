from keras.applications import MobileNet
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet import preprocess_input

base_model = MobileNet(weights='imagenet', include_top=False)

bbq_output = base_model.output
bbq_output = GlobalAveragePooling2D()(bbq_output)
bbq_output = Dense(1024, activation='relu')(bbq_output)
bbq_output = Dense(1024, activation='relu')(bbq_output)
bbq_output = Dense(5, activation='softmax')(bbq_output)

model = Model(inputs=base_model.input, outputs=bbq_output)

for layer in model.layers[:87]:
    layer.trainable = False

for i, layer in enumerate(model.layers):
    print(i, layer.name, layer.trainable)

train_data_generator = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

validation_data_generator = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

train_generator = train_data_generator.flow_from_directory(
    './images/train',
    target_size=(224, 224),
    color_mode='rgb',
    batch_size=64,
    class_mode='categorical',
    shuffle=True
)

validation_generator = validation_data_generator.flow_from_directory(
    './images/validate',
    target_size=(224, 224),
    color_mode='rgb',
    batch_size=10,
    class_mode='categorical',
    shuffle=True
)

model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

step_size_train = train_generator.n//train_generator.batch_size

model.fit_generator(
    generator=train_generator,
    steps_per_epoch=step_size_train,
    validation_data=validation_generator,
    validation_steps=4,
    epochs=5
)

model.save('./bbq_model.h5', overwrite=True)

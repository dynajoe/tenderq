from keras.applications import MobileNet
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet import preprocess_input

base_model = MobileNet(weights='imagenet', include_top=False)

bbq_output = base_model.output
bbq_output = GlobalAveragePooling2D()(bbq_output)
bbq_output = Dense(1024, activation='relu')(bbq_output)
bbq_output = Dense(1024, activation='relu')(bbq_output)
bbq_output = Dense(512, activation='relu')(bbq_output)
bbq_output = Dense(5, activation='softmax')(bbq_output)

model = Model(inputs=base_model.input, outputs=bbq_output)

for layer in model.layers[0:20]:
    layer.trainable = False

train_data_generator = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

test_data_generator = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

train_generator = train_data_generator.flow_from_directory(
    './images/train',
    target_size=(224, 224),
    color_mode='rgb',
    batch_size=32,
    class_mode='categorical',
    shuffle=True
)

# test_generator = test_data_generator.flow_from_directory(
#     './images/test',
#     target_size=(224, 224),
#     color_mode='rgb',
#     batch_size=32,
#     class_mode='categorical',
#     shuffle=True
# )

model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

step_size_train = train_generator.n//train_generator.batch_size

model.fit_generator(
    generator=train_generator,
    steps_per_epoch=step_size_train,
    # validation_data=test_generator,
    # validation_steps=10,
    epochs=10
)

model.save('./bbq_model.tf', overwrite=True)

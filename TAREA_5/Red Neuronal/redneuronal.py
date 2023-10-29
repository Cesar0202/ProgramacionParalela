import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos y transformar las etiquetas en codificación one-hot
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

# Crear un modelo secuencial
model = Sequential()

# Aplanar la entrada (28x28 imágenes)
model.add(Flatten(input_shape=(28, 28)))

# Capa oculta con 128 neuronas y función de activación ReLU
model.add(Dense(128, activation='relu'))

# Capa de salida con 10 neuronas para las 10 clases y función de activación softmax
model.add(Dense(10, activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Entrenar el modelo
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))
# Evaluar el rendimiento del modelo en el conjunto de prueba
loss, accuracy = model.evaluate(x_test, y_test)
print("Loss:", loss)
print("Accuracy:", accuracy)

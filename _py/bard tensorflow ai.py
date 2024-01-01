import tensorflow as tf
import tensorflow_datasets as tfds

# Завантажуємо набір даних тексту та коду
dataset = tfds.load("text_and_code", split="train", download=True)

# Створюємо нейронну мережу
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim=10000, output_dim=128),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(10000)
])

# Навчаємо нейронну мережу
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(dataset.map(lambda x, y: x), epochs=100)

# Використовуємо нейронну мережу для генерування тексту
text = model.predict(tf.constant(["Я - велика мовна модель."]))
print(text)

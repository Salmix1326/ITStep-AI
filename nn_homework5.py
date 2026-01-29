import onnxruntime as ort
from PIL import Image
from torchvision import transforms
import numpy as np

# открываем модель
session = ort.InferenceSession(
    "model-fruits.onnx"
)

# классы в датасете
class_names = [
    "Apple Braeburn",
    "Apple Granny Smith",
    "Apricot",
    "Avocado",
    "Banana",
    "Blueberry",
    "Cactus fruit",
    "Cantaloupe",
    "Cherry",
    "Clementine",
    "Corn",
    "Cucumber Ripe",
    "Grape Blue",
    "Kiwi",
    "Lemon",
    "Limes",
    "Mango",
    "Onion White",
    "Orange",
    "Papaya",
    "Passion Fruit",
    "Peach",
    "Pear",
    "Pepper Green",
    "Pepper Red",
    "Pineapple",
    "Plum",
    "Pomegranate",
    "Potato Red",
    "Raspberry",
    "Strawberry",
    "Tomato",
    "Watermelon"
]

# трансформер
test_transformer = transforms.Compose(
    [transforms.Resize([64, 64]),
     transforms.ToTensor()
    ]
)

# открытие картинки
img = Image.open("data/lesson many/fruits/25.jpg")
img.show()

# трансформация картинки
input_tensor = test_transformer(img)

# добавление 1 для тензора (reshape add 1)
input_tensor = input_tensor.unsqueeze(0)

# изменение картинки в numpy
input_tensor = input_tensor.numpy()

# использование модели
results = session.run(
    output_names=None,
    input_feed={
        "image": input_tensor
    }
)

# индекс с самой большой вероятностью -- ind из results (result для одной картинки)
result = results[0][0]
ind = result.argmax()

# обозначение класса по индексу
label = class_names[ind]

# просчет вероятностей через Softmax из result для одной картинки
max_num = result.max()
result -= max_num
exp_result = np.exp(result)
probs = exp_result / exp_result.sum()

target_prob = probs[ind]

print(probs)
print(f"Index with greatest probability: {ind}. Class name: {label}. Probability: {target_prob*100}%")
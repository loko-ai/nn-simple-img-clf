
## gli import non funzionano con python 3.10
## scomodo gli import che non vengono suggeriti automaticamente

from keras.utils.image_utils import load_img
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.resnet import ResNet50, decode_predictions
from keras.preprocessing.image import image_utils

model = ResNet50()

def classify(img):
    img = image_utils.img_to_array(img)
    print(img.shape)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    print(img.shape)
    img = preprocess_input(img)
    print(img.shape)
    #model.summary()
    print(model.input_shape)

    ris = model.predict(img)
    return decode_predictions(ris)[0][0][1]

if __name__ == '__main__':
    img = load_img("/home/alejandro/Pictures/cat_ex3.jpeg", target_size=(224,224))
    print(img)
    print(classify(img))

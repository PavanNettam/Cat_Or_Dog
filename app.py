import re
import numpy as np
from flask import Flask, render_template, request

from tensorflow import keras
cnn = keras.models.load_model('/Users/pavannettam/Desktop/CatOrDog/store')

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    imagefile = request.files["imagefile"]
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    
    test_image = load_img(image_path, target_size=(150,150))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn.predict(test_image)
    if result[0][0] == 1:
        classi = 'dog'
    else:
        classi = 'cat'
    
    return render_template('index.html',prediction=classi)





if __name__ == '__main__':
    app.run(port=3000,debug=True)

# Cat_Or_Dog

<h2>Abstract</h2>
This is Convolutional Neural Network classification to classify cats and dogs built with keras in Tensorflow. There are a total of 10,000 images of cats and dogs considered, out of which 8000 are 
used for training and 2000 are used for testing. The images are rescaled to 150 X 150 sized images. The model is trained with 30 epochs and a final accuracy of 
94.44% is achieved for Epoch 30/30.<br>

<img width="1155" alt="Screenshot 2022-03-13 at 10 27 55 PM" src="https://user-images.githubusercontent.com/79460453/158070466-d440daf4-82c0-4f89-ab93-ed72e8b20efa.png">

<h2>Improvements</h2>
Initially the model was trained with image rescaling of 64 X 64 and for 25 epochs the final accuracy obtained was 91%, however by increasing the scaling of the
image and the number of epochs the accuracy increased by 4.44%

<h2>Deployed</h2>
The model is deployed with the help of flask API in python, with a simple UI. You can choose an image file and upload the same into the website and click on
"Predict" button the website replies with a message indicating weather the image is cat or dog. However this is a bi-class classification model it classifies every
image to either cat or dog and nothing else.<br>

<img width="842" alt="Screenshot 2022-03-13 at 7 26 51 PM" src="https://user-images.githubusercontent.com/79460453/158070705-61014b64-ca82-493c-98b8-2ea13f5ddbcc.png">

<h2>References</h2>
1. Image data loading : https://keras.io/api/data_loading/image/ <br>
2. Save and load keras modules : https://www.tensorflow.org/guide/keras/save_and_serialize <br>
3. Deployment of machine Learning model : https://www.youtube.com/watch?v=0nr6TPKlrN0&t=9s <br>
4. CSS Bootstrap : https://getbootstrap.com/docs/3.4/css/ <br>


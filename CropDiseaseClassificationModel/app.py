import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__ ,template_folder='template')
from keras.models import load_model, model_from_json
# from keras.backend import set_session
# from tensorflow.compat.v1.keras.backend import set_session

from skimage.transform import resize
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
IMG_FOLDER = os.path.join( './uploads')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
print("Loading model")
global json_file
json_file = open("CropDiseaseClassificationModelzipped - Copy\CropDiseaseClassificationModel\global_model_vgg16_architecture.json", 'r')
global loaded_model_json
loaded_model_json = json_file.read()
json_file.close()
global loaded_model
loaded_model = model_from_json(loaded_model_json)
#global sess
#sess = tf.Session()
#set_session(sess)
# load weights into new model
# Write the file name of the weights

loaded_model.load_weights("CropDiseaseClassificationModelzipped - Copy\CropDiseaseClassificationModel\global_model_vgg16_weights.h5")

global model
#model = load_model('model.h5')
model=loaded_model
#global graph
#graph = tf.get_default_graph()
print("Model Loaded")
@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(r'CropDiseaseClassificationModelzipped - Copy\CropDiseaseClassificationModel\uploads', filename))
        return redirect(url_for('prediction', filename=filename))
    return render_template('indexD.html')
    
    #Call Prdiction 
@app.route('/prediction/<filename>')
def prediction(filename):
    import cv2

    #Step 1
    #my_image = plt.imread(os.path.join('uploads', filename))
    my_image = cv2.imread(os.path.join(r'CropDiseaseClassificationModelzipped - Copy\CropDiseaseClassificationModel\uploads', filename), cv2.COLOR_BGR2RGB)
    #my_image = cv2.cvtColor(my_imageo,cv2.COLOR_BGR2RGB)
    #Step 2
    # my_image_re = resize(my_image, (32,32,3))
    #my_image_re = resize(my_image, (60000,784))
    my_image_re = cv2.resize(my_image, (32,32))
    my_image_re = np.expand_dims(my_image_re,axis=0)
    # Write the index of the test sample to test
    #prediction = model.predict(np.array( [my_image_re,] ))[0,:]
    prediction = model.predict(my_image_re)
    print ("Shape of prediction", len(prediction))
    print(type(prediction))
    # print('Prediction\n',prediction[9])
    thresholded = (prediction>0.5)*1
    value = np.argmax(prediction,axis=-1)
    print('\nThresholded output\n',(prediction>0.5)*1)
    # act = os.path.join('uploads', 'Screenshot_9.png')
    # print(act)
    if (value==0):
        print("Apple_Scab")
        value = 'Apple_Scab'
    elif (value==1):
        print("Apple_Black_Rot")
        value = 'Apple_Black_Rot'
    elif (value==2):
        print("Apple_Cedar")
        value = 'Apple_Cedar'
    elif (value==3):
        print("Apple_Healthy")
        value = 'Apple_Healthy'
    elif (value==4):
        print("Blueberry_Healthy")
        value = 'Blueberry_Healthy'
    elif (value==5):
        print("Cherry_Powdery_Mildew")
        value = 'Cherry_Powdery_Mildew'
    elif (value==6):
        print("Cherry_Healthy")
        value = 'Cherry_Healthy'
    elif (value==7):
        print("Corn_gray_leaf_spot")
        value = 'Corn_gray_leaf_spot'
    elif (value==8):
        print("Corn_Common_Rust")
        value = 'Corn_Common_Rust'
    elif (value==9):
        print("Corn_Northern_Leaf_Blight")
        value = 'Corn_Northern_Leaf_Blight'
    elif (value==10):
        print("Corn_Healthy")
        value = 'Corn_Healthy'
    elif (value==11):
        print("Grape_Black_Rot")
        value = 'Grape_Black_Rot'
    elif (value==12):
        print("Grape_Black_Measles")
        value = 'Grape_Black_Measles'
    elif (value==13):
        print("Grape_Leaf_Blight")
        value = 'Grape_Leaf_Blight'
    elif (value==14):
        print("Grape_Healthy")
        value = 'Grape_Healthy'
    elif (value==15):
        print("Orange_Citrus_Greening")
        value = 'Orange_Citrus_Greening'
    elif (value==16):
        print("Peach_Bacterial_Spot")
        value = 'Peach_Bacterial_Spot'
    elif (value==17):
        print("Peach_Healthy")
        value = 'Peach_Healthy'
    elif (value==18):
        print("Pepper_Bell_Bacterial_Spot")
        value = 'Pepper_Bell_Bacterial_Spot'
    elif (value==19):
        print("Pepper_Bell_Healthy")
        value = 'Pepper_Bell_Healthy'
    elif (value==20):
        print("Potato_Early_blight")
        value = 'Potato_Early_Blight'
    elif (value==21):
        print("Potato_Late_blight")
        value = 'Potato_Late_Blight'
    elif (value==22):
        print("Potato_Healthy")
        value = 'Potato_Healthy'
    elif (value==23):
        print("Rasberry_Healthy")
        value = 'Rasberry_Healthy'
    elif (value==24):
        print("Soyabean_Healthy")
        value = 'Soyabean_Healthy'
    elif (value==25):
        print("Squash_Powdery_mildew")
        value = 'Squash_Powdery_mildew'
    elif (value==26):
        print("Strawberry_Leaf_Scorch")
        value = 'Strawberry_Leaf_Scorch'
    elif (value==27):
        print("Strawberry_Healthy")
        value = 'Strawberry_Healthy'
    elif (value==28):
        print("Tomato_Bacterial_Spot")
        value = 'Tomato_Bacterial_Spot'
    elif (value==29):
        print("Tomato_Early_Blight")
        value = 'Tomato_Early_Blight'
    elif (value==30):
        print("Tomato_Late_Blight")
        value = 'Tomato_Late_Blight'
    elif (value==31):
        print("Tomato_Leaf_Mould")
        value = 'Tomato_Leaf_Mould'
    elif (value==32):
        print("Tomato_Septoria_Leaf_Spot")
        value = 'Tomato_Septoria_Leaf_Spot'
    elif (value==33):
        print("Tomato_Two_Spotted_Spider_Mites")
        value = 'Tomato_Two_Spotted_Spider_Mites'
    elif (value==34):
        print("Tomato_Target_Spot")
        value = 'Tomato_Target_Spot'
    elif (value==35):
        print("Tomato_Yellow_Leaf_Curl_Virus")
        value = 'Tomato_Yellow_Leaf_Curl_Virus'
    elif (value==36):
        print("Tomato_Mosaic_Virus")
        value = 'Tomato_Mosaic_Virus'
    elif (value==37):
        print("Tomato_Healthy")
        value = 'Tomato_Healthy'
    
    
    ROC = os.path.join(app.config['UPLOAD_FOLDER'])    
    
    #Final Step
    # number_to_class = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # index = np.argsort(prediction, axis=-1)
    # print ("Shape of Index", len(index))
    # predictions = {
    #     "class1":number_to_class[index[9]],
    #     "class2":number_to_class[index[8]],
    #     "class3":number_to_class[index[7]],
    #     "prob1":prediction[index[9]],
    #     "prob2":prediction[index[8]],
    #     "prob3":prediction[index[7]],
    #    }
    # pred_class = decode_predictions(prediction, top=1)   # ImageNet Decode
    # result = str(pred_class[0][0][1]) 
    print('\nPredicted Disease:\n',np.where(thresholded == 1))
    return render_template('pass.html', filename=filename, predictions=value, thresholded = thresholded)
 
    
app.run(host='0.0.0.0', port=80)
import socketio
import eventlet
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

# create an object of socket libray to listen to a server
# made to establish a bidirectional communication with the
# simulator and the server
# middle ware to create traffic from the app
sio = socketio.Server()
# an object og flask .
app = Flask(__name__)# '__main__'
# speed limit
speed_limit = 10
#image preprocessing
# a function to pre process all the images of the data set
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3,3), 0 )# arg = img , kernal size and deviation
    img = cv2.resize(img , (200,66))
    img = img/255 # normalisation , explained in lane detection
    return img

# when connection is made we want an eventhandler
# to handle the eventlet
@sio.on('connect') # generally 3 names are reserved : message,disconnect,connect
def connect(sid, environ):
    print('Connected')
    send_control(0,0)


# specific event handler : telemetry
@sio.on('telemetry')
def telemetry(sio,data):
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))
    throttle = 1.0 - speed/speed_limit
    print('{} {} {}'.format(steering_angle, throttle , speed))
    send_control(steering_angle, throttle)

# controls :
def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })
# @app.route('/home')
# def greeting():
#     return 'welcome'

if __name__ == '__main__':
    model = load_model('model2.h5')
    app = socketio.Middleware(sio,app)
    eventlet.wsgi.server(eventlet.listen(('',4567)),app)

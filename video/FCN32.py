from tensorflow import keras
from keras.applications import vgg16
from keras.models import Model
from keras.layers import Conv2D,Conv2DTranspose,Input,Dropout,Reshape,Activation

def FCN32(nClasses,input_height,input_width):
    """
    Loads the pretrained version of VGG with the last layer cut off
    :return: pre-trained headless VGG16 Keras Model
    """
    img_input=Input(shape=(input_height,input_width,3))
    model=vgg16.VGG16(
        include_top=False,
        weights='imagenet',
        input_tensor=img_input
    )
    x=Conv2D(
        filters=4096,
        kernel_size=(7,7),
        padding='same',
        activation='relu',
        name='fc6'
    )(model.output)
    x=Dropout(rate=0.5)(x)
    x=Conv2D(
        filters=4096,
        kernel_size=(1,1),
        padding='same',
        activation='relu',
        name='fc7'
    )(x)
    x=Dropout(rate=0.5)(x)
    x=Conv2D(
        filters=nClasses,
        kernel_size=(1,1),
        padding='same',
        activation='relu',
        name='score_fr'
    )(x)
    x=Conv2DTranspose(
        filters=nClasses,
        kernel_size=(32,32),
        strides=(32,32),
        padding='valid'
    )(x)
    x=Reshape((-1,nClasses))(x)
    x=Activation('softmax')(x)
    fcn32=Model(inputs=img_input,outputs=x)
    return fcn32

m=FCN32(15,320,320)
m.summary()
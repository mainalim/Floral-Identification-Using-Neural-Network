import os
import sys
import random
import numpy as np
import tensorflow as tf

from PIL import Image
from sklearn import preprocessing
def load_data(data_directory):
    """Loads data from the specified directory
	Keyword Arguments:
	data_directory -- the directory containing train and test directory
    """
    directories = [directory for directory in os.listdir(data_directory)
	                  if os.path.isdir(os.path.join(data_directory,
                                                 directory))]
    labels = []
    images = []
    for directory in directories:
        label_directory = os.path.join(data_directory, directory)
        #print label_directory
        file_names = [os.path.join(label_directory, a_file)
                      for a_file in os.listdir(label_directory)
                      if a_file.endswith(".jpg")]
        for a_file in file_names:
            images.append(a_file)
            labels.append(directory)
    return(images, labels)

ROOT_PATH = "." #Denotes the current working directory
TRAIN_DATA_DIRECTORY = os.path.join(ROOT_PATH, "leafs_photos/training")
TEST_DATA_DIRECTORY = os.path.join(ROOT_PATH, "leafs_photos/testing")

IMAGES, LABELS = load_data(TRAIN_DATA_DIRECTORY)
#print IMAGES[:5], LABELS[:5]
#print IMAGES[0].shape
#sys.exit()
LABEL_ENCODER = preprocessing.LabelEncoder()
LABEL_ENCODER.fit(np.unique(LABELS))
LABELS = LABEL_ENCODER.transform(LABELS)
#print LABELS
#le.fit(unique)
#IMAGES28_INITIAL = [transform.resize(image, 28, 28) for image in IMAGES]
IMAGES28_INITIAL = []
for image in IMAGES:
    new_image = Image.open(image)
    new_image = new_image.convert('L')
    new_image = new_image.resize((28, 28), resample=0)
    IMAGES28_INITIAL.append(new_image)
#print IMAGES28_INITIAL[5].size
#sys.exit()
#IMAGES28_INITIAL = np.array(IMAGES28_INITIAL)
#print IMAGES28_INITIAL # each item in the list is a image object.
#sys.exit()
IMAGES28 = []
for image in IMAGES28_INITIAL:
    temp_image = np.array(image)
    IMAGES28.append(temp_image)
X = tf.placeholder(dtype=tf.float32, shape=[None, 28, 28])
Y = tf.placeholder(dtype=tf.int32, shape=[None])

IMAGES_FLAT = tf.contrib.layers.flatten(X)

# Fully conncted layer
LOGITS = tf.contrib.layers.fully_connected(IMAGES_FLAT, 62, tf.nn.relu)

# Defining a loss function
LOSS = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
			 labels=Y, logits=LOGITS))
# Define the optimizer
TRAIN_OP = tf.train.AdamOptimizer(learning_rate=0.001).minimize(LOSS)
# Conver logits to logic indexes
CORRECT_PREDICTION = tf.argmax(LOGITS, 1)

ACCURACY = tf.reduce_mean(tf.cast(CORRECT_PREDICTION, tf.float32))

tf.set_random_seed(1234)

SESS = tf.Session()

SESS.run(tf.global_variables_initializer())

for i in range(201):
    print('EPOCH', i)
    _, ACCURACY_VALUE = SESS.run([TRAIN_OP, ACCURACY], feed_dict={
				    X: IMAGES28, Y: LABELS})
    if i % 10 == 0:
        print("Loss: ", LOSS)
    print "DONE WITH EPOCH"
SAMPLE_INDEXES = random.sample(range(len(IMAGES28)), 10)
SAMPLE_IMAGES = [IMAGES28[i] for i in SAMPLE_INDEXES]
SAMPLE_LABELS = [LABELS[i] for i in SAMPLE_INDEXES]

#Running the CORRECT_PREDICTION operation

PREDICTED = SESS.run([CORRECT_PREDICTION], feed_dict={X: SAMPLE_IMAGES})[0]
print SAMPLE_LABELS
print PREDICTED





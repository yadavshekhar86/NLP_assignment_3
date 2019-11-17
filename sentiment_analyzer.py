# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:14:26 2019

@author: shekhar
"""
import gensim
import tensorflow as tf
import numpy as np
import pandas as pd

my_csv = pd.read_csv('train_test_cleaned.csv')
column1 = my_csv.tweet
my_csv2 = pd.read_csv('sentiment_cleaned.csv')
column2 = my_csv2.sentiment

tweet_train0 = []
tweet_train1 = []
for item in column1:
    tweet_train0.append(item)
data = [x.split() for x in tweet_train0]
for item in column2:
    tweet_train1.append(item)
y_train = np.asarray(tweet_train1) 

def create_tagged_document(list_of_list_of_words):
    for i, list_of_words in enumerate(list_of_list_of_words):
        yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])

train_data = list(create_tagged_document(data))  
model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)
model.build_vocab(train_data)
model.train(train_data, total_examples=model.corpus_count, epochs=model.epochs)
vector = []
for i in range(len(data)):
    vector.append(model.infer_vector(data[i]))

x_train = tf.keras.utils.normalize(vector, axis=1)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])
model.fit(x_train[0:15131], y_train[0:15131], epochs=100)

val_loss, val_acc = model.evaluate(x_train[15131:-1], y_train[15131:-1])
print(val_loss, val_acc)





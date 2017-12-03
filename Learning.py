

import tensorflow as tf  
import tensorflow.examples.tutorials.mnist.input_data as input_data  
  
# download the document to folder(MNIST_data)  
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)  
  
# y_actual = W * x + b  
x = tf.placeholder(tf.float32, [None, 784])                 # waiting input data  
y_actual = tf.placeholder(tf.float32, shape=[None, 10])     # waiting input data  
W = tf.Variable(tf.zeros([784, 10]))                        # give w a variable 
b = tf.Variable(tf.zeros([10]))                             # give b a variable
  
# make model  
y_predict = tf.nn.softmax(tf.matmul(x, W) + b)          # softmax function，gues value of result  
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_actual * tf.log(y_predict), reduction_indices=1))  
train = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)     # traning data  
  
# make testing model 
correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y_actual, 1))  # if the predit value equare actual value, return 1, else return 0  
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))                 # couunter the avarage value and got accuracy
  
# defination initialize 
init = tf.initialize_all_variables()  
  
# running 
with tf.Session() as sess:  
    sess.run(init)  
  
    for i in range(1000):       # training 1000times  
        batch_xs, batch_ys = mnist.train.next_batch(100)        # print it every 100 times  
         
        sess.run(train, feed_dict={x: batch_xs, y_actual: batch_ys})  
  
        if i % 100 == 0:        # test it every 100 times
            print("accuracy:", sess.run(accuracy, feed_dict={x: mnist.test.images, y_actual: mnist.test.labels}))  
            
    saver = tf.train.Saver()   
    #save the model on the path
    path = saver.save(sess, "model_data/model.ckpt")  
    #print("Saved:", path)
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
  
# 建立测试训练模型  
correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y_actual, 1))  # 若预测值与实际值相等则返回boolen值1，不等为0  
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))                 # 将返回的beelen数组转换为float类型，并求均值，即得到准确度  
  
# 初始化所有变量  
init = tf.initialize_all_variables()  
  
# 在一切操作之后，都用sess来run它们  
with tf.Session() as sess:  
    sess.run(init)  
  
    for i in range(5000):       # 训练阶段，迭代5000次  
        batch_xs, batch_ys = mnist.train.next_batch(100)        # 按批次训练，每批100行数据  
        # 执行训练（此处为占位符x, y_actual载入数据，然后使用配置好的train来训练）  
        sess.run(train, feed_dict={x: batch_xs, y_actual: batch_ys})  
  
        if i % 100 == 0:        # 每训练100次，测试一次  
            print("accuracy:", sess.run(accuracy, feed_dict={x: mnist.test.images, y_actual: mnist.test.labels}))  
            
    saver = tf.train.Saver()   
  
    path = saver.save(sess, "model_data/model.ckpt")  
    print("Saved:", path)
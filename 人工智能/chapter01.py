import tensorflow as tf
x1 = tf.placeholder(tf.int32,shape=[1],name='x1')
x2 = tf.constant(2,name='x2')
result = x1+x2
with tf.Session() as sess:
    print(sess.run(result,{x1:[3]}))
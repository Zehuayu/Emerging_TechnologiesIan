# Emerging-Technologies-Project-Year4
          
Student: Zehua Yu  Student number:G00307279
             Teacher: Ian
          
Project: this project is that create a web application in Python to recognise digits in images. Users are  able to visit the web application through their browser, submit an image containing a single digit, and the web application will respond with the digit contained in the image. 
 
 
 ## what is tensorflow 
  
  [tensorflow](https://www.tensorflow.org/?hl=zh-cn)is an open-source software library for dataflow programming across a range of tasks. It is a symbolic math library, and also used for machine learning applications such as neural networks.It is used for both research and production at Google,min 0:15/2:17 [4]:p.2 [3]:0:26/2:17 often replacing its closed-source predecessor, DistBelief.
  TensorFlow was developed by the Google Brain team for internal Google use. It was released under the Apache 2.0 open source license on November 9, 2015
  
  ## The resource 
  
  [Tensorflow-mnist example](https://github.com/sugyan/tensorflow-mnist)
  
  [Tensorflow start](https://www.tensorflow.org/)
  
  [Identify the image](http://blog.csdn.net/wlmnzf/article/details/51040158)
  
  [Flask](http://flask.pocoo.org/)
  
  ## using process
  
  1. setting environment
        
        install python
        pip3 install tensorflow (if using the pip, the tensorflow could be intalled in python2.7 library)
        pip3 install opencv-python(using cv2 scan the number photo) 
        pip3 install numpy
  
 
  2.open website on the browser
       
        git clone SSH or Download the ZIP

        FLASK_APP=webapp.py flask run
  
  
  ## running result
  
  this project owns three python file, learning.py is that machine learn how to discern number from image
  
  type python3 Learning.py   running
  
  
  this is result:
  ![image](https://github.com/Zehuayu/Emerging_TechnologiesIan/blob/master/photo/learning_result.jpg)
  
  Precision is 92% and save model into model_data folder
  
  next step is that running checking.py, which scan the number photo from folder and distinguish the number is
  . i had upload the 8 photo
  
  the photo is 
  
  ![image](https://github.com/Zehuayu/Emerging_TechnologiesIan/blob/master/photo/dog8.jpg)
  
  the result:
  
  ![image](https://github.com/Zehuayu/Emerging_TechnologiesIan/blob/master/photo/1Qai5MFRThuOSjPBdLWNuQ_thumb_1858.jpg)
  
  The website page
  ![image](https://github.com/Zehuayu/Emerging_TechnologiesIan/blob/master/photo/webpage.jpg)
  
  user can upload picture to upload folder, and checking.py can scan the photo and give response to user
  
  
  
  ## Problem Slove
  
  #### 1: how does picture be upload by AJAX
  
  [W3C school tutorial](http://www.w3school.com.cn/jquery/jquery_ajax_get_post.asp) and class example
  
  post/get function 
  
  code{
  
  $("button").click(function(){
  $.post("demo_test_post.asp",
  {
    name:"Donald Duck",
    city:"Duckburg"
  },
  function(data,status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
  }
  
  
  
  #### 2:studying machine learning 
  
  unsderstanding the structure of learning and important program
  
    
    
     input layer   hidden layer    output layer
               
      input ----     OOOOOOO  -------output
      
      

   tf.variable()          make one variable
   tf.constart()          make one constant
   
   init  = tf.initializ_all_variable()     Initialize all variables
   
   input = tf.placeholder(tf.float32)      waiting the value input
   
   sess = tf.Session()          running function
  
  
  
  #### How to identify the digital from folder
  
  [Tensorflow Mnist example](http://hpzhao.com/2016/08/09/TensorFlow%E5%AE%9E%E6%88%98%EF%BC%9A%E6%89%8B%E5%86%99%E6%95%B0%E5%AD%97%E8%AF%86%E5%88%AB/)
  
  
  
  #### How to scan the picture uploaded
  
  OpenCV function
  
  import cv2
  to scan the picture and change size, then translate this picture.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
=======
Dataset
=======

Dataset is a collection of data that is used to train a machine learning model. The dataset is usually split into two parts:  
training and testing. The training dataset is used to train the model, while the testing dataset is used to evaluate  
the model's performance.

    Origin of word "dataset": Latin data (things given) + set (group of things).

**ImageNet** is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories. 
The images were collected from the web and labeled by human labelers using Amazon’s Mechanical Turk crowd-sourcing tool. 

Starting in 2010, as part of the Pascal Visual Object Challenge, an annual competition called the ImageNet Large-Scale 
Visual Recognition Challenge (ILSVRC) has been held. ILSVRC uses a subset of ImageNet with roughly 1000 images in each of 1000 categories. 
In all, there are roughly 1.2 million training images, 50,000 validation images, and 150,000 testing images. 

ImageNet consists of variable-resolution images. Therefore, the images have been down-sampled to a fixed resolution of 256 x 256. 
Given a rectangular image, the image is rescaled and cropped out the central 256 x 256 patch from the resulting image.
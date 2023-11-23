==================
Image Segmentation
==================
involves converting an image into a collection of regions of pixels that are represented by a mask or a labeled image.  
By dividing an image into segments, you can process only the important segments of the image instead of processing the entire image.

* Use cases:  
  
  - Medical image analysis (identifying and segmenting tumors).
  - Robotics and autonomous vehicles (environment perception and scene understanding).

* Algorithms:  
  
  - U-Net, FCN (Fully Convolutional Network), and Mask R-CNN are common architectures for image segmentation.

.. image:: /files/images/image_segmentation.png
   :alt: Image Segmentation

Semantic Segmentation
=====================
is a computer vision task in which the goal is to categorize each pixel in an image into a class or object. The goal is to produce 
a dense pixel-wise segmentation map of an image, where each pixel is assigned to a specific class or object.

Instance Segmentation
=====================
is a computer vision task that involves identifying and separating individual objects within an image, including detecting  
the boundaries of each object and assigning a unique label to each object

..  image:: /files/images/obj_detect_segm.png
    :alt: Instance Segmentation
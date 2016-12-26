* How to install OpenCV onto the Pi in less than 3 days

```
% sudo apt-get install libopencv-dev python-opencv
% cp /usr/lib/python2.7/dist-packages/cv* ~/.virtualenvs/cv_py2/lib/python2.7/site-packages/
% workon cv_py2
% python -V
Python 2.7.9
% python
>>> import cv2
>>> cv2.__version__
'2.4.9.1'
>>> quit()
```

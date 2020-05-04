# Map-Segmentation

[![IMAGE ALT TEXT HERE](https://github.com/parshwa1999/Map-Segmentation/blob/master/.images/runningappdemo.png)](https://drive.google.com/file/d/1xERxOag1ENWiEQOLlojLYeoq23FdzGwY/view?usp=sharing)
#### Click on the image to watch the video

## Introduction
Everyday Geospatial Data Storages are deluged with millions of optical overhead
imagery captured from airborne or space-borne platforms. Manual data interpretation on
such a large amount of data becomes an intractable task, hence machine vision techniques
must be employed if we want to make any use of the available data. In this project, we
have made an application which would deal with semantic segmentation of
high-resolution (aerial) images where a semantic class label is assigned to each pixel via
supervised classification. Deep learning techniques have shown impressive performance,
particularly for image processing. However, a major drawback of using deep learning
techniques is that they are extremely data-hungry and using them leads us in exacerbating
the limitations of supervised learning, to get enough annotated training data. But on the
bright side, these techniques are immune to noise so instead of taking and annotating
large datasets we can use publicly available datasets. Such publicly available datasets
might contain errors but in return, a very high amount of data is available to us on which
we can train our model. As deep learning models would require high computational
power and in order to maintain high scalability we have tried to exploit the benefits of
Cloud Computing and RESTful services (Representational state transfer). We have
successfully built a REST API and deployed it on the institute's server. Our application
segments each map image into various segments through which we can perform time
series analysis on images and track development in various parts of our country.
Moreover, our time series analysis would help us in tracking various environmental
changes such as deforestation, afforestation, urbanization, etc and infrastructural changes
such as Rural development. Also, we would provide additional support files to load all
the detected classes as the layers in QGIS and improve segmentation parts through
LabelMe.

## HOW TO USE

#### Install and setup python 3.6
  Run this piece of code only if you have any other version of python installed
  One can check his/her python version by typing
  ```sh
  python3 --version
  ``` 
  on your terminal and if you get 
  ```
  Python 3.6.0
  ``` 
  as your response you have python 3.6 installed as default.
  or else install python 3.6 as follows
  ```sh
  sudo apt install build-essential checkinstall
  sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
  wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
  tar xvf Python-3.6.0.tar.xz
  cd Python-3.6.0/
  ./configure
  sudo make altinstall
  ```
 
#### Install pip and python virtual environment

  ```sh
  sudo apt install python3-pip
  sudo apt install python3-venv
  ```

#### Create virtual enviorment naming Map-Seg
  ```sh
  python3.6 -m venv Map-Seg
  cd Map-Seg
  source bin/activate
  ```

#### Clone the repository
  ```sh
  git clone https://github.com/parshwa1999/Map-Segmentation.git
  ```
  browse to directory by typing
  ```sh
  cd Map-Segmentation
  ```

#### Install all requirements from requirements.txt

  ```sh
  pip install -r requirements.txt
  pip freeze > requirements.txt
  ```

#### Migrate Database

  ```sh
  cd Achilles
  python3 manage.py migrate
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
#### Run Django Server
  ```sh
  python3 manage.py runserver
  ```
let the entire server run.

To visit application page [click here](http://127.0.0.1:8000/label/) and to visit admin page [click here](http://127.0.0.1:8000/admin/login/?next=/admin/)

Username: root

Password: 11to1or11

For further details one can refer my Report and Presentation

## Results

##### Roads
![Image Not Found](https://github.com/parshwa1999/Map-Segmentation/blob/master/.images/Roads.png)

##### Buildings
![Image Not Found](https://github.com/parshwa1999/Map-Segmentation/blob/master/.images/Buildings.png)

##### Cars
![Image Not Found](https://github.com/parshwa1999/Map-Segmentation/blob/master/.images/Cars.png)

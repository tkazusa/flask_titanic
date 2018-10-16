Flask practice with kaggle titanic tutorial
===========================================
[![CircleCI](https://circleci.com/gh/tkazusa/flask_titanic/tree/master.svg?style=svg)](https://circleci.com/gh/tkazusa/flask_titanic/tree/master)

Screenshots
-----------
You can add a passenger information on a imput form.

![input_form](https://github.com/tkazusa/flask_titanic/blob/images/flask_titanic_demo1.png)

Then, a machine learning model return a prediction whether he/she would servive or not the tragedy. 

![prediction](https://github.com/tkazusa/flask_titanic/blob/images/flask_titanic_demo2.png)

Commands
--------
```
make [command]
```


Example
-------
Build docker images for frontend and backend, then run both containers.

```
make install
make build
make run
```
Access to the web application at localhost:8080 .

Clean up the web apps.

```
make clean
```



Install app
-----------
Install dependences.
```
make install
```



Build Docker images
-------------------
Build Docker images for both frontend and backend from Dockerfiles.
```
make build
```



Run on docker
-------------
Generate frontend and backend docker containers from images, then start them.
```
make run
```



Clean containers and images up on docker
-------------------------------------
Clean containers and images up on docker. 
```
make clean
```



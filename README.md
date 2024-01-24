# Task Flask CRUD
A repository to save a project developed in python, used to learn the basic principles of API requests using this language

# Instructions
## Run code
To run the code, you must install the following libraries:
```
sudo apt install python3 python3-pip ipython3
```
After this, you need to install dependencies on requirements.txt using the following command:
```
pip3 install -r requirements.txt --upgrade
```
Now, run the app.py file using the command bellow:
```
python3 app.py
```
With this, your application is running correctly

## Run tests
To run tests you need to run your application first following the [Run code](#run-code) section
After this, you can run tests using the command bellow:
```
python3 -m pytest integration-tests.py -v
```
or use the following command if your `pytest` is globally installed 
```
pytest integration-tests.py -v
```
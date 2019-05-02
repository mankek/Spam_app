This is a small flask application with a machine learning model embedded within; made for learning purpose.

The model is a made using scikit-learn and is composed of a pipeline that includes standardization and a logistic regression model which undergoes 
5-fold cross-validation.

The data used for training was the SPAM E-mail Database data from the UCI Machine Learning repository.

The purpose of this application is to take the content of an email and return the likelihood that it is or is not spam.

The model itself was created and trained within the classifier_etc.py script, saved as a pickle object and loaded into the application. Since the 
original data is composed of various statistics about input text, the application has several functions dedicated to gathering these statistics 
which are then fed to the model.

**Running the application**

Navigate to the Classifier_app folder and run the following:

```
py -3 app.py
```

or

```
FLASK_APP=app.py
flask run
```
   

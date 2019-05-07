This is a small flask application with a machine learning model embedded within; made for learning purpose.

The model used is a an SGD classifier model implemented through scikit-learn. All data is standardized using an
StandardScaler object. The model is set up for online learning, with user input being stored in a sqlite database.

Note: The May 2, 2019 commit uses a StandardScaler + logistic regression pipeline incapable of online learning and no db.

The data used for training was the SPAM E-mail Database data from the UCI Machine Learning repository.

The purpose of this application is to take the text content of an email and return the likelihood that it is or is not spam.

The model itself was created and trained within the classifier_etc.py script, saved as a pickle object and loaded into the application. Since the 
original data is composed of various statistics about input text, the application has several functions dedicated to gathering these statistics 
which are then fed to the model.

The database that stores user input was initialized in the db_create.py script.

[The application is hosted on pythonanywhere here](http://kmanke.pythonanywhere.com/)

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
   

#!/usr/bin/python
import pickle
import os
import numpy
import sqlite3

cur_dir = os.path.dirname(__file__)
scaler = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'scaler.pkl'), 'rb'))


def update_model(db_path, model, batch_size=1000):

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''SELECT * FROM spam_db''')

    results = c.fetchmany(batch_size)

    while results:
        data = numpy.array(results)
        X = data[:, 0:57]
        y = data[:, -1].astype(int)
        X_train = scaler.transform(X)
        model.partial_fit(X_train, y)
        results = c.fetchmany(batch_size)

    conn.close()
    return model


clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))

db = os.path.join(cur_dir, 'spam.sqlite')

clf = update_model(db_path=db, model=clf)

pickle.dump(clf, open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'wb'), protocol=4)

print("Model has been updated.")




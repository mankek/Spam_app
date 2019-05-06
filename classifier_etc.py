#!/usr/bin/python
import numpy
import os
import pickle
import pandas
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold

spam_data = pandas.read_csv(r"C:\Users\krmanke\PycharmProjects\NLP_app\spambase.data")
labels = ["word_freq_make", "word_freq_address", "word_freq_all", "word_freq_3d", "word_freq_our", "word_freq_over",
          "word_freq_remove", "word_freq_internet", "word_freq_order", "word_freq_mail", "word_freq_receive",
          "word_freq_will", "word_freq_people", "word_freq_report", "word_freq_addresses", "word_freq_free",
          "word_freq_business", "word_freq_email", "word_freq_you", "word_freq_credit", "word_freq_your",
          "word_freq_font", "word_freq_000", "word_freq_money", "word_freq_hp", "word_freq_hpl", "word_freq_george",
          "word_freq_650", "word_freq_lab", "word_freq_labs", "word_freq_telnet", "word_freq_857", "word_freq_data",
          "word_freq_415", "word_freq_85", "word_freq_technology", "word_freq_1999", "word_freq_parts", "word_freq_pm",
          "word_freq_direct", "word_freq_cs", "word_freq_meeting", "word_freq_original", "word_freq_project",
          "word_freq_re", "word_freq_edu", "word_freq_table", "word_freq_conference", "char_freq_;", "char_freq_(",
          "char_freq_[", "char_freq_!", "char_freq_$", "char_freq_#", "capital_run_length_average",
          "capital_run_length_longest", "capital_run_length_total", "Class Label"]
spam_data.columns = labels
classes = {"spam": 1, "not spam": 0}
# print(spam_data.isnull().values.any())
# print(spam_data.head(5))
X = spam_data.iloc[:, :-1].values
y = spam_data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y, random_state=2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = SGDClassifier(random_state=1, loss="log", tol=0, max_iter=60)
# scores = cross_val_score(estimator=clf, X=X_train, y=y_train, cv=40, n_jobs=1)
# print(numpy.mean(scores))

clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
clf.partial_fit(X_test, y_test)


# pipeline = make_pipeline(StandardScaler(), SGDClassifier(random_state=1, loss="log", tol=0, max_iter=60))
# print(pipeline.get_params().keys())
# hyperparameters = {'sgdclassifier__tol': [0, 0.1, 0.2, 0.3, 0.4, 0.5],
#                    'sgdclassifier__max_iter': [10, 20, 30, 40, 50, 60, 70, 80]}
#
# clf = GridSearchCV(pipeline, hyperparameters, cv=10)
# clf.fit(X_train, y_train)
# print(clf.best_score_)
# print(clf.best_params_)


# example_1 = "The Google Foundation. " \
            # "The Google Foundation would like to notify you that you have been chosen by the "  \
            # "board of trustees as one of the final recipients of a cash Grant for your own personal, educational, and " \
            # "business development. The Google Foundation, established in the year 2005, is one of the biggest " \
            # "Foundation, Grants for Global Development in the World. In the year 2005, they started offering collection " \
            # "for the sole aim of human growth, educational and Community development. In conjunction with the UN, and " \
            # "EU, We are giving out a yearly Grant to 10 lucky recipients each year. These specific Grant will be awarded" \
            # " to 20 lucky international recipients worldwide; in different categories for their personal business " \
            # "development. The objective is to make a notable change in the standard of living of people all around the " \
            # "Universe (From America to Europe, Asia to Africa and all around). Kindly note that you will only be chosen " \
            # "to receive the Grant once, which means that subsequent yearly Grant will not get to you. Take time and " \
            # "thought in using the Grant wisely on something that will last you a long time. Based on the random " \
            # "selection exercise of internet websites, you were selected among the lucky recipients to receive the grant " \
            # "award sum as charity Grants from the Google Foundation, EU and the UN in accordance with the enabling act " \
            # "of Parliament. (Note that all beneficiaries email addresses were selected randomly from over 500,000 " \
            # "Internet websites in which you might have purchased something or sign up from). You are required to contact" \
            # " the Google Foundation Executive Secretary below, for qualification documentation and processing of your " \
            # "unclaimed grant. After contacting the secretary, you will be given your unclaimed grant pin number, which " \
            # "you will use in collecting the unclaimed grant. Please endeavor to quote your Qualification numbers " \
            # "(V-9920-1007, K-9770-549) in all discussions. Executive Secretary: Mr. Larry Brilliant Email: " \
            # "larrybrilliant859@gmail.com Please note that the EU, UN, strictly administers these grant. You are by all " \
            # "means hereby advised to keep this whole information confidential until you have been able to collect your " \
            # "unclaimed grant. On behalf of Google Foundation, UN and the EU, accept our warmest congratulations.May God " \
            # "Bless you with this Grant. Mr. Gerrod Rodgers. The Google Foundation."

example_1 = '''Caesar, beware of Brutus. Take heed of Cassius. Come not near Casca. 
Have an eye to Cinna. Trust not Trebonius. Mark well Metellus Cimber. 
Decius Brutus loves thee not. Thou hast wronged Caius Ligarius. 
There is but one mind in all these men, and it is bent against Caesar. 
If thou beest not immortal, look about you. 
Security gives way to conspiracy. The mighty gods defend thee!
Here will I stand till Caesar pass along,
And as a suitor will I give him this.
My heart laments that virtue cannot live
Out of the teeth of emulation.
If thou read this, O Caesar, thou mayst live.
If not, the Fates with traitors do contrive.
'''


def find_words(input_text):
    freqs = []
    important_words = ["make", "address", "all", "3d", "our", "over", "remove", "internet", "order", "mail", "receive",
                       "will", "people", "report", "addresses", "free", "business", "email", "you", "credit", "your",
                       "font", "000", "money", "hp", "hpl", "george", "650", "lab", "labs", "telnet", "857", "data",
                       "415", "85", "technology", "1999", "parts", "pm", "direct", "cs", "meeting", "original",
                       "project", "re", "edu", "table", "conference"]
    non_alphanum = ["#", "@", "-", ".", "$", "*", "(", ")", "+", ";", "~", ":", "'", "/", "%", "_", "?", ",", "=", "&",
                    "!"]

    for s in non_alphanum:
        input_text = input_text.split(s)
        input_text = " ".join(input_text)
    input_text = input_text.lower().split(" ")
    for t in important_words:
        word_count = input_text.count(t)
        freqs.append(round((word_count/len(input_text))*100, 2))
    return freqs


def find_chars(input_text):
    freqs = []
    important_chars = [";", "(", "[", "!", "$", "#"]
    for i in important_chars:
        char_count = input_text.count(i)
        freqs.append(round((char_count/len(input_text))*100, 2))
    return freqs


def find_capitals(input_text):
    capitals = []
    capital_lengths = []
    length = 0
    for i in input_text:
        if not i.islower():
            length += 1
        elif i.islower():
            if length != 0:
                capital_lengths.append(length)
            length = 0
    if length != 0:
        capital_lengths.append(length)
    if not capital_lengths:
        capitals.extend([0, 0, 0])
    else:
        capitals.append(round(sum(capital_lengths)/len(capital_lengths), 2))
        capitals.append(max(capital_lengths))
        capitals.append(len(capital_lengths))
    return capitals


example_1_params = []
example_1_params.extend(find_words(example_1))
example_1_params.extend(find_chars(example_1))
example_1_params.extend(find_capitals(example_1))

print(clf.predict([example_1_params]))
print(clf.predict_proba([example_1_params]))

# scores_2 = cross_val_score(estimator=clf, X=X_test, y=y_test, cv=55, n_jobs=1)
# print(scores_2)
# print(numpy.mean(scores_2))
# clf.fit(X, y)

dest = os.path.join("Spam_classifier", 'pkl_objects')
if not os.path.exists(dest):
    os.makedirs(dest)

pickle.dump(clf, open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol=4)
pickle.dump(scaler, open(os.path.join(dest, 'scaler.pkl'), 'wb'), protocol=4)








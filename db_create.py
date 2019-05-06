#!/usr/bin/python
import sqlite3

example_1 = "The Google Foundation. The Google Foundation would like to notify you that you have been chosen by the " \
            "board of trustees as one of the final recipients of a cash Grant for your own personal, educational, and " \
            "business development. The Google Foundation, established in the year 2005, is one of the biggest " \
            "Foundation, Grants for Global Development in the World. In the year 2005, they started offering collection " \
            "for the sole aim of human growth, educational and Community development. In conjunction with the UN, and " \
            "EU, We are giving out a yearly Grant to 10 lucky recipients each year. These specific Grant will be awarded" \
            " to 20 lucky international recipients worldwide; in different categories for their personal business " \
            "development. The objective is to make a notable change in the standard of living of people all around the " \
            "Universe (From America to Europe, Asia to Africa and all around). Kindly note that you will only be chosen " \
            "to receive the Grant once, which means that subsequent yearly Grant will not get to you. Take time and " \
            "thought in using the Grant wisely on something that will last you a long time. Based on the random " \
            "selection exercise of internet websites, you were selected among the lucky recipients to receive the grant " \
            "award sum as charity Grants from the Google Foundation, EU and the UN in accordance with the enabling act " \
            "of Parliament. (Note that all beneficiaries email addresses were selected randomly from over 500,000 " \
            "Internet websites in which you might have purchased something or sign up from). You are required to contact" \
            " the Google Foundation Executive Secretary below, for qualification documentation and processing of your " \
            "unclaimed grant. After contacting the secretary, you will be given your unclaimed grant pin number, which " \
            "you will use in collecting the unclaimed grant. Please endeavor to quote your Qualification numbers " \
            "(V-9920-1007, K-9770-549) in all discussions. Executive Secretary: Mr. Larry Brilliant Email: " \
            "larrybrilliant859@gmail.com Please note that the EU, UN, strictly administers these grant. You are by all " \
            "means hereby advised to keep this whole information confidential until you have been able to collect your " \
            "unclaimed grant. On behalf of Google Foundation, UN and the EU, accept our warmest congratulations.May God " \
            "Bless you with this Grant. Mr. Gerrod Rodgers. The Google Foundation."


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
    capitals.append(round(sum(capital_lengths)/len(capital_lengths), 2))
    capitals.append(max(capital_lengths))
    capitals.append(len(capital_lengths))
    return capitals


example_1_params = []
example_1_params.extend(find_words(example_1))
example_1_params.extend(find_chars(example_1))
example_1_params.extend(find_capitals(example_1))
example_1_params.append(1)
# print(example_1_params)

conn = sqlite3.connect('Classifier_app\spam.sqlite')
c = conn.cursor()
# c.execute('''SELECT * FROM spam_db''')
# results = c.fetchall()
c.execute('''CREATE TABLE spam_db
            (word_freq_make real, word_freq_address real, word_freq_all real, word_freq_3d real,
            word_freq_our real, word_freq_over real, word_freq_remove real, word_freq_internet real,
            word_freq_order real, word_freq_mail real, word_freq_receive real, word_freq_will real,
            word_freq_people real, word_freq_report real, word_freq_addresses real, word_freq_free real,
            word_freq_business real, word_freq_email real, word_freq_you real, word_freq_credit real,
            word_freq_your real, word_freq_font real, word_freq_000 real, word_freq_money real,
            word_freq_hp real, word_freq_hpl real, word_freq_george real, word_freq_650 real,
            word_freq_lab real, word_freq_labs real, word_freq_telnet real, word_freq_857 real,
            word_freq_data real, word_freq_415 real, word_freq_85 real, word_freq_technology real,
            word_freq_1999 real, word_freq_parts real, word_freq_pm real, word_freq_direct real,
            word_freq_cs real, word_freq_meeting real, word_freq_original real, word_freq_project real,
            word_freq_re real, word_freq_edu real, word_freq_table real, word_freq_conference real,
            `char_freq_;` real, `char_freq_(` real, `char_freq_[` real, `char_freq_!` real,
            char_freq_$ real, `char_freq_#` real, capital_run_length_average real,
            capital_run_length_longest integer, capital_run_length_total integer, label integer)''')


c.execute('''INSERT INTO spam_db VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
          ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          (0.23, 0.0, 1.15, 0.0, 0.23, 0.23, 0.0, 0.46, 0.0, 0.0, 0.46, 1.38, 0.23, 0.0, 0.23, 0.0, 0.46, 0.46, 3.0,
           0.0, 1.15, 0.0, 0.23, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.13, 0.0, 0.0, 0.0, 0.0, 1.53, 27, 364, 1)
          )
conn.commit()
conn.close()
# print(results)

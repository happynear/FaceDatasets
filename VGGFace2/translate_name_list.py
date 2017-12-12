import os
import csv
import unidecode
import string
from googletrans import Translator
translator = Translator()
from wikiapi import WikiApi
wiki = WikiApi()

def is_number(uchar):
    return uchar >= u'0' and uchar<=u'9'

def is_alphabet(uchar):
    return (uchar >= u'a' and uchar<=u'z') or (uchar >= u'A' and uchar<=u'Z')

def check_english(name):
    flag = True
    for uchar in name:
        if (not is_alphabet(uchar)) and (not is_number(uchar)) and (uchar != u'\u0020') and (uchar != u'-') and (uchar != u'.'):
            flag = False
    return flag

def non_english_character_count(name):
    count = 0
    for uchar in name:
        if (not is_alphabet(uchar)) and (not is_number(uchar)) and (uchar != u'\u0020') and (uchar != u'-') and (uchar != u'.'):
            count = count + 1
    return count

def get_full_name_from_wiki(name):
    results = wiki.find(name)
    if len(results) > 0:
        article = wiki.get_article(results[0])
        new_name = article.summary
        new_name = new_name[:new_name.find('(')-1]
        table = str.maketrans({key: None for key in string.punctuation + '\r\n'})
        new_name = new_name.translate(table)
        if len(new_name) > 4 and len(new_name) < 50:
            return new_name
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    file = open('vggface2_identity_trans.csv', 'w', encoding="utf8")
    with open('vggface2_identity.csv', 'r', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in spamreader:
            name = row[1].strip()[1:-1]
            if name == 'am':
                continue
            if not check_english(name):
                # If half of the names are regular English characters, see it as an accent.
                if non_english_character_count(name) < len(name) / 2:
                    name = unidecode.unidecode(name)
                # Or, take it as a foreign language.
                else:
                    name = translator.translate(name.replace('_', ' ')).text.replace(' ', '_')
                row[1] = ' "' + name + '"'
                print(row)
            file.write(','.join(row) + '\n')
            # If the name has only one word, we think this is a nickname,
            # then we will try to find the full name via Wikipedia,
            # and add a new entry into the list with the same Class_ID
            if len(name.split('_')) == 1:
                new_row = row
                new_name = get_full_name_from_wiki(name)
                if new_name is not None:
                    new_row[1] = ' "' + new_name + '"'
                    file.write(','.join(new_row) + '\n')
    file.close()
import os
import csv
import unidecode
from googletrans import Translator
translator = Translator()

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

if __name__ == '__main__':
    file = open('vggface2_identity_trans.csv', 'w', encoding="utf8")
    with open('vggface2_identity.csv', 'r', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for row in spamreader:
            name = row[1].strip()[1:-1]
            if not check_english(name):
                # if half of the names are regular English characters, see it as an accent.
                if non_english_character_count(name) < len(name) / 2:
                    name = unidecode.unidecode(name)
                # or, take it as a foreign language.
                else:
                    name = translator.translate(name.replace('_', ' ')).text.replace(' ', '_')
                row[1] = ' "' + name + '"'
                print(row)
            file.write(','.join(row) + '\n')
    file.close()
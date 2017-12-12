
'''
Here, we assume that word1 and word2 are both in English.
You can use unidecode.unidecode() to remove the accents in European languages,
and use googletrans.Translator.translate() to translate other languages into English.
'''
def match_words(word1, word2):
    if (len(word1) == 1 or len(word2) == 1) or (word1[1] == u'.' or word2[1] == u'.'):
        if word1.lower()[0] == word2.lower()[0]:
            return True
    else:
        if word1.lower() == word2.lower():
            return True
    return False

def count_upper(word):
    return len(list(filter(lambda c: c.isupper(), word)))

def split_name(name):
    word_list = name.split(' ')
    splitted_list = []
    for sub_word in word_list:
        if len(sub_word) > 1 and count_upper(sub_word) == len(sub_word) and len(sub_word) < 4:
            splitted_list.extend(list(sub_word))
        else:
            splitted_list.append(sub_word)
    return splitted_list

'''
TODO: Do we need to match one-word name to multiple-word name?
TODO: What if two people have the same first and last name, but different middle names?
TODO: Search Wiki for real names when processing one-word names. (T-Pain -> Faheem Rashad Najm)
TODO: Search Wiki for full names. (A. A. Gill -> Adrian Anthony Gill)
TODO: Read paper: https://infoscience.epfl.ch/record/161961/files/Lhuillery%20RP2009b.pdf 
'''
def match_names(name1, name2):
    name1 = name1.replace('-', '').replace('_',' ').strip()
    name2 = name2.replace('-', '').replace('_',' ').strip()
    if name1.lower() == name2.lower():
        return True
    name_list1 = split_name(name1)
    name_list2 = split_name(name2)
    if (len(name_list1) == 1 and len(name_list2) > 1) or (len(name_list2) == 1 and len(name_list1) > 1):
        return False
    if len(name_list1) == 1 and len(name_list2) == 1:
        if match_words(name_list1[0], name_list2[0]):
            return True
        else:
            return False
    if (match_words(name_list1[0], name_list2[0]) and match_words(name_list1[-1], name_list2[-1])) \
        or (match_words(name_list1[0], name_list2[-1]) and match_words(name_list1[-1], name_list2[0])):
        return True
    else:
        return False

if __name__ == '__main__':
    print(match_names('Fei-Fei Li', 'Li F.'))
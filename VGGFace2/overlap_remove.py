import csv
from match_names import match_names
from translate_name_list import is_short_name, get_full_name_from_wiki
import crash_on_ipy

def reference_name(name):
    if is_short_name(name):
        full_name = get_full_name_from_wiki(name)
        if full_name is None:
            return name
        else:
            return name + '(' + full_name + ')'
    return name

if __name__ == '__main__':
    all_test_names = []
    '''
    with open('lfw-names.txt', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            all_test_names.append(row[0].strip())
    '''
    with open('face_scrub_name.txt', 'r') as facescrub_file:
        all_test_names.extend(map(lambda x: x.strip(), facescrub_file.readlines()))
    counter = 0
    with open('vggface2_overlap.txt','w') as f:
        with open('vggface2_name_folder_list.csv', 'r', encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            for row in spamreader:
                for test_name in all_test_names:
                    if match_names(row[1], test_name):
                        counter = counter + 1
                        if row[1].lower() == test_name.lower():
                            print(('%d %s %s is the same with %s\n' %(counter, row[0], row[1], test_name)))
                            f.write(row[0] + '\n')
                        else:
                            row[1] = reference_name(row[1])
                            test_name = reference_name(test_name)
                            print(('%d %s %s is similar with %s\n' % (counter, row[0], row[1], test_name)))
                            f.write(('%s %s is similar with %s\n' % (row[0], row[1], test_name)))


import csv

def convert_to_standard_list(input_file, output_file):
    with open(output_file, 'w', encoding="utf8") as output_fid:
        with open(input_file, 'r', encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            for row in spamreader:
                name = row[1].strip().replace('"','').replace('-','_').replace('.','._').replace('__','_')
                output_fid.write(row[0] + ' ' + name + '\n')

if __name__ == '__main__':
    convert_to_standard_list('vggface2_identity_trans.csv', 'vggface2_name_folder_list.csv')
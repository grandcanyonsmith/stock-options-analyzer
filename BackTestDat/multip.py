import csv
heights = []
highest_gain = []
i = 0
ally = []
prices = []
all_gains = []
high_al = []
list_of_options = ['GOOG  191122C01110000','GOOG  191122C01090000','GOOG  191122C01242500']
# list_of_options = ['GOOG  191122C01242500']
# with open('options_goog_23587_20191029.txt') as csv_file:
with open('tesla1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    empty = []
    all_id = []
    certain_option = []
    big = []
    for row in csv_reader:
        # i += 1
        
        call_or_put = row[5]
        if call_or_put == 'C':
            print(call_or_put)
            empty.append(row)
            price = row[8]
            print(price)
            all_id.append(option_id)
    print(all_id)
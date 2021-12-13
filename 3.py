
def prepare_line(line):
    return line.strip()

with open("3_1.txt") as fp:
    value_lines = list(map(prepare_line, fp.readlines()))

counted_ones_dic = {}
for value_line in value_lines:
    for index, pos_val in enumerate(value_line):
        if pos_val == '1':
            if not index in counted_ones_dic:
                counted_ones_dic[index] = 0

            counted_ones_dic[index] = counted_ones_dic[index] +1

gamme_rate = ''
epsilon_rate = ''

for ind in range(len(value_lines[0])):
    if counted_ones_dic[ind] >= (len(value_lines)/2):
        gamme_rate = gamme_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamme_rate = gamme_rate + '0'
        epsilon_rate = epsilon_rate + '1'

print(int(gamme_rate, 2) * int(epsilon_rate, 2))


def filter_list(cur_list, keep_higher, filter_index):
    counted_ones_dic = {}
    for value_line in cur_list:
        for index, pos_val in enumerate(value_line):
            if pos_val == '1':
                if not index in counted_ones_dic:
                    counted_ones_dic[index] = 0

                counted_ones_dic[index] = counted_ones_dic[index] +1

    new_list = []
    if keep_higher:
        for cur_elem in cur_list:
            if (cur_elem[filter_index] == '1' and counted_ones_dic[filter_index] >= (len(cur_list)/2)) or \
                (cur_elem[filter_index] == '0' and counted_ones_dic[filter_index] < (len(cur_list)/2)):
                new_list.append(cur_elem)
    
    else:
        for cur_elem in cur_list:
            if (cur_elem[filter_index] == '0' and counted_ones_dic[filter_index] >= (len(cur_list)/2)) or \
                (cur_elem[filter_index] == '1' and counted_ones_dic[filter_index] < (len(cur_list)/2)):
                new_list.append(cur_elem)
    
    return new_list

dummy_oxy_lists = list(value_lines)
for cur_i in range(len(value_lines[0])):
    dummy_oxy_lists = filter_list(dummy_oxy_lists, True, cur_i)

    print(len(dummy_oxy_lists))
    if len(dummy_oxy_lists) == 1:
        print('fin')
        break
    
dummy_co2_lists = list(value_lines)
for cur_i in range(len(value_lines[0])):
    dummy_co2_lists = filter_list(dummy_co2_lists, False, cur_i)

    print(len(dummy_co2_lists))
    if len(dummy_co2_lists) == 1:
        print('fin')
        break


print(int(dummy_oxy_lists[0], 2) * int(dummy_co2_lists[0], 2))      
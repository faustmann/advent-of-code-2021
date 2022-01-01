from functools import reduce


def convert_hex2bin(hex_msg):
    num_of_bits = len(hex_msg) * 4
    return bin(int(hex_msg, 16))[2:].zfill(num_of_bits)


with open("16_1.txt") as fp:
    hex_msgs = fp.read().splitlines()

bin_msg = convert_hex2bin(hex_msgs[0])

sum_version = 0


def parse_bin_msg(bin_msg):
    global sum_version

    version = int(bin_msg[:3], 2)
    label = int(bin_msg[3:6], 2)

    sum_version = sum_version + version

    if label == 4:
        index = 6
        lit_bin_values = []
        while True:
            next_index = index + 5
            lit_bin_values.append(bin_msg[index + 1 : next_index])

            if bin_msg[index] == "0":
                break
            index = next_index

        lit_value = int("".join(lit_bin_values), 2)
        end_idx = next_index
        return lit_value, end_idx
    else:
        length_type_id = int(bin_msg[6:7], 2)

        lit_values = []

        if length_type_id == 0:
            num_bits_submsg = int(bin_msg[7:22], 2)

            submsg_start_idx = 22
            while True:
                lit_value, submsg_end_idx = parse_bin_msg(bin_msg[submsg_start_idx:])

                lit_values.append(lit_value)
                submsg_start_idx = submsg_start_idx + submsg_end_idx

                if submsg_start_idx - 22 >= num_bits_submsg:
                    break
        else:
            num_submsg = int(bin_msg[7:18], 2)

            submsg_start_idx = 18
            for submsg_idx in range(num_submsg):
                lit_value, submsg_end_idx = parse_bin_msg(bin_msg[submsg_start_idx:])

                lit_values.append(lit_value)
                submsg_start_idx = submsg_start_idx + submsg_end_idx

        op_lit_value = 0
        if label == 0:
            op_lit_value = sum(lit_values)
        elif label == 1:
            op_lit_value = reduce((lambda x, y: x * y), lit_values)
        elif label == 2:
            op_lit_value = min(lit_values)
        elif label == 3:
            op_lit_value = max(lit_values)
        elif label == 5:
            op_lit_value = int(lit_values[0] > lit_values[1])
        elif label == 6:
            op_lit_value = int(lit_values[0] < lit_values[1])
        elif label == 7:
            op_lit_value = int(lit_values[0] == lit_values[1])

        return op_lit_value, submsg_start_idx


print(parse_bin_msg(bin_msg))


print(f"fin {sum_version}")

def prepare_instance_line(line):
    test_signals, info_signals = list(
        map(lambda sig_part: sig_part.strip().split(" "), line.split("|"))
    )
    return (test_signals, info_signals)


with open("8_1.txt") as fp:
    instance_lines = fp.readlines()

    line_seperated_line_signals = list(map(prepare_instance_line, instance_lines))


all_signals = [
    signal for line_signals in line_seperated_line_signals for signal in line_signals[1]
]

easy_signals = [
    signal
    for signal in all_signals
    if len(signal) == 2 or len(signal) == 4 or len(signal) == 3 or len(signal) == 7
]

print(f"#easy signals {len(easy_signals)}")


def mapSeg2Digit(act_seg):
    if act_seg == set(["t", "tl", "tr", "bl", "br", "b"]):
        return 0
    elif act_seg == set(["tr", "br"]):
        return 1
    elif act_seg == set(["t", "tr", "m", "bl", "b"]):
        return 2
    elif act_seg == set(["t", "tr", "m", "br", "b"]):
        return 3
    elif act_seg == set(["tl", "tr", "m", "br"]):
        return 4
    elif act_seg == set(["t", "tl", "m", "br", "b"]):
        return 5
    elif act_seg == set(["t", "tl", "m", "bl", "br", "b"]):
        return 6
    elif act_seg == set(["t", "tr", "br"]):
        return 7
    elif act_seg == set(["t", "tl", "tr", "m", "bl", "br", "b"]):
        return 8
    elif act_seg == set(["t", "tl", "tr", "m", "br", "b"]):
        return 9
    else:
        return None


def find_mapping(test_signals):
    test_signals = list(map(lambda sig: set(sig), test_signals))
    get_sig_with_len = lambda length: [
        sig for sig in test_signals if len(sig) == length
    ]
    get_one_elem = lambda set: next(iter(set))

    one = get_sig_with_len(2)[0]
    four = get_sig_with_len(4)[0]
    seven = get_sig_with_len(3)[0]
    eight = get_sig_with_len(7)[0]

    mapping = {}
    mapping["t"] = get_one_elem(seven - one)

    len_5_sig = get_sig_with_len(5)

    three = get_one_elem(sig for sig in len_5_sig if one.issubset(sig))
    five = get_one_elem(sig for sig in len_5_sig if four.issubset(sig.union(one)))

    mapping["tl"] = get_one_elem(five - three)
    mapping["tr"] = get_one_elem(one - five)
    mapping["br"] = get_one_elem(one - set([mapping["tr"]]))
    mapping["m"] = get_one_elem(four - set([mapping["tl"], mapping["tr"], mapping["br"]]))
    mapping["b"] = get_one_elem(three - set([mapping["t"], mapping["tr"], mapping["m"], mapping["br"]]))
    mapping["bl"] = get_one_elem(eight - five - one)

    return {value: key for (key, value) in mapping.items()}


def list_of_digits_to_int(lst_digits):
    return int("".join(map(str, lst_digits)))


result = sum(
    [
        list_of_digits_to_int(
            [
                mapSeg2Digit({find_mapping(test_sig)[sig_par] for sig_par in signal})
                for signal in info_sig
            ]
        )
        for (test_sig, info_sig) in line_seperated_line_signals
    ]
)

print(f"sum {result}")

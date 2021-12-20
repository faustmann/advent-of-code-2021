from collections import Counter
from collections import defaultdict

with open("14_1.txt") as fp:
    instance_lines = fp.read()

    raw_template, raw_rules = instance_lines.split("\n\n")
    template = raw_template.strip()
    rules = dict(map(lambda line: line.split(" -> "), raw_rules.split("\n")))

# keep the fst version since it is so aesthetically pleasing
# ... but too slow
cur_template = template
for step in range(10):
    print(f"step {step}")
    new_template = cur_template[0]
    for ch1, ch2 in zip(cur_template, cur_template[1:]):
        new_template = new_template + rules.get(ch1 + ch2, "") + ch2
    cur_template = new_template

ch_occurences = Counter(cur_template).values()

print(f"fst result {max(ch_occurences) - min(ch_occurences)}")

raw_pairs = zip(template, template[1:])
pairs_dict = defaultdict(int)
for pair in raw_pairs:
    pairs_dict[pair] = pairs_dict[pair] + 1

for step in range(40):
    print(f"step {step}")
    new_pairs_dict = pairs_dict.copy()
    for pair in pairs_dict:
        if "".join(pair) in rules:
            new_chr = rules["".join(pair)]
            new_pairs_dict[pair] = new_pairs_dict[pair] - pairs_dict[pair]
            new_pairs_dict[(pair[0], new_chr)] = (
                new_pairs_dict.get((pair[0], new_chr), 0) + pairs_dict[pair]
            )
            new_pairs_dict[(new_chr, pair[1])] = (
                new_pairs_dict.get((new_chr, pair[1]), 0) + pairs_dict[pair]
            )
    pairs_dict = new_pairs_dict

ch_occurences = defaultdict(int)
for pair in pairs_dict:
    ch_occurences[pair[0]] = ch_occurences[pair[0]] + pairs_dict[pair]
ch_occurences[template[-1]] = ch_occurences[template[-1]] + 1

ch_occurences_values = ch_occurences.values()

print(f"snd result {max(ch_occurences_values) - min(ch_occurences_values)}")

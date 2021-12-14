from functools import reduce
from statistics import median

with open("10_1.txt") as fp:
    instance_lines = fp.read().splitlines()


def get_closing_of(opening):
    if opening == "(":
        return ")"
    elif opening == "[":
        return "]"
    elif opening == "{":
        return "}"
    elif opening == "<":
        return ">"
    else:
        return None


val_of_illegal_chr = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def find_fst_illegal_elem(instance):
    stack = []
    for chr in instance:
        closing = get_closing_of(chr)
        if closing == None:
            if len(stack) != 0 and stack[-1] == chr:
                stack.pop()
            else:
                return chr
        else:
            stack.append(closing)
    return list(reversed(stack))


syn_err_score = sum(
    map(
        lambda illegal_chr: val_of_illegal_chr[illegal_chr],
        filter(
            lambda elem: not isinstance(elem, list),
            [find_fst_illegal_elem(instance) for instance in instance_lines],
        ),
    )
)

print(f"total syntax error score {syn_err_score}")

val_completion_chr = {
    ")": lambda cur_val: cur_val * 5 + 1,
    "]": lambda cur_val: cur_val * 5 + 2,
    "}": lambda cur_val: cur_val * 5 + 3,
    ">": lambda cur_val: cur_val * 5 + 4,
}

completion_score = median(
    list(
        map(
            lambda completion_chars: reduce(
                lambda cur_val, completion_chr: val_completion_chr[completion_chr](
                    cur_val
                ),
                completion_chars,
                0,
            ),
            filter(
                lambda elem: isinstance(elem, list),
                [find_fst_illegal_elem(instance) for instance in instance_lines],
            ),
        )
    )
)

print(f"total completion score {completion_score}")

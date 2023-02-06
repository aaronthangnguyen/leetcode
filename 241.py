# 241. Different Ways to Add Parentheses
# O(2^n * n) time, O(n) space


from typing import List


def different_ways_to_add_parentheses(exp: str) -> List[int]:
    if exp.isdigit():
        return [int(exp)]

    res = []

    n = len(exp)
    for i in range(n):
        if exp[i] in "-+*":
            left = different_ways_to_add_parentheses(exp[:i])
            right = different_ways_to_add_parentheses(exp[i + 1 :])
            for l in left:
                for r in right:
                    match exp[i]:
                        case "+":
                            res.append(l + r)
                        case "-":
                            res.append(l - r)
                        case "*":
                            res.append(l * r)
    return res


if __name__ == "__main__":
    print(different_ways_to_add_parentheses("2*3-4*5"))

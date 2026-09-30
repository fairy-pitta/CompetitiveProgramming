from itertools import groupby


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

def main():
    S = input()
    S_encoded = runLengthEncode(S)
    print(len(S_encoded)-1)

main()
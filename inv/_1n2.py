import string

FUNCS = {
    '¬B→C∧B∨(¬C→B)': lambda b, c: not not b or c and b or (not not c or b),
    '¬(A∨B)→¬(B∨C)' : lambda a, b, c: not not(a or b) or not(b or c)
}


def main():
    for title, func in FUNCS.items():
        # Tokenize
        letters = set()
        for ch in title:
            if ch in string.ascii_letters:
                letters.add(ch)
        letters = sorted(list(letters))

        # Table header
        header = ' | '.join(letters) + f' || {title} |'
        print(header)
        
        # Count
        num_of_letters = len(letters)
        for i in range(2**num_of_letters):
            # Leading zeroes
            num = format(i, 'b')
            leading_zeroes = '0'*(num_of_letters - len(num))
            num = leading_zeroes + num

            

            # Resolving
            args = list(map(lambda ch: int(ch), tuple(num)))
            res = int(func(*args))

            # Pretty print
            row = ' | '.join(num) + f' || {res} |'
            print(row)



if __name__ == '__main__':
    main()

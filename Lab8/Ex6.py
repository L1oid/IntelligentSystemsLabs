import random


def random_line(file):
    try:
        line = next(file)
        for num, aline in enumerate(file, 2):
            if random.randrange(num):
                continue
            line = aline
        print(line)
    except StopIteration:
        return


random_line(open("lines.txt"))
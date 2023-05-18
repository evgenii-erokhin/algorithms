# id успешной посылки - 87103339

def read_input():
    num_tap = int(input()) * 2
    raund = [input() for _ in range(4)]
    matrix = [item for lst in raund for item in lst]

    return num_tap, matrix


def find_nearest_zero(num_tap, matrix):
    score = 0

    for time in range(10):
        quantity_t = matrix.count(str(time))
        if 0 < quantity_t <= num_tap:
            score += 1
    return score


if __name__ == '__main__':
    num_tap, matrix = read_input()
    print(find_nearest_zero(num_tap, matrix))

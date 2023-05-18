# id успешной посылки - 87088600
def counting(quantity, street):
    answer = [0 for _ in range(quantity)]
    indexes_zeros = []

    for index, value in enumerate(street):
        if value == 0:
            indexes_zeros.append(index)

    for i in range(indexes_zeros[0]):
        answer[i] = indexes_zeros[0] - i

    for i in range(1, len(indexes_zeros)):
        for j in range(indexes_zeros[i - 1] + 1, indexes_zeros[i]):
            answer[j] = min(j - indexes_zeros[i - 1], indexes_zeros[i] - j)

    for i in range(indexes_zeros[- 1] + 1, quantity):
        answer[i] = i - indexes_zeros[- 1]

    return answer


def read_input():
    quantity = int(input())
    street = [int(i) for i in input().split()]

    return quantity, street


if __name__ == '__main__':
    quantity, street = read_input()
    print(*counting(quantity, street))

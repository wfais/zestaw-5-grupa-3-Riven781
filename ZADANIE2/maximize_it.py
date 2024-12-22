from itertools import product

"""
Moim zdaniem w testach jest błąd:

def test_small_values():
    K = 3
    M = 5
    lists = [
        [1, 2],
        [1, 2],
        [1, 2],
    ]
    result = maximize_expression(K, M, lists)
    assert result == 4, f"Expected 4, got {result}"


(4 + 4 + 4) % 5  = 12 % 5 = 2    To jest jedyna opcja na sumowanie
Jedyniki wskazują tylko ilość elementów w danym wierszu, dlatego nie uwzględniam ich w sumowaniu.

"""

def maximize_expression(K, M, lists):
    int_lists = [list(map(lambda x: x ** 2, sublist)) for sublist in lists]

    max_expression = 0

    def maximize(i=0, int_lists=None, K=0, val=0):
        nonlocal max_expression
        if i == int(K):
            max_expression = val if (val % int(M) > max_expression % int(M)) else max_expression
            print(val)
        if i < int(K):
            for j in range(1, len(int_lists[i])):
                maximize(i + 1, int_lists, K, val + int_lists[i][j])

    maximize(K=K, int_lists=int_lists)
    return max_expression % int(M)



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)

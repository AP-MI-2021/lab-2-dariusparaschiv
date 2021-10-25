import math
'''
    def function get_base_2(p:str):
    cuv = ''
    while p != '':
        cuv = cuv + str(int(p % 2))
        p = p[:-1]
    return cuv

'''

def get_n_choose_k(n: int, k: int):
    t = (math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
    return t


def is_palindrome(n):
    t = 0
    aux = n
    while aux != 0:
        t = t * 10 + aux % 10
        aux = aux // 10
    return t == n


def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
    return True


def get_largest_prime_below(n):
    n = n-1
    if n<2:
        return 0
    else:
        while n>1:
            if is_prime(n):
                return n
            else:
                n = n-1
    return 0


def test_get_largest_prime_below():
    assert get_largest_prime_below(2) == 0
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(9) == 7


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(2) is True
    assert is_prime(19) is True


def test_get_n_choose_k():
    assert get_n_choose_k(5, 1) == 5
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(5, 2) == 10


def test_is_palindrome():
    assert is_palindrome(3) is True
    assert is_palindrome(121) is True
    assert is_palindrome(334) is False


def main():
    test_get_n_choose_k()
    test_is_palindrome()
    test_is_prime()
    test_get_largest_prime_below()
    while True:
        print('1.Calculează combinări de `n` luate câte `k`')
        print('2.Verifica daca un nr e palindrom ')
        print('3.Cel mai mare nr prim, mai mic decat n dat')
        print('x. Iesire')
        optiune = input('Alegeti optiunea ')
        if optiune == '1':
            n = int(input('Combinari de '))
            k = int(input('luate cate  '))
            if k <= n:
                print(get_n_choose_k(n, k))
            else:
                print('nu se poate')
        elif optiune == '2':
            n = int(input('Scrieti un nr '))
            print(is_palindrome(n))
        elif optiune == '3':
            n = int(input('Scrieti un nr '))
            t = get_largest_prime_below(n)
            if t == 0:
                print("nu exista")
            else:
                print(t)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


main()

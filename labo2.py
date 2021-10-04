
import math
def get_n_choose_k(n: int, k: int):
    t=(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))
    return t


def is_palindrome(n):
    t=0
    aux=n
    while aux!=0:
        t=t*10+aux % 10
        aux=aux//10
    return t==n


def test_get_n_choose_k():
    assert get_n_choose_k(5,1)==5
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(5, 2) == 10
test_get_n_choose_k()


def test_is_palindrome():
    assert is_palindrome(3)==True
    assert is_palindrome(121) == True
    assert is_palindrome(334) == False
test_is_palindrome()



def main():
    while True:
        print('1.Calculează combinări de `n` luate câte `k`')
        print('2.Verifica daca un nr e palindrom')
        print('x. Iesire')
        optiune=input('Alegeti optiunea ')
        if optiune=='1':
            n=int(input('Combinari de '))
            k=int(input('luate cate  '))
            if k<=n:
                print(get_n_choose_k(n,k))
            else:
                print('nu se poate')
        elif optiune=='2':
            n = int(input('Scrieti un nr'))
            print(is_palindrome(n))
        elif optiune =='x':
            break
        else:
            print('Optiune invalida')

main()

def show_menu():
    print('1. Citire lista')
    print('2. Afisare numere intregi')
    print('3. Afisarea celui mai mare nr divizibil cu un nr citit')
    print('4. Afisare float-uri cu partea fractionara palindrom')
    print('5. Procesare float-uri')
    print('x. Exit')

def read_list():
    floats_as_str = input('Dati o lista de float-uri separate prin spatiu: ')
    floats_as_list_of_str = floats_as_str.split(' ')
    floats = []
    for float_str in floats_as_list_of_str:
        floats.append(float(float_str))

    return floats

def get_integers(lst):
    """
    Determina numerele intregi din lst (de ex. 2 si 8.0)
    :param lst: lista de float-uri
    :return: o lista cu numerele intregi din lst
    """
    result = []
    for num in lst:
        if int(num) == num:
            result.append(num)
    return result
def test_get_integers():
    assert get_integers([1.2, 5.3, 3, 4, 12.0]) == [3, 4, 12.0]
    assert get_integers([]) == []
    assert get_integers([5.3, 5.64]) == []

def show_integers(lst):
    print(f'Numerele intregi din lista: {lst} sunt: {get_integers(lst)}')


def get_max_div(lst, num):
    """
    Determina cel mai mare numar din lst care este divizibil cu num.
    :param lst: lista de float-uri
    :param num: int, numarul cu care se verifica divizibilitatea.
    :return: cel mai mare numar din lst care este divizibil cu num.
    """
    result = None
    for elem in lst:
        if int(elem) == elem and elem % num == 0:
            if result is None:
                result = int(elem)
            else:
                result = max(result, elem)
    return result
def test_get_max_div():
    assert get_max_div([2.4, 6.9], 4) is None
    assert get_max_div([2.4, 6.9, 10], 4) is None
    assert get_max_div([2.4, 6.9, 8], 4) == 8
    assert get_max_div([2.4, 6.9, 8, 4, 12, 13], 4) == 12

def show_max_div(lst):
    num = int(input('Dati numarul pentru care se va testa divizibilitatea: '))
    result = get_max_div(lst, num)
    print(f'Cel mai mare numar din {lst} divizibil cu {num} este: {result}')

def get_with_decimals_palindrome(lst):
    """
    Determina toate numerele cu partea fractionara palindrom.
    :param lst: lista de float-uri
    :return: o lista cu float-uri care au partea zecimala palindrom
    """
    result = []
    for elem in lst:
        str_elem = str(elem)
        if '.' in str_elem:
            decimals = str_elem.split('.')[1]
            if decimals == decimals[::-1]:
                result.append(elem)
    return result
def test_get_with_decimals_palindrome():
    assert get_with_decimals_palindrome([5, 5.25, 5.121, 81.1223221, 7.31]) == [5.121, 81.1223221]
    assert get_with_decimals_palindrome([5.25, 7.31]) == []
    assert get_with_decimals_palindrome([]) == []

def show_with_decimals_palindrome(lst):
    result = get_with_decimals_palindrome(lst)
    print(f'Numerele cu partea zecimala palindrom din lista: {lst} sunt: {result}')


def is_prime(num):
    """
    Determina daca un numar este prim.
    :param num: numarul considerat.
    :return: True daca num este prim si False in caz contrar.
    """
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(19) == True
    assert is_prime(15) == False

def get_processing_result(lst):
    """
    Determina lista obtinuta din lista initiala în care float-urile
    cu partea întreagă a radicalului număr prim sunt puse ca
    string-uri cu caracterele în ordine inversă.
    :param lst: lista de float-uri
    :return: lista rezultat
    """
    result = []
    for elem in lst:
        if elem >= 0:
            int_sqrt = int(elem ** 0.5)
            if is_prime(int_sqrt):
                #daca se cere tuplu
                #result.append((elem, str(elem)[::-1]))
                result.append(str(elem)[::-1])
            else:
                result.append(elem)
        else:
            result.append(elem)
    return result
def test_get_processing_result():
    assert get_processing_result([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
    assert get_processing_result([]) == []
    assert get_processing_result([100.0]) == [100.0]

def show_processing_result(lst):
    result = get_processing_result(lst)
    print(f'Lista {lst} procesata conform enuntului este: {result}')

def main():
    lst = []
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            show_integers(lst)
        elif option == '3':
            show_max_div(lst)
        elif option == '4':
            show_with_decimals_palindrome(lst)
        elif option == '5':
            show_processing_result(lst)
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')

if __name__ == '__main__':
    test_get_integers()
    test_get_max_div()
    test_get_with_decimals_palindrome()
    test_is_prime()
    test_get_processing_result()
    main()

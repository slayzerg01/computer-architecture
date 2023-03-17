def int_to_bin(n, value):                     ## Перевод в двичный код
    binary = ""                               ## запись 2-ного числа в строку
    while n > 0:                              ## n - кол-во разрядов
        binary = str(value % 2) + binary      ## остаток от деления на 2
        value //= 2                           ## целочисленное деление на 2
        n -= 1
    return binary

def input_data(n, file_name):                 ## Входные данные
    f = open(file_name, "r")                  ## Переменная для чтения файла
    truth_values = {}                         ## Истинные значения. Элементы внутри словаря, внутри разные типы данных(уникальные)
    values = f.readline().strip().split(' ')                 ## Метод разделяет значения через пробел
    for value in values:
        truth_values[int(value)] = int_to_bin(n, int(value))
    return truth_values



def combine(implA, implB):
    n = 0                                          ## Кол-во совпадений
    k = -1                                          ## Индекс несовпавшего символа
    combined = True
    for i in range(len(implA)):
        if implA[i] != implB[i]:
            n += 1
            k = i
        if n > 1:
            combined = False
            break
    return combined, k

def pQMC(n, truth_values):
    simple_impls = set()                          ## Множество простых ипликант СИМПЛ ДИМПЛ

    prev_impls = [set() for i in range(n + 1)]    ## Разбиение ипликант 0-го уровня на группы по количеству единиц
    for key in truth_values.keys():
        ones = truth_values[key].count("1")       ## Обращение к значению ключа(двоич. число), выявляет количество единиц
        prev_impls[ones].add(truth_values[key])
        simple_impls.add(truth_values[key])

    for i in range(n):                                  ## По уровням(столбцам| | |)
        next_impls = [set() for i in range(n + 1)]      ## Формирование списка ипликант следующего уровня

        for j in range(n):                              ## Добавление испликант текущего уровня к множеству простых импликант
            for impl in prev_impls[j]:
                simple_impls.add(impl)

        for j in range(n-1):                            ## По строкам рядомстоящие

            for implA in prev_impls[j]:

                for implB in prev_impls[j + 1]:
                    combined, k = combine(implA, implB)
                    if combined:
                        simple_impls.discard(implA)             ## Удаление implA и implB из множества простых импликантов
                        simple_impls.discard(implB)
                        ## Формирование новой импликанты и добавление ее в список импликант следующего уровня
                        implB = implB[:k] + "-" + implB[k+1:]   ##[:k] - срезает список от начала до k, [k+1:] - от k+1 до конца, между ними дефис
                        ones = implB.count("1")
                        next_impls[ones].add(implB)

        ## Переход к следующему уровню
        prev_impls = next_impls
    print(simple_impls)
        # print(next_impls)

def main():
    n = int(input("Введите разрядность входного слова: "))
    truth_values = input_data(n, "input_data.txt")
    print(truth_values)
    pQMC(n, truth_values)

    ##print(combine("0001", "0011")) - склейка

if __name__ == '__main__':      ## Точка входа в программу
    main()

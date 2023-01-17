"""Игра угадай число"""
import numpy as np
def random_predict(number: int = 50) -> int: 
    """ Функция укадывает число методом половинного деления
    Args:
        number (int, optional): загаданное число. Defaults to 50.
    Returns:
        int: число попыток, потребоваашихся для отгадывания
    """    
    
    pred_min = 1
    pred_max =  101
    count = 0
    while True:
        count += 1
        predict = (pred_min + pred_max) // 2 # предполагаемое число
        if predict > number:
            pred_max = predict
        elif predict < number:
            pred_min = predict
        else:
            break
    return count
print(f'Количество попыток: {random_predict()}')

def score_game(predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

print(score_game(random_predict))



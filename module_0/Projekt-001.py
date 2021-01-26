import numpy as np

min_num=int(input("Введите нижние значение диаппазона чисел: "))
max_num=int(input("Введите верхние значение диаппазона чисел: "))
print("Ваш диапазон для загадывания и угадывания чисел находится в интервале:",min_num,'-',max_num)


def comparative_search(num, min_n, max_n):  # функция угадывания загаданного числа num
                                            # путем подбора предполагаемого числа predictable
                                            # с наводящими сравнениями предполагаемого и искомого
    min_n, max_n = min_num, max_num
    interval = [min_n,max_n]
    predictable = (interval[0] + interval[1])//2
    counter = 0
    
    while num != predictable:
        counter +=1
        #print('Попытка №', counter, '. Предполагаемой число - ', predictable)
        if predictable < num:
            #print('Предполагаемое число меньше Искомого')
            interval = [predictable, interval[1]]
            if interval[0]+1 == interval[1]:
                predictable = interval[1]
            else:
                predictable = (predictable + interval[1])//2
        else:
            #print('Предполагаемое число больше Искомого')
            interval = [interval[0], predictable]
            predictable = (interval[0] + predictable)//2
    counter +=1
    #print('Попытка №', counter, '. Предполагаемой число - ', predictable)
    #print ('Предполагаемое число', predictable, 'равно искомому', num)
    #print ('Число попыток угадывания -', counter)
    return counter


def enumeration_sequential (num, min_n, max_n):  #Функция перебора искомого по порядку
    min_n, max_n = min_num, max_num
    for n in range(min_n, max_n+1):
        if n==num: break
    return n


series_quantity = int(input('Введите желаемое количество серий для испытаний: '))
tests_quantity = int(input('Введите желаемое количество испытаний в каждой серии: '))


def score_game(game_core, tests_quant=tests_quantity):     #Функция тестирования испытаний в 1 серии
    print('Запускаем угадывание', tests_quant,'раз, чтобы узнать, как быстро игра угадывает число')
    count_ls = []
    count = 0  # Нужно было только для контрольных распечаток при работе функции
    #np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(min_num,max_num, size=(tests_quant))
    #print(random_array)
    for number in random_array:
        count += 1  # Нужны были только для контрольных распечаток при работе функции
        #print('"ЭКСПЕРИМЕНТ №" - ', count, ' с Искомым', number, '. Попыток -', game_core(number))
        count_ls.append(game_core(number, min_num, max_num))
    score = float(np.mean(count_ls))
    print(f'В серии из {tests_quant} испытаний число угадано в среднем за {score} попыток')
    return(score)


def score_series (score_gm, enumeration_type, series_quant=series_quantity): #ьесьтрование нескольких серий
    count_means=[]
    print('start')
    for i in range(1,series_quant+1):
        print (i, 'серия')
        #score_gm(enumeration_type)
        count_means.append(score_gm(enumeration_type))
    general_mean = float(np.mean(count_means))
    min_mean = min(count_means)
    max_mean = max(count_means)
    print('\nСписок результатов', count_means )
    print(f'Среднее по сериям {general_mean}. Мин среднее {min_mean}. Макс среднее {max_mean}\n\n')
    

#Проба двух вариантов поиска
score_series (score_game, enumeration_sequential)


score_series (score_game, comparative_search)
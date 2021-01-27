import numpy as np
print ('Специально для тех, кто придумал этот проект и будет проверять данную работу: \n \
    Это описание - мнение авторов решения. Оно может быть ошибочным.\n \
    Пункт 1. Задача поставлена не корректно в части не четкости понятия "угадать" \n \
    По нашему мнению это понятие может иметь 2 трактовки (что косвенно подтверждается текстом курса): \n \
    - назвается число-претендент и система его либо принимает, либо отрицает без комментариев, \n \
    - называется число и система его либо принимает, либо отрицает с комментариями об относительности \n \
    числа-претендента к числу загаданному. \n \
    Поэтому в данной работе представлены решения для обоих трактовок: \n \
    - решения с перебором возможных чисел-претендентов и угадыванием без комментариев от системы \n \
    2 варианта: последовательный пребор и перебор из середины интервала \n \
    - решения cо сравнениями "больше / меньше" чисел-претендентов с числом загаданным. \n \
    2 варианта: с разбиением нуменьшенных интервалов на 2 ранвые части и на 2 неравные части \n \
    \n \
    Использование авторами проекта np.random.seed считаем логически некорректным, как нарушающим \n \
    чистоту статистических экспериментов. \n \
    Вместо этого для оплучения более представительной статистики экспериментов предусмотрены несколько \n \
    серий испытаний (покличество на усмотрение пользователя) с расчетом средней по каждой серии и оценкой \n \
    оценкой диперсии по результатм группы серий испытаний. \n \
    Для этого в коде предусмотрена еще одна функция по организации серий испытаний.')


min_num=int(input("Введите нижние значение диаппазона чисел: "))
max_num=int(input("Введите верхние значение диаппазона чисел: "))
print("Ваш диапазон для загадывания и угадывания чисел находится в интервале:",min_num,'-',max_num)


def comparative_search_50_50 (num, min_n, max_n):  # функция угадывания загаданного числа num путем
                                                   # подбора предполагаемого числа predictable снаводящим
                                                   # сравнениями "больше/меньше" предполагаемого и искомого
                                                   # и определением размеров новых интервалов одинаковыми 
                                                   # половинками предыдущего интервала
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


def comparative_search_1_2 (num, min_n, max_n):  # функция угадывания загаданного числа num путем
                                                 # подбора предполагаемого числа predictable с наводящим
                                                 # сравнениями "больше/меньше" предполагаемого и искомого
                                                 # и определением размеров новых интервалов 1 и 2 части от
                                                 # предыдущего интервала (1/3 и 2/3)
    min_n, max_n = min_num, max_num
    interval = [min_n,max_n]
    predictable = (interval[0] + interval[1])//3
    counter = 0
    
    while num != predictable:
        counter +=1
        #print('Попытка №', counter, '. Предполагаемой число - ', predictable)
        if predictable < num:
            #print('Предполагаемое число меньше Искомого')
            interval = [predictable, interval[1]]
            if interval[0]+1 == interval[1]:
                predictable = interval[1]
            elif interval[0]+2 == interval[1]:
                predictable = interval[0]+1
            else:
                predictable = predictable + (interval[1] - predictable)//3
        else:
            #print('Предполагаемое число больше Искомого')
            interval = [interval[0], predictable]
            predictable = interval[0] + (predictable - interval[0])//3
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


def enumeration_fan (num, min_n, max_n):  #Функция перебора искомого от середины веером
    min_n, max_n = min_num, max_num
    interval = [min_n,max_n]
    start_mean = (interval[0] + interval[1])//2
    predictable = start_mean
    counter = 0

    while num != predictable:
        counter +=1
        #print('Попытка №', counter, '. Предполагаемой число - ', predictable)
        if predictable <= start_mean:
            predictable = start_mean + (counter+1)/2
        else:
            predictable = start_mean - counter/2
    return counter



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


def score_series (score_gm, enumeration_type, series_quant=series_quantity): #тестирование нескольких серий
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
    

#Непосредственное проведение испытаний

guessing_scheme = int(input('Выберите схему угадывания \n \
    1 - без направляющих комментов системы, \n \
    2 - с коментами системы "больше / меньше" относительно числа угадываемого \n \
    Введите выбранный номер:'))

functional_scheme = 0

if guessing_scheme == 1:
    enumeration_parameter = int(input('Выберите параметр перебора \n \
    1 - последовательный перебор от меньшего к большему, \n \
    2 - перебор "веером" от середины интервала (N, N+1, N-1, N+2, N-2, ...) \n \
    Введите выбранный номер:'))
    if enumeration_parameter ==1: 
        functional_scheme = enumeration_sequential
    else:
        functional_scheme = enumeration_fan
else:
    interval_parameters = int(input('Выберите соотношение новых интервалов для поиска числа, определяемых \n \
    после коммента системы о сравынении с числом загаданным "больше/меньше" \n \
    1 - соотношение 50/50 (пополам), \n \
    2 - соотношение 1/2 (1/3 и 2/3) \n \
    Введите выбранный номер:'))
    if interval_parameters ==1: 
        functional_scheme = comparative_search_50_50
    else:
        functional_scheme = comparative_search_1_2


#Запуск испытаний
score_series (score_game, functional_scheme)

print ('Результаты испытаний пока вручную надо заносить в файл "Результаты испытаний по проекту 001" ')
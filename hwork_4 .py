#Первая задача
geo_logs = [
    {'visit1' : ['Москва', 'Россия']},
    {'visit2' : ['Дели', 'Индия']},
    {'visit3' : ['Владимир', 'Россия']},
    {'visit4' : ['Лиссабон', 'Португалия']},
    {'visit5' : ['Париж', 'Франция']},
    {'visit6' : ['Лиссабон', 'Португалия']},
    {'visit7' : ['Тула', 'Россия']},
    {'visit8' : ['Тула', 'Россия']},
    {'visit9' : ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
print(list(filter(lambda item: tuple(item.items())[0][1][1] == 'Россия' , geo_logs)))
print()
#Вторая задача
from itertools import chain
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]} 
result = list(dict.fromkeys(chain(*ids.values())).keys())
print(result)
print()

#Третья задача
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
storage = {}

for query in queries:
    words = query.split()
    if len(words) in storage.keys():
        storage[len(words)] += 1
    else:
        storage.update({
            len(words): 1
        })

for key, value in storage.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слов: {percentage}% ({value} запр.)')

print()

# Четвертая задача
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
print (max(stats, key = lambda k: stats[k]))
print()
# Из списка в словарь
from functools import reduce
data = ['2018-01-01', 'yandex', 'cpc', 100]

print(reduce(lambda val, key: {key: val}, reversed(data)))
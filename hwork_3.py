#Первая задача
boys = ['Peter','Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == 5:
  print('Идеальная пара:')
else:
  print('Кто то может остаться без пары')
boys.sort()                #сортируем список мальчиков
girls.sort()               #сортируем список девочек
dating = zip(boys, girls)  #обьединяем списки
for couple in dating:
   print(f'{couple[0]} и {couple[1]}')

  
# Вторая задача 
cook_book = [ ['салат',[
         ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],  ]
  ],
  ['пицца',    [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'], ],
  ],
  ['фруктовый десерт',  [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  ]]]
person=5
for dish, ingrs in cook_book:
  print(f'{dish.capitalize()}:')
  for name, q, measure in ingrs:
    print(f'{name}, {q*person} {measure}')
  print()

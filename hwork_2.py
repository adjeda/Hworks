# Зодиак Вводим месяц и день рождения ,получаем знак Зодиака
month = int(input ('Введите месяц Вашего рождения  :  '))
date = int(input ('Введите дату Вашего рождения :  '))

if(date >= 21 and date <= 18 and month == 1) or( month == 4 and date >= 1 and date <= 19):
    print ('Овен')
elif(date >= 20 and date <= 30 and month == 4) or( month == 5 and date >= 1 and date <= 20):
    print ('Телец')
elif(date >= 21 and date <= 31 and month == 5) or( month == 6 and date >= 1 and date <= 21):
    print ('Близнецы')
elif(date >= 22 and date <= 30 and month == 6) or( month == 7 and date >= 1 and date <= 22):
    print ('Рак')
elif(date >= 23 and date <= 31 and month == 7) or( month == 8 and date >= 1 and date <= 22):
    print ('Лев')
elif(date >= 23 and date <= 31 and month == 8) or( month == 9 and date >= 1 and date <= 22):
    print ('Дева')
elif(date >= 23 and date <= 30 and month == 9) or( month == 10 and date >= 1 and date <= 23):
    print ('Весы')
elif(date >= 24 and date <= 31 and month == 10) or( month == 11 and date>=1 and date<=22):
    print ('Скорпион')
elif(date >= 23 and date <= 30 and month == 11) or( month == 12 and date >= 1 and date <= 21):
    print ('Стрелец')
elif(date >= 22 and date <= 31 and month == 12) or( month == 1 and date >= 1 and date <= 20):
    print('Козерог')
elif(date >= 21 and date <= 31 and month == 1) or( month == 2 and date >= 1 and date <= 18):
    print ('Водолей')
elif(date >= 19 and date <= 29 and month == 2) or( month == 3 and date >= 1 and date <= 20):
    print ('Рыбы')
    
    # Задача ипотечного калькулятора
regions_dvostok = ['Амурская область','Еврейская автономная область','Забайкальский край','Камчатский край','Магаданская область','Приморский край','Республика Бурятия','Республика Саха','Сахалинская область','Хабаровский край','Чукотский автономный округ']
base_rate = float(7.8)
regions = input('Введите регион проживания :\n   ')
if regions in regions_dvostok :
    print('Базовая ставка для Вашего региона - 2 %')
  
num_child = int(input('Введите количество детей:\n      '))
salary_client = input('Являетесь ли Вы зарплатным клиентом банка ?:  ')
insur_client = input('\n        Если Вы оформите страховку \n, то базовая ставка уменьшается на 1.5 % \n Желаете оформить страховку ?   ')

if num_child >= 3 and salary_client =='Да' and insur_client =='Да':
   print('\n Базовая ставка составляет',(base_rate - 1 - 0.5 - 1.5),' % ' )
elif num_child >= 3 and salary_client =='Да' and insur_client =='Нет': 
  print('\n Базовая ставка составляет',(base_rate - 1 - 0.5),' % ' )
elif num_child >= 3 and salary_client =='Нет' and insur_client =='Да': 
  print('\n Базовая ставка составляет',(base_rate - 1 - 1.5),' % ' )
elif num_child >= 3 and salary_client =='Нет' and insur_client =='Нет': 
  print('\n Базовая ставка составляет',(base_rate - 1),' % ' )
elif num_child <= 3 and salary_client =='Да' and insur_client =='Да':  
 print('\n Базовая ставка составляет',(base_rate - 0.5 - 1.5),' % ' )
elif num_child <= 3 and salary_client =='Нет' and insur_client =='Да':  
  print('\n Базовая ставка составляет',(base_rate - 1.5),' % ' )
elif num_child <= 3 and salary_client =='Да' and insur_client =='Нет':  
  print('\n Базовая ставка составляет',(base_rate - 0.5),' % ' )
elif num_child <= 3 and salary_client =='Нет' and insur_client =='Нет':  
  print('\n Обратитесь к работникам нашего банка!\n Они помогут подобрать нужную программу !')
  
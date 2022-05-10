# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# duration - целое число: время в секундах. Вы можете вводить duration с клавиатуры или сразу занести в код.
# Формат вывода результата:
# 1. до минуты: <s> сек;
# 2. до часа: <m> мин <s> сек;
# 3. до суток: <h> час <m> мин <s> сек;
# 4. в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите время в секундах: '))

days = duration // 86400
hours = duration // 3600 % 24
minutes = duration // 60 % 60
seconds = duration % 60

if not duration // 60:
    print(f'{duration} сек')
elif 1 <= duration // 60 < 60:
    print(f'{minutes} мин {seconds} сек')
elif 60 <= duration // 60 < 1440:
    print(f'{hours} час {minutes} мин {seconds} сек')
else:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')

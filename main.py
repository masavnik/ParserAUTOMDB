a = ['автомобильный бренд', 'модель', 'Страна марки', 'Класс автомобиля', 'Тип кузова', 'Количество дверей',
     'Количество мест', 'Ширина (с зеркалами)', 'Ширина', 'Длина', 'Высота', 'Колесная база', 'Колея передняя',
     'Колея задняя', 'Объем багажника минимальный', 'Объем багажника максимальный', 'Дорожный просвет', 'Тип двигателя',
     'Расположение двигателя', 'Объем двигателя', 'Мощность', 'При оборотах в минуту', 'Мощность (кВт)',
     'Крутящий момент', 'Система питания', 'Тип наддува', 'Газораспределительный механизм', 'Расположение цилиндров',
     'Количество цилиндров', 'Количество клапанов на цилиндр', 'Тип топлива', 'Диаметр цилиндра и ход поршня',
     'Степень сжатия', 'Модель двигателя', 'Выбросы CO2, г/км', 'Экологический стандарт', 'Тип передней подвески',
     'Тип задней подвески', 'Тип КПП', 'Кол-во передач', 'Передаточное отношение главной пары', 'Привод',
     'Передние тормоза', 'Задние тормоза', 'Максимальная скорость', 'Время разгона (0-100 км/ч)',
     'Расход топлива в городе на 100 км', 'Расход топлива на шоссе на 100 км', 'Расход топлива средний на 100 км',
     'Снаряженная масса автомобиля', 'Допустимая полная масса', 'Объем топливного бака', 'Размер шин',
     'Колесные диски (Размер)', 'Запас хода', 'Полная зарядка', 'Диаметр разворота', 'Тип рулевого управления']

b = ['Toyota', 'Hilux', ' Япония', ' J', ' Пикап Двойная кабина', ' 4', ' 5', ' -', ' 1855 мм', ' 5325 мм', ' 1815 мм',
     ' 3085 мм', ' 1540 мм', ' 1550 мм', ' - л.', ' - л.', ' 227 мм', ' Бензин', ' переднее, продольное', ' 2694 см³',
     ' 166 л.с.', ' 5200', ' 122 кВт', ' 245 Нм', ' распределенный впрыск (многоточечный)', ' нет', ' -', ' рядное',
     ' 4', ' 4', ' 92', ' 95 × 95 мм', ' 10.2', ' -', ' 253', ' Euro 5', ' независимая, пружинная',
     ' зависимая (рессорная)', ' механика', ' 5', ' -', ' Полный привод', ' дисковые вентилируемые',
     ' дисковые вентилируемые', ' 180 км/ч', ' 12.1 сек.', ' -', ' -', ' 10.6 л.', ' 1950 кг', ' 2730 кг', ' 80 л.',
     ' 265/65/R17 265/60/R18', ' -', ' -', ' -', ' -', ' -']

d = [i.capitalize() for i in a]


h = dict(zip(d, b))

print(h)
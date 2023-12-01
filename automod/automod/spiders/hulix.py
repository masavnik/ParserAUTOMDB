import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector


class HulixSpider(scrapy.Spider):
    name = "hulix"
    allowed_domains = ["automdb.com"]
    start_urls = ["https://automdb.com/lang/ru/toyota/hilux"]

    def parse(self, response, **kwargs):
        link = response.css('div.auto_model_block a::attr(href)').extract()

        for i_link in link:
            yield response.follow(i_link, callback=self.open_link_auto)

    def open_link_auto(self, response):

        for url in response.css('td.auto_mod_list_data a::attr(href)').extract():
            yield response.follow(url, callback=self.get_info_car)

    def get_info_car(self, response):

        car_modification = ' '.join(response.css('div.auto_generation_subtitle span::text').get().split()[2:])
        car_ear = int(''.join(response.css('div.auto_generation_subtitle span::text').get().split()[-1]))
        car_proper = response.css('td.auto_mod_name_data ::text').extract()
        name_proper = response.css('td.auto_mod_name ::text').extract()
        general_proper = dict(zip(name_proper, car_proper))

        item = {
            'Модификация': car_modification,
            'Год': car_ear,
            'Автомобильный бренд': general_proper.get('автомобильный бренд'),
            'ТИП КУЗОВА': '',
            'Модель': general_proper.get('модель'),
            'Страна марки': general_proper.get('Страна марки'),
            'Класс автомобиля': general_proper.get('Класс автомобиля'),
            'Тип кузова': general_proper.get('Тип кузова'),
            'Количество дверей': general_proper.get('Количество дверей'),
            'Количество мест': general_proper.get('Количество мест'),
            'Ширина (с зеркалами)': general_proper.get('Ширина (с зеркалами)'),
            'Ширина': general_proper.get('Ширина'),
            'Длина': general_proper.get('Длина'),
            'Высота': general_proper.get('Высота'),
            'Колесная база': general_proper.get('Колесная база'),
            'Колея передняя': general_proper.get('Колея передняя'),
            'Колея задняя': general_proper.get('Колея задняя'),
            'Объем багажника минимальный': general_proper.get('Объем багажника минимальный'),
            'Объем багажника максимальный': general_proper.get('Объем багажника максимальный'),
            'Дорожный просвет': general_proper.get('Дорожный просвет'),
            'ДВИГАТЕЛЬ': '',
            'Тип двигателя': general_proper.get('Тип двигателя'),
            'Расположение двигателя': general_proper.get('Расположение двигателя'),
            'Объем двигателя': general_proper.get('Объем двигателя'),
            'Мощность': general_proper.get('Мощность'),
            'При оборотах в минуту': general_proper.get('При оборотах в минуту'),
            'Мощность (кВт)': general_proper.get('Мощность (кВт)'),
            'Крутящий момент': general_proper.get('Крутящий момент'),
            'Система питания': general_proper.get('Система питания'),
            'Тип наддува': general_proper.get('Тип наддува'),
            'Газораспределительный механизм': general_proper.get('Газораспределительный механизм'),
            'Расположение цилиндров': general_proper.get('Расположение цилиндров'),
            'Количество цилиндров': general_proper.get('Количество цилиндров'),
            'Количество клапанов на цилиндр': general_proper.get('Количество клапанов на цилиндр'),
            'Диаметр цилиндра и ход поршня': general_proper.get('Диаметр цилиндра и ход поршня'),
            'Степень сжатия': general_proper.get('Степень сжатия'),
            'Модель двигателя': general_proper.get('Модель двигателя'),
            'Выбросы CO2, г/км': general_proper.get('Выбросы CO2, г/км'),
            'Экологический стандарт': general_proper.get('Экологический стандарт'),
            'ПОДВЕСКА': '',
            'Тип передней подвески': general_proper.get('Тип передней подвески'),
            'Тип задней подвески': general_proper.get('Тип задней подвески'),
            'ТРАНСМИССИЯ': '',
            'Тип КПП': general_proper.get('Тип КПП'),
            'Кол-во передач': general_proper.get('Кол-во передач'),
            'Передаточное отношение главной пары': general_proper.get('Передаточное отношение главной пары'),
            'Привод': general_proper.get('Привод'),
            'ТОРМОЗНАЯ СИСТЕМА': '',
            'Передние тормоза': general_proper.get('Передние тормоза'),
            'Задние тормоза': general_proper.get('Задние тормоза'),
            'ЭКСПЛУАТАЦИОННЫЕ ПОКАЗАТЕЛИ': '',
            'Максимальная скорость': general_proper.get('Максимальная скорость'),
            'Время разгона (0-100 км/ч)': general_proper.get('Время разгона (0-100 км/ч)'),
            'Расход топлива в городе на 100 км': general_proper.get('Расход топлива в городе на 100 км'),
            'Расход топлива на шоссе на 100 км': general_proper.get('Расход топлива на шоссе на 100 км'),
            'Снаряженная масса автомобиля': general_proper.get('Снаряженная масса автомобиля'),
            'Расход топлива средний на 100 км': general_proper.get('Расход топлива средний на 100 км'),
            'Допустимая полная масса': general_proper.get('Допустимая полная масса'),
            'Объем топливного бака': general_proper.get('Объем топливного бака'),
            'Размер шин': general_proper.get('Размер шин'),
            'Колесные диски (Размер)': general_proper.get('Колесные диски (Размер)'),
            'Запас хода': general_proper.get('Запас хода'),
            'Полная зарядка': general_proper.get('Полная зарядка'),
            'РУЛЕВОЕ УПРАВЛЕНИЕ': '',
            'Диаметр разворота': general_proper.get('Диаметр разворота'),
            'Тип рулевого управления': general_proper.get('Тип рулевого управления'),

        }

        yield item


# response.css('div.auto_model_block a::attr(href)').extract() - Ссылки на модели
# https://automdb.com/lang/ru/toyota/hilux

# response.css('td.auto_mod_list_data a::attr(href)').extract() - Ссылки на модификации
# https://automdb.com/lang/ru/toyota/hilux/viii_res/group_pickup_4dr

# response.css('div.auto_generation_subtitle span::text').get() - Имя автомобиля Достать модификкапцию и год


# response.css('td.auto_mod_name_data ::text').extract() - Все характеристики
# response.css('td.auto_mod_name ::text').extract() - Имя характеристик

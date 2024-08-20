import unittest
import sys
import os
sys.path.append(os.getcwd())

import main


class TestQuadraticEquationFunc(unittest.TestCase):
    '''Тесты функции solve_quadratic_equation
    '''
    def test_quadratic_equation_2_roots(self):
        for i, (a, b, c, res_manual) in enumerate([
            (1, 8, 15, (-3.0, -5.0)),
            (1, -13, 12, (12.0, 1.0)),
            (1, 20, 10, (-0.51, -19.49))
        ], 1):
            with self.subTest(i):
                res_func = main.solve_quadratic_equation(a, b, c)
                self.assertTupleEqual(res_func, res_manual)

    def test_quadratic_equation_1_roots(self):
        for i, (a, b, c, res_manual) in enumerate([
            (-4, 28, -49, 3.5),
            (1, -16, 64, 8.0),
            (1, 10, 25, -5.0)
        ], 1):
            with self.subTest(i):
                res_func = main.solve_quadratic_equation(a, b, c)
                self.assertEqual(res_func, res_manual)

    def test_quadratic_equation_no_roots(self):
        for i, (a, b, c) in enumerate([
            (1, 6, 45),
            (1, -2, 5),
            (2, 3, 2)
        ], 1):
            with self.subTest(i):
                res_func = main.solve_quadratic_equation(a, b, c)
                self.assertEqual(res_func, 'Корней нет')

class TestUniqueNamesFunc(unittest.TestCase):
    '''Тест функции collect_unique_names
    '''
    def test_unique_names_nested_lists(self):
        names = [
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        res_manual = 'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
        res_func = main.collect_unique_names(names)
        self.assertMultiLineEqual(res_func, res_manual)
    
    def test_unique_names_flat_list(self):
        names = ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"]
        res_manual = 'Алексей, Анатолий, Анна, Антон, Вадим, Денис, Евгений, Иван, Илья, Константин, Максим, Никита, Павел, Ринат, Сергей, Тимур, Филипп, Юрий'
        res_func = main.collect_unique_names(names)
        self.assertMultiLineEqual(res_func, res_manual)

class TestInitialsFunc(unittest.TestCase):
    '''Тест функции get_initials
    '''
    def test_initials(self):
        for i, (name, res_manual) in enumerate([
            (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
            (['Жан', 'Клот', 'Вандамович'], 'ЖКВ'),
            (['Павлов', 'Иван', 'Уралович'], 'ПИУ'),
            (['Семейный', 'Доминик', 'Торретович'], 'СДТ'),
            (['Футболист', 'Сборной', 'Индии'], 'ФСИ')
        ], 1):
            with self.subTest(i):
                res_func = main.get_initials(name)
                self.assertMultiLineEqual(res_func, res_manual)
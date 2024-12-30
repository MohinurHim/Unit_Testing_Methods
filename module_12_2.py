# Методы Юнит-тестирования
import unittest
import module_12_0_2 as runn
from module_12_0_2 import Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # словарь в который будут сохраняться результаты всех тестов
    def setUp(self):
        self.run_1 = runn.Runner('Усейн', 10)
        self.run_2 = runn.Runner('Андрей', 9)
        self.run_3 = runn.Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls): # метод, где выводятся all_results по очереди в столбец
       for result in cls.all_results.values():
           res = {}
           for place, runner in result.items():
               res[place] = runner.name
               print(res)
    def test_1(self):
        self.tournament_1 = Tournament(90, self.run_1, self.run_3)
        self.all_results = self.tournament_1.start() # словарь записываем результат функции
        last_name = self.all_results[max(self.all_results.keys())].name  # имя с максимальным местом
        self.assertTrue(last_name, self.run_3) # сравнение
        TournamentTest.all_results[1] = self.all_results # словарь

    def test_2(self):
        self.tournament_2 = Tournament(90, self.run_2, self.run_3)
        self.all_results = self.tournament_2.start()  # словарь записываем результат функции
        last_name = self.all_results[max(self.all_results.keys())].name  # имя с максимальным местом
        self.assertTrue(last_name, self.run_3.name)  # сравнение
        TournamentTest.all_results[2] = self.all_results  # словарь

    def test_3(self):
        self.tournament_3 = Tournament(90, self.run_1,self.run_2, self.run_3)
        self.all_results = self.tournament_3.start()  # словарь записываем результат функции
        last_name = self.all_results[max(self.all_results.keys())].name  # имя с максимальным местом
        self.assertTrue(last_name, self.run_3)  # сравнение
        TournamentTest.all_results[3] = self.all_results  # словарь

if __name__ == "__main__":
    unittest.main()
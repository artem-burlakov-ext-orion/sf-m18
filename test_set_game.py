import unittest
import set_game

class GetCardTest(unittest.TestCase):

    def setUp(self):
        print(f'Запускается тест {self.shortDescription()}')

    def tearDown(self):
        print(f'Очистка после прогона {self.id()}')

    def test_return_isinstance(self):
        'Проверка класса возвращаемых обьектов функции генерации карт'
        for i in set_game.get_three_cards_from_index(set_game.set_3):
            self.assertIsInstance(i, set_game.Card)

    def test_raise_error_1(self):
        'Возврат ошибки при неверных аргументах'
        with self.assertRaises(ValueError):
            set_game.get_three_cards_random(set_game.error_args_1, set_game.no_error_args, set_game.no_error_args)

    def test_raise_error_2(self):
        'Возврат ошибки при неверных аргументах'
        with self.assertRaises(ValueError):
            set_game.get_three_cards_random(set_game.no_error_args, set_game.error_args_2, set_game.no_error_args)

    def test_raise_error_3(self):
        'Возврат ошибки при неверных аргументах'
        with self.assertRaises(ValueError):
            set_game.get_three_cards_random(set_game.no_error_args, set_game.no_error_args, set_game.error_args_3)

class CheckSetTest(unittest.TestCase):

    def setUp(self):
        print(f'Запускается тест {self.shortDescription()}')

    def tearDown(self):
        print(f'Очистка после прогона {self.id()}')

    def test_check_set_return_true_1(self):
        'Возврат True при комбинации set'
        self.assertEqual(set_game.check_set(set_game.get_three_cards_from_index(set_game.set_1)), True)

    def test_check_set_return_true_2(self):
        'Возврат True при комбинации set'
        self.assertEqual(set_game.check_set(set_game.get_three_cards_from_index(set_game.set_2)), True)

    def test_check_set_return_true_3(self):
        'Возврат True при комбинации set'
        self.assertEqual(set_game.check_set(set_game.get_three_cards_from_index(set_game.set_3)), True)

    def test_check_set_return_false_1(self):
        'Возврат False при комбинации noset'
        self.assertEqual(set_game.check_set(set_game.get_three_cards_from_index(set_game.no_set_1)), False)

    def test_check_set_return_false_2(self):
        'Возврат False при комбинации noset'
        self.assertEqual(set_game.check_set(set_game.get_three_cards_from_index(set_game.no_set_2)), False)

    def test_check_set_return_false_3(self):
        'Возврат False при комбинации noset'
        self.assertEqual(set_game.check_set(set_game.get_three_cards_from_index(set_game.no_set_3)), False)

if __name__ == '__main__':
    unittest.main()

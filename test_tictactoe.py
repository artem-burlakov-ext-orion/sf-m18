import pytest
from tictactoe import get_board, validate_board, game_finished, render_board
import random



class TestValidateBoard():

    def test_return_type(self):
        assert isinstance(validate_board(get_board()), bool)

    def test_return_true_1(self):
        assert validate_board(get_board()) == True

    def test_return_true_2(self):
        assert validate_board([[1,2,1],[2,1,2],[1,2,1]]) == True

    def test_return_false_1(self):
        assert validate_board(get_board(rows=4)) == False

    def test_return_false_2(self):
        assert validate_board(get_board([1, 4, 2])) == False

    def test_return_false_3(self):
        assert validate_board(get_board([0, 1, 2, 1])) == False

    def test_return_false_4(self):
        assert validate_board(get_board([0, 1])) == False

class TestGameFinished():

    def test_return_type(self):
        assert isinstance(game_finished(get_board()), int)

    def test_return_zero(self):
        assert game_finished([[2, 0, 2],[1, 1, 0],[0, 1, 0]]) == 0

    def test_return_one_1(self):
        assert game_finished(get_board()) == 1

    def test_return_one_2(self):
        assert game_finished([[1, 0, 2], [2, 1, 0], [2, 0, 1]]) == 1

    def test_return_one_3(self):
        assert game_finished([[1, 0, 2], [1, 1, 1], [2, 2, 1]]) == 1

    def test_return_two_1(self):
        assert game_finished([[2, 2, 2],[0, 2, 1],[1, 2, 0]]) == 2

    def test_return_two_2(self):
        assert game_finished([[1, 0, 2],[0, 2, 1],[2, 1, 0]]) == 2

    def test_return_two_3(self):
        assert game_finished([[2, 0, 1],[2, 0, 1],[2, 1, 0]]) == 2

    def test_return_minus_one_1(self):
        assert game_finished([[2, 1, 1],[1, 2, 2],[2, 1, 1]]) == -1

    def test_return_minus_one_2(self):
        assert game_finished([[1, 2, 2],[2, 1, 1],[1, 1, 2]]) == -1

class TestRenderBoard():

    def test_return_type_1(self):
        assert isinstance(render_board(get_board()), str)

    def test_return_type_2(self):
        assert isinstance(render_board([[1,2,1],[2,1,2],[1,2,1]]), str)

    def test_return_type_3(self):
        assert isinstance(render_board([[1, 0, 2],[0, 2, 1],[2, 1, 0]]), str)

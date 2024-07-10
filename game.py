def check_duplicate_char(guess_num):
    return len({c for c in guess_num}) != 3


def check_invalid_input(guess_num):
    if not guess_num:
        raise TypeError('입력이 존재하지 않습니다.')
    if len(guess_num) != 3:
        raise TypeError('입력은 세글자여야만 합니다.')
    for c in guess_num:
        if not ord('0') <= ord(c) <= ord('9'):
            raise TypeError('입력은 숫자로만 이뤄져야 합니다.')
    if check_duplicate_char(guess_num):
        raise TypeError('입력은 서로 다른 숫자로 이뤄져야 합니다.')


class GameResult:
    def __init__(self, solved, strike, ball):
        self.__solved: bool = solved
        self.__strike: int = strike
        self.__ball: int = ball

    def get_solved(self):
        return self.__solved

    def get_strike(self):
        return self.__strike

    def get_ball(self):
        return self.__ball


class Game:
    def __init__(self):
        self.question = ''

    def is_solved(self, guess_num):
        return self.question == guess_num

    def get_strike_and_ball(self, guess_num):
        strike = 0
        ball = 0
        for user_input, answer in zip(self.question, guess_num):
            if user_input == answer:
                strike += 1
            elif user_input in guess_num:
                ball += 1
        return GameResult(False, strike, ball)

    def guess(self, guess_num: str):
        check_invalid_input(guess_num)

        if self.is_solved(guess_num):
            return GameResult(True, 3, 0)
        return self.get_strike_and_ball(guess_num)

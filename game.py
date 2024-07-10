class Game:
    def guess(self, guess_num: str):
        if not guess_num:
            raise TypeError('입력이 존재하지 않습니다.')
        if len(guess_num) != 3:
            raise TypeError('입력은 세글자여야만 합니다.')

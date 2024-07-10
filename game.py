class Game:
    def guess(self, guess_num: str):
        if not guess_num:
            raise TypeError('입력이 존재하지 않습니다.')

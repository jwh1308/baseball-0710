class Game:
    def guess(self, guess_num: str):
        if not guess_num:
            raise TypeError('입력이 존재하지 않습니다.')

        if len(guess_num) != 3:
            raise TypeError('입력은 세글자여야만 합니다.')

        for c in guess_num:
            if not ord('0') <= ord(c) <= ord('9'):
                raise TypeError('입력은 숫자로만 이뤄져야 합니다.')

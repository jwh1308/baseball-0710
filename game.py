class Game:
    def guess(self, guess_num: str):
        if not guess_num:
            raise TypeError('입력이 존재하지 않습니다.')

        if len(guess_num) != 3:
            raise TypeError('입력은 세글자여야만 합니다.')

        for c in guess_num:
            if not ord('0') <= ord(c) <= ord('9'):
                raise TypeError('입력은 숫자로만 이뤄져야 합니다.')

        char_set = set()
        for c in char_set:
            char_set.add(c)
        if len(char_set) != 3:
            raise TypeError('입력은 서로 다른 숫자로 이뤄져야 합니다.')

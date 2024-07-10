class Game:
    def guess(self, input: str):
        if not input:
            raise TypeError('입력이 존재하지 않습니다.')

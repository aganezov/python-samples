

class ConsoleGameLogger(object):

    def __init__(self, game):
        """ A logger, that outputs board's statistics tot he console every time the lifecycle is completed """
        self.game = game

    def update_on_board_status(self):
        board = self.game.board
        print("=" * 80)
        print("Generation     : {step}".format(step=board.step))
        print("# living cells : {number_living}".format(number_living=board.number_living))
        print("# living cells : {number_dead}".format(number_dead=board.number_dead))
        print()

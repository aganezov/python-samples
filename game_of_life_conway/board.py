import random

VERTICAL_SIZE = 50
HORIZONTAL_SIZE = VERTICAL_SIZE


class Board(object):
    def __init__(self, board=None, v_size=VERTICAL_SIZE, h_size=HORIZONTAL_SIZE):
        """ Model-like object, encapsulating data and logic for the Conway's game of life

        If no board data-structure is provided, an empty board with all organisms dead is generated

        Living cells are represented by 1s, dead by 0s
        Board data structure is s nested list of lists
        Implementing an observer pattern for board changes notifications
        """
        self.step = 0
        self.board = board if board is not None else BoardFactory.generate_empty_board_field(v_size=v_size, h_size=h_size)
        self.observers = []

    def count_living_neighbours(self, h_index, v_index):
        """ Index checking is not important, as out of range indexes calls return 0 by default """
        result = 0
        result += self.get_value(h_index - 1, v_index)
        result += self.get_value(h_index + 1, v_index)
        result += self.get_value(h_index, v_index - 1)
        result += self.get_value(h_index, v_index + 1)
        result += self.get_value(h_index - 1, v_index - 1)
        result += self.get_value(h_index + 1, v_index + 1)
        result += self.get_value(h_index - 1, v_index + 1)
        result += self.get_value(h_index + 1, v_index - 1)
        return result

    @property
    def vertical_size(self):
        return len(self.board)

    @property
    def horizontal_size(self):
        return len(self.board[0])

    @property
    def number_living(self):
        """ As living cells are represented as 1s, the sum is sufficient """
        return sum(value for row in self.board for value in row)

    @property
    def number_dead(self):
        return self.vertical_size * self.horizontal_size - self.number_living

    def execute_single_life_cycle(self):
        """ Single generation lifecycle, following the rules of Conway's game of life
        (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) """
        new_board_value = BoardFactory.generate_empty_board_field(v_size=self.vertical_size,
                                                                  h_size=self.horizontal_size)
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                neighbours_cnt = self.count_living_neighbours(v_index=i, h_index=j)
                if value == 1:
                    if neighbours_cnt in (2, 3):
                        # if a living cell is surrounded by 2 or 3 living neighbours, it goes into next generation
                        new_board_value[i][j] = 1
                    else:
                        # if less than 2, or more than 3 neighbours surround an organism, it dies from starvation / overpopulation
                        new_board_value[i][j] = 0
                elif neighbours_cnt == 3:
                    # previously dead cell, that is surrounded by exactly 3 living organisms is resurrected
                    new_board_value[i][j] = 1
        self.board = new_board_value
        self.step += 1
        self.update_observers()

    def get_value(self, h_index, v_index):
        """ Allows for our of range indexes, returning 0 in respective cases """
        if h_index < 0 or h_index >= self.horizontal_size:
            return 0
        if v_index < 0 or v_index >= self.vertical_size:
            return 0
        return self.board[v_index][h_index]

    def set_value(self, h_index, v_index, value):
        """ Sets a value for a specified location. Allows for index out of range assignments, silently mocking them """
        try:
            self.board[v_index][h_index] = value
            self.update_observers()
        except IndexError:
            pass

    def switch_value(self, h_index, v_index):
        """ Flips the value for a specified location. Allows for index out of range assignments, silently mocking them """
        if h_index < 0 or h_index >= self.horizontal_size or v_index < 0 or v_index >= self.vertical_size:
            return
        self.set_value(h_index=h_index, v_index=v_index, value=1 if self.get_value(h_index, v_index) == 0 else 0)
        self.update_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        """ Removes and observer for current subject. Allows for a non-existing observer removal, silently mocking it """
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def update_observers(self):
        """ Observer pattern implementation """
        for observer in self.observers:
            observer.update_on_board_status()


class BoardFactory(object):
    @staticmethod
    def generate_empty_board_field(v_size=VERTICAL_SIZE, h_size=HORIZONTAL_SIZE):
        """ Generates a board data structure with all organisms dead """
        return [[0 for _ in range(h_size)] for __ in range(v_size)]

    @staticmethod
    def generate_empty_board(v_size=VERTICAL_SIZE, h_size=HORIZONTAL_SIZE):
        return Board(v_size=v_size, h_size=h_size)

    @staticmethod
    def generate_randomized_board(v_size=VERTICAL_SIZE, h_size=HORIZONTAL_SIZE, probability=50):
        """ Generates a board object with organisms randomly being alive / dead, based on supplied probability,
         ranging from 0 to 100 (0 being guarantee dead, 100 being guarantee alive)"""
        result = Board(v_size=v_size, h_size=h_size)
        result.board = BoardFactory.generate_randomized_board_field(v_size=v_size,
                                                                    h_size=h_size, probability=probability)
        return result

    @staticmethod
    def generate_randomized_board_field(v_size=VERTICAL_SIZE, h_size=HORIZONTAL_SIZE, probability=50):
        """ Generates a board data-structure with every organism being alive with a probability, specified by
         `probability` parameter, independently from all other organisms. Supplied probability is normalized by 100 """
        result = [[0 for _ in range(h_size)] for __ in range(v_size)]
        for x_index, row in enumerate(result):
            for y_index, _ in enumerate(row):
                value = 1 if random.randrange(100) < probability else 0
                result[x_index][y_index] = value
        return result

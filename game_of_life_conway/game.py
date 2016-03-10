import tkinter as tk
import tkinter.font as tkfonts
import tkinter.simpledialog as tkdialogs

import board
from console import ConsoleGameLogger
from widgets import GameCanvas, GameStatisticsLabel, GameWindowMenu


class Game(object):
    """ Display related class variables """
    cell_size = 12
    color_living = "blue"
    color_dead = "grey"
    delay_in_milliseconds = 500

    def __init__(self, board_instance, cell_size=None):
        """ The main managing object, that works as a master GUI view for the specified game of life board_instance """
        self.board = board_instance
        self.auto = False
        self.cell_size = cell_size if cell_size is not None else self.cell_size

        # GUI initialization
        self.root_gui = tk.Tk()
        self.root_gui.wm_title("JetBrains GWU || Conway's game of life")
        self.non_canvas_frame = tk.Frame(master=self.root_gui)
        self.game_canvas = GameCanvas(game=self, master=self.root_gui,
                                      width=self.board.horizontal_size * self.cell_size + 1,
                                      height=self.board.vertical_size * self.cell_size + 1,
                                      highlightthickness=0,
                                      bd=0,
                                      bg=self.color_dead)
        self.game_statistics_label = GameStatisticsLabel(game=self, master=self.non_canvas_frame,
                                                         bg="white", justify=tk.LEFT, relief=tk.GROOVE,
                                                         font=tkfonts.Font(weight="bold"))
        self.game_statistics_label.grid(row=1, column=0, pady=20)
        self.board.add_observer(self.game_statistics_label)
        self.board.add_observer(self.game_canvas)
        self.window_game_menu = GameWindowMenu(game=self, master=self.non_canvas_frame)
        self.window_game_menu.grid(row=0, column=0, pady=20)
        self.non_canvas_frame.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        self.game_canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.board.update_observers()

    def get_color(self, value):
        return self.color_living if value == 1 else self.color_dead

    def reset_board(self):
        probability = tkdialogs.askinteger("Probability",
                                           "Enter a probability of a cell being alive, ranging from 0 to 100\n"
                                           "\tTo get an empty board use the '0' value")
        if probability is None or probability < 0 or probability > 100: # None is returned if 'Cancel' is pressed
            return
        self.board.board = board.BoardFactory.generate_randomized_board_field(h_size=self.board.horizontal_size,
                                                                              v_size=self.board.vertical_size,
                                                                              probability=probability)
        self.board.update_observers()   # update all observers over changed board manually

    def start_auto(self):
        self.auto = True
        self.run_auto()

    def run_auto(self):
        if self.auto:
            self.board.execute_single_life_cycle()
            self.root_gui.after(ms=self.delay_in_milliseconds, func=self.run_auto)

    def stop_auto(self):
        """ Variable update is sufficient, as it is checked in the "auto" run loop on every auto-call to lifecycle execution """
        self.auto = False

    def start(self):
        self.root_gui.mainloop()

    def stop(self):
        self.root_gui.quit()


if __name__ == "__main__":
    game = Game(board_instance=board.BoardFactory.generate_randomized_board(v_size=30,
                                                                            h_size=40,
                                                                            probability=30),
                cell_size=20)
    console_logger = ConsoleGameLogger(game=game)
    game.board.add_observer(console_logger)
    game.start()

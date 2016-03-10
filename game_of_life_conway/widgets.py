import tkinter as tk


class GameCanvas(tk.Canvas):
    def __init__(self, game, master=None, cnf={}, **kw):
        """ A widget, responsible for visual rectangle-based representation of the board """
        super().__init__(master, cnf, **kw)
        self.game = game
        self.bind("<Button-1>", self.switch_game_cell) # left-mouse is denoted by "<Button-1>"

    def draw_board(self, board_instance):
        self.delete(tk.ALL) # removes all existing rectangles from canvas
        for y_index in range(board_instance.vertical_size):
            for x_index in range(board_instance.horizontal_size):
                color = self.game.get_color(board_instance.get_value(h_index=x_index, v_index=y_index))
                cell_size = self.game.cell_size
                self.create_rectangle(x_index * cell_size, y_index * cell_size,
                                      (x_index + 1) * cell_size, (y_index + 1) * cell_size,
                                      fill=color)

    def switch_game_cell(self, event):
        self.game.board.switch_value(h_index=event.x // self.game.cell_size,
                                     v_index=event.y // self.game.cell_size)

    def update_on_board_status(self):
        """ Whenever the board is updated, it must be redrawn """
        self.draw_board(self.game.board)


class GameStatisticsLabel(tk.Label):
    def __init__(self, game, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.game = game

    def update_on_board_status(self):
        self.configure(text="# living cells: {living_cnt}\n"
                            "# dead cells:   {dead_cnt}\n"
                            "generation:     {step}"
                            "".format(living_cnt=self.game.board.number_living,
                                      dead_cnt=self.game.board.number_dead,
                                      step=self.game.board.step))


class GameWindowMenu(tk.Frame):
    button_width = 10
    x_padding = 10
    y_padding = 10

    def __init__(self, game, master=None, cnf={}, **kw):
        """ A Widget with "in-window" menu containing game operational controls """
        super().__init__(master, cnf, **kw)
        self.game = game
        self.setup_buttons()

    def setup_buttons(self):
        """ Sets up all buttons in the "in-window" menu

        Menu setup
            * "Next step"   -- executes a single board lifecycle
            * "Start auto"  -- starts auto execution of the board lifecycle command
            * "Stop auto"   -- stops auto execution of the board lifecycle command
            * "Reset board" -- prompts for a new living density and then creates a new board accordingly
            * "Exit"        -- exits the program
        """
        step_button = tk.Button(master=self, text="Next step",
                                width=self.button_width,
                                command=self.game.board.execute_single_life_cycle)
        step_button.grid(row=1, column=0,
                         padx=self.x_padding,
                         pady=self.y_padding)
        start_button = tk.Button(master=self, text="Start auto",
                                 width=self.button_width,
                                 command=self.game.start_auto)
        start_button.grid(row=2, column=0,
                          padx=self.x_padding,
                          pady=self.y_padding)
        stop_button = tk.Button(master=self, text="Stop auto",
                                width=self.button_width,
                                command=self.game.stop_auto)
        stop_button.grid(row=3, column=0,
                         padx=self.x_padding,
                         pady=self.y_padding)
        reset_button = tk.Button(master=self, text="Reset board",
                                 width=self.button_width,
                                 command=self.game.reset_board)
        reset_button.grid(row=4, column=0,
                          padx=self.x_padding,
                          pady=self.y_padding)
        exit_button = tk.Button(master=self, text="Exit",
                                width=self.button_width,
                                command=self.game.stop)
        exit_button.grid(row=5, column=0,
                         padx=self.x_padding,
                         pady=self.y_padding)
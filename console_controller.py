"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    try:
        model.move(origin, dest)

    except IllegalMoveError as error:
        print(error)



class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """

        self.cheese_model = TOAHModel(number_of_stools)
        self.cheese_model.fill_first_stool(number_of_cheeses)
        self.number_of_cheese = number_of_cheeses
        self.number_of_stools = number_of_stools

        print("Welcome to the game. ")
        print("You will be asked to input the number of cheeses and "\
              "stools that you would like to play with")
        print("Make sure your inputs are a single int of how many cheeses "\
              "or stools you would like.")
        print("If you would like to stop playing, simply type 'quit'. ")


    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """

        while True:

            answer_first_stool = input("Enter the first stool: ")
            answer_last_stool = input("Enter the last stool: ")

            if answer_first_stool == "quit" or answer_last_stool == "quit":
                break
            else:
                new_answer_last_stool = int(answer_last_stool)
                new_answer_first_stool = int(answer_first_stool)

                if (new_answer_last_stool < self.number_of_stools) and \
                        (new_answer_first_stool < self.number_of_stools):
                    move(self.cheese_model, new_answer_first_stool, new_answer_last_stool)
                else:
                    raise IllegalMoveError("Cannot place larger cheese on top of smaller")
                print(self.cheese_model)









if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.

    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.

    while True:
        try:
            answer_cheese = input("How many cheeses would you like ")
            new_answer_cheese = int(answer_cheese)

            answer_stools = input("How many stools would you like")
            new_answer_stools = int(answer_stools)
            if new_answer_stools <= 0 or new_answer_cheese <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a value greater than 0")
    game = ConsoleController(new_answer_cheese, new_answer_stools)
    game.play_loop()



    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")

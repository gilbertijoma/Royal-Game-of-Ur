"""
File: royal_game_of_ur.py
Author: Gilbert Ijoma
Date: 11/13/2020
The royal game of ur Main file
"""

from sys import argv
from random import choice
from board_square import BoardSquare, UrPiece


class RoyalGameOfUr:
    STARTING_PIECES = 7

    def __init__(self, board_file_name):
        self.board = None
        self.load_board(board_file_name)

    def load_board(self, board_file_name):
        """
        This function takes a file name and loads the map, creating BoardSquare objects in a grid.

        :param board_file_name: the board file name
        :return: sets the self.board object within the class
        """

        import json
        try:
            with open(board_file_name) as board_file:
                board_json = json.loads(board_file.read())
                self.num_pieces = self.STARTING_PIECES
                self.board = []
                for x, row in enumerate(board_json):
                    self.board.append([])
                    for y, square in enumerate(row):
                        self.board[x].append(BoardSquare(x, y, entrance=square['entrance'], _exit=square['exit'], rosette=square['rosette'], forbidden=square['forbidden']))

                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if board_json[i][j]['next_white']:
                            x, y = board_json[i][j]['next_white']
                            self.board[i][j].next_white = self.board[x][y]
                        if board_json[i][j]['next_black']:
                            x, y = board_json[i][j]['next_black']
                            self.board[i][j].next_black = self.board[x][y]
        except OSError:
            print('The file was unable to be opened. ')

    def draw_block(self, output, i, j, square):
        """
        Helper function for the display_board method
        :param output: the 2d output list of strings
        :param i: grid position row = i
        :param j: grid position col = j
        :param square: square information, should be a BoardSquare object
        """
        MAX_X = 8
        MAX_Y = 5
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if x == 0 or y == 0 or x == MAX_X - 1 or y == MAX_Y - 1:
                    output[MAX_Y * i + y][MAX_X * j + x] = '+'
                if square.rosette and (y, x) in [(1, 1), (1, MAX_X - 2), (MAX_Y - 2, 1), (MAX_Y - 2, MAX_X - 2)]:
                    output[MAX_Y * i + y][MAX_X * j + x] = '*'
                if square.piece:
                    #print(square.piece.symbol)
                    output[MAX_Y * i + 2][MAX_X * j + 3: MAX_X * j + 5] = square.piece.symbol

    def display_board(self):
        """
        Draws the board contained in the self.board object
        """
        if self.board:
            output = [[' ' for _ in range(8 * len(self.board[i//5]))] for i in range(5 * len(self.board))]
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if not self.board[i][j].forbidden:
                        self.draw_block(output, i, j, self.board[i][j])

            print('\n'.join(''.join(output[i]) for i in range(5 * len(self.board))))

    def roll_d4_dice(self, n=4):
        """

        :param n: the number of tetrahedral d4 to roll, each with one dot on
        :return: the result of the four rolls.
        """
        dots = 0
        for _ in range(n):
            dots += choice([0, 1])
        return dots

    def set_game(self):
        #set the necessary variables for the game

        # white path board square

        self.bs_0 = BoardSquare(-1, -1)

        self.bs_1 = BoardSquare(3, 0)
        self.board[3][0] = self.bs_1
        self.piece0 = UrPiece(WHITE, 'W0')

        self.piece0.position = self.bs_0
        self.piece1 = UrPiece(WHITE, 'W1')
        self.piece1.position = self.bs_0
        self.piece2 = UrPiece(WHITE, 'W2')
        self.piece2.position = self.bs_0
        self.piece3 = UrPiece(WHITE, 'W3')
        self.piece3.position = self.bs_0
        self.piece4 = UrPiece(WHITE, 'W4')
        self.piece4.position = self.bs_0
        self.piece5 = UrPiece(WHITE, 'W5')
        self.piece5.position = self.bs_0
        self.piece56 = UrPiece(WHITE, 'W6')
        self.piece56.position = self.bs_0


        self.piece6 = UrPiece(BLACK, 'B0')
        self.piece6.position = self.bs_0
        self.piece7 = UrPiece(BLACK, 'B1')
        self.piece7.position = self.bs_0
        self.piece8 = UrPiece(BLACK, 'B2')
        self.piece8.position = self.bs_0
        self.piece9 = UrPiece(BLACK, 'B3')
        self.piece9.position = self.bs_0
        self.piece10 = UrPiece(BLACK, 'B4')
        self.piece10.position = self.bs_0
        self.piece11 = UrPiece(BLACK, 'B5')
        self.piece11.position = self.bs_0
        self.piece12 = UrPiece(BLACK, 'B6')
        self.piece12.position = self.bs_0

        self.bs_2 = BoardSquare(2, 0)
        self.board[2][0] = self.bs_2

        self.bs_3 = BoardSquare(1, 0)
        self.board[1][0] = self.bs_3

        self.bs_4 = BoardSquare(0, 0)
        self.board[0][0] = self.bs_4

        self.bs_5 = BoardSquare(0, 1)
        self.board[0][1] = self.bs_5

        self.bs_6 = BoardSquare(1, 1)
        self.board[1][1] = self.bs_6

        self.bs_7 = BoardSquare(2, 1)
        self.board[2][1] = self.bs_7

        self.bs_8 = BoardSquare(3, 1)
        self.board[3][1] = self.bs_8

        self.bs_9 = BoardSquare(4, 1)
        self.board[4][1] = self.bs_9

        self.bs_10 = BoardSquare(5, 1)
        self.board[5][1] = self.bs_10

        self.bs_11 = BoardSquare(6, 1)
        self.board[6][1] = self.bs_11

        self.bs_12 = BoardSquare(7, 1)
        self.board[7][1] = self.bs_12

        self.bs_13 = BoardSquare(7, 0)
        self.board[7][0] = self.bs_13

        self.bs_14 = BoardSquare(6, 0)
        self.board[6][0] = self.bs_14

        # black path that aren't white path

        self.bs_15 = BoardSquare(3, 2)
        self.board[3][2] = self.bs_15

        self.bs_16 = BoardSquare(2, 2)
        self.board[2][2] = self.bs_16

        self.bs_17 = BoardSquare(1, 2)
        self.board[1][2] = self.bs_17

        self.bs_18 = BoardSquare(0, 2)
        self.board[0][2] = self.bs_18

        self.bs_19 = BoardSquare(7, 2)
        self.board[7][2] = self.bs_19

        self.bs_20 = BoardSquare(6, 2)
        self.board[6][2] = self.bs_20

        self.bs_21 = BoardSquare(-2,-2)
        self.bs_22 = BoardSquare(-3, -3)
        self.bs_22.exit = True
        self.bs_23 = BoardSquare(-3, -4)
        self.bs_23.exit = True
        self.bs_24 = BoardSquare(-2, -5)
        self.bs_24.exit = True

        self.list_boardsquares = [self.bs_1, self.bs_2, self.bs_3, self.bs_4, self.bs_5, self.bs_6, self.bs_7, self.bs_8, self.bs_9,
                                  self.bs_10, self.bs_11, self.bs_12, self.bs_13, self.bs_14, self.bs_15, self.bs_16, self.bs_17, self.bs_18,
                                  self.bs_19, self.bs_20, self.bs_22, self.bs_23, self.bs_24]

        self.list_pieces = [self.piece0, self.piece1, self.piece2, self.piece3, self.piece4, self.piece5, self.piece56, self.piece6, self.piece7, self.piece8, self.piece9, self.piece10, self.piece11, self.piece12]

        # set up white_next and black_next
        self.bs_0.next_white = self.bs_1
        self.bs_0.next_black = self.bs_15

        self.bs_1.next_white = self.bs_2
        self.bs_2.next_white = self.bs_3
        self.bs_3.next_white = self.bs_4
        self.bs_4.next_white = self.bs_5
        self.bs_5.next_white = self.bs_6
        self.bs_6.next_white = self.bs_7
        self.bs_7.next_white = self.bs_8
        self.bs_8.next_white = self.bs_9
        self.bs_9.next_white = self.bs_10
        self.bs_10.next_white = self.bs_11
        self.bs_11.next_white = self.bs_12
        self.bs_12.next_white = self.bs_13
        self.bs_13.next_white = self.bs_14
        self.bs_14.next_white = self.bs_21
        self.bs_21.next_white = self.bs_22
        self.bs_22.next_white = self.bs_23
        self.bs_23.next_white = self.bs_24

        self.bs_15.next_black = self.bs_16
        self.bs_16.next_black = self.bs_17
        self.bs_17.next_black = self.bs_18
        self.bs_18.next_black = self.bs_5
        self.bs_5.next_black = self.bs_6
        self.bs_6.next_black = self.bs_7
        self.bs_7.next_black = self.bs_8
        self.bs_8.next_black = self.bs_9
        self.bs_9.next_black = self.bs_10
        self.bs_10.next_black = self.bs_11
        self.bs_11.next_black = self.bs_12
        self.bs_12.next_black = self.bs_19
        self.bs_19.next_black = self.bs_20
        self.bs_20.next_black = self.bs_21
        self.bs_21.next_black = self.bs_22
        self.bs_22.next_black = self.bs_23
        self.bs_23.next_black = self.bs_24

        #set up the rosettes

        self.bs_4.rosette = True
        self.bs_18.rosette = True
        self.bs_8.rosette = True
        self.bs_19.rosette = True
        self.bs_13.rosette = True

    def white_turn(self):
        #used this function for the white pieces turn
        roll = self.roll_d4_dice()
        print("You rolled", roll)

        if self.piece0.position == self.bs_0:
            print('1: W0 currently off the board')
        elif self.piece0.complete != True:
            print('1: W0',self.piece0.position.position)
        else:
            print('W0 has completed the race.')

        if self.piece1.position == self.bs_0:
            print('2: W1 currently off the board')
        elif self.piece1.complete != True:
            print('2: W1', self.piece1.position.position)
        else:
            print('W1 has completed the race.')

        if self.piece2.position == self.bs_0:
            print('3: W2 currently off the board')
        elif self.piece2.complete != True:
            print('3: W2', self.piece2.position.position)
        else:
            print('W2 has completed the race.')

        if self.piece3.position == self.bs_0:
            print('4: W3 currently off the board')
        elif self.piece3.complete != True:
            print('4: W3', self.piece3.position.position)
        else:
            print('W3 has completed the race.')

        if self.piece4.position == self.bs_0:
            print('5: W4 currently off the board')
        elif self.piece4.complete != True:
            print('5: W4', self.piece4.position.position)
        else:
            print('W4 has completed the race.')

        if self.piece5.position == self.bs_0:
            print('6: W5 currently off the board')
        elif self.piece5.complete != True:
            print('6: W5', self.piece5.position.position)
        else:
            print('W5 has completed the race.')

        if self.piece56.position == self.bs_0:
            print('7: W6 currently off the board')
        elif self.piece56.complete != True:
            print('7: W6', self.piece56.position.position)
        else:
            print('W6 has completed the race.')

        move = '8'

        while move != '1' and move != '2' and move != '3' and move != '4' and move != '5' and move != '6' and move != '7':
            move = input('Which move do you wish to make? ')
            if move == '1':
                if self.piece0.complete == True:
                    move = '8'
            elif move == '2':
                if self.piece1.complete == True:
                    move = '8'
            elif move == '3':
                if self.piece2.complete == True:
                    move = '8'
            elif move == '4':
                if self.piece3.complete == True:
                    move = '8'
            elif move == '5':
                if self.piece4.complete == True:
                    move = '8'
            elif move == '6':
                if self.piece5.complete == True:
                    move = '8'
            elif move == '7':
                if self.piece56.complete == True:
                    move = '8'

        if move == '1':
            if self.piece0.can_move(roll):
                if self.piece0.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()
        elif move == '2':
            if self.piece1.can_move(roll):
                if self.piece1.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()
        elif move == '3':
            if self.piece2.can_move(roll):
                if self.piece2.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()
        elif move == '4':
            if self.piece3.can_move(roll):
                if self.piece3.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()
        elif move == '5':
            if self.piece4.can_move(roll):
                if self.piece4.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()
        elif move == '6':
            if self.piece5.can_move(roll):
                if self.piece5.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()
        elif move == '7':
            if self.piece56.can_move(roll):
                if self.piece56.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.white_turn()


    def black_turn(self):
        #used this for the black pieces turn

        roll = self.roll_d4_dice()
        print("You rolled", roll)

        if self.piece6.position == self.bs_0:
            print('1: B0 currently off the board')
        elif self.piece6.complete != True:
            print('1: B0', self.piece6.position.position)
        else:
            print('B0 has completed the race.')

        if self.piece7.position == self.bs_0:
            print('2: B1 currently off the board')
        elif self.piece7.complete != True:
            print('2: B1', self.piece7.position.position)
        else:
            print('B1 has completed the race.')

        if self.piece8.position == self.bs_0:
            print('3: B2 currently off the board')
        elif self.piece8.complete != True:
            print('3: B2', self.piece8.position.position)
        else:
            print('B2 has completed the race.')

        if self.piece9.position == self.bs_0:
            print('4: B3 currently off the board')
        elif self.piece9.complete != True:
            print('4: B3', self.piece9.position.position)
        else:
            print('B3 has completed the race.')

        if self.piece10.position == self.bs_0:
            print('5: B4 currently off the board')
        elif self.piece10.complete != True:
            print('5: B4', self.piece10.position.position)
        else:
            print('B4 has completed the race.')

        if self.piece11.position == self.bs_0:
            print('6: B5 currently off the board')
        elif self.piece11.complete != True:
            print('6: B5', self.piece11.position.position)
        else:
            print('B5 has completed the race.')

        if self.piece12.position == self.bs_0:
            print('7: B6 currently off the board')
        elif self.piece12.complete != True:
            print('7: B6', self.piece12.position.position)
        else:
            print('B6 has completed the race.')

        move = '8'

        while move != '1' and move != '2' and move != '3' and move != '4' and move != '5' and move != '6' and move != '7':
            move = input('Which move do you wish to make? ')
            if move == '1':
                if self.piece6.complete == True:
                    move = '8'
            elif move == '2':
                if self.piece7.complete == True:
                    move = '8'
            elif move == '3':
                if self.piece8.complete == True:
                    move = '8'
            elif move == '4':
                if self.piece9.complete == True:
                    move = '8'
            elif move == '5':
                if self.piece10.complete == True:
                    move = '8'
            elif move == '6':
                if self.piece11.complete == True:
                    move = '8'
            elif move == '7':
                if self.piece12.complete == True:
                    move = '8'

        if move == '1':
            if self.piece6.can_move(roll):
                if self.piece6.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()
        elif move == '2':
            if self.piece7.can_move(roll):
                if self.piece7.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()
        elif move == '3':
            if self.piece8.can_move(roll):
                if self.piece8.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()
        elif move == '4':
            if self.piece9.can_move(roll):
                if self.piece9.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()
        elif move == '5':
            if self.piece10.can_move(roll):
                if self.piece10.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()
        elif move == '6':
            if self.piece11.can_move(roll):
                if self.piece11.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()
        elif move == '7':
            if self.piece12.can_move(roll):
                if self.piece12.position.rosette == True:
                    self.display_board()
                    print("You have landed on a rosette, go again")
                    return self.black_turn()

    def set_board(self):
        #this functionis used to have pieces that were knocked off, return to the start position
        #also to help with pieces that were finished with the race

        count = 0
        for i in self.list_pieces:
            for j in self.list_boardsquares:
                if j.piece == None:
                    count += 1
                elif i != j.piece:
                    count += 1
            if count == 23 and i.complete != True:
                i.position = self.bs_0
            count = 0

        for i in self.list_pieces:
            for j in self.list_boardsquares:
                if i.complete == True:
                    if j.piece == i:
                        j.piece = None

    def start_game(self):
#start game function
        self.name = input('Player 1, what is ur name? ')
        print('You will play as white.')
        self.name2 = input('Player 2, what is ur name? ')
        print('You will play as black.')

    def check_winner(self):
        # I used this function to help check to see if one player won, and return either true or false
        count = 0
        for i in self.list_pieces[0:7]:
            if i.complete == True:
                count += 1
        if count == 7:
            print(self.name,'won!')
            return True


        count2 = 0
        for i in self.list_pieces[7:14]:
            if i.complete == True:
                count2 += 1
        if count2 == 7:
            print(self.name2,'won!')
            return True
        else:
            return False


    def play_game(self):


        self.start_game()
        self.set_game()
        end_game = False
        while end_game == False:
            self.display_board()
            self.set_board()
            self.white_turn()
            self.set_board()
            end_game = self.check_winner()
            if end_game == False:
                self.display_board()
                self.set_board()
                self.black_turn()
                self.set_board()
                end_game = self.check_winner()


WHITE = 'white'
BLACK = 'black'
if __name__ == '__main__':
    file_name = input('What is the file name of the board json? ') if len(argv) < 2 else argv[1]
    rgu = RoyalGameOfUr(file_name)
    rgu.play_game()



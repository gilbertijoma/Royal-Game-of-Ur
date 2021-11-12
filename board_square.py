"""
File: board_square.py
Gilbert Ijoma
Date: 11/13/2020
The royal game of ur, class UrPiece with can_move function, class BoardSquare.
"""
class UrPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol

    def can_move(self, num_moves):
        #this checks board conditions to see if the piece can move, if so it will move also in this function
        if num_moves == 0:
            return False

        if self.color == 'white':
            if num_moves == 1:
                if self.position.next_white.position == (-2, -2):
                    self.complete = True
                if self.position.next_white.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_white.piece = self
                    self.position = self.position.next_white
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_white.piece.color == self.color:
                    return False
                else:
                    if self.position.next_white.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_white.piece = self
                        self.position = self.position.next_white
                        print("You have kicked the other players piece")
                        return True

            elif num_moves == 2:
                if self.position.next_white.next_white.position == (-2, -2):
                    self.complete = True
                if self.position.next_white.next_white.exit == True:
                    return False
                if self.position.next_white.next_white.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_white.next_white.piece = self
                    self.position = self.position.next_white.next_white
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_white.next_white.piece.color == self.color:
                    return False
                else:
                    if self.position.next_white.next_white.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_white.next_white.piece = self
                        self.position = self.position.next_white.next_white
                        print("You have kicked the other players piece")
                        return True

            elif num_moves == 3:
                if self.position.next_white.next_white.next_white.position == (-2, -2):
                    self.complete = True
                if self.position.next_white.next_white.next_white.exit == True:
                    return False
                if self.position.next_white.next_white.next_white.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_white.next_white.next_white.piece = self
                    self.position = self.position.next_white.next_white.next_white
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_white.next_white.next_white.piece.color == self.color:
                    return False
                else:
                    if self.position.next_white.next_white.next_white.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_white.next_white.next_white.piece = self
                        self.position = self.position.next_white.next_white.next_white
                        print("You have kicked the other players piece")
                        return True

            elif num_moves == 4:
                if self.position.next_white.next_white.next_white.next_white.position == (-2, -2):
                    self.complete = True
                if self.position.next_white.next_white.next_white.next_white.exit == True:
                    return False
                if self.position.next_white.next_white.next_white.next_white.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_white.next_white.next_white.next_white.piece = self
                    self.position = self.position.next_white.next_white.next_white.next_white
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_white.next_white.next_white.next_white.piece.color == self.color:
                    return False
                else:
                    if self.position.next_white.next_white.next_white.next_white.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_white.next_white.next_white.next_white.piece = self
                        self.position = self.position.next_white.next_white.next_white.next_white
                        print("You have kicked the other players piece")
                        return True

        if self.color == 'black':
            if num_moves == 1:
                if self.position.next_black.position == (-2, -2):
                    self.complete = True
                if self.position.next_black.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_black.piece = self
                    self.position = self.position.next_black
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_black.piece.color == self.color:
                    return False
                else:
                    if self.position.next_black.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_black.piece = self
                        self.position = self.position.next_black
                        print("You have kicked the other players piece")
                        return True

            elif num_moves == 2:
                if self.position.next_black.next_black.position == (-2, -2):
                    self.complete = True
                if self.position.next_black.next_black.exit == True:
                    return False
                if self.position.next_black.next_black.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_black.next_black.piece = self
                    self.position = self.position.next_black.next_black
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_black.next_black.piece.color == self.color:
                    return False
                else:
                    if self.position.next_black.next_black.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_black.next_black.piece = self
                        self.position = self.position.next_black.next_black
                        print("You have kicked the other players piece")
                        return True

            elif num_moves == 3:
                if self.position.next_black.next_black.next_black.position == (-2, -2):
                    self.complete = True
                if self.position.next_black.next_black.next_black.exit == True:
                    return False
                if self.position.next_black.next_black.next_black.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_black.next_black.next_black.piece = self
                    self.position = self.position.next_black.next_black.next_black
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_black.next_black.next_black.piece.color == self.color:
                    return False
                else:
                    if self.position.next_black.next_black.next_black.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_black.next_black.next_black.piece = self
                        self.position = self.position.next_black.next_black.next_black
                        print("You have kicked the other players piece")
                        return True

            elif num_moves == 4:
                if self.position.next_black.next_black.next_black.next_black.position == (-2, -2):
                    self.complete = True
                if self.position.next_black.next_black.next_black.next_black.exit == True:
                    return False
                if self.position.next_black.next_black.next_black.next_black.piece == None:
                    self.position.piece = None
                    if self.complete != True:
                        self.position.next_black.next_black.next_black.next_black.piece = self
                    self.position = self.position.next_black.next_black.next_black.next_black
                    if self.complete == True:
                        self.position.piece = None
                    return True
                elif self.position.next_black.next_black.next_black.next_black.piece.color == self.color:
                    return False
                else:
                    if self.position.next_black.next_black.next_black.next_black.rosette:
                        return False
                    else:
                        self.position.piece = None
                        self.position.next_black.next_black.next_black.next_black.piece = self
                        self.position = self.position.next_black.next_black.next_black.next_black
                        print("You have kicked the other players piece")
                        return True

class BoardSquare:
    def __init__(self, x, y, entrance=False, _exit=False, rosette=False, forbidden=False):
        self.piece = None
        self.position = (x, y)
        self.next_white = None
        self.next_black = None
        self.exit = _exit
        self.entrance = entrance
        self.rosette = rosette
        self.forbidden = forbidden

    def load_from_json(self, json_string):
        import json
        loaded_position = json.loads(json_string)
        self.piece = None
        self.position = loaded_position['position']
        self.next_white = loaded_position['next_white']
        self.next_black = loaded_position['next_black']
        self.exit = loaded_position['exit']
        self.entrance = loaded_position['entrance']
        self.rosette = loaded_position['rosette']
        self.forbidden = loaded_position['forbidden']

    def jsonify(self):
        next_white = self.next_white.position if self.next_white else None
        next_black = self.next_black.position if self.next_black else None
        return {'position': self.position, 'next_white': next_white, 'next_black': next_black, 'exit': self.exit, 'entrance': self.entrance, 'rosette': self.rosette, 'forbidden': self.forbidden}

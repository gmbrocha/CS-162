# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 11/21/2022
# Description: Text based Mancala game that utilizes 3 classes: class Player which defines player objects containing
#              the names of the players one and two; class Node which is utilized to create Node objects representing
#              'pits' or 'stores' that will become both a linked list (for looping during play_game() method) and a
#              typical list for easy referencing; class Mancala defines the main game objects that contain a text
#              'mancala board' and provides methods to add players to the object, to print the board state and score,
#              to check for win conditions and display winners (or ties) on that condition; the last method in class
#              Mancala does most of the work - it takes a player and a position (pit #) as an argument and 'plays' the
#              game according to the rules mancala_rules.pdf in the repository (this includes 2 special conditions) -
#              it then returns the board state (seed #s in pits and stores) as a typical list. FINAL PROJECT


class Player:
    """defines creation of Player objects with private data member name - passed as a string"""

    def __init__(self, name):
        """instantiates Player objects"""
        self._name = name

    def get_name(self):
        """returns private data member name (string)"""
        return self._name


class Node:
    """defines the creation of Node objects by class Mancala to form both a linked list and typical list; private data
    members: seeds - current integer, ind - index for some referencing, next - references next Node in linked list"""

    def __init__(self, ind):
        """initializes linked list Node objects"""
        self._seeds = 4
        self._ind = ind
        self._next = None

    def get_seeds(self):
        """returns private data member seeds"""
        return self._seeds

    def get_ind(self):
        """returns private data member Node index"""
        return self._ind

    def get_next(self):
        """returns private data member next - holds next Node object in the linked list"""
        return self._next

    def set_seeds(self, val):
        """sets private data member seeds to reflect the value passed as an argument"""
        self._seeds = val

    def set_next(self, next_):
        """sets private data member next (Node object in linked list) for Node"""
        self._next = next_


class Mancala:
    """defines creation of Mancala objects that represent a game played by 2 players. These objects that will both
    contain a linked list of Node objects (for easy looping from the last object to the head) and well as a typical list
    of those same Node objects for easy indexing - these lists represent the board to be played on; provides methods to
    set up the Mancala board, to create players one and two, to print the board (current state), to check and return a
    winner (or announce tie) if the game has completed; the final method play_game() uses Mancala rules to adjust pits
    and stores and returns a list of current state after each play"""

    def __init__(self):
        """instantiates Mancala objects with private data members: player one, player two - which will hold string names
        ; head of the linked list of Nodes; Node list as typical py list; and sets up the board"""

        self._player_one = None
        self._player_two = None
        self._head = None
        self._nodes_list = []
        self.setup_board()

    def setup_board(self, index=0, curr=None):
        """sets up a linked list of Node objects for easy looping from last object to first object, and also appends
        them to a typical list for easy indexing"""

        if self._head is None:
            self._head = Node(index)  # set head, THIS LINKED LIST IS JUST TO MAKE EASY LOOPING FROM LAST ---> FIRST
            self._nodes_list.append(self._head)  # append to a typical list for easy indexing
        if curr is None:
            curr = self._head  # begin the linked list with head Node
        if curr.get_next() is not None:  # if the next parameter is not None we will have arrived back at head Node
            return
        elif curr.get_next() is None:
            curr.set_next(Node(index + 1))  # set ._next to a Node object creation call
            self._nodes_list.append(curr.get_next())  # append that immediately to the typical list
            if index == 6:
                curr.set_seeds(0)
            elif index == 13:
                curr.set_seeds(0)
                curr.set_next(self._head)
            self.setup_board(index + 1, curr.get_next())

    def create_player(self, name):
        """create Player objects for the Mancala game"""

        if self._player_one is None:
            self._player_one = (Player(name))
            return self._player_one
        elif self._player_two is None:
            self._player_two = (Player(name))
            return self._player_two
        elif self._player_two is not None:  # if player_two already contains a player, return error message
            return "players 1 and 2 already defined"

    def print_board(self):
        """print the current state of the game to the console including player #, store value for player #, pits 1-6 for
        player #"""

        print("player1:")
        print("store: " + str(self._nodes_list[6].get_seeds()))  # get seeds from store 1 and concatenate for display
        temp_list = []
        for n in range(0, 6):
            temp_list.append(self._nodes_list[n].get_seeds())  # append player 1 pits to temp_list and display
        print(temp_list)
        print("player2: ")
        print("store: " + str(self._nodes_list[13].get_seeds()))  # get seeds from store 2 and concatenate for display
        temp_list.clear()
        for n in range(7, 13):
            temp_list.append(self._nodes_list[n].get_seeds())  # append player 2 pits to temp_list and display
        print(temp_list)

    def return_winner(self):
        """method checks whether game has ended, and if so returns which player has won including the player name, or
        if the game outcome is a tie"""

        count1, count2 = self.split_count()
        if count1 != 0 and count2 != 0:  # if neither sublist (player 1 or 2 pits) sum is 0, return game not ended
            return "Game has not ended"
        store1, store2 = self._nodes_list[6], self._nodes_list[13]
        if store1.get_seeds() > store2.get_seeds():  # block of conditionals to display winner or tie
            return "Winner is player 1: " + self._player_one.get_name()
        elif store2.get_seeds() > store1.get_seeds():
            return "Winner is player 2: " + self._player_two.get_name()
        elif store1.get_seeds() == store2.get_seeds():
            return "It's a tie"

    def split_count(self):
        """method utilized by other methods to quickly sum both player 1 and player 2 pits and return those values"""

        count1, count2 = 0, 0
        for n in range(0, 6):  # will sum player 1 pits (indices 0 to 5)
            count1 += self._nodes_list[n].get_seeds()
        for n in range(7, 13):  # will sum player 2 pits (indices 7 to 12)
            count2 += self._nodes_list[n].get_seeds()
        return count1, count2

    def update_end(self):
        """Takes no parameters, returns nothing; utilizes split count to get sums and checks each sum for zero; when
        zero found adds the other players sum to the store; then sets all pits for that player to zero"""

        count1, count2 = self.split_count()
        store1, store2 = self._nodes_list[6], self._nodes_list[13]
        if count1 == 0:  # if player 1 pits are zeroed, add up player 2 pits, set them to zero and add to store2
            store2.set_seeds(store2.get_seeds() + count2)
            for n in range(7, 13):
                self._nodes_list[n].set_seeds(0)
        elif count2 == 0:  # if player 2 pits are zeroed, add up player 1 pits, set them to zero and add to store1
            store1.set_seeds(store1.get_seeds() + count1)
            for n in range(0, 6):
                self._nodes_list[n].set_seeds(0)

    def play_game(self, player, pit):
        """Two parameters; method accepts a player number integer and a pit integer (1-6 per player); follows Mancala
        game rules to increment/decrement seed #s in each player's pits and stores, and checks for special case rules in
        mancala_rules.pdf in the repo"""

        if pit > 6 or pit <= 0:
            return "Invalid number for pit index"
        count1, count2 = self.split_count()  # set counts and check for game end state; if it's over return error
        if count1 == 0 or count2 == 0:
            return "Game is ended"
        else:  # potentially combine these 2? the conditionals for player 1 or 2
            if player == 1:

                def rec_seeds(curr=None, count=None):
                    """function used recursively to set pits and stores according to rules; default parameters curr will
                     hold a Node object, count will be set to the number of seeds in the ‘picked up’ pit"""

                    if count == 0:  # base case for recursion to end
                        return
                    if curr.get_ind() == 13:  # since player one, if current obj index is 13 (store 2), don't add seed
                        rec_seeds(curr.get_next(), count)  # NOT SURE if efficient at all but ***** this is the reason
                        # for the linked list .next values **** very easy to pass next object from the end of the list
                        # straight to the head of the list
                    else:
                        curr.set_seeds(curr.get_seeds() + 1)  # add a seed to current obj
                        if count == 1 and curr.get_seeds() - 1 == 0 and curr.get_ind() < 6:  # if count is 1
                            # (last recursion), and curr get_seeds - 1 == 0 (the pit was empty before last instruction)
                            # AND curr index < 6 (must be on player1's side) ---> THEN do the special rule below
                            curr.set_seeds(0)  # set current seeds to zero (will add 1 to mancala later)
                            self._nodes_list[6].set_seeds(self._nodes_list[6].get_seeds() +
                                                          self._nodes_list[12 - curr.get_ind()].get_seeds() + 1)
                            self._nodes_list[12 - curr.get_ind()].set_seeds(0)  # opposite object set to zero
                        if count == 1 and curr.get_ind() == 6:  # second special rule
                            print("Player 1 take another turn")
                        rec_seeds(curr.get_next(), count - 1)  # PUT SECOND RULE ABOVE OTHER

                seeds = self._nodes_list[pit - 1].get_seeds()  # temp store seeds in pit - 1
                self._nodes_list[pit - 1].set_seeds(0)  # then set seeds in pit - 1 to zero
                current = self._nodes_list[pit]  # set current to pit
                rec_seeds(current, seeds)  # call recursive function
            if player == 2:

                def rec_seeds(curr=None, count=None):
                    """function used recursively to set pits and stores according to rules; default parameters curr will
                    hold a Node object, count will be set to the number of seeds in the ‘picked up’ pit"""

                    if count == 0:
                        return
                    if curr.get_ind() == 6:  # since player two, if current obj index is 6 (store 1), don't add seed
                        rec_seeds(curr.get_next(), count)
                    else:
                        curr.set_seeds(curr.get_seeds() + 1)  # add seed to current obj
                        if count == 1 and curr.get_seeds() - 1 == 0 and curr.get_ind() > 6 \
                                and not curr.get_ind() == 13:  # if count = 1 (last recursion) AND curr.get_seeds - 1
                            # (pit was empty prior to last instruction) AND curr index > 6 but not 13 (store 2) ------>
                            # THEN apply special rule below
                            curr.set_seeds(0)  # set current seeds to zero (will add 1 to mancala later)
                            opp = curr.get_ind() - (curr.get_ind() - 6) * 2  # get the opposite side index
                            self._nodes_list[13].set_seeds(self._nodes_list[13].get_seeds() +
                                                           self._nodes_list[opp].get_seeds() + 1)
                            self._nodes_list[opp].set_seeds(0)  # opp set to zero
                        if count == 1 and curr.get_ind() == 13:  # second special rule
                            print("Player 2 take another turn")
                        rec_seeds(curr.get_next(), count - 1)

                seeds = self._nodes_list[pit + 6].get_seeds()
                self._nodes_list[pit + 6].set_seeds(0)
                current = self._nodes_list[pit + 7]
                rec_seeds(current, seeds)
            count1, count2 = self.split_count()  # set counts and if either 0, end game is reached
            if count1 == 0 or count2 == 0:
                self.update_end()  # end state update the board to all zeroes, add to stores
            temp_list = []  # create temp list and fill with current pit and store values; return the list
            for n in range(0, 14):
                temp_list.append(self._nodes_list[n].get_seeds())
            return temp_list

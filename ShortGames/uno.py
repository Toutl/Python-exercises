# By Toutl

from os import system
import random

system("cls")


class Card:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

    def __str__(self):
        return f'{self.colour} {self.type}'


class Deck:
    def __init__(self):
        colours = ['red', 'yellow', 'green', 'blue']
        types = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                 'seven', 'eight', 'nine', 'skip', 'draw two', 'reverse',]
        self.cards = [Card(type, colour) for colour in colours
                      for type in types] * 2
        self.cards.extend([Card(type, 'wild')
                           for type in ['jocker', 'draw four']] * 4)

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt


class Player:
    def __init__(self, order):
        self.cards = []
        self.order = order
        self.name = None

    def __str__(self):
        return f"This is {self.name}, is {self.order}"

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def get_name(self):
        if self.name is None:
            self.name = input(f"You're player {self.order}\n"
                              "What is your name? ")
            system("cls")

    def display(self):
        print("Your hand:")
        for index, card in enumerate(self.cards):
            print(f"{index + 1:2}: {card}")
        print("")


class Game:
    def __init__(self):
        self.winner = False
        self.players = []
        self.deck = Deck()
        self.last_card = None

    def play(self):
        number_players = int(input("How many people want to play? "))
        system("cls")

        self.deck.shuffle()

        self.players = [Player(order)
                        for order in range(1, number_players + 1)]
        for player in self.players:
            player.add_card(self.deck.deal(7))

        self.last_card = self.deck.deal(1)[0]

        while not self.winner:
            for player in self.players:
                self.turn(player)
                system("cls")

            for i in range(3):
                print(i)
                if i == 2:
                    self.winner = True

        print("end")

    def turn(self, player):
        player.get_name()

        print()
        print('*' * 30)
        print(f"Turn of {player.name}")
        print('*' * 30)
        input("")

        print(f"Last discarded card: {self.last_card}\n")
        player.display()

        card_played = player.cards[int(input("\nWhat card do you want to play?"
                                             " (enter the number): ")) - 1]
        if card_played.type == self.last_card.type or \
           card_played.colour == self.last_card.colour:
            self.last_card = card_played
            player.cards.remove(card_played)
        # TODO: Make sure you can only play allowed cards
        # TODO: Add the get from deck if you don't want to play your card.
        #       Do it the zero option

        if not player.cards:
            self.winner = player
        # player.add_card(self.deck.deal(1))

        input("")


g = Game()
g.play()

"""
p = Player()
p.add_card()
print(*p.cards, sep='')

    # print(*player.cards, sep=', ')
"""

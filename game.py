from deck import Deck
from hand import Hand

class Game:

    PLAYING = "playing"
    BUSTED = "player_busted"
    GAMEOVER = "game_over"
    DEALER_WIN = "dealer_win"
    TIE = "tie"
    PLAYER_WIN = "player_win"

    def __init__(self):
        self.state = Game.PLAYING
        self.result = None

    def start_game(self):
        self.state = Game.PLAYING
        self.result = None
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

        for _ in range(2):
            self.player_hand.add_card(self.deck.deal(1))
            self.dealer_hand.add_card(self.deck.deal(1))

        if self.player_hand.is_blackjack():
            if self.dealer_hand.is_blackjack():
                self.result = Game.TIE
                self.state = Game.GAMEOVER
            else:
                self.result = Game.PLAYER_WIN
                self.state = Game.GAMEOVER
        elif self.dealer_hand.is_blackjack():
            self.result = Game.DEALER_WIN
            self.state = Game.GAMEOVER

    #check if the player busted when take a new card
    def player_busted(self):
        return self.player_hand.get_value() > 21

    #function for take another card
    def player_hit(self):
        if self.state != Game.PLAYING:
            return

        self.player_hand.add_card(self.deck.deal(1))

        if self.player_busted():
            self.result = Game.DEALER_WIN
            self.state = Game.GAMEOVER

    def dealer_busted(self):
        return self.dealer_hand.get_value() > 21

    def dealer_turn(self):
        if self.state != Game.PLAYING or self.result:
            return
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal(1))

            if self.dealer_busted():
                self.result = Game.PLAYER_WIN
                self.state = Game.GAMEOVER
                return

        self.state = Game.GAMEOVER
        self.check_winner()

    def check_winner(self):
        if self.state != Game.PLAYING:
            return
        player = self.player_hand.get_value()
        dealer = self.dealer_hand.get_value()

        if player == dealer:
            self.result = Game.TIE
        elif player > dealer:
            self.result = Game.PLAYER_WIN
        else:
            self.result = Game.DEALER_WIN


    def get_player_cards(self):
        return [str(card) for card in self.player_hand.cards]

    def get_dealer_cards(self):
        return [str(card) for card in self.dealer_hand.cards]

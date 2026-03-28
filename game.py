
from deck import Deck
from hand import Hand

class Game:

    def start_game(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

        for _ in range(2):
            self.player_hand.add_card(self.deck.deal(1))
            self.dealer_hand.add_card(self.deck.deal(1))

    def player_hit(self):
        if self.player_hand.get_value() < 21:
            self.player_hand.add_card(self.deck.deal(1))

    def dealer_turn(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal(1))


    def check_winner(self, game_over= False):
        if not game_over:
            if self.player_hand.get_value() >21:
                return "Gano el dealer"
                #return True
            elif self.dealer_hand.get_value() >21:
                return "Ganaste"
            elif self.dealer_hand.is_blackjack() and self.player_hand.is_blackjack():
                return "Empate"
            elif self.dealer_hand.is_blackjack():
                return "Gano el dealer"
        else:
            if self.player_hand.get_value() > self.dealer_hand.get_value():
                return "Ganaste"
            elif self.player_hand.get_value() == self.dealer_hand.get_value():
               return "Empate"
            else:
                return "Gano el dealer"
        return "Ganaste"

    def get_player_cards(self):
        return [str(card) for card in self.player_hand.cards]

    def get_dealer_cards(self):
        return [str(card) for card in self.dealer_hand.cards]

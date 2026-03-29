from flask import Flask, render_template, redirect

from game import Game

app = Flask(__name__)

game = Game()
game.start_game()

@app.route("/")
def home():

    player_cards = game.get_player_cards()
    dealer_cards = game.get_dealer_cards()
    winner = game.result

    return render_template(
        "index.html",
        player_cards=player_cards,
        dealer_cards=dealer_cards,
        winner=winner
    )

@app.route("/hit", methods=["POST"])
def hit():
    game.player_hit()
    return redirect("/")

@app.route("/stand", methods=["POST"])
def stand():
    game.dealer_turn()
    return redirect("/")

@app.route("/restart", methods=["POST"])
def restart():
    game.start_game()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

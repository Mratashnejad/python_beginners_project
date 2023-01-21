
def FinalScore():
    global bank, bet

    # different win conditions
    # pays the player their original bet * 2

    if player_score == dealer_score and player_score <= 21:
        print("It's a tie!")
        bank = bank + bet
        print("You currently have $",bank,"left.")
        Restart()
    elif player_score > 21:
        print("You lost!")
        print("You currently have $",bank,"left.")
        Restart()
    elif player_score < 21 and dealer_score > player_score:
        print("You lost!")
        print("You currently have $",bank,"left.")
        Restart()
    elif player_score > dealer_score and player_score <= 21:
        print("You win!")
        bank = bet + bet + bank
        print("You currently have $",bank,"left.")
        Restart()
    elif dealer_score > 21 and player_score <= 21:
        print("You win!")
        bank = bet + bet + bank
        print("You currently have $",bank,"left.")
        Restart()

FinalScore()

# blackjack.py
This is a blackjack python game that I have built from scratch. You are playing agianst the dealer. It doesn't exactly follow Blackjack guidelines. But it is somewhat close.
It is a modified version.

You will be asked if you want to play.
If yes, you will be asked the amount of money you want to gamble at the table.
You will then be asked how much money you would like to bet on the current round.

The deck is shuffled and you are given two cards and the dealer is given two cards.
You will see your cards and one of the dealers card (The other is hidden)

You will be asked if you want to hit or stand.
If you hit and are still under 21, you can hit or stand again.
If you hit and hit 21, you get blackjack.
If you hit and go over 21, you bust and lose.

Once you decide to stand, the dealer will then make their move (Dependant on your current state)
The dealer is almost a cheat code in this game as they compare their cards to your cards after you decide to stand.
They will only hit if their total amount of cards is less than yours. Otherwise, they will stand and most likely win.

If you win that round, the amount you gambled for the round is doubled and given back to you.
If you lose that round, the amount you gambled for the round is subtracted from your total.
You can continue to play as long as you have more than $0 dollars to your name.

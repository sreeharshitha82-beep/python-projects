import random
import sys

HEARTS = '♥'
DIAMONDS = '♦'
SPADES = '♠'
CLUBS = '♣'
BACK = 'back'


def main():
    print('''Blackjack

Try to get as close to 21 as possible without going over.

J, Q, K = 10
A = 1 or 11
2-10 = face value

H = Hit
S = Stand
D = Double down
''')

    money = 5000

    while True:
        if money <= 0:
            print("You're out of money!")
            print("Thanks for playing!")
            sys.exit()

        print('Money:', money)
        bet = get_bet(money)

        deck = get_deck()
        dealer = [deck.pop(), deck.pop()]
        player = [deck.pop(), deck.pop()]

        print('Bet:', bet)

        while True:
            display_hands(player, dealer, False)
            print()

            if get_value(player) > 21:
                break

            move = get_move(player, money - bet)

            if move == 'D':
                extra = get_bet(min(bet, money - bet))
                bet += extra
                print('Your bet is now:', bet)

            if move in ('H', 'D'):
                card = deck.pop()
                print('You got the {} of {}.'.format(card[0], card[1]))
                player.append(card)

                if get_value(player) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if get_value(player) <= 21:
            while get_value(dealer) < 17:
                print('Dealer hits...')
                dealer.append(deck.pop())
                display_hands(player, dealer, False)

                if get_value(dealer) > 21:
                    break

                input('Press Enter to continue...')
                print()

        display_hands(player, dealer, True)

        player_value = get_value(player)
        dealer_value = get_value(dealer)

        if dealer_value > 21:
            print('Dealer busts! You win ${}.'.format(bet))
            money += bet

        elif player_value > 21 or player_value < dealer_value:
            print('You lost ${}.'.format(bet))
            money -= bet

        elif player_value > dealer_value:
            print('You won ${}!'.format(bet))
            money += bet

        else:
            print("It's a tie. Your bet is returned.")

        input('Press Enter to continue...')
        print('\n')


def get_bet(max_bet):
    while True:
        print('How much do you want to bet? (1-{}, or QUIT)'.format(max_bet))
        bet = input('> ').upper().strip()

        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if bet.isdecimal():
            bet = int(bet)

            if 1 <= bet <= max_bet:
                return bet


def get_deck():
    deck = []

    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))

        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))

    random.shuffle(deck)
    return deck


def display_hands(player, dealer, show_dealer):
    print()

    if show_dealer:
        print('DEALER:', get_value(dealer))
        display_cards(dealer)
    else:
        print('DEALER: ???')
        display_cards([BACK] + dealer[1:])

    print('PLAYER:', get_value(player))
    display_cards(player)


def get_value(cards):
    value = 0
    aces = 0

    for card in cards:
        rank = card[0]

        if rank == 'A':
            aces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    value += aces

    for i in range(aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    rows = ['', '', '', '', '']

    for card in cards:
        rows[0] += ' ___  '

        if card == BACK:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def get_move(player, money):
    while True:
        options = ['(H)it', '(S)tand']

        if len(player) == 2 and money > 0:
            options.append('(D)ouble down')

        prompt = ', '.join(options) + ': '
        move = input(prompt).upper()

        if move in ('H', 'S'):
            return move

        if move == 'D' and '(D)ouble down' in options:
            return move


if __name__ == '__main__':
    main()
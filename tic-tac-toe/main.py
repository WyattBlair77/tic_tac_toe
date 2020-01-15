from board import Board

state_initial = [[None, None, None],[None, None, None],[None, None, None]]
done = False
Game = Board(state_initial)

while not done:

    Game.game_loop()
    again = ''

    while again.lower() != 'y' and again.lower() != 'n':
        print()
        again = input('Play again? [y/n]: ')
        print()

    if again.lower() == "n":
        done = True

    Game.state = Game.initial_state



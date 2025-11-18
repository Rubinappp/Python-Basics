# create a game function and return a score..Read a file which
# contains previous high score .write a program to update 
#the highscore whenever game() breaks the highscore
def game():
    return 64
score=game()
with open("highscore.txt") as f:
    highscore=int(f.read())
if highscore<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))


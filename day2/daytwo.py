class Game():
    id = 0
    listOfThrow = []

gameRules =  {
    "red": 12,
    "green": 13,
    "blue": 14
}
idSum = 0
f = open('input.csv', encoding="utf-8")
for line in f:
    game = Game()
    game.id = line.split(':')[0].split(' ')[1]
    game.listOfThrow = line.split(':')[1].split(';')
    throwOk = True
    for throw in game.listOfThrow:
        throw_dict = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for cube in throw.split(','):

            color = cube.split(' ')[2]
            number = cube.split(' ')[1]
            throw_dict.update({color: number})
        for color in list(gameRules.keys()):
            throwOk = throwOk and (int(throw_dict.get(color)) <= gameRules.get(color))
    print("game:" + game.id + " is " + str(throwOk))
    if (throwOk):
        print(str(idSum) + " + " + game.id)
        idSum = idSum + int(game.id)
        
print(idSum)
        
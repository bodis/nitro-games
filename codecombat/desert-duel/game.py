
tesztVariable = "asdasdasd"
defendedLane = -1

while True:
    defend()
    attack()

def defend():
    protectCastQuickSand()
    defendLane()

def attack():
    if castToThrow3Points('charger'):
        return
    elif sendSniperAfterBig():
        return
    sendAttackTeam()

def castToThrow3Points(playerType):
    c = findMyFurthestPlayerOnLane(1, playerType)
    if c is not None and c.x > 60 and c.x < 66:
        print('cast HOT on lane 1 for ' + playerType)
        hero.play('hot', 1)
        return True
    c = findMyFurthestPlayerOnLane(2, playerType)
    if c is not None and c.x > 60 and c.x < 66:
        print('cast HOT on lane 2 for ' + playerType)
        hero.play('hot', 1)
        return True
    c = findMyFurthestPlayerOnLane(0, playerType)
    if c is not None and c.x > 50 and c.x < 56:
        print('cast HOT on lane 0 for ' + playerType)
        hero.play('hot', 0)
        return True
    return False


def sendSniperAfterBig():
    c = findMyFurthestPlayerOnLane(1, 'big')
    if c is not None and c.x > 60 and c.health >= 30:
        print('send sniper after big on line 1')
        hero.summon('sniper', 1)
        return True
    c = findMyFurthestPlayerOnLane(2, 'big')
    if c is not None and c.x > 60 and c.health >= 30:
        print('send sniper after big on line 2')
        hero.summon('sniper', 2)
        return True
    c = findMyFurthestPlayerOnLane(0, 'big')
    if c is not None and c.x > 50 and c.health >= 30:
        print('send sniper after big on line 0')
        hero.summon('sniper', 0)
        return True
    return False

def findAllByType(playerType):
    return countType(hero.findMyPlayers(0)) + countType(hero.findMyPlayers(1)) + countType(hero.findMyPlayers(1))

def countType(players, playerType):
    count = 0
    for player in players:
        if player.type == playerType:
            count = count+1
    return count

def sendAttackTeam():
    if findAllByType('charger') == 3 and findAllByType('threat') == 3:
        hero.summon('big', 1)
    else:
        hero.summon('charger', 2)
        hero.summon('threat', 0)




def defendLane():
    print("goliath is ready " + hero.isReady("goliath"))
    if not hero.isReady("goliath"):
        return


    if defendedLane > -1:
        defender = findMyFurthestPlayer(defendedLane, "big")
        if defender == None:
            defendedLane = -1

    if defendedLane is not None:
        defendedLane = findLaneWithPlayersLessThan(0)
        if (defendedLane > -1):
            print("startDefendLane: " + defendedLane)
            hero.summon("big", defendedLane)
            hero.play("goliath")

def findLaneWithPlayersLessThan(threshold):
    if len(hero.findMyPlayers(0)) <= threshold:
        return 0
    elif len(hero.findMyPlayers(1)) <= threshold:
        return 1
    elif len(hero.findMyPlayers(2)) <= threshold:
        return 2
    return -1

def findMyFurthestPlayerOnLane(lane, playerType):
    players = hero.findMyPlayers(lane)
    p = None
    pos = -1
    for player in players:
        if pos<player.x:
            if playerType == None or player.type == playerType:
                p = player
                pos = player.x
    return p


def protectCastQuickSand():
    targetLane = getLongestOpponentLaneSize(3);
    if hero.isReady("quicksand") and targetLane>-1:
        print("QUICKSAND!!!! lane: " + targetLane);
        hero.play("quicksand", targetLane);


def getLongestOpponentLaneSize(threshold):
    lane0 = len(hero.findTheirPlayers(0));
    lane1 = len(hero.findTheirPlayers(1));
    lane2 = len(hero.findTheirPlayers(2));
    max = max([lane0, lane1, lane2]);
    if max < threshold:
        return -1;
    elif max == lane0:
        return 0
    elif max == lane1:
        return 1
    elif max == lane2:
        return 2
    else:
        return -1


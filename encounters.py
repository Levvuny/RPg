import pandas as pd
import random
import requests
import time
import combat

EnemySheet = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1_Ym0miRRwRvT6j0cTkbwEgiiZ9GImDkJqhR7OAw33R8/values/Sheet1?key=AIzaSyB5DWWVzSER7OpXYIFVuhq0KysBzQocy7U")

EnemySheet = EnemySheet.json()

EnemyInfo = pd.DataFrame(EnemySheet["values"], columns=EnemySheet["values"][0])
EnemyInfo.drop(index=0, inplace=True)

monsterNames = []

for x in EnemyInfo["Name"]:
    monsterNames.append(x)


def encounter_decider(player, enemy, game):
    encounter_list = [old_man, short_rest, sunny_road, damaged_bridge_encounter]
    random.shuffle(encounter_list)
    return encounter_list[0](player, enemy, game)


def d20():  # a basic d20 that also tells for critical fails/successes.
    d20_roll = random.randint(1, 20)
    if d20_roll == 1:
        print("Critical fail!")
        return d20_roll
    elif d20_roll == 20:
        print("Critical success!")
        return d20_roll
    else:
        return d20_roll


def basic_dialogue(player, enemy, game):
    option = random.randint(1, 10)
    if option == 1:
        print("You see a squirrel run around an ancient oak tree.")
    elif option == 2:
        print("As you continue down the path, you stop at by a small well and fetch a drink and then continue")
        print("down your journey.")
    elif option == 3:
        print("As you walk down the worn path, you see a great forest full of life. You cannot even fathom all that")
        print("hides within those ancient trees. A blast of wind hits you and you watch as the trees dance to the beat")
        print("of the breeze.")
    elif option == 4:
        print("You sure are hungry, but you keep on going.")
    elif option == 5:
        print("A wild boar crosses your path. It looks at you with deep, unknowing eyes and slowly walks away.")
        if "boar" not in player.knownMonsters:
            player.knownMonsters.append("boar")
    elif option == 6:
        random_thing = ["your mother", "a lizard", "a... tree", "Greg"]
        random.shuffle(random_thing)
        print(f"You pass by a tree that kind of looks like {random_thing[0]}.")
    elif option == 7:
        vowels = ["a", "e", "i", "o", "u"]
        if enemy.name[0:1] in vowels:  # grammar is good
            grammar = "an"
        else:
            grammar = "a"
        print(f'You see {grammar} {enemy.name}. You named it John')



def lonely_inn():  # locations that player can revisit as they explore more of the world
    pass


def damaged_bridge_encounter(player, enemy, game):  # shows the bridge area and allows player to come back.
    if "bridge" in game.knowledge:
        return basic_dialogue(player, enemy, game)

    print("You come to a raging river that seems too terrifying to try to ford. You can see a relaxing meadow full of")
    print("fruit trees on the other side, but the bridge to it is far too damaged to cross. Maybe if you bring some")
    print("wood to fix it you can see the other side.")

    game.knowledge.append("bridge")

    return


def damaged_bridge(player, enemy, game):  # is only available till bridge is fixed
    options = ["repair", "gaze", "leave"]
    print("You return to the broken bridge. What do you want to do?")
    for i in options:
        print(i)
    answer = input().lower()
    while answer != "leave":

        if answer not in options:
            answer = input("Please put a valid option\n").lower()

        if answer == "gaze":
            print("You stare at where you want to be, but will you do anything to get there?")
            answer = input().lower()

        if answer == "repair":
            if player.inv["wood"] > 10:
                print("You spend the whole day fixing the bridge. It isn't the most beautiful work, but you")
                print("successfully repair the broken bridge and are able to access the other side.")

                game.knowledge.remove("bridge")
                game.knowledge.append("meadow")
                return

            else:
                print("You have the ambition, but not the resources. You should get some wood to repair it.")
                answer = input().lower()

    if answer == "leave":
        print("You leave the bridge. There's plenty of other places to go.")
        return


def meadow(player, enemy, game):
    print("You made it to the meadow.")


def stormy_night(player, enemy, game):
    pass


def fire_shrine(player, enemy, game):
    pass


def sunny_road(player, enemy, game):  # small events like this that just happen, small thing happens one or two options
    placeholder = enemy

    if random.randint(1, 20) + player.stat_ability["cha"] >= 11:
        print("The sun shines brightly down on you. What a lovely day.\n(+ 1 health)")
        if player.status["health"] < player.status["max_health"]:
            player.status["health"] += 1
    else:
        print("The sun is bright today.\n")


def smokey_camp(player, enemy, game):
    pass


def buried_house(player, enemy, game):  # lore areas
    pass


def short_rest(player, enemy, game):
    d20r = random.randint(1, 20)
    wisdom_roll = d20r + player.stat_ability["wis"]
    if d20r == 1:
        print("The journey has taken a toll on you and even rest seems hard to find. You try to find some comfort, but")
        print("it seems that the road calls to you without stopping. Abandoning your rest, you answer the call.")
        player.status["summonGreg"] += 1
        return

    if wisdom_roll >= 20:
        print("You find an old statue to lay down beside. The statue, ancient in making, is the form of one of the")
        print("ancient rulers of the land. Vines have overtaken much of the statue but you can still see a scowl on")
        print("on the face of the once king. One hand has fallen to the weather, but the remaining one points forward.")
        print("You wonder what the Frowning King was pursuing. Maybe they just made this statue on one of his bad days")
        time.sleep(3)
        print("As you get up to continue your journey, the statue continues to point towards the horizon forever more.")
        player.status["health"] = player.status["max_health"]
        game.knowledge.append("Frowning King")
        player.status["poison"] = 0
        return

    elif wisdom_roll == range(13, 20):
        print("You sit by a tree and take in the world around you. Sometimes part of the journey is enjoying the")
        print("little parts. You watch the ants as they scramble through the grass and wonder if anyone watches you")
        print("as you do the same.\n")
        if player.status["health"] < player.status["max_health"]:
            player.status["health"] += 1
        player.status["poison"] = 0
        time.sleep(3)
        print("After enjoying the scenery for a beautiful moment you decide the road is calling you yet again.")
        return

    elif wisdom_roll == range(5, 13):
        print("You rest for a short hour, contemplating the journey that you have had and the one that is to come.")
        print("You know you cannot relax for the long, though. The road calls.")
        return

    elif wisdom_roll > 5:
        print("As you lay down to relax, you accidentally stab yourself on a stick. Ow!")
        if player.status["health"] > 1:
            player.status["health"] -= 1
        return


def old_man(player, enemy, game):
    answer = input("You meet an old man resting by the side of the road. What do you do?\nApproach/Leave\n")
    answer = answer.lower()
    answers = ["approach", "leave"]
    while answer not in answers:
        print("Please put approach or leave.")
        answer = input().lower()

    if answer == "leave":
        print("")
        print("You share a glance with the man as you leave.")
        print("The quiet path has always been the one you favored.")
        time.sleep(0.5)
        print("And that's okay.")
        return

    if answer == "approach":
        d20r = random.randint(1, 20)
        if d20r > 17:
            print(f'You approach the man. The closer you get to him the more aged he seems.\nHe asks you to have some'
                  f' soup that looks slightly burnt. He seems to be eager to share his cooking.\nJoin/Decline')
            soup = input()
            soup = soup.lower()
            soups = ["join", "decline"]
            while soup not in soups:
                print("Please put join or decline.")
                soup = input().lower()

            if soup == "decline":
                print("You decide to stay on the safe side. After talking to the man for a time, you decide it's time")
                print("to continue your journey. As the old man fades into the distance, you focus on the path to your")
                print("front.")
                return

            if soup == "join" and player.skills["defend"] != 1:
                random.shuffle(monsterNames)
                print("The soup is disgusting, but the company is worth it. The old man tells you tales of fights long")
                print("done that he participated in. As he talks, he gives some tips of how to defend yourself when")
                print("you're in battle. As you get up to continue your journey, you are grateful for the time. His")
                print(f'last words warn you to watch out for {monsterNames[1]}s. He saw one recently.\n')
                player.skills["defend"] = 1
                player.status["health"] = player.status["max_health"]
                player.status["poison"] = 0
                print("Skill: 'Defense' learned!")
                if monsterNames[1] not in player.knownMonsters:
                    player.knownMonsters.append(monsterNames[1])
                return

            else:
                print("The soup is actually pretty good. The man seems to have learned some cooking during his time")
                print("on the road. As you talk and enjoy the night with each other, he tells you of his great fights")
                print(f"with {monsterNames[1]}s. He even gives you some tips of how to fight them if you see")
                print("them. As your time to leave comes, you know that you will treasure this night with a stranger.")
                player.status["poison"] = 0
                player.status["health"] = player.status["max_health"]
                if monsterNames[1] not in player.knownMonsters:
                    player.knownMonsters.append(monsterNames[1])
                return

        if d20r in range(7, 18):
            random.shuffle(monsterNames)
            print("The old man's eyes seem almost glazed over. He seems so tired. He faces you and seems to come to")
            print("life more. You seem to remind him of someone he used to know. He tells you of to watch out for")
            print(f'{monsterNames[1]}s. He seems to have seen a lot of them lately.')
            if monsterNames[1] not in player.knownMonsters:
                player.knownMonsters.append(monsterNames[1])

        if d20r < 7:
            print(f"It seems this wasn't a man at all, but rather a {player.knownMonsters[0]} pretending to be one.")
            d20r2 = random.randint(1, 20)
            if d20r2 < 6:
                print("The creature seems angry that you disturbed it and gets ready to attack you.")
                return combat.combat(player, enemy)

            else:
                print("The creature doesn't seem to be dangerous, but you can never be too safe. What do you do?")
                print("Attack/Leave")
                moral = input()
                moral = moral.lower()
                morals = ["attack", "leave"]
                while moral not in morals:
                    print("Please put attack or leave.")
                    moral = input().lower()

                if moral == "leave":
                    print("The creature doesn't seem to be harming anyone. You decide to focus on the journey you have")
                    print("instead of ending someone else's.")
                    return

                if moral == "attack":
                    return combat.combat(player, enemy)

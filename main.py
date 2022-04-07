# -*- coding: utf-8 -*-
# IMPORTS|
# -------------------------------------------------------------------------------
import random
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# Func|
# -------------------------------------------------------------------------------


def day_ini():
    print()
    print("DAY:", str(day), ",", username.upper(), 'THE', title, ",", "GOLD:", gold)
    l_inv.sort()
    print("YOUR INVENTORY CONTAINS:", l_inv)
    print("YOUR SPELLS ARE:", l_spl)
    if len(l_soul) >= 1:
        print("ነፍሳት ተሰብስበዋል:", l_soul)
    print("0. STATS")
    print("1. SLEEP")
    print()
    print(opener)


def clear():
    print()
    print()


def debug_stats():
    print("DEBUGGING...")
    print()
    print("GOLD:", gold)
    print("USERNAME:", username)
    print("ADDITIONAL:", additional)
    print("DAY:", day)
    print("OPENER:", opener)
    print("INVENTORY:", l_inv)
    print("SPELLS:", l_spl)
    print("SOULS:", l_soul)
    print("MORALITY:", morality)
    print()
    print("DEBUG STATS")


def print_stats():
    print(username, 'THE', title)
    print(gold, 'GOLD')
    print("TITLES:", title_list)
    print('REPUTATION:', morality)
    print("DAY:", day)


# -------------------------------------------------------------------------------
# INTRO|
# -------------------------------------------------------------------------------
while True:
    try:
        username = str(input("WHAT IS YOUR NAME?: "))
        username = username.upper()
        break
    except ValueError:
        print("INVALID NAME")
clear()
print("WELCOME TO CAVE GAME, " + username.upper() + "!")
# -------------------------------------------------------------------------------
# Var|
# -------------------------------------------------------------------------------
day = 1
year = 1
l_inv = []
l_spl = []
l_soul = []
morality = 1
gold = 0
title = 'PRISONER'
title_list = ['PRISONER']
# -------------------------------------------------------------------------------
# Dungeon cell|
# -------------------------------------------------------------------------------
additional = False
opener = "YOU FIND YOURSELF IN A DUNGEON CELL."
while True:
    day_ini()
    print("2. LOOK THROUGH THE WINDOW")
    if 'KEY' in l_inv:
        print("3. UNLOCK AND OPEN DOOR")
    else:
        print("3. TRY TO OPEN CELL DOOR")
    if additional and 'COOL LADYBUG' not in l_inv:
        print("4. PICK UP COOL LADYBUG")
    if day >= 3 and 'KEY' not in l_inv:
        print("5. YOU NOTICE AN OBJECT IN YOUR BEDSHEETS. PICK UP?")
    try:
        e = int(input("WHAT WILL YOU DO?: "))
    except ValueError:
        print("UNKNOWN INPUT")
        e = 0
    clear()
    print()
    if e == 0:
        print_stats()
    elif e == 1:
        print("YOU FALL ASLEEP.")
        day = day + 1
    elif e == 2:
        print("YOU SEE A LARGE KINGDOM, AND A SLIGHT CRACK IN THE WALL.")
        if 'COOL LADYBUG' in l_inv:
            print("A COOL LADYBUG ONCE RESTED HERE.")
        else:
            print("A COOL LADYBUG PERCHES ITSELF UPON THE WINDOW.")
        additional = True
    elif e == 3:
        if 'KEY' in l_inv:
            print("CONGRATULATIONS. THE DOOR IS UNLOCKED.")
            break  # LOOP BREAK
        else:
            print("THE DOOR WILL NOT BUDGE.")
    elif e == 4 and 'COOL LADYBUG' not in l_inv:
        print("YOU OBTAINED [COOL LADYBUG].")
        l_inv.append('COOL LADYBUG')
    elif e == 5 and 'KEY' not in l_inv:
        print("YOU NOTICED THE KEY HIDDEN IN YOUR BEDSHEET, AND PICKED IT UP.")
        print("YOU OBTAINED [KEY]")
        print("NEXT TO THE KEY, YOU SEE A NOTE.")
        print("YOU OBTAINED [NOTE FROM A FRIEND]")
        print("IT READS: 'MEET ME BEHIND JOSHUA'S SHOP'")
        l_inv.append('NOTE FROM A FRIEND')
        l_inv.append("KEY")
    else:  # VALIDATION
        print("UNKNOWN COMMAND.")
# -------------------------------------------------------------------------------
# Main dungeon|
# -------------------------------------------------------------------------------
opener = 'IN FRONT OF YOU, A CORRIDOR STRETCHES OUT. YOU CAN SEE MULTIPLE CELLS.'
additional = False
while True:
    day_ini()
    print()
    print("2.TRY THE SECOND CELL")
    if 'BOOK OF FLAME' not in l_inv:
        print("3.TRY THE THIRD CELL")
    if 'COIN?' not in l_inv:
        print("4.TRY THE FOURTH CELL")
    print("5.MOVE FORWARDS")
    if 'BOOK OF FLAME' in l_inv and 'COOL LADYBUG' in l_inv:
        print("6. BURN LADYBUG AS A SACRIFICIAL EFFIGY TO THE THIRD CELL")
    while True:
        try:
            e = int(input("WHAT WILL YOU DO?: "))
            break
        except ValueError:
            print("UNKNOWN INPUT")
    clear()
    if e == 0:
        print_stats()
    elif e == 1:
        print("YOU FALL ASLEEP.")
        day += 1
    elif e == 2:
        print("THE CELL IS ENTIRELY EMPTY.")
        if 'COIN?' in l_inv:
            print("THE GROUND SHAKES.")
            print("FROM IT, RISES A FIGURE.")
            print()
            print("IT: '", username.upper(), "'")
            print("IT: 'YOU KNOW YOU DESIRE TO GIVE ME THE COIN'")
            print("IT: 'WILL YOU SHOW ME YOUR ALLEGIANCE?'")
            print()
            print("1.YES 2.NO")
            try:
                bc = int(input("GIVE 'IT' THE COIN?: "))
            except ValueError:
                print("INVALID ID.")
                bc = 0
            clear()
            if bc == 1:
                l_inv.remove('COIN?')
                l_inv.append('EFFIGY TO ???')
                print("YOU HAVE OBTAINED [MYSTERIOUS EFFIGY]")
            if bc == 2:
                print("???: VERY WELL.")
                print("THE SHADOW FIGURE VANISHES")
    elif e == 3 and 'BOOK OF FLAME' not in l_inv:
        if 'MARK OF ZENO' in l_inv:
            print("THE WALLS ARE BLOODSTAINED AND A SCORCH MARK IN THE SHAPE OF A MAN RESTS IN THE WALL")
            print("YOU HAVE NO DESIRE TO SEE THIS FOR LONGER THAN YOU MUST")
        elif 'COIN?' in l_inv:
            print("THERE IS A MAN IN THE CELL.")
            print("MAN: 'YOUNG ONE.'")
            print("MAN: 'I BESTOW UPON THEE UNUSUAL KNOWLEDGE.'")
            print("MAN: 'JUST GIVE ME THE SHINY.'")
            print()
            print("1.YES 2.NO")
            try:
                bc = int(input("WILL YOU GIVE HIM THE COIN?: "))
            except ValueError:
                print("ANSWER, COWARD")
                bc = 0
            clear()
            if bc == 1:
                l_inv.remove('COIN?')
                print("YOU HAVE OBTAINED [BOOK OF FLAME]")
                l_inv.append('BOOK OF FLAME')
            elif bc == 2:
                print("THIS WILL BRING REGRET UPON YOUR LIFE,", username.upper())
                l_inv.append('MARK OF ZENO')
            bc = 0
    elif e == 4 and 'COIN?' not in l_inv:
        print("THERE SEEMS TO BE A WAY OUT THROUGH THE WEAKNESS IN THIS CELL'S WALL")
        print("HOPE, HOWEVER, LIES BEHIND CLOSED DOORS")
        if not additional:
            print("AND YOU FIND A COIN ON THE FLOOR")
            l_inv.append('COIN?')
            print("YOU HAVE OBTAINED WHAT YOU THINK IS A [COIN]")
            additional = True
    elif e == 5:
        print("YOU MOVE ON TO THE NEXT SPOT.")
        break
    elif e == 6 and 'COOL LADYBUG' and 'BOOK OF FLAME' in l_inv:
        print("YOU BURN THE LADYBUG AS A TOKEN FOR THE GOD OF FLAME.")
        l_inv.remove('COOL LADYBUG')
        if 'KEY' in l_inv:
            print("THE COIN IN YOUR POCKETS TURNED OUT TO BE AN EFFIGY TOKEN FROM THE MAD GOD ZENO.")
            l_inv.remove('KEY')
            l_inv.append('GOLDEN EFFIGY TO MAD GOD')
            print("YOU HAVE OBTAINED (ELDRITCH ABSORPTION)")
            l_spl.append('ELDRITCH ABSORPTION')
            morality -= 1
    else:
        print("UNKNOWN COMMAND.")
if 'COIN?' in l_inv:
    l_inv.remove('COIN?')
    print("UPON CLOSER INVESTIGATION, THIS WAS INDEED AN INCREDIBLY RARE IMPERIAL COIN")
    print("YOU OBTAINED 200 GOLD")
    gold += 200
print("YOU WALK PAST THE CELLS AND LEAVE THE DUNGEON ENTRANCE.")
opener = "YOU FIND YOURSELF AT JOSHUA'S MARKET"
additional = False
while True:
    day_ini()
    print()
    print('2. BUY')
    print('3. SELL')
    print("4. GO TO THE SHED BEHIND JOSHUA'S SHOP")
    print("5. LOOK AROUND")
    if 'ELDRITCH ABSORPTION' in l_spl and "JOSHUA'S SOUL" not in l_soul:
        print("6. DESTROY JOSHUA'S MORTAL FLESH AND STEAL HIS SOUL")
    try:
        e = int(input("DO: "))
    except ValueError:
        print("UNKNOWN INPUT.")
    if e == 0:
        print_stats()
    elif e == 1:
        print("YOU FALL ASLEEP.")
        day += 1
    if e == 3 and "JOSHUA'S SOUL" not in l_soul:
        print()
        print("WHICH ITEM DO YOU WANT TO SELL?")
        for i in l_inv:
            print(i)
        tc = str(input("ITEM: "))
        tc = tc.upper()
        if tc.upper() == 'COOL LADYBUG' and 'COOL LADYBUG' in l_inv:
            print("VERY WELL. THAT WILL BE 20 GOLD.")
            gold += 20
            l_inv.remove('COOL LADYBUG')
        elif tc.upper() == 'KEY' and 'KEY' in l_inv:
            print("VERY WELL. THAT WILL BE 40 GOLD.")
            gold += 40
            l_inv.remove('KEY')
        elif tc.upper() == 'MY SOUL' and not additional:
            print("ነፍስህ ለዘላለም የኢያሱዋ ነች")
            gold += 500
            additional = True
            morality -= 10
            title = 'SOULLESS'
            title_list.append(title)
        elif tc.upper() == 'BOOK OF FLAME' and 'BOOK OF FLAME' in l_inv:
            print("THAT IS AN AMAZING FIND! THAT WILL BE 100 GOLD, AND A GIFT FROM ME.")
            gold += 100
            l_inv.remove('BOOK OF FLAME')
            l_inv.append('JOSHUA SOUVENIR')
            print("YOU OBTAINED [JOSHUA SOUVENIR]")

        else:
            print("NOT A SELLABLE ITEM.")
    if e == 2 and "JOSHUA'S SOUL" not in l_soul:
        print("WHICH ITEM DO YOU WANT TO BUY?")
        if 'BOMB' not in l_inv:
            print("BOMB: 50 GOLD")
        if 'FOLDING SWORD' not in l_inv:
            print("FOLDING SWORD: 200 GOLD")
        while True:
            try:
                tc = str(input("BUY: "))
                break
            except ValueError:
                print("Invalid ID")
        tc = tc.upper()
        if tc == 'BOMB' and gold >= 50:
            print("YOU OBTAINED [BOMB]")
            gold -= 50
            l_inv.append('BOMB')
        elif tc == 'FOLDING SWORD' and gold >= 200:
            print("YOU OBTAINED [FOLDING SWORD]")
            l_inv.append('FOLDING SWORD')
            gold -= 200
        else:
            print("UNKNOWN ITEM.")
    if e == 4:
        break
    if e == 5 and 'ROCK' not in l_inv:
        print("YOU FIND A ROCK.")
        print("YOU OBTAINED [ROCK]")
        l_inv.append('ROCK')
    if e == 6 and 'ELDRITCH ABSORPTION' in l_spl and "JOSHUA'S SOUL" not in l_soul:
        print("THE ABSORPTION OF A HUMAN SOUL MAKES YOU STRONGER.")
        print("YOU HAVE OBTAINED {JOSHUA'S SOUL}")
        l_soul.append("JOSHUA'S SOUL")
if 'ROCK' in l_inv:
    print("YOU HAVE DECIDED TO NAME YOUR ROCK MATHIAS")
    l_inv.remove('ROCK')
    l_inv.append('MATHIAS, THE ROCK')

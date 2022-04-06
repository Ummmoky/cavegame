# -*- coding: utf-8 -*-
# IMPORTS|
# -------------------------------------------------------------------------------
import random
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# INTRO|
# -------------------------------------------------------------------------------
username = str(input("What's your name?: "))
print("WELCOME TO CAVE GAME, " + username.upper() + "!")
# -------------------------------------------------------------------------------
# Var|
# -------------------------------------------------------------------------------
day = 1
year = 1
opener = ''
l_inv = []
morality = 0
gold = 0


# -------------------------------------------------------------------------------
# Func|
# -------------------------------------------------------------------------------
def day_ini():
    print()
    print("DAY:", str(day), ",", username.upper(), ",", "GOLD:", gold)
    l_inv.sort()
    print("YOUR INVENTORY CONTAINS:", l_inv)
    print("0. ???")
    print("1. SLEEP")
    print()
    print(opener)


def clear():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


def debug_stats():
    print("DEBUGGING...")
    print("GOLD:", gold)
    print("USERNAME:", username)
    print("ADDITIONAL:", additional)
    print("DAY:", day)
    print("OPENER:", opener)
    print("INVENTORY:", l_inv)
    print("MORALITY:", morality)
    print("DEBUG STATS")


# -------------------------------------------------------------------------------
# Dungeon cell|
# -------------------------------------------------------------------------------
additional = False
opener = "YOU FIND YOURSELF IN A DUNGEON CELL."
while True:
    day_ini()
    print()
    print("2. LOOK THROUGH THE WINDOW")
    if 'KEY' in l_inv:
        print("3. UNLOCK AND OPEN DOOR")
    else:
        print("3. TRY TO OPEN CELL DOOR")
    if additional and 'COOL LADYBUG' not in l_inv:
        print("4. PICK UP COOL LADYBUG")
    if day >= 3 and 'KEY' not in l_inv:
        print("5. YOU NOTICE AN OBJECT IN YOUR BEDSHEETS. PICK UP?")
    e = int(input("WHAT WILL YOU DO?: "))
    clear()
    print()
    if e == 1:
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
            break
        else:
            print("THE DOOR WILL NOT BUDGE.")
    elif e == 4 and 'COOL LADYBUG' not in l_inv:
        print("YOU OBTAINED [COOL LADYBUG].")
        l_inv.append('COOL LADYBUG')
    elif e == 5 and 'KEY' not in l_inv:
        print("YOU NOTICED THE KEY HIDDEN IN YOUR BEDSHEET, AND PICKED IT UP.")
        print("YOU OBTAINED [KEY]")
        l_inv.append("KEY")
    else:
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
        print("6. BURN LADYBUG AS A SACRIFICIAL EFFIGY TO THE SECOND CELL")
    e = int(input("WHAT WILL YOU DO?: "))
    clear()
    if e == 1:
        print("YOU FALL ASLEEP.")
        day += 1
    elif e == 2:
        print("THE CELL IS ENTIRELY EMPTY.")
        if 'COIN?' in l_inv:
            print("THE GROUND SHAKES.")
            print("FROM IT, RISES A FIGURE.")
            print()
            print("???:'", username.upper(), "'")
            print("???: 'YOU KNOW YOU DESIRE TO GIVE ME THE COIN'")
            print("???: 'WILL YOU SHOW ME YOUR ALLEGIANCE'")
            print()
            print("1.YES 2.NO")
            bc = int(input("???: "))
            clear()
            if bc == 1:
                l_inv.remove('COIN?')
                l_inv.append('EFFIGY TO ???')
                print("YOU HAVE OBTAINED [MYSTERIOUS EFFIGY]")
            if bc == 2:
                print("???: VERY WELL.")
                print("THE SHADOW FIGURE VANISHES")
    elif e == 3 and 'BOOK OF FLAME' not in l_inv:
        print("THERE IS A MAN IN THE CELL.")
        if 'COIN?' in l_inv:
            print("MAN: 'YOUNG ONE.'")
            print("MAN: 'I BESTOW UPON THEE UNUSUAL KNOWLEDGE.'")
            print("MAN: 'JUST GIVE ME THE SHINY.'")
            print()
            print("1.YES 2.NO")
            bc = int(input("WILL YOU GIVE HIM THE KEY?: "))
            clear()
            if bc == 1:
                l_inv.remove('COIN?')
                print("YOU HAVE OBTAINED [BOOK OF FLAME]")
                l_inv.append('BOOK OF FLAME')
            elif bc == 2:
                print("THIS WILL BRING REGRET UPON YOUR LIFE,", username.upper())
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
            morality -= 1
if 'COIN?' in l_inv:
    l_inv.remove('COIN?')
    print("UPON CLOSER INVESTIGATION, THIS WAS INDEED AN INCREDIBLY RARE IMPERIAL COIN")
    print("YOU OBTAINED 200 GOLD")
    gold = gold + 200
print("CONGRATULATIONS. THE GAME IS OVER FOR NOW.")
debug_stats()

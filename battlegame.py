wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
dragon_damage = 50

# Begin task#2
while True:
    print(
        f"Following are the Characters to select:\n1. {wizard}\n2. {elf}\n3. {human}")
    character = input("Select the character from the list (1-3): ")
    if character == "1":
        my_character = wizard
        my_health = wizard_hp
        my_damage = wizard_damage
        break
    elif character == '2':
        my_character = elf
        my_health = elf_hp
        my_damage = elf_damage
        break
    elif character == '3':
        my_character = human
        my_health = human_hp
        my_damage = human_damage
        break
    else:
        print("Invalid selection. Please make a valid selection between 1 and 3.")

print("Selected character:")
print(f"Character: {my_character}")
print(f"Health: {my_health}")
print(f"Damage: {my_damage}")

"""
Battle with Dragon - Task#4
"""
while True:
    dragon_hp -= my_damage
    print(f"The {my_character} damaged the Dragon!")
    print(f"The Dragon's hit points are now: {dragon_hp}")

    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_health -= dragon_damage
    print(f"The Dragon strikes back at {my_character}")
    print(f"The {my_character}'s hit points are now: {my_health}")

    if my_health <= 0:
        print(f"{my_character} has lost the battle")
        break

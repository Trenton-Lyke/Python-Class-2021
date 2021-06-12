import time

username = ''
weapon = 'none'
armour = 'none'
hate = 0
hp = 10
weapon_verbs = {}
monster_health = {"www": 30, "sss": 30, "ttt": 0, "ff":30, "mm":30}

def clean_input(input):
    return input.strip().lower()

def yes_no_input(prompt):
    return fixed_option_input(prompt, "yes", "no")

def get_option_reminders(*options):
    number_of_options = len(options)
    onErrorPrefix = 'Sorry could you please enter '
    generalSuffix = '('
    if len(options) == 1:
        onErrorPrefix += clean_input(options[0])
        generalSuffix += clean_input(options[0])
    else:
        for i in range(number_of_options):
            if i < number_of_options - 2:
                onErrorPrefix += clean_input(options[i]) + ", "
                generalSuffix += clean_input(options[i]) + "/"
            elif i < number_of_options - 1:
                if number_of_options > 2:
                    onErrorPrefix += clean_input(options[i]) + ", or "
                else:
                    onErrorPrefix += clean_input(options[i]) + " or "
                generalSuffix += clean_input(options[i]) + "/"
            else:
                onErrorPrefix += clean_input(options[i])
                generalSuffix += clean_input(options[i])
    onErrorPrefix += ". "
    generalSuffix += "): "
    return onErrorPrefix, generalSuffix
def is_response_in_options(response, *options):
    for option in options:
        if clean_input(response) == clean_input(option):
            return True
    return False
def get_selected_option(response, *options):
    for option in options:
        if clean_input(response) == clean_input(option):
            return option
    return None
def fixed_option_input(prompt, *options):
    if len(options) == 0:
        print('Oops, looks like the programmer forgot to give you any options for the prompt: "' + prompt + '"')
        return 'error no options given'
    onErrorPrefix, generalSuffix = get_option_reminders(*options)
    response = input(prompt + generalSuffix)
    while not is_response_in_options(response, *options):
        response = input(onErrorPrefix + prompt + generalSuffix)
    return get_selected_option(response, *options)
def prompt_numbered_output(prompt, *options, error=False):
    number_of_options = len(options)
    if not error:
        print(prompt)
        for i in range(number_of_options):
            print(str(i + 1) + ". " + options[i])
    response = input(
        ("Sorry it looks like your last response was not a valid number in the numbered answers range.\n" if error else "") +"Please enter a number (1-" + str(number_of_options) + ") that corresponds to the option above that you would like to select: ")
    return response
def is_valid_response_number(response, number_of_options):
    try:
        numeric_response = int(clean_input(response))
        return numeric_response >= 1 and numeric_response <= number_of_options
    except:
        return False
def numbered_option_input_number(prompt, *options):
    number_of_options = len(options)
    if number_of_options == 0:
        print('Oops, looks like the programmer forgot to give you any options for the prompt: "' + prompt + '"')
        return 'error no options given'
    response = prompt_numbered_output(prompt, *options)
    while not is_valid_response_number(response, number_of_options):
        response = prompt_numbered_output(prompt, *options, error=True)
    return int(clean_input(response))

def numbered_option_input_string(prompt, *options):
    return options[numbered_option_input_number(prompt, *options)-1]

def delay(duration=1):
    time.sleep(duration)
def print_with_delay(string, duration=1):
    print(string)
    delay(duration=duration)
def hate_check(hater):
    global hate
    hate += 1
    if hate >= 10:
        print_with_delay(hater+": I can't take this anymore. You are literally the worst.",2)
        print_with_delay(username+": I think you mean figuratively :D",3)
        print_with_delay(hater+": ...")
        print_with_delay(username + ": Right? :D", 2)
        print_with_delay(hater+": ...")
        print_with_delay(username + ": "+hater+"? :D", 2)
        print_with_delay(hater+": Zap Zap Za Boom Booms! Wizard Magic!")
        print_with_delay("** "+hater+" was fed up with you since you were such a jerk all the time.")
        print_with_delay("** The wizard magic is too strong you're body can't handle it.")
        return True
    else:
        return False

def hp_check(companion):
    global hp
    hp -= 1
    if hp <= 0:
        print_with_delay(username+": AHHHHH!!!!",3)
        print_with_delay(companion+": Oh no "+username+" you don't look so good!")
        print_with_delay(username+": Aight bro, I'm about to make like a tree and leave.")
        return True
    else:
        return False

def game_over():
    if hate < 10 and hp > 0:
        print("** Congratulations "+username+" you survived Danger Island with a score of "+str((hp-hate+10)/10*100)+"%")
    else:
        print("** Sorry " + username + ". You passed out and were teleported back home in shame. At least you had a score of " + str(
            (hp - hate + 10) / 10 * 100) + "%")
def start():
    global username
    print_with_delay("Leroy: You're finally awake.")
    print_with_delay("Leroy: We're about to fly over Danger Island. I hope you're ready for this.",2)
    username = input("Leroy: By the way, what's your name adventurer?: ")
    delay()
    decision = yes_no_input("Leroy: Nice to meet you " + username + ". Are you ready to explore Danger Island? ")
    delay()
    if decision == "yes":
        print_with_delay("Leroy: Alright we better get prepared first though.")
        armour_up()
    else:
        print_with_delay("Leroy: Forget you then! I'll jump out on my own then. Bye!")


def armour_up():
    global weapon, hp, hate
    print_with_delay("Leroy: Okay kid. You're going to need some armour and weapons if you're going to survive danger island.")
    weapon = numbered_option_input_string("Select a weapon to take with you on the island: ", "light saber", "ray gun", "plasma grenade", "none")
    delay()
    global armour
    armour = numbered_option_input_string("Select a weapon to take with you on the island: ", "doom armour", "spartan armour", "samus armour", "none")
    delay()
    if weapon == "none" and armour == "none":
        print_with_delay("Leroy: I'm gonna be real with you...")
        print_with_delay("Leroy: you're probably going to die.")

    elif weapon == "none":
        print_with_delay("Leroy: Wow no weapon...")
        print_with_delay("Leroy: Good luck!")
        hate += 3
        hp += 3
    elif armour == "none":
        print_with_delay("Leroy: Wow no armour...")
        print_with_delay("Leroy: Good luck!")
        hate += 2
    else:
        print_with_delay("Leroy: Good choices.")
        print_with_delay("Leroy: The only thing I love more than "+armour+" is a trusty old "+weapon, 3)
        hate += 5
        hp += 3
    deploy()


def deploy():
    print_with_delay("Leroy: Okay listen everyone. Danger Island is split up into 5 main areas...",3)
    print_with_delay("Leroy: Wild Winter Wonderland, where the only thing wilder than the animals are the fierce snow storms.",4)
    print_with_delay("Leroy: Stinky Sewage Swamp, it smells a little fishy and sadly the it's not the worst smell in that place.",4)
    print_with_delay("Leroy: Terrible TNT Town, BOOOOM!!! That's all the description you need.",3)
    print_with_delay("Leroy: Ferocious Fireland, a nice place to stay warm, but also a good place to barbeque and I'm not talking about food.",4)
    print_with_delay("Leroy: Monster Mazeland, I don't know what's scarier. The flesh-eating monsters roaming around or the fact that no one has found a way path the maze.",5)
    location = numbered_option_input_string("Leroy: Okay so where we dropping people?", "wild winter wonderland", "stinky sewage swamp", "terrible tnt town", "ferocious fireland", "monster mazeland")
    delay()
    if location == "wild winter wonderland":
        print_with_delay("Leroy: Wild Winter Wonderland? That's cold team, but okay.",3)
        jump_dialogue()
        www_diving()
    elif location == "stinky sewage swamp":
        print_with_delay("Leroy: Stinky Sewage Swamp? Y'all are disgusting.",3)
        jump_dialogue()
        sss_diving()
    elif location == "terrible tnt town":
        print_with_delay("Leroy: Terrible TNT Town? Why tho?",2)
        jump_dialogue()
        ttt_diving()
    elif location == "ferocious fireland":
        print_with_delay("Leroy: Ferocious Fireland? It's about to get hot in here.",3)
        jump_dialogue()
        ff_diving()
    else:
        print_with_delay("Leroy: Monster Mazeland? Did you not hear the part about flesh eating?",3)
        jump_dialogue()
        mm_diving()

def jump_dialogue():
    print_with_delay("Leroy: Grab those parachutes and get ready to jump.", 2)
    print_with_delay("** The planes cargo door opens up.")
    print_with_delay("Leroy: OKAY EVERYONE IT'S DO OR DIE TIME! LET'S MOVE OUT!",2)
    print_with_delay("** Everyone jumps out of the plane and you're soaring towards the ground.",3)

def www_diving():
    print_with_delay("WOOSH!")
    print_with_delay("** A harsh wind bombards the group.",2)
    print_with_delay("Leroy: AHHHHH!")
    print_with_delay("** Leroy is getting carried away by the wind!", 2)
    decision = numbered_option_input_number("Leroy: Help me "+username+"!","Grab Leroy","Let Leroy fly away. I'm not really vibing with them.")
    delay()
    if decision == 1:
        hp_check("Leroy")
        print_with_delay("** You grab onto Leroy and get carried away with him...", 2)
        print_with_delay("** Both of you release your parachutes, but you crash hard in the snow.", 3)
        print_with_delay("Leroy: You saved me " + username + "! I definitely was about to be a goner.", 2)
        www_with_leroy()
    else:
        if hate_check("Everyone"):
            return
        else:
            www_without_leroy()



def www_with_leroy():
    print_with_delay("Leroy: Man it's freezing out here.", 1.5)
    if monster_health["www"] <= 0:
        print_with_delay("Leroy: Let's go somewhere war-", .5)
        print_with_delay("???: ROOOAAARRR!!!.", 1.5)
        decision = numbered_option_input_number("Leroy: What was that?", username+": Let's go find out.",username+": I regret everything please just take me home.")
        delay()
        if decision == 1:
            abominal_snowman()
        else:
            if hate_check("Leroy"):
                return
            else:
                print_with_delay("Leroy: Okay I get it jeez "+username+".")
                leave_www_with_leroy()
    else:
        print_with_delay("Leroy: There's nothing to do out here anymore. Let's go somewhere else", 1.5)


def abominal_snowman():
    pass

def leave_www_with_leroy():
    location = numbered_option_input_number("Leroy: Okay scaredy cat. Where do you want to go next?","stinky sewage swamp", "terrible tnt town", "ferocious fireland", "monster mazeland")
    if location == "stinky sewage swamp":
        print_with_delay("Leroy: Stinky Sewage Swamp? Gross, but let's go.", 3)
        jump_dialogue()
        sss_diving()
    elif location == "terrible tnt town":
        print_with_delay("Leroy: Terrible TNT Town? Why tho? Like seriously, why?", 3)
        jump_dialogue()
        ttt_diving()
    elif location == "ferocious fireland":
        print_with_delay("Leroy: Ferocious Fireland? Well at least it's warmer than here.", 3)
        jump_dialogue()
        ff_diving()
    else:
        print_with_delay("Leroy: Monster Mazeland? I thought you were afraid of monsters?", 3)
        jump_dialogue()
        mm_diving()
def www_without_leroy():
    pass

#Trinity do this
def sss_diving():
    print_with_delay("Pop!")
    print_with_delay("** A huge bubble in the swamp bursts releasing mysterious swamp gas.", 3)
    print_with_delay("Leroy: Oh hecky nah!")
    print_with_delay("** Leroy darts to the left and glides away from the group.", 2)
    decision = numbered_option_input_number("Leroy: Stick with the stinky if you want. I'm gonna dip real quick. " + username + "!", "Follow Leroy",
                                            "Let Leroy fly away. I'm not really vibing with them.")
    delay()
    if decision == 1:
        if hate_check("Everyone"):
            return
        else:
            print_with_delay("** You follow Leroy...", 2)
            print_with_delay("** Both of you release your parachutes and land safely in the swamp.", 3)
            print_with_delay("Leroy: Okay let's go explore.", 2)
            sss_with_leroy()
    else:
        if hp_check("Leroy"):
            return
        else:
            sss_without_leroy()

#Trinity Do this
def ttt_diving():
    print_with_delay("** Your soar down to ground.", 2)
    print_with_delay("BOOM! POW! KLABAMO!")
    print_with_delay("** All of Terrible TNT Town explodes as you land", 2)
    print_with_delay("Everyone: AHHHHH!")
    global hp, hate
    hp = 0
    hate = 10

#Trinity Do this
def ff_diving():
    print_with_delay("CRACKLE! CRACKLE! CRACKLE!")
    print_with_delay("** The group falls for what feels like an eternity. It gets hotter and hotter.", 3)
    print_with_delay("Leroy: Ay yo dawg that place over there looking mad chill homie. I'm bout to dip out peace.")
    print_with_delay("** Leroy changes direction", 2)
    print_with_delay("Everyone Else: Nah dawg stick to the plan.")
    decision = numbered_option_input_number("Leroy: Stick to the plan if you want, but whoever wants to get this bread follow me.", "Grab Leroy",
                                            "Let Leroy fly away. This whole situation has gotten way too \"Hey fellow kids\" for my liking.")
    delay()
    if decision == 1:
        if hate_check("Everyone"):
            return
        else:
            print_with_delay("** You change directions and follow Leroy...", 2)
            print_with_delay("** Both of you release your parachutes and safely land in the flames.", 3)
            print_with_delay("Leroy: Hey " + username + " WHADUP! It's about to be LIT up in here.", 3)
            print_with_delay("Leroy: Check out all this stuff man. This place is HOT!", 3)
            print_with_delay("** You immediately realize your mistake.", 2)

            ff_with_leroy()
    else:
        if hp_check("Leroy"):
            return
        else:
            ff_without_leroy()

#Trinity Do this
def mm_diving():
    print_with_delay("ROAR! HISS!...")
    print_with_delay("I HAVE NEGATIVE OPINIONS ON BEYONCE!")
    print_with_delay("** You can already here all the monsters below.", 2)
    print_with_delay("Leroy: AHHHHH!")
    print_with_delay("** Leroy is getting carried away by a pterodactyl!", 2)
    decision = numbered_option_input_number("Leroy: Help me " + username + "!", "Grab onto the pterodactyl",
                                            "Let the pterodactyl take Leroy. I'm not really vibing with them.")
    delay()
    if decision == 1:
        if hp_check("Leroy"):
            return
        else:
            print_with_delay("** You grab onto the pterodactyl and get carried away with Leroy...", 3)

            print_with_delay("** Both of you release your parachutes, but you crash hard in the snow.", 3)
            print_with_delay("Leroy: You saved me " + username + "! I definitely was about to be a goner.", 2)
            mm_with_leroy()
    else:
        if hate_check("Everyone"):
            return
        else:
            mm_without_leroy()

def pterodactyl():
    print_with_delay("Leroy: You gotta find a way to get this thing to let go of me", 3)
    if weapon != "none":
        pterodactyl_weapon()
    else:
        pterodactyl_none()

def pterodactyl_weapon():
    decision = numbered_option_input_number("Leroy: You got a "+weapon+"! Use it!","use your "+weapon+" on the pterodactyl", "pl")

def main():
    play = 'yes'
    while clean_input(play) == 'yes':
        start()
        game_over()
        play = yes_no_input('Would you like to play again?')
    print("Thanks for playing goodbye!")

if __name__ == '__main__':
    main()

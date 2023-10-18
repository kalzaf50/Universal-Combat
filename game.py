import pygame, sys
from button import Button
import time
from pygame.locals import *
from pygame import mixer
import random

#Initialization
pygame.init()
mixer.init()

#Sound effects
buttonSound = pygame.mixer.Sound("assets/button.wav")
punchSound = pygame.mixer.Sound("assets/punch.wav")
kickSound = pygame.mixer.Sound("assets/kick.wav")
bankaiSound = pygame.mixer.Sound("assets/bankai.wav")
emperorSound = pygame.mixer.Sound("assets/summon.wav")
smashSound = pygame.mixer.Sound("assets/smash.wav")
kerisSound = pygame.mixer.Sound("assets/keris.wav")
chargeSound = pygame.mixer.Sound("assets/charge.wav")
mixer.music.load("assets/background.wav")

#Declaring variables
characters = [["SATORI", "BANKAI", 100, 100, [14, 24]], 
            ["CHONG WEI", "LIBASAN KILAT", 100, 100, [17, 22]], 
            ["HANG JEBAT", "RAGING KERIS", 100, 100, [18 , 20]],
            ["EMPEROR QIN", "EMPEROR WRATH", 100, 100, [19 , 24]]]
lenCharacter = len(characters)
playerSelecting = True
Right = 1

#Create window
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("UNIVERSAL COMBAT")
background = pygame.image.load("assets/icon.png")

#Determine the fonts used in the program
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

#To display the character's icon in the program
def userCharacterIcon(playerImage, playerX, playerY):
    screen.blit(playerImage, (playerX, playerY))

#Display the result after the fight has ended showing the winner with the scores obtained from the fight.
def results(userCharacter, winner):

    #Backgrounds
    result1 = pygame.image.load('assets/Result (Satori).png')
    result2 = pygame.image.load('assets/Result (Chong Wei).png')
    result3 = pygame.image.load('assets/Result (Hang Jebat).png')
    result4 = pygame.image.load('assets/Result (Emperor Qin).png')

    #Score calculation
    healthScore = userCharacter[2] * 100
    energyScore = userCharacter[3] * 100
    totalScore = healthScore + energyScore

    #Page loop
    while True:

        #Mouse position
        Results_Mouse_Pos = pygame.mouse.get_pos()

        Player_Winner = get_font(30).render(str(winner), True, "#FFDE59")
        Player_Winner_Rect = Player_Winner.get_rect(center=(545, 112))

        Health_Score = get_font(15).render(str(healthScore), True, "White")
        Health__Score_Rect = Health_Score.get_rect(center=(575, 180))

        Energy_Score = get_font(15).render(str(energyScore), True, "White")
        Energy_Score_Rect = Energy_Score.get_rect(center=(575, 235))

        Total_Score = get_font(15).render(str(totalScore), True, "White")
        Total_Score_Rect = Total_Score.get_rect(center=(575, 290))
        
        if userCharacter[0] == "SATORI":
            screen.blit(result1, (0, 0))
        elif userCharacter[0] == "CHONG WEI":
            screen.blit(result2, (0, 0))
        elif userCharacter[0] == "HANG JEBAT":
            screen.blit(result3, (0, 0))
        elif userCharacter[0] == "EMPEROR QIN":
            screen.blit(result4, (0, 0))

        screen.blit(Player_Winner, Player_Winner_Rect)
        screen.blit(Health_Score, Health__Score_Rect)
        screen.blit(Energy_Score, Energy_Score_Rect)
        screen.blit(Total_Score, Total_Score_Rect)
     
        Results_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")

        Results_Menu.changeColor(Results_Mouse_Pos)
        Results_Menu.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:
                if Results_Menu.checkForInput(Results_Mouse_Pos):
                    buttonSound.play()
                    main_menu()

        pygame.display.update()

#Display the main gameplay where the player will fight with the computer after they have chosen their fighters for training.    
def training(userCharacter, opponentCharacter):

    #Declare images
    icon_char1 = pygame.image.load('assets/satori.jpeg')
    icon_char2 = pygame.image.load('assets/chongwei.png')
    icon_char3 = pygame.image.load('assets/hangjebat.png')
    icon_char4 = pygame.image.load('assets/qin.png')
    background = pygame.image.load("assets/Fight Page.png")
    pause = pygame.image.load('assets/Pause.png')

    #Declare variables
    message = ""
    fightPeriod = 1
    playerTurn = 1
    User_Action = False
    Opponent_Action = True
    game_pause = False

    #Game loop
    while fightPeriod == 1:

        #Mouse position
        Single_Mouse_Pos = pygame.mouse.get_pos()

        #Page background
        screen.blit(background, (0, 0))

        #General texts in page
        User_Health = get_font(15).render(str(userCharacter[2]), True, "White")
        User_Health_Rect = User_Health.get_rect(center=(375, 175))

        User_Energy = get_font(15).render(str(userCharacter[3]), True, "White")
        User_Energy_Rect = User_Health.get_rect(center=(375, 233))

        Opponent_Health = get_font(15).render(str(opponentCharacter[2]), True, "White")
        Opponent_Health_Rect = User_Health.get_rect(center=(860, 175))

        Opponent_Energy = get_font(15).render(str(opponentCharacter[3]), True, "White")
        Opponent_Energy_Rect = User_Health.get_rect(center=(860, 233))

        message_fight = get_font(15).render(str(message), True, "White")
        message_rect = message_fight.get_rect(center=(480, 490))

        #General buttons
        Menu_Button = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Main_Button = Button(image=None, pos=(482, 200), 
                            text_input="MAIN MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Resume_Button = Button(image=None, pos=(482, 300), 
                            text_input="RESUME", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Quit_Button = Button(image=None, pos=(482, 400), 
                            text_input="QUIT", font=get_font(30), base_color="White", hovering_color="Red")
        
        #User buttons
        if playerTurn == 1 and game_pause == False:
            User_Punch = Button(image=None, pos=(170, 320), 
                                text_input="PUNCH", font=get_font(17), base_color="White", hovering_color="cadetblue1")
            
            User_Kick = Button(image=None, pos=(300, 320), 
                                text_input="KICK", font=get_font(17), base_color="White", hovering_color="cadetblue1")
            
            User_Special = Button(image=None, pos=(172, 360), 
                                text_input="SPECIAL", font=get_font(17), base_color="White", hovering_color="cadetblue1")
            
            User_Charge = Button(image=None, pos=(301, 360), 
                                text_input="CHARGE", font=get_font(17), base_color="White", hovering_color="cadetblue1")

        
        Menu_Button.changeColor(Single_Mouse_Pos)
        Menu_Button.update(screen)

        screen.blit(User_Health, User_Health_Rect)
        screen.blit(User_Energy, User_Energy_Rect)
        screen.blit(Opponent_Health, Opponent_Health_Rect)
        screen.blit(Opponent_Energy, Opponent_Energy_Rect)
        screen.blit(message_fight, message_rect)
        
        #Loads user's icon
        if userCharacter[0] == "SATORI":
            userCharacterIcon(icon_char1, 90, 140)
        elif userCharacter[0] == "CHONG WEI":
            userCharacterIcon(icon_char2, 90, 140)
        elif userCharacter[0] == "HANG JEBAT":
            userCharacterIcon(icon_char3, 90, 140)
        elif userCharacter[0] == "EMPEROR QIN":
            userCharacterIcon(icon_char4, 90, 140)

        #Loads opponent's icon
        if opponentCharacter[0] == "SATORI":
            userCharacterIcon(icon_char1, 575, 140)
        elif opponentCharacter[0] == "CHONG WEI":
            userCharacterIcon(icon_char2, 575, 140)
        elif opponentCharacter[0] == "HANG JEBAT":
            userCharacterIcon(icon_char3, 575, 140)
        elif opponentCharacter[0] == "EMPEROR QIN":
            userCharacterIcon(icon_char4, 575, 140)

        #If the game is paused, this code will run
        if game_pause == True:
            print("The game is being paused")
            screen.blit(pause, (0, 0))
            for button in [Main_Button, Resume_Button, Quit_Button]:
                button.changeColor(Single_Mouse_Pos)
                button.update(screen)

        #If its player's 1 turn and the game is not paused, these buttons will appear
        if playerTurn == 1 and game_pause == False:

            for button in [User_Punch, User_Kick, User_Special, User_Charge]:
                button.changeColor(Single_Mouse_Pos)
                button.update(screen)
        
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #If it's player 1's turn and the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and playerTurn == 1 and event.button == Right:

                #If the "MENU" button is being clicked
                if Menu_Button.checkForInput(Single_Mouse_Pos) and game_pause == False:
                    buttonSound.play()
                    game_pause = True
                
                #If the game is being paused, this code will run
                if game_pause == True:
                    if Resume_Button.checkForInput(Single_Mouse_Pos):
                        buttonSound.play()
                        game_pause = False

                    if Main_Button.checkForInput(Single_Mouse_Pos):
                        buttonSound.play()
                        main_menu()
                    
                    if Quit_Button.checkForInput(Single_Mouse_Pos):
                        buttonSound.play()
                        buttonSound.play()
                        time.sleep(0.3)
                        pygame.quit()
                        sys.exit()
                
                #If it's player 1's turn and the game is not paused, this code will run
                if playerTurn == 1 and game_pause == False:
                    
                    print("Player 1's Turn")
                    
                    #Checking which moves player chooses
                    if playerTurn == 1 and Opponent_Action == True:
                        if User_Punch.checkForInput(Single_Mouse_Pos):
                            message = userTurn(playerTurn, 1, userCharacter, opponentCharacter)
                            User_Action = True

                        elif User_Kick.checkForInput(Single_Mouse_Pos):
                            message = userTurn(playerTurn, 2, userCharacter, opponentCharacter)
                            User_Action = True

                        elif User_Special.checkForInput(Single_Mouse_Pos):
                            message = userTurn(playerTurn, 3, userCharacter, opponentCharacter)
                            User_Action = True

                        elif User_Charge.checkForInput(Single_Mouse_Pos):
                            message = userTurn(playerTurn, 4, userCharacter, opponentCharacter)
                            User_Action = True

                        if message == "You don't have enough energy to use that move!":
                            continue
                       
                        fightPeriod = checkFighterHealth(userCharacter, opponentCharacter)
                        if fightPeriod == 0 and userCharacter[2] > 0 and opponentCharacter[2] <= 0:
                            results(userCharacter, playerTurn)
                    
                    #After player 1 has chosen a move, the turn will change to player 2
                    if User_Action == True:
                        playerTurn = 2
                        Opponent_Action = False
        
                    continue
            
            #If it's player 2's turn and player 1 has chosen a move, this code will run
            if playerTurn == 2 and User_Action == True:
                
                print("Player 2's Turn")

                #The program will randomly choose moves
                message = opponentRandomMove(userCharacter, opponentCharacter)
                Opponent_Action = True

                #Checking both players' health
                fightPeriod = checkFighterHealth(userCharacter, opponentCharacter)
                if fightPeriod == 0 and userCharacter[2] <= 0 and opponentCharacter[2] > 0:
                    results(opponentCharacter, playerTurn)
                
                #After player 2 has chosen a move, the turn will change to player 1
                if Opponent_Action == True:
                    playerTurn = 1
                    User_Action = False

        pygame.display.update()

#To execute the chosen move during the fight
def userTurn(playerTurn, userMove, userCharacter, opponentCharacter):

        if userMove <= 6:
            #If the player's move is "PUNCH"
            if userMove == 1 and userCharacter[3] >= 10:
                punchSound.play()
                punchDamage = random.randrange(1,5)
                userCharacter[3] = userCharacter[3] - 10
                opponentCharacter[2] = opponentCharacter[2] - punchDamage
                message = "Player " +str(playerTurn) +" landed a punch and it dealts " +str(punchDamage) +" damages!"
                return message

            #If the player's move is "KICK" 
            elif userMove == 2 and userCharacter[3] >= 15:
                kickSound.play()
                kickDamage = random.randrange(5,10)
                userCharacter[3] = userCharacter[3] - 15
                opponentCharacter[2] = opponentCharacter[2] - kickDamage
                message = "Player " +str(playerTurn) +" landed a kick and it dealts " +str(kickDamage) +" damages!"
                return message
            
            #If the player's move is "SPECIAL"
            elif userMove == 3 and userCharacter[3] >= 30:
                if userCharacter[0] == "SATORI":
                    bankaiSound.play()
                elif userCharacter[0] == "CHONG WEI":
                    smashSound.play()
                elif userCharacter[0] == "HANG JEBAT":
                    kerisSound.play()
                elif userCharacter[0] == "EMPEROR QIN":
                    emperorSound.play()

                abilityDamage = random.randrange(userCharacter[4][0], userCharacter[4][1])
                userCharacter[3] = userCharacter[3] - 30
                opponentCharacter[2] = opponentCharacter[2] - abilityDamage
                message = "Player " +str(playerTurn) +" used " +userCharacter[1] +" and it dealts " +str(abilityDamage) +" damages!"
                return message
            
            #If the player's move is "CHARGE"
            elif userMove == 4:
                chargeSound.play()
                userCharacter[3] = userCharacter[3] + 20
                message = "Player " +str(playerTurn) +" charged and gained +20 energy"
                return message
            
            #If the player's don't have enough energy to choose certain move
            else:
                message = "You don't have enough energy to use that move!"
                return message

#Will randomly choose moves for the computer during the fight 
def opponentRandomMove(userCharacter, opponentCharacter):
        randomMove = random.randrange(1,4)
        
        #If the program's move is "PUNCH"
        if randomMove == 1 and opponentCharacter[3] >= 10:
            punchSound.play()
            punchDamage = random.randrange(1,5)
            opponentCharacter[3] = opponentCharacter[3] - 10
            userCharacter[2] = userCharacter[2] - punchDamage
            message = "Player 2 landed a punch and it dealts " +str(punchDamage) +" damages!"
            return message
        
        #If the program's move is "KICK"
        elif randomMove == 2 and opponentCharacter[3] >= 15:
            kickSound.play()
            kickDamage = random.randrange(5,10)
            opponentCharacter[3] = opponentCharacter[3] - 15
            userCharacter[2] = userCharacter[2] - kickDamage
            message = "Player 2 landed a kick and it dealts " +str(kickDamage) +" damages!"
            return message
        
        #If the program's move is "SPECIAL"
        elif randomMove == 3 and opponentCharacter[3] >= 30:
            if opponentCharacter[0] == "SATORI":
                bankaiSound.play()
            elif opponentCharacter[0] == "CHONG WEI":
                smashSound.play()
            elif opponentCharacter[0] == "HANG JEBAT":
                kerisSound.play()
            elif opponentCharacter[0] == "EMPEROR QIN":
                emperorSound.play()

            abilityDamage = random.randrange(opponentCharacter[4][0], opponentCharacter[4][1])
            opponentCharacter[3] = opponentCharacter[3] - 30
            userCharacter[2] = userCharacter[2] - abilityDamage
            message = "Player 2 used " +opponentCharacter[1] +" and it dealts " +str(abilityDamage) +" damages!"
            return message
        
        #If the program's move is "CHARGE"
        else:
            chargeSound.play()
            opponentCharacter[3] = opponentCharacter[3] + 20
            message = "Player 2 charged and gained +20 energy"
            return message

#Display the main gameplay where the player will fight with other players after they have chosen their fighters.
def fightPage(userCharacter, opponentCharacter):

    #Declare images
    icon_char1 = pygame.image.load('assets/satori.jpeg')
    icon_char2 = pygame.image.load('assets/chongwei.png')
    icon_char3 = pygame.image.load('assets/hangjebat.png')
    icon_char4 = pygame.image.load('assets/qin.png')
    background = pygame.image.load("assets/Fight Page.png")
    pause = pygame.image.load('assets/Pause.png')

    #Declare variables
    message = ""
    fightPeriod = 1
    playerTurn = 1
    game_pause = False

    #Page loop
    while fightPeriod == 1:

        #Mouse position
        Double_Mouse_Pos = pygame.mouse.get_pos()

        #Page background
        screen.blit(background, (0, 0))

        User_Health = get_font(15).render(str(userCharacter[2]), True, "White")
        User_Health_Rect = User_Health.get_rect(center=(375, 175))

        User_Energy = get_font(15).render(str(userCharacter[3]), True, "White")
        User_Energy_Rect = User_Health.get_rect(center=(375, 233))

        Opponent_Health = get_font(15).render(str(opponentCharacter[2]), True, "White")
        Opponent_Health_Rect = User_Health.get_rect(center=(860, 175))

        Opponent_Energy = get_font(15).render(str(opponentCharacter[3]), True, "White")
        Opponent_Energy_Rect = User_Health.get_rect(center=(860, 233))

        message_fight = get_font(15).render(str(message), True, "White")
        message_rect = message_fight.get_rect(center=(480, 490))

        #Universal
        Menu_Button = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")

        Main_Button = Button(image=None, pos=(482, 200), 
                            text_input="MAIN MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Resume_Button = Button(image=None, pos=(482, 300), 
                            text_input="RESUME", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Quit_Button = Button(image=None, pos=(482, 400), 
                            text_input="QUIT", font=get_font(30), base_color="White", hovering_color="Red")
        
        #User buttons
        User_Punch = Button(image=None, pos=(170, 320), 
                            text_input="PUNCH", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        User_Kick = Button(image=None, pos=(300, 320), 
                            text_input="KICK", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        User_Special = Button(image=None, pos=(172, 360), 
                            text_input="SPECIAL", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        User_Charge = Button(image=None, pos=(301, 360), 
                            text_input="CHARGE", font=get_font(17), base_color="White", hovering_color="cadetblue1")

        #Opponent buttons
        Opponent_Punch = Button(image=None, pos=(655, 320), 
                            text_input="PUNCH", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Opponent_Kick = Button(image=None, pos=(785, 320), 
                            text_input="KICK", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Opponent_Special = Button(image=None, pos=(657, 360), 
                            text_input="SPECIAL", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Opponent_Charge = Button(image=None, pos=(786, 360), 
                            text_input="CHARGE", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Menu_Button.changeColor(Double_Mouse_Pos)
        Menu_Button.update(screen)

        screen.blit(User_Health, User_Health_Rect)
        screen.blit(User_Energy, User_Energy_Rect)
        screen.blit(Opponent_Health, Opponent_Health_Rect)
        screen.blit(Opponent_Energy, Opponent_Energy_Rect)
        screen.blit(message_fight, message_rect)
        
        
        #Loads user's icon
        if userCharacter[0] == "SATORI":
            userCharacterIcon(icon_char1, 90, 140)
        elif userCharacter[0] == "CHONG WEI":
            userCharacterIcon(icon_char2, 90, 140)
        elif userCharacter[0] == "HANG JEBAT":
            userCharacterIcon(icon_char3, 90, 140)
        elif userCharacter[0] == "EMPEROR QIN":
            userCharacterIcon(icon_char4, 90, 140)

        #Loads opponent's icon
        if opponentCharacter[0] == "SATORI":
            userCharacterIcon(icon_char1, 575, 140)
        elif opponentCharacter[0] == "CHONG WEI":
            userCharacterIcon(icon_char2, 575, 140)
        elif opponentCharacter[0] == "HANG JEBAT":
            userCharacterIcon(icon_char3, 575, 140)
        elif opponentCharacter[0] == "EMPEROR QIN":
            userCharacterIcon(icon_char4, 575, 140)

        #If the game is paused
        if game_pause == True:
            screen.blit(pause, (0, 0))
            for button in [Main_Button, Resume_Button, Quit_Button]:
                button.changeColor(Double_Mouse_Pos)
                button.update(screen)

        #If it's player 1's turn and the game is not paused, these buttons will appear
        if playerTurn == 1 and game_pause == False:
            for button in [User_Punch, User_Kick, User_Special, User_Charge]:
                button.changeColor(Double_Mouse_Pos)
                button.update(screen)
        
        #If it's player 2's turn and the game is not paused, these buttons will appear
        elif playerTurn == 2 and game_pause == False:
            for button in [Opponent_Punch, Opponent_Kick, Opponent_Special, Opponent_Charge]:
                button.changeColor(Double_Mouse_Pos)
                button.update(screen)
        
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:

                 #If the "MENU" button is clicked, the game will be paused
                if Menu_Button.checkForInput(Double_Mouse_Pos) and game_pause == False:
                    buttonSound.play()
                    game_pause = True

                if game_pause == True:
                    if Resume_Button.checkForInput(Double_Mouse_Pos):
                        buttonSound.play()
                        game_pause = False

                    if Main_Button.checkForInput(Double_Mouse_Pos):
                        buttonSound.play()
                        main_menu()
                    
                    if Quit_Button.checkForInput(Double_Mouse_Pos):
                        buttonSound.play()
                        buttonSound.play()
                        time.sleep(0.3)
                        pygame.quit()
                        sys.exit()
                
                if playerTurn == 1 and game_pause == False:

                    print("Player 1's Turn")

                    User_Action = False
                    User2_Action = True

                    if playerTurn == 1 and User_Action == False:
                        if User_Punch.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 1, userCharacter, opponentCharacter)
                            User_Action = True

                        elif User_Kick.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 2, userCharacter, opponentCharacter)
                            User_Action = True

                        elif User_Special.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 3, userCharacter, opponentCharacter)
                            User_Action = True

                        elif User_Charge.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 4, userCharacter, opponentCharacter)
                            User_Action = True

                        if message == "You don't have enough energy to use that move!":
                            continue
                
                        fightPeriod = checkFighterHealth(userCharacter, opponentCharacter)
                        if fightPeriod == 0 and userCharacter[2] > 0 and opponentCharacter[2] <= 0:
                            results(userCharacter, playerTurn)

                        if User_Action == True:
                            playerTurn = 2
                            User2_Action = False
                
                if playerTurn == 2 and game_pause == False:

                    print("Player 2's Turn")

                    if playerTurn == 2 and User_Action == True:

                        if Opponent_Punch.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 1, opponentCharacter, userCharacter)
                            User2_Action = True

                        elif Opponent_Kick.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 2, opponentCharacter, userCharacter)
                            User2_Action = True

                        elif Opponent_Special.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 3, opponentCharacter, userCharacter)
                            User2_Action = True

                        elif Opponent_Charge.checkForInput(Double_Mouse_Pos):
                            message = userTurn(playerTurn, 4, opponentCharacter, userCharacter)
                            User2_Action = True

                        if message == "You don't have enough energy to use that move!":
                            continue
                
                        fightPeriod = checkFighterHealth(userCharacter, opponentCharacter)
                        if fightPeriod == 0 and userCharacter[2] <= 0 and opponentCharacter[2] > 0:
                            results(opponentCharacter, playerTurn)
                        
                        if User2_Action == True:
                            playerTurn = 1
                            User_Action = False
                    
        pygame.display.update()

#Display a few options of characters for the users to choose.
def characterOption(playerTurn):

    #Page background
    background = pygame.image.load("assets/Character Page.png")
    message = "PLAYER " +str(playerTurn) +" IS CHOOSING FIGHTER...."

    #Page loop
    while True:

        #Mouse position
        Character_Mouse_Pos = pygame.mouse.get_pos()

        #Page background
        screen.blit(background, (0, 0))

        message_character = get_font(15).render(str(message), True, "White")
        message_rect = message_character.get_rect(center=(480, 490))

        #Character buttons
        Character_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Character_c1 = Button(image=None, pos=(147, 390), 
                            text_input="SATORI", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Character_c2 = Button(image=None, pos=(370, 390), 
                            text_input="CHONG WEI", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Character_c3 = Button(image=None, pos=(595, 390), 
                            text_input="HANG JEBAT", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Character_c4 = Button(image=None, pos=(815, 390), 
                            text_input="EMPEROR QIN", font=get_font(17), base_color="White", hovering_color="cadetblue1")
    
        for button in [Character_Menu, Character_c1, Character_c2, Character_c3, Character_c4]:
            button.changeColor(Character_Mouse_Pos)
            button.update(screen)
        
        screen.blit(message_character, message_rect)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run     
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:
                if Character_Menu.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                
                if Character_c1.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    userCharacter = characters[0][:]
                    return userCharacter
                if Character_c2.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    userCharacter = characters[1][:]
                    return userCharacter
                if Character_c3.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    userCharacter = characters[2][:]
                    return userCharacter
                if Character_c4.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    userCharacter = characters[3][:]
                    return userCharacter

        pygame.display.update()

#Display each character for the users to choose and view their stats  
def characterStats():

    background = pygame.image.load("assets/Character Page.png")

    while True:

        #Mouse position
        Character_Mouse_Pos = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        Character_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        Character_c1 = Button(image=None, pos=(147, 390), 
                            text_input="SATORI", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Character_c2 = Button(image=None, pos=(370, 390), 
                            text_input="CHONG WEI", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Character_c3 = Button(image=None, pos=(595, 390), 
                            text_input="HANG JEBAT", font=get_font(17), base_color="White", hovering_color="cadetblue1")
        
        Character_c4 = Button(image=None, pos=(815, 390), 
                            text_input="EMPEROR QIN", font=get_font(17), base_color="White", hovering_color="cadetblue1")

        for button in [Character_Menu, Character_c1, Character_c2, Character_c3, Character_c4]:
            button.changeColor(Character_Mouse_Pos)
            button.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:
                if Character_Menu.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                
                if Character_c1.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    stats(1)
                if Character_c2.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    stats(2)
                if Character_c3.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    stats(3)
                if Character_c4.checkForInput(Character_Mouse_Pos):
                    buttonSound.play()
                    stats(4)

        pygame.display.update()

#Display the game's credits.
def credits():

    background = pygame.image.load("assets/Credits.png")
    
    #Page loop
    while True:

        #Mouse position
        Credits_Mouse_Pos = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        Credits_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")

        Credits_Menu.changeColor(Credits_Mouse_Pos)
        Credits_Menu.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:
                if Credits_Menu.checkForInput(Credits_Mouse_Pos):
                    buttonSound.play()
                    main_menu()

        pygame.display.update()

#Display the tutorials of the game as the guides for the players.
def tutorial():

    page = 1

    #Page loop
    while True:
        
        #If the current page is page 1
        if page == 1:
            background = pygame.image.load("assets/Tutorials.png")
        
        #If the current page is page 2
        elif page == 2:
            background = pygame.image.load("assets/Tutorials(1).png")

        #Mouse position
        Tutorials_Mouse_Pos = pygame.mouse.get_pos()

        #Page background
        screen.blit(background, (0, 0))

        #Buttons instance
        Tutorials_Menu = Button(image=None, pos=(482, 43), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        Tutorials_Next = Button(image=pygame.image.load("assets/next.png"), pos=(830, 300), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        Tutorials_Back = Button(image=pygame.image.load("assets/back.png"), pos=(130, 300), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="cadetblue1")

        Tutorials_Menu.changeColor(Tutorials_Mouse_Pos)
        Tutorials_Menu.update(screen)

        if page == 1:
            Tutorials_Next.changeColor(Tutorials_Mouse_Pos)
            Tutorials_Next.update(screen)

        if page == 2:
            Tutorials_Back.changeColor(Tutorials_Mouse_Pos)
            Tutorials_Back.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:
                if Tutorials_Menu.checkForInput(Tutorials_Mouse_Pos):
                    buttonSound.play()
                    main_menu()
                
                if Tutorials_Next.checkForInput(Tutorials_Mouse_Pos) and page == 1:
                    buttonSound.play()
                    page = 2

                if Tutorials_Back.checkForInput(Tutorials_Mouse_Pos) and page == 2:
                    buttonSound.play()
                    page = 1

        pygame.display.update()

#Display the main menu of the game.
def main_menu():

    userCharacter = ["N/A", "N/A", "N/A", "N/A", "N/A"]
    opponentCharacter = ["N/A", "N/A", "N/A", "N/A", "N/A"]
    lenCharacter = len(characters)

    while True:

        #Page background
        screen.blit(background, (0, 0))

        #Mouse position
        Mouse_Pos = pygame.mouse.get_pos()

        Training_Button = Button(image=None, pos=(480, 310), 
                            text_input="TRAINING", font=get_font(25), base_color="#d7fcd4", hovering_color="cadetblue1")
        Play_Button = Button(image=None, pos=(480, 250), 
                            text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="cadetblue1")
        Character_Button = Button(image=None, pos=(480, 370), 
                            text_input="CHARACTER", font=get_font(25), base_color="#d7fcd4", hovering_color="cadetblue1")
        Tutorials_Button = Button(image=None, pos=(480, 430), 
                            text_input="TUTORIALS", font=get_font(25), base_color="#d7fcd4", hovering_color="cadetblue1")
        Credits_Button = Button(image=None, pos=(480, 490), 
                            text_input="CREDITS", font=get_font(25), base_color="#d7fcd4", hovering_color="cadetblue1")
        Exit_Button = Button(image=None, pos=(480, 550), 
                            text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="Red")

        for button in [Training_Button, Play_Button, Character_Button, Tutorials_Button, Credits_Button, Exit_Button]:
            button.changeColor(Mouse_Pos)
            button.update(screen)
        
        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:

                #If the "TRAINING" button is clicked, this code will run
                if Training_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()

                    if userCharacter[0] == "N/A": #If the user does not has a character, this code will run
                
                        while (playerSelecting == True):

                            if userCharacter[0] == "N/A":
                                playerTurn = 1
                                print("\nPlayer 1 is choosing fighter.....")
                                userCharacter = characterOption(playerTurn)
                                print(userCharacter)
                                continue
                            
                            else:
                                break

                    opponentCharacter = randomPickCharacter(random.randrange(1,lenCharacter + 1)) #Let the program picked the character for the opponent
                    userCharacter = defaultAttribute(userCharacter) #Reset the user's character health and energy to 100
                    opponentCharacter = defaultAttribute(opponentCharacter) #Reset the user's character health and energy to 100
                    training(userCharacter, opponentCharacter)

                #If the "PLAY" button is clicked, this code will run
                if Play_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()

                    if userCharacter[0] == "N/A": #If the user does not has a character, this code will run
                
                        while (playerSelecting == True):

                            if userCharacter[0] == "N/A" and opponentCharacter[0] =="N/A":
                                playerTurn = 1
                                print("\nPlayer 1 is choosing fighter.....")
                                userCharacter = characterOption(playerTurn)
                                print(userCharacter)
                                continue
                            
                            elif opponentCharacter[0] == "N/A":
                                playerTurn = 2
                                print("\nPlayer 2 is choosing fighter.....")
                                opponentCharacter = characterOption(playerTurn) #Loads the character page for the user to choose character
                                print(opponentCharacter)
                                continue
                            
                            else:
                                break

                    userCharacter = defaultAttribute(userCharacter) #Reset the user's character health and energy to 100
                    opponentCharacter = defaultAttribute(opponentCharacter) #Reset the user's character health and energy to 100
                    fightPage(userCharacter, opponentCharacter)

                #If the "CHARACTER" button is clicked, this code will run
                if Character_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    characterStats()

                #If the "TUTORIALS" button is clicked, this code will run
                if Tutorials_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    tutorial()
                
                #If the "CREDITS" button is clicked, this code will run
                if Credits_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    credits()

                #If the "EXIT" button is clicked, this code will run
                if Exit_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    time.sleep(0.3)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#Display the background and general information for each fighter for the players to analyze.
def stats(userOption):

    #Page loop
    while True:
        
        #Mouse position
        Mouse_Pos = pygame.mouse.get_pos()

        #Button instance
        Back_Button = Button(image=None, pos=(482, 43), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="cadetblue1")
        
        if userOption == 1:
            background = pygame.image.load("assets/Satori.png")
            screen.blit(background, (0, 0))
        
        elif userOption == 2:
            background = pygame.image.load("assets/Chong Wei.png")
            screen.blit(background, (0, 0))


        elif userOption == 3:
            background = pygame.image.load("assets/Hang Jebat.png")
            screen.blit(background, (0, 0))
        
        elif userOption == 4:
            background = pygame.image.load("assets/Emperor Qin.png")
            screen.blit(background, (0, 0))
        
        Back_Button.changeColor(Mouse_Pos)
        Back_Button.update(screen)

        #Check events
        for event in pygame.event.get():

            #If the user close the program, it will exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the left mouse is being clicked, this code will run 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == Right:

                #If the "BACK" button is clicked, this code will run
                if Back_Button.checkForInput(Mouse_Pos):
                    buttonSound.play()
                    characterStats()

        pygame.display.update()

#Fix the character's health and energy to default
def defaultAttribute(character): 
        character[2] = 100
        character[3] = 100

        return character

#For the program to randomly select the opponent's character
def randomPickCharacter(opponentOption): 
    return characters[opponentOption - 1][:]

#Will set the fighter's health and energy to default value
def checkFighterHealth(userCharacter, opponentCharacter):

        #If the opponent health is zero or below
        if userCharacter[2] > 0 and opponentCharacter[2] <= 0:
            return 0
        
        #If the user health is zero or below
        elif opponentCharacter[2] > 0 and userCharacter[2] <= 0:
            return 0
        
        else:
            return 1

#Loop the music in the program
mixer.music.play(loops=-1)

#Execute the function main_menu() to start the program.
main_menu()

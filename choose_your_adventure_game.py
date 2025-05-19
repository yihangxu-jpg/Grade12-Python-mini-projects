def game_start():
  
  cover = r""" .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\                                                                    / /\ 
/ /\ \   _  ___   __    __     _   _                                    / /\ \
\ \/ /  / |/ _ \ / /_  / /_   | \ | | ___  _ __ _ __ ___   __ _ _ __    \ \/ /
 \/ /   | | | | | '_ \| '_ \  |  \| |/ _ \| '__| '_ ` _ \ / _` | '_ \    \/ / 
 / /\   | | |_| | (_) | (_) | | |\  | (_) | |  | | | | | | (_| | | | |   / /\ 
/ /\ \  |_|\___/ \___/ \___/  |_| \_|\___/|_|  |_| |_| |_|\__,_|_| |_|  / /\ \
\ \/ /   / ___|___  _ __   __ _ _   _  ___  ___| |_                     \ \/ /
 \/ /   | |   / _ \| '_ \ / _` | | | |/ _ \/ __| __|                     \/ / 
 / /\   | |__| (_) | | | | (_| | |_| |  __/\__ \ |_                      / /\ 
/ /\ \   \____\___/|_| |_|\__, |\__,_|\___||___/\__|                    / /\ \
\ \/ /                       |_|                                        \ \/ /
 \/ /                                                                    \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' """

  print("\033[1;33;40m", cover)
  print("\033[0;37;40m It's year 1066 \n\n Edward the Confessor, who was the previous English king, has just died \n\n The newly crowned English king Harold Godwinson is facing two foreign powerful crown claimants: Harald III of Norway and William, the Duke of Normandy \n\n In history, the death of Harold Godwinson marked the end of the reign of Anglo-Saxon kings of England, and has changed the history of England forever \n\n England and France started to fight with each other since the king of England was once a duke of the King of France. \n\n However, by making different decisions, maybe there are other possibilities for the future of England? \n\n In this game you can play as King Harold to win a chance for yourself and your kingdom.\n\n")



  def StageOne():
    print("Let's travel back to January of 1066, when Edward the Confessor just died. \n\n Your scout has reported the landing of Norwegian army on the east coast of England. \n\n Now, you have two options: \n\n")


    C1 = input("\033[1m A. Stay in your capital Winchester to be safe. \n\nB. Mobilize and lead your army to fight against the Norwegians. \n\n")
    C1 = C1.lower()

    while True: 
      if C1 == 'a':
        print("\n\n\033[0m You are safe...temporarily. \n\n However, you gave a chance for the Norwegians to recover and prepare. The Norwegians and the Normans from Normandy together crushed your army. \n\n You are killed in the siege of Winchester. \n\n\033[1;31m GAME OVER \n\n")
        print("\033[1;35;40m Ending 1 unlocked: \n\n IRRESOLUTE KING\n\n")

        break

      elif C1 == 'b':
        print("\n\n\n\n\033[0m The Norwegians were not ready for battle due to a recent landing. Your sudden strike defeated them in the Battle of Stamford Bridge. One of your crown claimant is not a threat anymore.")
        StageTwo()
        break

      else:
        C1 = input("\033[1m A. Stay in your capital Winchester to stay safe. \n\nB. Mobilize and lead your army to fight against the Norwegians. \n\n")
        C1 = C1.lower()


      


  def StageTwo():
    print("\n\nYou and your nobles celebrates your glorious victory in the Battle of Stamford Bridge. \n\n Yet, you heard a emergency reporting that William, the Duke of Normandy, has led his Norman army landed on the south of England. With the high morale from the last victory, you decided to lead your army to fight against the Norman army, like how you did to the Norwegians. \n\n English and Norman army has met in Hastings in East Sussex, England. \n\n The battle begins. \n\n")

    
    
    print("\nThe Normans attacks first. \n\n Their archers started to fire at your army.")
    print(r""">>>>>----------------------->    >>>>>----------------------->    >>>>>----------------------->""")
    print(r"""  >>>>>----------------------->    >>>>>----------------------->    >>>>>----------------------->""")
    print(r"""    >>>>>----------------------->    >>>>>----------------------->    >>>>>----------------------->""")
    print("What order will you send? \n\n")
    
    while True:
      C2 = input("\033[1m A. Shield walls! \n\nB. Charge! The arrows will not reach us as long as we run fast enough. \n\n")
      C2 = C2.lower()

      if C2 == 'a':
        print("\n\n\033[0m The shield walls work really well. Some of the Norman arrows are missed, the rest were deflected or stopped by the shields")

        StageThree()
        break

      elif C2 == 'b':
        print("\n\n\n\n\033[0mThe Duke of Normandy laughed at you. Half of your soldiers were shot and killed when charging towards the Normans. Those ones who reached the frontline were defeated in the close combat by well prepared Norman soldiers. \n\n You are killed in the battle of Hastings. \n\n\033[1;31m GAME OVER \n\n")

        print("\033[1;35;40m Ending 2 unlocked: RECKLESS KING\n\n")

        break

      else:
        C2 = input("\033[1m A. Shield walls! \n\nB. Charge! The arrows will not reach us as long as we charge fast enough. \n\n")
        C2 = C2.lower()
      
    
      
      
      


  def StageThree():
    print("\n\nThe Norman archers fall back after realizing their arrows don't work really well. \n\n They start to approach your shield walls for a close combat. \n\n Approximately an hour later, the Norman army starts to retreat from the frontline.\n\n You decide to...\n\n")

    print(r"""           /\                                                 /\
 _         )( ______________________   ______________________ )(         _
(_)///////(**)______________________> <______________________(**)\\\\\\\(_)
           )(                                                 )(
           \/                                                 \/""")

    C3 = input("\033[1m A. Retreating must mean their will of fight is destroyed. Shield walls, off! Soldiers, charge! \n\n B. According to the intel we got, the Normans are not as weak as being crushed within an hour. We should be careful and exhaust their forces slowly to win the battle. ")
    C3 = C3.lower()

    while True:
      if C3 == 'a':
        print("\n\n\n\n\033[0m It's a trap! Without the shield walls, the Norman archers soon start to mown down our soildiers. \n\n Our soldiers are separated and then annihilated. After the Norman soldiers outnumber your soldiers, the battle turns in favor of them. \n\n You are killed in the midst of chaos of a battle without any chance to win. \n\n\033[1;31m GAME OVER \n\n")
        print("\033[1;31;40m Ending 3 unlocked: HISTORICAL REAL ENDING\n\n")
        break


      elif C3 == 'b':
        print("\n\n\n\n\033[0m Your patience and cauciusness have paid off. The Duke's army cannot stand with the English environment and a flawless defense. William, the Duke of Normandy, has experienced a great setback and is not likely to invade England in the coming years. \n\n The Battle of Hastings will be recorded in history as a textbook-perfect defensive battle. \n\n")
        print("\033[1;32;40m Ending 4 unlocked: KING HAROLD'S AMBITION\n\n")
        crown = (r"""                                                                                                    

                                               ÆÆÆÆÆÆ                                               
                                             Æ  ÆÆÆÆ                                                
                                             ÆÆÆÆÆÆÆÆÆ                                              
                                             ÆÆÆÆÆÆÆÆÆ                                              
                                             ÆÆÆ ÆÆ ÆÆ                                              
                                                 ÆÆ                                                 
                                               ÆÆÆÆÆÆ                                               
                                             ÆÆÆÆÆÆÆÆÆ                                              
                                             ÆÆÆÆÆÆÆÆÆ                                              
                                  Æ   ÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆ    ÆÆÆÆ   Æ                                  
                                 ÆÆÆÆ  ÆÆÆ     ÆÆÆÆÆÆ     ÆÆÆ  ÆÆÆÆÆ                                
                            ÆÆÆ  ÆÆÆ             Æ              ÆÆÆ  ÆÆÆ                            
                        ÆÆ  ÆÆÆ     ÆÆÆÆÆÆÆÆÆ   ÆÆÆÆ   ÆÆÆÆÆÆÆÆÆ     ÆÆÆ  ÆÆÆ                       
                       ÆÆÆÆ   ÆÆÆÆÆÆÆ      ÆÆÆ   Æ     ÆÆ      ÆÆÆÆÆÆÆ   ÆÆÆÆ                       
                   ÆÆÆ    ÆÆÆÆÆÆ            ÆÆ  ÆÆÆ   ÆÆ             ÆÆÆÆÆ    ÆÆÆÆ                  
               ÆÆ      ÆÆÆÆ                 ÆÆ   ÆÆ   ÆÆ                 ÆÆÆÆ      ÆÆ               
              ÆÆÆÆ  ÆÆÆÆ   Æ                 ÆÆ  Æ   ÆÆÆ                Æ   ÆÆÆÆ   ÆÆÆ              
           ÆÆ     ÆÆÆ     ÆÆÆÆ                   ÆÆ                   ÆÆÆÆ     ÆÆÆÆ    ÆÆ           
           ÆÆ  ÆÆÆÆ      ÆÆÆÆÆÆ              ÆÆÆÆÆÆÆÆÆÆ              ÆÆÆÆÆÆ       ÆÆÆ  ÆÆ           
             ÆÆÆ         ÆÆÆÆÆÆÆ              ÆÆÆÆÆÆÆÆ               ÆÆÆÆÆÆ         ÆÆÆ             
           Æ             ÆÆÆÆÆÆÆ               ÆÆÆÆÆÆ   Æ           ÆÆÆÆÆÆÆ             ÆÆ          
     ÆÆÆÆÆÆ               ÆÆÆÆÆÆÆÆÆÆÆÆÆÆ   ÆÆÆ ÆÆÆÆÆÆ ÆÆÆ    ÆÆÆÆÆÆÆ ÆÆÆÆÆÆ               ÆÆÆÆÆ     
      ÆÆÆÆ  ÆÆ     ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ      Æ   ÆÆÆÆ     
      ÆÆÆÆÆÆÆÆ   ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ   ÆÆÆÆÆÆÆÆ      
      ÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆ   ÆÆÆÆ   ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ   ÆÆÆÆÆÆÆÆ      
      Æ  ÆÆÆÆÆÆ  ÆÆÆÆÆ     ÆÆÆÆÆ      ÆÆ   ÆÆ   ÆÆÆÆ  ÆÆÆ    ÆÆ     ÆÆÆÆÆÆ    ÆÆÆÆÆÆ ÆÆÆÆÆÆ  Æ      
      ÆÆÆÆÆ ÆÆÆÆ ÆÆÆÆ       ÆÆÆÆ               ÆÆÆÆÆÆ                ÆÆÆÆ       ÆÆÆ  ÆÆÆ ÆÆÆÆÆ      
        ÆÆÆ       ÆÆ       ÆÆÆÆÆ               ÆÆÆÆÆÆÆ              ÆÆÆÆÆ       ÆÆ       ÆÆÆ        
         ÆÆÆ               ÆÆÆÆÆÆÆ           ÆÆÆÆÆÆÆÆÆÆÆ          ÆÆÆÆÆÆÆÆ              ÆÆÆ         
         ÆÆÆÆ            ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ            ÆÆÆÆ         
          ÆÆÆÆÆ        ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ        ÆÆÆÆÆÆ         
          ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ       ÆÆÆÆÆ ÆÆÆÆÆÆ     ÆÆÆÆÆÆÆ ÆÆÆÆÆ       ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ          
          ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ          ÆÆÆÆÆÆÆÆÆÆÆÆ    ÆÆÆÆÆÆÆÆÆÆÆÆ          ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ          
          ÆÆÆÆÆÆÆÆÆ  ÆÆÆÆÆÆ         ÆÆÆÆ ÆÆÆÆÆÆÆÆ ÆÆÆÆÆÆÆÆÆ ÆÆÆÆÆ         ÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆ          
          ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ    ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ     ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ ÆÆ          
          ÆÆ   ÆÆÆÆÆ  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ ÆÆÆÆÆ   ÆÆ          
          ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ                            ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ          
            ÆÆÆÆÆÆÆÆÆÆÆÆ        ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ         ÆÆÆÆÆÆÆÆÆÆÆ            
               ÆÆÆ    ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ    ÆÆÆÆ              
                  ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ                  
                 ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ                 
                   ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ                  
                        ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ                        
                                    ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    """)
        print("\033[1;33;40m", crown)


        break

      else:
        C3 = input("\033[1m A. Retreating must mean their will of fight is destroyed. Shield walls, off! Soldiers, charge!\n\nB. According to the intel we got, the Normans are not as weak as being crushed within an hour. We should be careful and exhaust their forces slowly to win the battle. ")
        C3 = C3.lower()
      

  StageOne()



while True:
  game_start()

  res = input("Press 'ENTER' to restart")

  if res != '':
    break


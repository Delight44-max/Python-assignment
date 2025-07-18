print("1. Phone Book")
print("2. Messages")
print("3. Chat")
print("4. Call Register")
print("5. Tones")
print("6. Settings")
print("7. Call Divert")
print("8. Games")
print("9. Calculator")
print("10. Reminders")
print("11. Clock")
print("12. Profiles")
print("13. SIM Services")
print("0. EXIT")

menu = input("Enter menu").strip()

match menu:
    case "1": 
        print("PHONE BOOK\n 1. Search\n 2. Add name\n Erase/ Edit/ Assign tone\n 3. Speed dails\n 4. Voice tags")

    case "2":
        print("MESSAGE\n 1. Write messages\n 2. inbox\n 3. outbox\n 4. picture messages\n 5. Templates\n 6. messages settings")

    case "3":
        print("CHAT\n 1. SMS")

    case "4":
        print("CALL REGISTER\n 1. Missed\n 2. Recieved\n 3. Dailled calls\n 4. call Duration")

    case "5":
        print("TONES\n 1. Ringing tone and volumn\n 2. composer\n 3. Message tone / keypad tone\n 4. vibrating alert/Screen saver")

    case "6":
        print("SETTING\n 1. Call setting\n 2. phone setting\n 3. Message tone / Keypad tone\n 4. Vibrating Alert / Screen settings")

    case "7":
        print("CALL DIVERT\n 1. divert when busy\n 2. unreachable")
    
    case "8":
        print("GAMES\n 1. Snakes\n 2. Space Impact\n 3. Bantumi\n 4. paira")

    case "9":
        print("CALCULATOR\n 1. Alarm clock\n 2. Stopwatch / Countdown timer\n 3. Date & time settings")

    case "10":
        print("REMINDERS\n 1. Short text notes with alarm")

    case "11":
        print("CLOCKS\n 1. Alarm clock\n 2. Stopwatch\n 3. Date & Time settings")
    
    case "12":
        print("PROFILES\n 1. general\n 2. Silent\n 3. Loud\n")

    case "13":
        print("SIM Services\n 1. Moblile bank")

    case "0":
        print("THANKS FOR USING NOKIA\n GOODBYE")

    case _:
        print(" INVALID CHOICE!") 

       
 

        
         
import subprocess, sys
from os import system, name
from time import sleep


msg = ""
Phone_num = ""
repeat = ""


def Ascii():
    clear()
    print("+++++++++++++++++++++++++++++++++++++++.")
    print("++++++++++++++77       77I++++++++++++++")
    print("++++++++++77               77+++++++++++")
    print("========77                   77=========")
    print("=======7                       7========")
    print("======7                         7=======")
    print("=====7                           7======")
    print("=====                             ======")
    print("=====                             ======")
    print("=====                             ======")
    print(
        "=====7                           7======    _ __  __                                "
    )
    print(
        "~~~~~~7                         7~~~~~~~   (_)  \/  |                               "
    )
    print(
        "~~~~~~~7                       7~~~~~~~~    _| \  / | ___  ___ ___  __ _  __ _  ___ "
    )
    print(
        "~~~~~~~~77                   77~~~~~~~~~   | | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \ "
    )
    print(
        "~~~~~~~~~~77               77~~~~~~~~~~~   | | |  | |  __/\__ \__ \ (_| | (_| |  __/"
    )
    print(
        "~~~~~~~~~~~~   77     777I~~~~~~~~~~~~~~   |_|_|  |_|\___||___/___/\__,_|\__, |\___|"
    )
    print(
        "~~~~~~~~~~~ 7I~~~~~~~~~~~~~~~~~~~~~~~~~~                                  __/ |     "
    )
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.                                 |___/     "
    )
    print("\nWith Python!")
    sleep(3)


def intro():
    clear()
    print("Welcome to iMessage for Python.\n")
    print(
        "This Adapts From The AppleScript and Uses Elements From Python to Send Automated Messages to Others.\n"
    )
    print('This Uses US Based Numbers "(+1)" Only.\n')

    print(
        "🚨[WARNING] By Agreeing to Use this Software, Any Liability Due to Misuse Will NOT be Placed On the Author. 🚨"
    )
    sleep(5)


def clear():
    _ = system("clear")


def questions():
    clear()
    global msg, Phone_num, repeat
    print('NO Dashes "-", Spaces "_", or parentheses"()"  or the script WILL Fail.')
    print("Input Ex:XXXXXXXXX\n")
    Phone_num = str(input("Enter Here:"))
    clear()
    print("What is Your Message?\n")
    msg = input("Enter Here:")
    clear()
    print("How Many Times do You Want to Send this Message?\n")
    repeat = input("Enter Here:")
    clear()


def apple():

    applescript = (
        """
    tell application "Messages"
        
        set targetBuddy to "+1 """
        + Phone_num
        + """"
        set targetService to id of 1st service whose service type = iMessage
        set i to 1
        set p to "Sent" 
        repeat {0}
            
            set textMessage to "{1}"
            
            set theBuddy to buddy targetBuddy of service id targetService
            send textMessage to theBuddy
            delay 1
            
            log ("Repeated " & i &" Time(s).") 
            
            set i to i + 1
            
            
        end repeat
        
    end tell
    """.format(
            repeat, msg
        )
    )
    args = [
        item
        for x in [("-e", l.strip()) for l in applescript.split("\n") if l.strip() != ""]
        for item in x
    ]
    proc = subprocess.Popen(["osascript"] + args, stdout=subprocess.PIPE)
    progname = proc.stdout.read().strip()


def finish():

    clear()
    sleep(1.1)
    print(
        "\b\b\b\b\bTexted "
        + Phone_num
        + ' With the Message:"'
        + msg
        + '" '
        + repeat
        + " Times!"
    )


def main():
    Ascii()
    intro()
    questions()
    apple()
    finish()


if __name__ == "__main__":
    main()

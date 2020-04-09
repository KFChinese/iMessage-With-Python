from tkinter import *
import subprocess, sys

import webbrowser

from PIL import Image, ImageTk


class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))  # skip to next frame
        except EOFError:
            pass  # we're done

        try:
            self.delay = im.info["duration"]
        except KeyError:
            self.delay = 100

        first = seq[0].convert("RGBA")
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert("RGBA")
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)


root = Tk()
anim = MyLabel(root, "animated.gif")
anim.grid(row=1, column=1)


def stop_it():
    anim.after_cancel(anim.cancel)


def instructions():
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ")


def click():

    msg = messages.get()
    repeat = three_peats.get()
    Phone_num = phone.get()
    label = "Sent To iMessage!"
    labels["text"] = label
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


root.title("Python iMessage")

Label(root, text="Automatic iMessage With Python", font=("San Francisco", 24)).grid(
    row=0, column=1
)
Button(root, text="Stop Animation", command=stop_it).grid(row=1, column=2)
Label(root, text="Ex Ph No.: XXXXXXXXXX").grid(row=2, column=0)
Label(
    root,
    text="(NO Dashes '-', Spaces '_', or parentheses'()' or the script WILL Fail.)",
).grid(row=2, column=1)
Label(root, text="Phone No.:",).grid(row=3, column=0)
phone = Entry(root)
Label(root, text="repeat Qty.:",).grid(row=4, column=0)
three_peats = Entry(root)
Label(root, text="iMessage:",).grid(row=5, column=0)
messages = Entry(root)

Button(root, text="Send", command=click).grid(row=3, column=2)

Button(root, text="Instructions", command=instructions).grid(row=4, column=2)

Button(root, text="Quit", command=root.destroy).grid(row=5, column=2)

phone.grid(row=3, column=1)
three_peats.grid(row=4, column=1)
messages.grid(row=5, column=1)

labels = Label(root)
labels.grid(row=2, column=2)

root.resizable(0, 0)

root.iconbitmap("py.ico")

root.mainloop()

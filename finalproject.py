# Name: Toby
# Period: 7th
# Assignment: Final Project
# Time Spent: I worked on it for 18 days, maybe 18 hours spent I think. I don't know.

# Imports tkinter and random and messagebox
import tkinter as tk
import random
from tkinter import messagebox

# words for Hangman Game
words = ["scholar", "prophets", "final", "huh", "familyguy", "google", "etc", "dog", "cat", "unfathomable", "indubitably"]
word = random.choice(words)

# Blanket for where the game is going to happen
class game(tk.Tk):   
    def __init__(self):
        super().__init__()
        self.letterGuessed = ''
        # title of the window
        self.title("Fight an Evil Wizard.")

        # calls to center the screen
        self.center()

        # generates a random word using the very complex and hard to master code contained inside of randomWord
        self.randomWord()

        # runs the wizard narration
        run_wiz = wizard(self, self.randWord)

        # shows the wizard narration
        run_wiz.pack()

        # makes entry box
        self.entryb()

        # makes a button to submit things, calls checker1 when pressed
        myButton = tk.Button(self, text="Submit", command=self.checker1)
        myButton.pack(pady=10)

    # centers the screen, thanks to geeks for geeks.
    def center(window):
        window.update_idletasks()
        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()
        width += 500 
        height += 40
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    # makes an entrybox
    def entryb(self):
        self.EntryBox = tk.Entry(self, width=50, borderwidth=5)
        self.EntryBox.pack()

    # generates the requirement of amount of words that the user will need to use to pass phase 1
    def randomWord(self):
        self.randWord = random.randint(1,6)

    # this checks if the user enters the correct amount of words for phase 1. 
    # firstAnsRight is if the user is right.
    # firstAnsWrong is for if the user is wrong.
    def checker1(self):
        # gets the user's input
        checker = self.EntryBox.get()
        # checks its length
        check_words = len(checker.split())
        # trys to check if the amount of words you used matches the amount of words required, any exception handled and told to user through the terminal
        # If-else to check if you are right or not
        try:
            if check_words == self.randWord:
                firstAnsRight = tk.Label(self, text="CORRECT!")
                firstAnsRight.pack()
                self.after(1000, self.phase_two)
            else:
                firstAnsWrong = tk.Label(self, text="Wrong! DESTROY!")
                firstAnsWrong.pack()
                self.after(1000, self.destroy)
        except Exception as e:
            print(f"Cause of Death: {e}")

# starts the second phase
    def phase_two(self):

        # destroys previous widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Wizard is now saying something else. .pack() on the same line so I don't have to make this a variable
        tk.Label(text="'I like how you think. Now, you must guess the word I'm thinking of!\nIf you don't do it within 12 guesses, you will be DESTROYED!'").pack()

        # holds the _ that match however many letters are in the word selected
        wordsplaceholder = []
        for _ in word:
            wordsplaceholder.append("_")
        
        # how many guesses the user has
        self.guesses = 12

        # makes a Label which shows how many _'s there are, which correleates to the amount of letters in the word
        self.hiddenword = tk.Label(text=wordsplaceholder)
        self.hiddenword.pack()
        # makes an entry box
        self.hangmanentry = tk.Entry(self, width=50, borderwidth=5)
        self.hangmanentry.pack()
        # makes a button which, when pressed, calls checker2
        self.myButton2 = tk.Button(self, text="Submit", command=self.checker2)
        self.myButton2.pack(pady=10)

        
# second checker
    def checker2(self):
        # gets the user's entry in a lowercase format
        checker_2 = self.hangmanentry.get().lower()
        self.hangmanentry.delete(0, tk.END)
        # checks if the user only put in one letter or if they did wrong
        if len(checker_2) != 1:
            return
        # Try Except for the If, For, If, and If.
        try:
            # Checks the letter the user submitted then compares it to the word selected
            if checker_2 in word.lower():
                self.letterGuessed += checker_2 * word.count(checker_2)
            # temp list made to figure out what the _'s in the label should look like
            display_chars = []
            # for character in word, add to the display_chars and make the addition be a character from the letter gussed
            for char in word:
                if char in self.letterGuessed:
                    display_chars.append(char)
                else:
                    display_chars.append('_')
            self.hiddenword.config(text=" ".join(display_chars))

            # If no _, then you win this section and wizard threatens you
            if "_" not in display_chars:
                threat = messagebox.askyesno("You've won for now...",  "But just you wait! in ten years, I will come back to get you!\nDO YOU UNDERSTAND ME?!")
                self.myButton2.config(state="disabled")
                if threat:
                    self.phase_three()
                else:
                    self.phase_three()
            # If wrong guess, remove the amount of guesses you have left by one.
            if checker_2 not in word.lower():
                self.guesses -= 1
                secAnsWrong = tk.Label(self, text=f"Try Again! {self.guesses} guesses left.")
                secAnsWrong.pack()
                self.after(2000, secAnsWrong.destroy)
                # destroy if no guesses left
                if self.guesses <= 0:
                    self.destroy()
        
        except Exception as e:
            print(f"Cause of Death: {e}")
    # phase three
    def phase_three(self):
        # deletes previous widgets
        for widget in self.winfo_children():
            widget.destroy()
        # backstory
        self.finalWizz = tk.Label(self, text="Ten years have passed since the wizard vowed to come back for you...\nEverything seems fine. That is, until one day the wizard appears in a cloud of smoke in front of you!")
        self.finalWizz.pack()
        # after five seconds, make the wizard deliever Full Power Frieza's line when he decides to take Super Saiyan Goku's mercy for granted
        self.after(5000, self.configurefinalWizz)
    # The finale of the wizzard
    def configurefinalWizz(self):
        # It's over. Never hurt anyone EVER AGAIN.
        self.finalWizz.config(text="The wizard says: 'I'm the STRONGEST in the UNIVERSE! And that is why... \nYou... Horrible... You must...\nYOU MUST DIE BY MY HAND!!!'", font=("Times New Roman", 16, "bold"), fg="Purple", height=4, relief="groove")

        self.finalEntryBox = tk.Entry(self, width=50, borderwidth=5)
        self.finalEntryBox.pack()
        self.myButton3 = tk.Button(self, text="Submit", command=self.final_check)
        self.myButton3.pack(pady=10)

    def final_check(self):
        youfool = self.finalEntryBox.get().upper()
        ssjgokuquotes = {"YOU FOOL", "YOU FOOL!", "YOU FOOL!!", "YOU FOOL!!!", "YOU MORON!!!", "Huh? You fool! Ha!", "YOU MORON", "YOU MORON!", "YOU MORON!!", "You foolish bastard!", "BAKAYARO!", "bakayarō!", "ESTUPIDO!"}
        ssjgokuquotes_upper = {item.upper() for item in ssjgokuquotes}
        try:
            if youfool in ssjgokuquotes_upper:
                for widget in self.winfo_children():
                    widget.destroy()
                self.config(bg="#3F3F36")
                self.super_final_label = tk.Label(self, text="You angrily fire a large wave of ki at the wizard.\n This wipes him off the face of the universe.\nYou win.", fg="#FFDD00", bg="#3F3F36", font=("Arial", 16, "bold"), height=4)
                self.super_final_label.pack()
                self.quit_button = tk.Button(self, text="Quit", command=self.destroy)
                self.quit_button.pack(pady=50)
            else:
                for widget in self.winfo_children():
                    widget.destroy()
                self.config(bg="#35063e")
                super_final_loss = tk.Label(self, text="The evil wizard got his revenge on you through a sneak attack.\nYou lose.", font=("Times New Roman", 16, "bold"), fg="#CBC3E3", bg="#35063e", height=4, relief="groove")
                super_final_loss.pack()
                self.quit_button = tk.Button(self, text="Quit", command=self.destroy)
                self.quit_button.pack(pady=50)
        except Exception as e:
            print(f"Cause of Death: {e}")

# blanket for stuff involving the wizard
class wizard(tk.Frame):
    def __init__(self, parent, number):
        super().__init__(parent)
        self.number = number
        self.backstory()
        self.after(5000, self.wizardspeech)

    def backstory(self):
        self.backstoryLabel = tk.Label(self, text="You have stumbled into a wrecked town after waking up in the middle of nowhere.\nYou come across a sterotypical looking wizard who has something to say.")
        self.backstoryLabel.pack(pady=20)

    def wizardspeech(self):
        ampm = ("PM", "AM")
        ampm_rand = random.choice(ampm)
        self.backstoryLabel.config(text=f"He says: 'This town has been destroyed by a {self.number} eyed monster! This happened at {random.randint(1,12)}:{random.randint(0,59)} {ampm_rand}!\nWhat say you, you {random.randint(0,32)}-toothed freak?!")
        self.after(5000, self.show_hint)

    def show_hint(self):
        helloneighbor = tk.Label(self, text="Hint: One of these numbers correlates to the amount of words you should say.")
        helloneighbor.pack(pady=5)
# works
def main():
    app = game()
    app.mainloop()        

if __name__ == "__main__":
    main()


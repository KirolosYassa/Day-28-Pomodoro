from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

#Image
canvas = Canvas(width=300, height=250, bg=YELLOW, highlightthickness=0, )
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 100, image=tomato_img)

canvas.create_text(150, 120, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")
canvas.pack()

# start_button = Button(50, 200, text="Start") 
# reset_button = Button(250, 200, text="reset") 

# start_button.pack()
# reset_button.pack()

window.mainloop()
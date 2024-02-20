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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_timer():
    global reps
    
    Work_in_SECONDS = WORK_MIN * 60
    Short_Break_in_SECONDS = SHORT_BREAK_MIN * 60
    Long_Break_in_SECONDS = LONG_BREAK_MIN * 60
    
    reps += 1
    
    if reps in [1, 3, 5, 7]:
        timer_label.config(text="Work", foreground=GREEN)
        countdown(count=Work_in_SECONDS)
    elif reps in [2, 4, 6]:
        timer_label.config(text="Break", foreground=PINK)
        countdown(count=Short_Break_in_SECONDS)
    elif reps == 8:
        timer_label.config(text="Break", foreground=RED)
        countdown(count=Long_Break_in_SECONDS)
    
    

def countdown(count):
    
    minutes_remaining = int(count / 60)
    seconds_remaining = int(count % 60)
    
    if minutes_remaining < 10:
        minutes_remaining = f"0{minutes_remaining}"
    if seconds_remaining < 10:
        seconds_remaining = f"0{seconds_remaining}"
    
    canvas.itemconfig(timer_count, text = f"{minutes_remaining}:{seconds_remaining}")
    
    if count > 0:
        window.after(1, countdown, count - 1)
    else:
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 38, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

#Image
canvas = Canvas(width=300, height=250, bg=YELLOW, highlightthickness=0, )
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 100, image=tomato_img)

timer_count = canvas.create_text(150, 120, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer) 
reset_button = Button(text="reset") 

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

checkMark_label = Label(text="✔️", font=(35), fg=GREEN, bg=YELLOW)
checkMark_label.grid(row=2, column=1)



window.mainloop()
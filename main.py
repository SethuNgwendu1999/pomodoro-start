from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
COLS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global REPS
    REPS = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    header.config(text="Timer", fg=GREEN, bg=YELLOW, font=("ariel", 50, "bold"))
    tick.config(text="")






# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    print(REPS)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        header.config(text="Break", fg=PINK, bg=YELLOW, font=("ariel", 50, "bold"))

    elif REPS % 2 == 0:
        count_down(short_break_sec)
        header.config(text="Break", fg=PINK, bg=YELLOW, font=("ariel", 50, "bold"))

    else:
        count_down(work_sec)
        header.config(text="Work", fg=GREEN, bg=YELLOW, font=("ariel", 50, "bold"))

    # count_down(1 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global COLS

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += "✔"
        tick.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro-start")
window.config(padx=100, pady=50, bg=YELLOW)

header = Label(text="Timer", fg=GREEN, bg=YELLOW)
header.config(font=("ariel", 50, "bold"))
header.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.config(font=("ariel", 10, "bold"))
start.grid(column=0, row=2)

tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

start = Button(text="Reset", highlightthickness=0, command=reset_timer)
start.config(font=("ariel", 10, "bold"))
start.grid(column=2, row=2)

window.mainloop()

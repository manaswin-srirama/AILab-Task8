import tkinter as tk
import random

WORDS = ["TIGER","APPLE","GRAPE","PLANT","STONE",
         "CRANE","PLANE","CHAIR","SHEEP","BRICK"]

GRID = 5

solution = []
entries = []
score = 0
time_left = 0
timer_running = False
dark_mode = True


def generate_puzzle():
    word = random.choice(WORDS)
    grid = [["" for _ in range(GRID)] for _ in range(GRID)]

    # place word horizontally
    row = random.randint(0,4)
    for i in range(5):
        grid[row][i] = word[i]

    return grid


def create_board():

    global solution

    solution = generate_puzzle()

    for widget in board.winfo_children():
        widget.destroy()

    entries.clear()

    for r in range(GRID):

        row_entries = []

        for c in range(GRID):

            e = tk.Entry(
                board,
                width=2,
                font=("Arial",24,"bold"),
                justify="center",
                relief="solid",
                bd=2
            )

            e.grid(row=r,column=c,padx=6,pady=6)

            # randomly show hint
            if solution[r][c] != "" and random.random() < 0.4:
                e.insert(0,solution[r][c])
                e.config(state="disabled")

            row_entries.append(e)

        entries.append(row_entries)


def check_puzzle():

    global score

    correct = True

    for r in range(GRID):
        for c in range(GRID):

            if solution[r][c] != "":

                val = entries[r][c].get().upper()

                if val == solution[r][c]:
                    entries[r][c].config(bg="lightgreen")

                else:
                    entries[r][c].config(bg="#ff8080")
                    correct = False

    if correct:
        score += 10
        score_label.config(text=f"Score: {score}")
        result_label.config(text="🎉 Correct Word!")


def start_game():

    global time_left, timer_running

    try:
        time_left = int(timer_entry.get())
    except:
        time_left = 60

    timer_running = True
    update_timer()


def update_timer():

    global time_left

    if timer_running:

        timer_label.config(text=f"Time: {time_left}")

        if time_left > 0:
            time_left -= 1
            root.after(1000,update_timer)

        else:
            result_label.config(text="⏰ Time Up!")


def new_game():
    create_board()
    result_label.config(text="")


def toggle_theme():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        root.config(bg="#1e1e1e")
        title.config(bg="#1e1e1e",fg="white")
        board.config(bg="#1e1e1e")

    else:
        root.config(bg="white")
        title.config(bg="white",fg="black")
        board.config(bg="white")


root = tk.Tk()
root.title("Word Puzzle Game")
root.geometry("420x520")

root.config(bg="#1e1e1e")

title = tk.Label(root,text="Word Puzzle Game",
                 font=("Arial",26,"bold"),
                 fg="white",bg="#1e1e1e")

title.pack(pady=15)

score_label = tk.Label(root,text="Score: 0",
                       font=("Arial",14),
                       fg="white",bg="#1e1e1e")
score_label.pack()

timer_label = tk.Label(root,text="Time: 0",
                       font=("Arial",14),
                       fg="white",bg="#1e1e1e")
timer_label.pack()

timer_frame = tk.Frame(root,bg="#1e1e1e")
timer_frame.pack(pady=8)

tk.Label(timer_frame,text="Set Time:",
         fg="white",bg="#1e1e1e").pack(side="left")

timer_entry = tk.Entry(timer_frame,width=5)
timer_entry.insert(0,"60")
timer_entry.pack(side="left")

start_btn = tk.Button(root,text="Start Game",
                      command=start_game,
                      bg="#28a745",fg="white",
                      width=15)
start_btn.pack(pady=5)

board = tk.Frame(root,bg="#1e1e1e")
board.pack(pady=20)

create_board()

btn_frame = tk.Frame(root,bg="#1e1e1e")
btn_frame.pack()

check_btn = tk.Button(btn_frame,text="Check",
                      command=check_puzzle,
                      bg="#007acc",fg="white",
                      width=10)
check_btn.grid(row=0,column=0,padx=5)

new_btn = tk.Button(btn_frame,text="New Puzzle",
                    command=new_game,width=10)
new_btn.grid(row=0,column=1,padx=5)

theme_btn = tk.Button(btn_frame,text="Toggle Theme",
                      command=toggle_theme,width=12)
theme_btn.grid(row=0,column=2,padx=5)

result_label = tk.Label(root,text="",
                        font=("Arial",14),
                        fg="lightgreen",
                        bg="#1e1e1e")

result_label.pack(pady=10)

root.mainloop()

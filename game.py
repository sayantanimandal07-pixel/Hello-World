import tkinter as tk
import random

# -----------------------------
# GAME SETTINGS
# -----------------------------
score = 0
lives = 3
level = 1
clicks = 0

# -----------------------------
# RANDOM EVENTS
# -----------------------------
events = [
    ("💰 JACKPOT!", 50, 0),
    ("😂 Why did you press it?!", 10, 0),
    ("💣 BOOM! You lost a life!", 0, -1),
    ("👻 A GHOST APPEARED!", 20, 0),
    ("🎁 Mystery Bonus!", 30, 0),
    ("😈 The button is angry...", -20, 0),
    ("🍀 Lucky Click!", 40, 0),
    ("💀 BAD CHOICE!", 0, -1),
    ("🚀 SUPER BOOST!", 100, 0),
    ("🤖 The AI is watching you...", 5, 0)
]

# -----------------------------
# BUTTON CLICK FUNCTION
# -----------------------------
def press_button():

    global score, lives, level, clicks

    clicks += 1

    # Random event
    message, points, life_change = random.choice(events)

    score += points
    lives += life_change

    # Prevent negative score
    if score < 0:
        score = 0

    # Level increases every 5 clicks
    level = (clicks // 5) + 1

    # Update labels
    score_label.config(text=f"💰 Score: {score}")
    lives_label.config(text=f"❤️ Lives: {lives}")
    level_label.config(text=f"🔥 Level: {level}")

    message_label.config(text=message)

    # Change button position
    move_button()

    # Random button text
    button_texts = [
        "DON'T PRESS ME 😈",
        "STOP! 🛑",
        "SERIOUSLY?! 😭",
        "ONE MORE CLICK? 👀",
        "NOOOOO! 💀",
        "WHY?! 😂",
        "PRESS AGAIN 😈"
    ]

    button.config(text=random.choice(button_texts))

    # Change background randomly
    colors = [
        "#111111",
        "#1a0033",
        "#001a33",
        "#330000",
        "#003300",
        "#222222"
    ]

    root.config(bg=random.choice(colors))

    # Game over
    if lives <= 0:
        game_over()


# -----------------------------
# MOVE BUTTON
# -----------------------------
def move_button():

    x = random.randint(50, 500)
    y = random.randint(200, 450)

    button.place(x=x, y=y)


# -----------------------------
# GAME OVER
# -----------------------------
def game_over():

    button.place_forget()

    message_label.config(
        text=f"💀 GAME OVER!\n\nFinal Score: {score}\nClicks: {clicks}",
        font=("Arial", 24, "bold")
    )

    restart_button.place(
        relx=0.5,
        rely=0.8,
        anchor="center"
    )


# -----------------------------
# RESTART GAME
# -----------------------------
def restart_game():

    global score, lives, level, clicks

    score = 0
    lives = 3
    level = 1
    clicks = 0

    root.config(bg="#111111")

    score_label.config(text="💰 Score: 0")
    lives_label.config(text="❤️ Lives: 3")
    level_label.config(text="🔥 Level: 1")

    message_label.config(
        text="I BET YOU CAN'T RESIST... 😈",
        font=("Arial", 18, "bold")
    )

    restart_button.place_forget()

    button.config(
        text="DON'T PRESS ME 😈"
    )

    move_button()


# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()

root.title("DON'T PRESS THE BUTTON 😈")
root.geometry("600x600")
root.resizable(False, False)

root.config(bg="#111111")


# -----------------------------
# TITLE
# -----------------------------

title = tk.Label(
    root,
    text="⚠️ DON'T PRESS THE BUTTON ⚠️",
    font=("Arial", 24, "bold"),
    fg="red",
    bg="#111111"
)

title.pack(pady=20)


# -----------------------------
# SCORE
# -----------------------------

score_label = tk.Label(
    root,
    text="💰 Score: 0",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111"
)

score_label.place(x=30, y=80)


# -----------------------------
# LIVES
# -----------------------------

lives_label = tk.Label(
    root,
    text="❤️ Lives: 3",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111"
)

lives_label.place(x=250, y=80)


# -----------------------------
# LEVEL
# -----------------------------

level_label = tk.Label(
    root,
    text="🔥 Level: 1",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111"
)

level_label.place(x=470, y=80)


# -----------------------------
# MESSAGE
# -----------------------------

message_label = tk.Label(
    root,
    text="I BET YOU CAN'T RESIST... 😈",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#111111"
)

message_label.pack(pady=40)


# -----------------------------
# THE EVIL BUTTON 😈
# -----------------------------

button = tk.Button(
    root,
    text="DON'T PRESS ME 😈",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    activebackground="darkred",
    activeforeground="white",
    padx=20,
    pady=10,
    command=press_button
)

button.place(x=200, y=250)


# -----------------------------
# RESTART BUTTON
# -----------------------------

restart_button = tk.Button(
    root,
    text="🔄 PLAY AGAIN",
    font=("Arial", 15, "bold"),
    bg="green",
    fg="white",
    padx=20,
    pady=10,
    command=restart_game
)


# -----------------------------
# START GAME
# -----------------------------

root.mainloop()

import requests
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import io

# Fetch Pokémon data from PokéAPI and extract key battle stats and sprite info
def fetch_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        sprite_url = data['sprites']['front_default']

        pokemon = {
            'name': data['name'].capitalize(),
            'hp': stats.get('hp', 50),
            'attack': stats.get('attack', 50),
            'defense': stats.get('defense', 50),
            'speed': stats.get('speed', 50),
            'height': data['height'],
            'weight': data['weight'],
            'types': [t['type']['name'] for t in data['types']],
            'sprite_url': sprite_url
        }
        return pokemon
    except requests.exceptions.RequestException:
        return None

# Simulates a turn-based battle between two Pokémon based on their stats
def battle(pokemon1, pokemon2):
    log = []

    # Determine which Pokémon goes first based on speed
    if pokemon1['speed'] >= pokemon2['speed']:
        attacker, defender = pokemon1, pokemon2
    else:
        attacker, defender = pokemon2, pokemon1

    log.append(f"{attacker['name']} attacks first due to higher speed!\n")

    # Turn-based damage exchange until one Pokémon faints
    while pokemon1['hp'] > 0 and pokemon2['hp'] > 0:
        damage = max(1, attacker['attack'] - defender['defense'] + random.randint(-5, 5))
        defender['hp'] -= damage
        log.append(f"{attacker['name']} deals {damage} damage to {defender['name']}. {defender['name']} HP left: {max(defender['hp'], 0)}")

        if defender['hp'] <= 0:
            winner = attacker['name']
            break

        attacker, defender = defender, attacker  # Swap turns

    log.append(f"\nWinner: {winner}!")
    return log

# Saves the most recent battle log to a text file
def save_battle_log(log, filename="battle_log.txt"):
    try:
        with open(filename, 'w') as file:
            for line in log:
                file.write(line + "\n")
        messagebox.showinfo("Saved", f"Battle log saved to {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving battle log: {e}")

# Loads and resizes the Pokémon sprite image from URL
def load_sprite(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((96, 96))  # Resize to fit nicely in GUI
        return ImageTk.PhotoImage(img)
    except:
        return None

# Handles user input, runs battle, and updates GUI with results and images
def start_battle():
    p1_name = entry_p1.get().strip()
    p2_name = entry_p2.get().strip()

    if not p1_name or not p2_name:
        messagebox.showerror("Input Error", "Please enter both Pokemon names.")
        return

    p1 = fetch_pokemon(p1_name)
    p2 = fetch_pokemon(p2_name)

    if not p1 or not p2:
        messagebox.showerror("Fetch Error", "Failed to fetch one or both Pokemon. Please check the names and try again.")
        return

    sprite1 = load_sprite(p1['sprite_url'])
    sprite2 = load_sprite(p2['sprite_url'])

    if sprite1:
        label_sprite1.configure(image=sprite1)
        label_sprite1.image = sprite1  # Keep reference to avoid garbage collection

    if sprite2:
        label_sprite2.configure(image=sprite2)
        label_sprite2.image = sprite2

    log = battle(p1, p2)

    text_area.delete(1.0, tk.END)
    for line in log:
        text_area.insert(tk.END, line + "\n")

    global last_battle_log
    last_battle_log = log

# Called when save button is clicked, writes the last battle log if available
def save_last_battle():
    if last_battle_log:
        save_battle_log(last_battle_log)
    else:
        messagebox.showwarning("No Battle", "No battle to save yet.")

# ---------------- GUI Setup ----------------

app = tk.Tk()
app.title("Pokemon Battle Simulator")

# Input section
label_p1 = tk.Label(app, text="Enter First Pokemon Name:")
label_p1.pack()
entry_p1 = tk.Entry(app)
entry_p1.pack()

label_p2 = tk.Label(app, text="Enter Second Pokemon Name:")
label_p2.pack()
entry_p2 = tk.Entry(app)
entry_p2.pack()

# Button to start the battle
start_button = tk.Button(app, text="Start Battle", command=start_battle)
start_button.pack(pady=5)

# Area for displaying Pokémon sprites
sprite_frame = tk.Frame(app)
sprite_frame.pack()
label_sprite1 = tk.Label(sprite_frame)
label_sprite1.pack(side=tk.LEFT, padx=10)
label_sprite2 = tk.Label(sprite_frame)
label_sprite2.pack(side=tk.RIGHT, padx=10)

# Text area to show battle log
text_area = scrolledtext.ScrolledText(app, width=60, height=20)
text_area.pack(pady=10)

# Button to save the battle log
save_button = tk.Button(app, text="Save Battle Log", command=save_last_battle)
save_button.pack(pady=5)

# Stores the last completed battle log for saving
last_battle_log = []

# Start the GUI loop
app.mainloop()

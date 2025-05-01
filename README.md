# 🌟 Pokemon Battle Simulator (Python + Tkinter)

A GUI-based Pokémon battle simulator built with Python and Tkinter, using real-time data from the PokéAPI. This project allows users to input two Pokémon names, visualize their sprites, and simulate a turn-based battle using their actual stats.

---

## 🔧 Features

- ✨ Real-time stat fetching from [PokéAPI](https://pokeapi.co/)
- 🎭 GUI interface using `tkinter` for user input, battle display, and image rendering
- ⚔️ Turn-based battle simulation based on HP, attack, defense, and speed
- 📃 Scrollable battle log with option to save as `.txt`
- ❄ Graceful error handling for invalid inputs or connection issues

---

## 📊 Demo

![Screenshot](screenshot.png) <!-- Replace with your actual screenshot filename -->

---

## ⚡ Requirements

- Python 3.7+
- `requests`
- `Pillow`

Install requirements with:
```bash
pip install requests pillow
```

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pokemon-battle-simulator.git
cd pokemon-battle-simulator
```

2. Run the script:
```bash
python pokemon_battle_gui.py
```

3. Enter two Pokémon names in the GUI and click **Start Battle**.

4. View the battle log and optionally click **Save Battle Log** to export it.

---

## 🎓 Learning Highlights

- Consumed REST APIs and parsed JSON responses
- Built modular, reusable Python functions
- Applied conditional logic and flow control
- Managed GUI state and user interaction
- Practiced clean commenting and structured code

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 👋 Acknowledgments

- [PokéAPI](https://pokeapi.co/) for providing public Pokémon data and sprites
- Python `tkinter` and `Pillow` documentation
- Code guidance and conceptual support via OpenAI's ChatGPT

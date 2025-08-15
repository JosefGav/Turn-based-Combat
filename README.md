As a requirement for my **Grade 10 Computer Science course**, this game was developed using the [CMU Academy Online Graphics IDE](https://academy.cs.cmu.edu/).  

Due to limitations of the IDE:
- The entire game is written in **a single file**.
- All images are pulled from the internet at runtime — if they're removed from the source, the game may fail to load properly.
- You can try the game here (fullscreen button in top right corner):  
  🔗 [Play the Game](https://academy.cs.cmu.edu/sharing/cyanCow5780)  
  ⚠️ *Note: This link may not always function due to external image dependencies.*

## 🎮 How to Play

1. **Select Your Characters**
   - Use the **arrow keys on-screen** to choose your team.
   - **Hold `i`** while hovering over a character to view stats.

2. **Start the Game**
   - Press **“Play”** when ready.
   - ⏳ *Be patient — the game may take some time to load.*

3. **Win Conditions**
   - Defeat all opposing players, **or**
   - Destroy the enemy **vault**.

4. **Controls & Turn Rules**
   - Each player gets **1 move** and **1 attack** per turn.
   - **To move:** drag and drop the character.
   - **To attack:**
     - Hover over your character
     - Press **`a`**
     - Click on your target
   - Hover + hold **`i`** to view any player’s health and stats.
   - End your turn by clicking **“End Turn”** in the top left.

5. **Important Notes**
   - ❗ *Do not click “End Turn” twice in a row — it will skip your next turn.*
   - Wait for **“Your Turn”** (top right) before making a move.
   - When it says **“Enemies Turn”**, sit tight — the enemy team is acting.

---
## 🧠 Technical Highlights

- **Object-Oriented Programming (OOP):**  
  The game was designed using OOP principles. Each game entity (e.g., characters, tiles, and structures) is represented as a class, with encapsulated properties and behaviors. This allowed for scalable code organization and made it easier to manage game state, actions, and interactions.

- **Pathfinding Algorithm:**  
  Players and enemies use **pathfinding algorithm** to determine the shortest path across the game map, ensuring that characters move within legal bounds, avoid obstacles, and follow strategic paths.

- **Turn-Based Logic:**  
  The game enforces a turn-based structure where each unit gets one move and one attack per round. Game flow is controlled using a state machine that switches between player turns and enemy turns.

- **Real-Time UI Feedback:**  
  Player stats (health, attack, etc.) are accessible in-game by hovering and holding the **`i`** key. This interactivity provides a smoother user experience without cluttering the screen.

- **Single-File Design (Due to IDE limitations):**  
  Although the entire project is contained in one file, it’s structured in a modular way internally using functions and classes.

- **External Image Loading:**  
  Sprites and visuals are pulled directly from online sources at runtime, due to limitations of the CMU IDE.
---

## 🖥️ Running the File Locally

🚧 *Coming soon...*  
Instructions for downloading and running the file locally (outside the CMU IDE) will be added here in a future update.


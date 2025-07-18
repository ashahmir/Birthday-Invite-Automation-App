# Birthday Invitation Letter Generator 🎉

This Python script automatically personalizes birthday invitation letters for a list of names and saves each customized letter as a `.txt` file. The core idea is to take a base invitation letter containing a placeholder (`[name]`) and replace it with actual names from a text file.

## 📂 Project Structure

├── Input
│ ├── Letters
│ │ └── starting_letter.txt
│ └── Names
│ └── invited_names.txt
├── Output
│ └── ReadyToSend
│ └── [name].txt ← personalized letters will be saved here
└── main.py ← the script that generates the letters

📜 How It Works
  Reads a list of names from invited_names.txt
  
  Loads the template letter from starting_letter.txt
  
  Replaces the [name] placeholder with each name from the list
  
  Saves the customized letters in the Output/ReadyToSend/ directory

🚀 Usage
  Put your base letter with [name] placeholder in Input/Letters/starting_letter.txt
  
  Add names (one per line) in Input/Names/invited_names.txt
  
  Find the personalized invitations in the Output/ReadyToSend/ folder.

🧠 Author
Shahmir Ali

Feel free to customize and use this for any event!

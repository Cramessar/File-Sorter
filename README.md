# 🗂️ Auto File Sorter - Because Your Downloads Folder is a Digital Dumpster Fire

## 🤔 Why This Exists
You ever open your **Downloads** folder and immediately regret every life decision you've made? Yeah, me too. It's a **wild wasteland** of memes, random PDFs, shady ZIP files you *swear* are safe, and that one `.exe` you downloaded but were too scared to run.

This **File Sorter** is here to **restore order to the chaos** and prevent your future self from suffering when you inevitably need that "Final_Final_v3_ACTUALFINAL.docx" but can't find it.

## 🛠️ What This Does
This **glorious** piece of automation:
✅ Organizes your messy downloads into categorized folders like "Documents," "Images," "Videos," and even "Game ROMs" (because let's be real, we know why you're here).  
✅ Monitors your selected folder and **automagically** moves files where they belong.  
✅ Gives you a **super fancy** desktop app with buttons (because CLIs are for peasants).  
✅ Lets you start and stop the sorting process whenever you feel like embracing order (or chaos).  
✅ Logs everything it does, so you can flex on your past self about how organized you are now.  

## 🔧 How to Install
1. **Make sure you have Python installed.** If not, fix your life.  
2. Clone this repo like a proper hacker:
   ```sh
   git clone https://github.com/cramessar/File-Sorter.git
   cd Auto-File-Sorter
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the program:
   ```sh
   python "Auto File Sorter.py"
   ```

## 🚀 How to Use
1. **Run the app** and bask in its organizational glory.  
2. Click **"Select Folder"** and choose where you want files to be sorted.  
3. Click **"Start Organizing"** and watch your files **magically** move to their rightful places.  
4. Click **"Stop Organizing"** if you feel like embracing the chaos again.  
5. Profit.  

## 📁 Default Sorting Folders
As a side note this is just a small list of file types. I have no idea what format you are using, but add to the list as you see fit. Maybe someone can create a master list
of file extension types and categorize them but I don't have the mental capacity for something like that. 

- **Documents** 📄 (`.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`)
- **Images** 🖼️ (`.jpg`, `.png`, `.gif`, `.bmp`)
- **Videos** 🎥 (`.mp4`, `.mov`, `.avi`, `.mkv`)
- **Music** 🎵 (`.mp3`, `.wav`, `.flac`)
- **Archives** 📦 (`.zip`, `.rar`, `.tar`, `.gz`)
- **Executables** 🖥️ (`.exe`, `.msi`, `.sh`, `.bat`)
- **Game ROMs** 🎮 (`.gba`, `.nds`, `.nsp`, `.iso`, `.bin`, `.cso`)
- **Others** 🤷‍♂️ (Everything else, because life is unpredictable)

## 🛠️ Troubleshooting
### "I ran it, but nothing is happening."
- First, **relax**. Check if you actually selected a folder.  
- Make sure the files are in the root folder you selected. The script won't hunt them down like a bounty hunter.  
- Check the log window in the app. If it says "Monitoring started..." you're good. If it says nothing, **try turning it off and on again.**
- Also try adding something to the folder and check again. If that doesn't work hit me up and I'd be happy to take a look with you.

### "Could not find platform independent libraries <prefix>"
- This is Python screaming for help. Reinstall dependencies:
  ```sh
  pip install --force-reinstall -r requirements.txt
  ```
- If that doesn’t work, run it explicitly:
  ```sh
  python "File Sorter.py"
  ```

### "I accidentally moved my entire life into the 'Others' folder."
- Yeah… **been there.** But no worries, you can manually move files back. **Ctrl+Z might save you** if you act fast!

## 💡 Future Features (If I Ever Stop Procrastinating)
- 🗑️ "Delete Trash Files" mode (automatically remove duplicate memes & cursed downloads)
- 🖥️ Windows tray mode (so you can let it run silently like a true background app)
- 🏆 Leaderboard for "Most Organized Person of the Month" (JK, but wouldn’t that be cool?)

## 📜 License
This project is **free to use** because the world deserves less chaos. But if you somehow make money with it, **send some pizza my way** 🍕, if you make a lot of money,
lets upgrade that pizza to pepperoni pizza.

---

Now go forth and clean up your digital disaster zone! 🚀


# 🧠 Linux Command Line Mastery – Summary, Solutions & Knowledge Check 🎯💻

Welcome to the **Linux Command Line** – a powerful environment for interacting directly with your system! Whether you're managing files, controlling processes, or customizing your environment, the terminal is your all-access pass to deep system functionality.

---

## 🧰 **What You’ll Learn**
- 🌲 Navigate the Linux file system like a pro
- 📂 Manage files & directories (create, move, delete, copy)
- 🧪 Search content with `grep` & `find`
- ⚙️ Manage running processes with `top`, `ps`, `kill`, `pkill`
- 🌍 Customize your shell environment with `.bashrc`, `export`, etc.
- 📦 Archive/unarchive using `zip`, `tar`, etc.
- 🆘 Use help systems like `--help`, `man`, and `help`

---

## 📌 **Key Command Concepts**

### 🔍 Navigation & File Management
- `pwd`: Print working directory 📍
- `ls`, `ls -l`, `ls -a`: List directory contents 📂
- `cd`, `cd ..`, `cd ~`: Change directory 🔄
- `mkdir`, `touch`: Create folders/files 🏗️
- `cp`, `mv`, `rm`: Copy, move/rename, and delete 📁
- `cat`, `less`, `head`, `tail`: View file contents 📄
- `echo`, `>>`: Output to terminal or append to file 📝
- Wildcards: `*` matches many, `?` matches one 🎯

### 🔎 Viewing & Searching
- `grep`: Search text in files 🔍  
- `find`: Locate files/folders by name/type/etc 📂

### 🖥️ Process Management
- `top`, `htop`: Live process monitor 📊  
- `ps aux`: List running processes 🧠  
- `kill`, `kill -9`, `pkill`: Stop processes 🔫  

### 💾 Environment & Variables
- `echo $VAR`: View env variable 🌐  
- `export VAR="value"`: Set variable  
- `~/.bashrc`: Add aliases, configs 🛠️  
- `history`, `!NUM`: Command recall ⏳  

### 📦 Archiving
- `zip/unzip`: Compress/extract zip files 📦  
- `tar -czvf`, `tar -xzvf`: Create/extract tar.gz archives 💨  

### 🆘 Getting Help
- `--help`: Quick usage info ⚡  
- `man command`: Full manual 📘  
- `help command`: Shell built-ins 📖  

---

## ✅ **Assignment Solutions**

### 1. ✅ Create and Navigate
```bash
mkdir my_project
cd my_project
pwd  # Output: /home/yourusername/my_project
```
### 2. 📄 File Management
```bash
touch report.txt data.csv
mkdir archive
cp report.txt archive/
ls archive/  # Should show report.txt
```
### 3. 🔐 View Permissions
```bash
ls -la
# View file types, permissions, owner, group
```
### 4. 📑 View Content
```bash
echo "Name,Age" > data.csv
echo "Alice,30" >> data.csv
cat data.csv
less data.csv  # Press 'q' to quit
```
### 5. 🌟 Wildcards
```bash
touch document1.txt document2.md photo.jpg report_final.txt
ls *.txt        # All .txt files
ls doc*.txt     # Files starting with 'doc' and ending in .txt
ls *.md         # Only .md files
ls report?.txt  # report_final.txt (if it matches)
```
## ⚙️ Process Management Examples

### 🔎 Bash Process
```bash
ps aux | grep bash
```
### ⌨️ .bashrc Alias + Source
```bash
echo "alias ll='ls -la'" >> ~/.bashrc
source ~/.bashrc
ll  # Should work like ls -la
```
### 📜 Command History
```bash
history
!10  # Re-execute command number 10
```
### 🧠 Disk & CPU Info
```bash
df -h
lscpu
```

## 🔍 Search & Find

### 📝 grep
```bash
grep "important" my_notes.txt
grep -i "important" my_notes.txt  # Case-insensitive
```
### 📂 find
```bash
find . -name "*.csv"
```

## 📦 Archive Management

### 🗜️ ZIP
```bash
mkdir zip_test && cd zip_test
touch test1.txt test2.html test3.css
zip my_web_files.zip test*
rm test*
unzip my_web_files.zip
```
### 📚 tar.gz
```bash
mkdir -p tar_test/data
echo "{}" > tar_test/data/config.json
tar -czvf my_data_backup.tar.gz tar_test/
rm -r tar_test/
tar -xzvf my_data_backup.tar.gz
ls tar_test/data/
```
## 🤔 Knowledge Check – Answers

- 📍 **pwd** prints the current working directory  
- 📂 **mkdir dirname** creates a new directory  
- 📖 **cat** shows full file content; **less** allows paginated viewing  
- 🔢 Use **top** or `ps aux | grep process_name` to find PID  
- 🎯 **kill** uses PID, **pkill** uses process name  
- 🛠️ Add aliases to `~/.bashrc` and run `source ~/.bashrc` to activate  
- 📘 Use `man ls` for detailed help; `ls --help` for quick usage  
- 🔍 **grep** searches for text patterns in files  
- 💨 **tar.gz** is preferred for large/many files – better compression than zip  

---

🎉 **You did it!** You now have a solid foundation in the Linux command line.  
Keep practicing these tools, and they’ll become second nature. 💪🐧

---

## 🔗 Additional Resources

- 📘 [The Linux Command Line Book](https://linuxcommand.org/tlcl.php)  
- 📺 [Linux Command Line Tutorials – YouTube](https://www.youtube.com/results?search_query=linux+command+line+tutorial)  
- 📑 [Linux Command Cheat Sheet](https://linuxtrainingacademy.com/linux-command-line-cheat-sheet/)  
- 🎥 [Shell Init Files Explained – .bashrc vs .bash_profile](https://www.youtube.com/watch?v=YHFzr-akOas)

> ⚡ *“The terminal isn't scary — it's just powerful.”*  
> Keep exploring and experimenting!

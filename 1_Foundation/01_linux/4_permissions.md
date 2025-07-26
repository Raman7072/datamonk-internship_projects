# 📁 Linux Filesystems & Permissions: A Practical Guide

## 📌 Introduction
Linux organizes data like a highly structured **library**, where:
- **Filesystems** are rooms storing various books (files).
- **Permissions** are rules that determine who can access, modify, or run files and enter directories.

Mastering this helps you securely manage files and understand application behavior.

---

## 🧭 Lesson Overview
You'll learn:
- Linux filesystem structure.
- File/directory permissions (read, write, execute).
- Viewing permissions (`ls -l`).
- Modifying permissions (`chmod`) and ownership (`chown`).
- Using `sudo` for administrative tasks.
- Basic user management (`useradd`).

---

## 🗂️ Linux Filesystem Hierarchy
Key directories:
- `/etc`: System-wide configuration files.
- `/media`: Auto-mounted removable media (USBs, CDs).
- `/mnt`: Manually mounted filesystems.
- `/home`: User directories (e.g., `/home/kakarot`).
- `/usr`: Applications, docs, libraries.
- `/sys`: Interface to kernel data structures (virtual).

🔎 **What's in `/etc`?**  
Configuration files for services like networking, users, startup scripts.

---

## 🔐 Permissions in Linux
Linux uses a **three-tier permission model**:
- **Owner (u)**: Creator of the file.
- **Group (g)**: Group the file belongs to.
- **Others (o)**: Everyone else.

Each can have:
- **Read (r)**: View content or list directory.
- **Write (w)**: Modify or rename.
- **Execute (x)**: Run file or enter directory.

---

## 📄 Viewing Permissions with `ls -l`
```bash
ls -l
```
Example:
```sql
-rw-r--r--  user group  myfile.txt
drwxr-xr-x  user group  mydirectory/
```
`-`: Regular file, `d`: Directory
`rw-`: Owner can read/write
`r--`: Group and others can read

## 🔧 Changing Permissions with `chmod`
### Symbolic mode:
```bash
chmod u+x script.sh        # Add execute for owner
chmod go-w file.txt        # Remove write from group and others
chmod a=rwx dir/           # All: read, write, execute
```
### Octal mode:
| Mode | Value |
| ---- | ----- |
| r    | 4     |
| w    | 2     |
| x    | 1     |

Examples:
```bash
chmod 755 file.sh   # rwxr-xr-x
chmod 644 file.txt  # rw-r--r--
chmod 777 file.txt  # rwxrwxrwx (not recommended)
```

## 👥 Changing Ownership with `chown`
```bash
chown user file.txt             # Change owner
chown :group file.txt           # Change group
chown user:group file.txt       # Change both
chown -R user directory/        # Recursive ownership
```

## ⚠️ Using `sudo`: Elevated Privileges
### Run admin commands:
```bash
sudo apt update                 # Update system packages
sudo systemctl restart apache2 # Restart service
```
**🔐 Why doesn’t the terminal show password characters when typing?**
For security, Linux hides password input—just type and press Enter.

## 👤 Adding Users with `useradd`
```bash
sudo useradd -m newuser       # Create user + home dir
sudo passwd newuser           # Set password
```
**🧠 Why learn this?** Even if you don’t manage users daily, understanding user access is key for secure systems.

## 🧪 Exercises (Do it yourself!)
- Use `ls -l`, `chmod`, `chown` and `sudo`.
- Create files and directories.
- Set different permissions using symbolic and octal modes.
- Make a script file executable and run it.
- Change ownership with `chown`.

**💡 What’s the default permission for a new file and directory?**
- File: `rw-r--r--`
- Directory: `rwxr-xr-x`

## ✅ Knowledge Check – Quick Q&A

- **What is `/etc` used for?**
System configuration files.

- **What does `chmod 755` mean?**
Owner: all permissions; Group & Others: read, execute.

- **How does `ls -l` help?**
Shows file type, permissions, ownership, and timestamps.

- **Why use `sudo` cautiously?**
It can modify the entire system—know what you're doing!

- **How do you give only the owner full access to a file?**
`chmod 700 filename`

- **How do you create a user with a home directory?**
`sudo useradd -m username`

### 📚 Additional Resources
- [Linux File Hierarchy (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
- [chmod Octal Mode – TutorialsPoint](https://www.tutorialspoint.com/unix/unix-file-permission.htm)
- [Linode Linux Permissions Guide](https://www.linode.com/docs/guides/linux-file-permissions/)
- [Interactive Permissions Calculator](https://chmod-calculator.com/)

#### 🚀 Keep Practicing!
Mastering permissions, ownership, and filesystems is foundational to becoming a power Linux user. With every command, you gain more confidence and control.

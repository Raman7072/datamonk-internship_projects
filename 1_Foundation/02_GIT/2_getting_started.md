# Getting Started

When you’re building your personal portfolio website—a simple project that showcases your name, photo, skills, and a few projects—you want to keep track of your progress, avoid tears, and look professional.

Enter **Git Workflow** — your organized roadmap from idea to polished code.

---

## `git init`

**Before you begin:** Git needs to be told to start tracking your project.

```bash
git init
```

This creates a hidden `.git` folder that allows Git to track all changes moving forward.

> 💡 **Think of this like turning on a surveillance camera for your project — Git now sees all.**

---

## Add a File

Suppose you add your first file: `index.html`.

Git does not track new files automatically. To start tracking it:

```bash
git add index.html
```

### 📌 What is the **Staging Area**?

The **staging area** is like a waiting room. You’ve told Git what files you want to save, but haven’t officially saved them yet.

- You can remove a file from staging or add more files before committing.

---

## `git commit`

When you're ready to record the staged changes:

```bash
git commit -m "Add homepage with intro"
```

This **permanently records** your work with a message explaining what changed.

> 📝 A good commit message is like a diary entry for your code.

---

## `.gitignore` — Tell Git What *Not* to Track

Imagine you created a file `notes.txt` for personal to-do items and **don't** want it in your Git history.

To prevent Git from tracking it:

```bash
echo "notes.txt" >> .gitignore
```

> ✅ Keeps your repo clean and professional, especially when pushing to GitHub.

---

## `git checkout` — Undo Mistakes Gracefully

Oops! You added a weird background color in `index.html` and want to discard that change.

```bash
git checkout -- index.html
```

> ⛔ This restores the file to the last committed version.  
> ⚠️ Only use if you're okay with **losing uncommitted changes** in that file.

---

## `git rm --cached` — Remove a Tracked File Without Deleting It

Let’s say you accidentally added `secrets.txt` and want Git to forget about it—but not delete it from your machine.

```bash
git rm --cached secrets.txt
```

> 🔒 Ideal for removing **sensitive files** from Git without deleting them.

---

## `git grep` — Search Your Codebase

As your project grows with multiple files, you want to find where you used the word `contact`.

```bash
git grep "contact"
```

> 🔍 This searches your entire project—like **Google for your codebase**.

---

## `git stash` — Pause Your Work Temporarily

You're editing the “Projects” section but suddenly need to fix a typo elsewhere. Your current work is incomplete.

```bash
git stash
```

Git safely tucks your changes away. Now switch tasks freely.

To bring them back:

```bash
git stash pop
```

> 🎒 Think of this like putting your work in a backpack while handling something else.

---

## Final Thoughts

By the time your portfolio is complete, your Git workflow will have helped you:

- ✅ Track every small change with purpose
- 🛠️ Fix mistakes with confidence
- 🧹 Keep your project clean and professional
- 🔁 Juggle multiple tasks without chaos

> **Git isn’t just a tool — it’s your project’s safety net, journal, and time-travel machine.**

---

## 🧪 Try This: Explore Your `.git` Folder

**Question: Where is your `.git` folder located?**

- 📍 **Answer:** It is located inside your project’s root directory. You can reveal it by running:

```bash
ls -a
```

This will list all files including hidden ones (those starting with a `.`).

**Question: What kind of files or folders does it contain?**

- 📂 **Answer:** It typically contains folders like `objects/`, `refs/`, and files like `HEAD`, `config`, and `index`, which Git uses to manage versions, branches, and commit history.

> 🕵️ Git is quietly tracking everything behind the scenes.

---

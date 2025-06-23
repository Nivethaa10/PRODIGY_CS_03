# PRODIGY_CS_03
# 🔐 Password Complexity Checker (Pure Python)

## ⚠️ Disclaimer

> This tool is built purely for **educational and personal use**. It does not collect, store, or transmit passwords.  
> Use responsibly and **never use it to evaluate or store someone else's password without consent**.

---

## 📜 About the Project

This is a simple, interactive **Password Complexity Checker** written in pure Python without any third-party libraries. It evaluates a password's complexity based on length, uppercase, lowercase, numbers, and special characters.

Perfect for beginner Python programmers learning:
- String manipulation
- Conditional logic
- User input handling

---

## ✅ Features

- Pure Python, no external imports
- Password scoring system (out of 5)
- Feedback on missing character types
- Friendly emoji-based complexity rating

---

## 🧪 Password Criteria

| Criterion               | Required?    |
|------------------------|--------------|
| Length ≥ 8             | ✅            |
| At least one uppercase | ✅            |
| At least one lowercase | ✅            |
| At least one number    | ✅            |
| At least one symbol    | ✅            |

---

## 🏷️ Complexity Levels

| Score | Rating               |
|-------|----------------------|
| 5     | Very Strong 💪       |
| 4     | Strong 👍             |
| 3     | Moderate 🤔           |
| 2     | Weak ⚠               |
| 0-1   | Very Weak ❌          |

---

## ▶️ How to Run

1. Open the `password_complexity_checker.py` in any Python 3.x environment (IDLE, terminal, VSCode, etc.).
2. Run the file.
3. Enter your password when prompted.
4. See detailed feedback and complexity rating.

```bash
$ python password_complexity_checker.py
Enter your password: MyPass@123
```

---

## 🧾 Sample Output

```
Password Strength Feedback:
✓ Length >= 8       : True
✓ Has Uppercase     : True
✓ Has Lowercase     : True
✓ Has Numbers       : True
✓ Has Special Chars : True

Overall Password Strength: Very Strong 💪
```

---

## 🛡️ Security Note

This tool **does not store or transmit** the entered password. It is meant for **local use only** and is safe for self-testing. However, always practice caution with sensitive data.

---

## 📌 Final Note

You’re welcome to fork, modify, and improve the logic (e.g., entropy-based strength calculation).  
Star ⭐ the repo if you found it helpful!

---

# 🎂 Birthday Wisher

An automated birthday email sender powered by **Python** and **GitHub Actions** — set it up once, and it automatically sends personalized birthday wishes to your family and friends every year, right on their special day!

---

## ✨ Features

- 📅 **Fully Automated** — runs daily at 8:00 AM IST via GitHub Actions (no server needed!)
- 💌 **Personalized Emails** — picks a random letter template and fills in the person's name
- 📋 **Easy to Manage** — just edit `birthdays.csv` to add/remove people
- 🔐 **Secure** — email credentials are stored as GitHub Secrets, never in code
- 📝 **Multiple Templates** — 3 unique letter templates chosen at random for variety

---

## 📁 Project Structure

```
Birthday Wisher/
├── .github/
│   └── workflows/
│       └── birthday_wisher.yml   # GitHub Actions automation
├── letter_templates/
│   ├── letter_1.txt              # Birthday letter template 1
│   ├── letter_2.txt              # Birthday letter template 2
│   └── letter_3.txt              # Birthday letter template 3
├── birthdays.csv                 # Your family & friends list
├── main.py                       # Core Python script
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 How It Works

1. GitHub Actions triggers the script every day at **8:00 AM IST**
2. `main.py` reads today's date and checks it against `birthdays.csv`
3. If there's a match, it picks a random letter template and personalizes it
4. The email is sent via **Gmail SMTP** using your credentials stored as GitHub Secrets

---

## 🛠️ Setup Guide

### 1. Fork or Clone this Repository

```bash
git clone https://github.com/AbhijaySinghPanwar/Birthday_Wisher.git
cd Birthday_Wisher
```

### 2. Add Your People to `birthdays.csv`

Edit `birthdays.csv` with your family and friends:

```csv
name,email,year,month,day
Mummy,mummy@example.com,1972,12,6
Papa,papa@example.com,1976,4,8
Best Friend,friend@example.com,1999,7,15
```

### 3. Customize the Letter Templates (Optional)

Edit any of the files inside `letter_templates/`:

```
Dear [NAME],

Happy Birthday! Wishing you all the joy today!

Love,
Abhijay
```

> The `[NAME]` placeholder is automatically replaced with the person's name.

### 4. Add GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Secret Name | Value |
|---|---|
| `MY_EMAIL` | Your Gmail address (e.g. `you@gmail.com`) |
| `MY_PASSWORD` | Your **Gmail App Password** (16-char code) |

> **How to get a Gmail App Password:**  
> [myaccount.google.com](https://myaccount.google.com) → Security → 2-Step Verification → App Passwords → Generate

### 5. That's it! 🎉

The workflow runs automatically every day. You can also trigger it manually:  
**Actions tab** → **Birthday Wisher** → **Run workflow**

---

## ⚙️ Workflow Schedule

The GitHub Actions workflow runs at `02:30 UTC` which equals **8:00 AM IST** every day.

```yaml
schedule:
  - cron: "30 2 * * *"
```

---

## 🧪 Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
$env:MY_EMAIL = "your@gmail.com"        # PowerShell
$env:MY_PASSWORD = "your_app_password"  # PowerShell

# Run the script
python main.py
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `pandas` | Reading and parsing `birthdays.csv` |
| `smtplib` | Sending emails (built into Python) |

---

## 🔒 Security Note

- **Never** hardcode your email or password in the code
- Always use **GitHub Secrets** for credentials
- Use a **Gmail App Password**, not your regular Gmail password
- The `.gitignore` already excludes `.env` files from being committed

---

## 📄 License

This project is open source and free to use. Feel free to fork and customize it for your own family and friends! ❤️

---

<p align="center">Made with ❤️ by <a href="https://github.com/AbhijaySinghPanwar">Abhijay Singh Panwar</a></p>

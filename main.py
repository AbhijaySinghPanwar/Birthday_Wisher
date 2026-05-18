import smtplib
import datetime as dt
import random
import os
import pandas

# ---------------- EMAIL (from GitHub Secrets / env vars) ---------------- #
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

if not MY_EMAIL or not PASSWORD:
    raise EnvironmentError(
        "Missing required environment variables: MY_EMAIL and/or MY_PASSWORD. "
        "Add them as GitHub Secrets or set them locally in a .env file."
    )

# ---------------- DATE ---------------- #
today = dt.datetime.now()
today_tuple = (today.month, today.day)
print(f"[INFO] Checking birthdays for {today.strftime('%B %d')}...")

# ---------------- READ CSV ---------------- #
# Use the directory of this script so it works from any working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "birthdays.csv")
data = pandas.read_csv(csv_path)

birthdays_dict = {
    (int(row["month"]), int(row["day"])): row
    for (index, row) in data.iterrows()
}

# ---------------- CHECK BIRTHDAY ---------------- #
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(f"[INFO] 🎂 It's {birthday_person['name']}'s birthday! Sending email...")

    # -------- PICK A RANDOM LETTER -------- #
    letter_num = random.randint(1, 3)
    letter_path = os.path.join(script_dir, "letter_templates", f"letter_{letter_num}.txt")

    with open(letter_path) as letter_file:
        letter_contents = letter_file.read()

    # Replace [NAME] placeholder
    personalized_letter = letter_contents.replace("[NAME]", birthday_person["name"])

    # ---------------- SEND EMAIL ---------------- #
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"].strip(),
            msg=f"Subject:Happy Birthday! 🎂\n\n{personalized_letter}"
        )

    print(f"[SUCCESS] ✅ Birthday email sent to {birthday_person['name']} ({birthday_person['email'].strip()})")

else:
    print("[INFO] No birthdays today. Nothing to do.")
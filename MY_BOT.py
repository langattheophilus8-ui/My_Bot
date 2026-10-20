# ============================================================
# PROJECT: Building A Simple Chatbot
# TOPIC:   Introduction to Python
# CONCEPTS: Variables, Numbers (int & float), Strings, Booleans
# IDE:     PyCharm
# ============================================================

# ---------- 1. VARIABLES that store STRINGS ----------
# A string is text. It is written inside quotes.
bot_name = "PyFriend"
bot_creator = "KIPRUTO"      # <-- change this to your name!
greeting = "Hello! I am " + bot_name + ", your Python learning bot."

# ---------- 2. VARIABLES that store NUMBERS ----------
# int   = whole numbers (e.g. 5, 2026)
# float = numbers with decimals (e.g. 1.5, 3.14)
bot_version = 2.0
# float
current_year = 2026        # int
bot_lives_left = 3         # int

# ---------- 3. VARIABLES that store BOOLEANS ----------
# A boolean is either True or False (capital first letter!)
is_friendly = True
is_sleeping = False

# ---------- 4. SHOW the variables ----------
print("=" * 45)
print(greeting)
print("Created by:", bot_creator)
print("Version:", bot_version)
print("Year:", current_year)
print("Am I friendly?", is_friendly)
print("Am I sleeping?", is_sleeping)
print("=" * 45)

# ---------- 5. GET INPUT from the user (always a string) ----------
user_name = input("What is your name? ")
print("Nice to meet you, " + user_name + "!")

# Strings can be changed with built-in methods
print("Your name in CAPITALS:", user_name.upper())
print("Your name in lowercase:", user_name.lower())
print("Your name has", len(user_name), "letters.")

# ---------- 6. Convert string -> number with int() ----------
age_text = input("How old are you? ")      # this is a STRING, e.g. "20"
age = int(age_text)                        # now it is a NUMBER, e.g. 20

# ---------- 7. MATH with numbers ----------
birth_year = current_year - age
age_next_year = age + 1
age_in_months = age * 12

print("You were born around the year", birth_year)
print("Next year you will be", age_next_year)
print("That is about", age_in_months, "months old!")

# ---------- 8. Use BOOLEANS to compare things ----------
is_adult = age >= 18
is_older_than_bot = age > bot_version      # comparing int with float is fine

print("Are you an adult?", is_adult)
print("Are you older than my version number?", is_older_than_bot)

# ---------- 9. Mini game: guess the bot's secret number ----------
secret_number = 7
guess = int(input("Guess my secret number (1-10): "))
is_correct = guess == secret_number        # == checks if two values are equal

print("Was your guess correct?", is_correct)
if is_correct:
    print("Well done, " + user_name + "! You win!")
else:
    bot_lives_left = bot_lives_left - 1    # update a variable
    print("Not this time. I still have", bot_lives_left, "lives left.")

# ---------- 10. Check the TYPE of each variable ----------
print()
print("--- Data types in this program ---")
print("bot_name       ->", type(bot_name))
print("bot_version    ->", type(bot_version))
print("current_year   ->", type(current_year))
print("is_friendly    ->", type(is_friendly))

# ---------- 11. Goodbye ----------
print()
print("Goodbye " + user_name + "! Thanks for chatting with " + bot_name + ".")
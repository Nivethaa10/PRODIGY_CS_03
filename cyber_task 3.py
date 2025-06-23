def assess_password_strength(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/\\`~"

    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Scoring
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Strength Level
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Moderate 🤔"
    elif score == 2:
        strength = "Weak ⚠"
    else:
        strength = "Very Weak ❌"

    # Feedback
    print("\nPassword Strength Feedback:")
    print("✓ Length >= 8       :", length >= 8)
    print("✓ Has Uppercase     :", has_upper)
    print("✓ Has Lowercase     :", has_lower)
    print("✓ Has Numbers       :", has_digit)
    print("✓ Has Special Chars :", has_special)
    print("\nOverall Password Strength:", strength)

# === Run Test ===
user_input = input("Enter your password: ")
assess_password_strength(user_input)

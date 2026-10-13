import streamlit as st
import string

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Application title
st.title("🔐 Password Strength Checker")
st.write("Check your password strength and learn how to improve it.")

st.info(
    "Your password is analyzed locally by this application. "
    "Do not use a real password for assignment screenshots."
)

# Password input field
password = st.text_input(
    "Enter your password:",
    type="password",
    placeholder="Enter a password to check"
)

if password:
    # Check the five password criteria
    length_ok = len(password) >= 8
    uppercase_ok = any(char.isupper() for char in password)
    lowercase_ok = any(char.islower() for char in password)
    number_ok = any(char.isdigit() for char in password)
    special_ok = any(
        char in string.punctuation for char in password
    )

    # Calculate score out of 5
    score = sum([
        length_ok,
        uppercase_ok,
        lowercase_ok,
        number_ok,
        special_ok
    ])

    # Determine password strength
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    # Display analysis
    st.subheader("Password Strength Analysis")
    st.markdown(
        f"### Strength: :{color}[{strength}]"
    )
    st.metric("Password Strength Score", f"{score} / 5")

    # Visual progress bar
    st.write("Strength Progress")
    st.progress(score / 5)

    # Checklist of criteria
    st.subheader("Password Criteria Checklist")

    criteria = [
        ("At least 8 characters", length_ok),
        ("At least one uppercase letter", uppercase_ok),
        ("At least one lowercase letter", lowercase_ok),
        ("At least one number", number_ok),
        ("At least one special character", special_ok)
    ]

    for description, satisfied in criteria:
        if satisfied:
            st.success(f"✓ {description}")
        else:
            st.error(f"✗ {description}")

    # Suggestions for improvement
    st.subheader("Suggestions for Improvement")

    suggestions = []

    if not length_ok:
        suggestions.append(
            "Use at least 8 characters."
        )
    if not uppercase_ok:
        suggestions.append(
            "Add at least one uppercase letter (A-Z)."
        )
    if not lowercase_ok:
        suggestions.append(
            "Add at least one lowercase letter (a-z)."
        )
    if not number_ok:
        suggestions.append(
            "Include at least one number (0-9)."
        )
    if not special_ok:
        suggestions.append(
            "Include a special character, such as !, @, or #."
        )

    if suggestions:
        for suggestion in suggestions:
            st.write(f"• {suggestion}")
    else:
        st.success(
            "Excellent! Your password meets all five criteria."
        )

else:
    st.warning("Please enter a password to begin the analysis.")

st.caption("Password Strength Checker | Python + Streamlit")

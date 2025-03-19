import streamlit as st
from zxcvbn import zxcvbn

# Streamlit App Title
st.title("🔐 Password Strength Checker")

# Input Field (Password)
password = st.text_input("Enter a password:", type="password")

# Function to check password strength
def check_password_strength(password):
    result = zxcvbn(password)
    return result

# Display results
if password:
    result = check_password_strength(password)
    
    # Password strength score (0-4)
    score = result['score']
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
    # Display strength rating
    st.subheader(f"🔎 Password Strength: {strength_levels[score]} ({score}/4)")
    
    # Suggestions to improve password security
    if result["feedback"]["suggestions"]:
        st.subheader("💡 Suggestions:")
        for suggestion in result["feedback"]["suggestions"]:
            st.write(f"- {suggestion}")

    # Estimated time to crack the password
    st.subheader("⏳ Estimated Time to Crack:")
    st.write(f"Online attack: {result['crack_times_display']['online_no_throttling_10_per_second']}")
    st.write(f"Offline fast attack: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
else:
    st.warning("Enter a password to check its strength.")

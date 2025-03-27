
import streamlit as st
from zxcvbn import zxcvbn

# Streamlit App Title
st.title("🔐 Password Strength Checker")

# Input Field ( Password )
password = st.text_input("Enter a password:", type="password")

# Function to check password strength
def check_password_strength(password):
    return zxcvbn(password)

# Strength levels
strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]

# Display results
if password:
    result = check_password_strength(password)
    score = result['score']
    
    # Show strength level
    st.subheader(f"🔎 Password Strength: **{strength_levels[score]}** ({score}/4)")

    # Suggestions for improvement
    if result["feedback"]["suggestions"]:
        st.subheader("💡 Suggestions:")
        for suggestion in result["feedback"]["suggestions"]:
            st.write(f"- {suggestion}")

    # Estimated time to crack
    st.subheader("⏳ Estimated Time to Crack:")
    st.write(f"🔹 **Online attack:** {result['crack_times_display']['online_no_throttling_10_per_second']}")
    st.write(f"🔹 **Offline fast attack:** {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
else:
    st.warning("Enter a password to check its strength.")

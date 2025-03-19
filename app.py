
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

# Define strength levels and corresponding colors
strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
strength_colors = ["#FF0000", "#FF4500", "#FFA500", "#32CD32", "#008000"]  # Red → Orange → Yellow → Green → Dark Green

# Display results
if password:
    result = check_password_strength(password)
    
    # Get score (0-4)
    score = result['score']
    
    # Display color-coded strength rating
    st.markdown(
        f'<h3 style="color:{strength_colors[score]};">🔎 Password Strength: {strength_levels[score]} ({score}/4)</h3>',
        unsafe_allow_html=True
    )

    # Suggestions to improve password security
    if result["feedback"]["suggestions"]:
        st.subheader("💡 Suggestions:")
        for suggestion in result["feedback"]["suggestions"]:
            st.write(f"- {suggestion}")

    # Estimated time to crack the password
    st.subheader("⏳ Estimated Time to Crack:")
    st.write(f"🔹 **Online attack:** {result['crack_times_display']['online_no_throttling_10_per_second']}")
    st.write(f"🔹 **Offline fast attack:** {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

    # Strength bar using Streamlit columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display a horizontal color-coded bar based on the score
    if score >= 0:
        col1.markdown(f'<div style="background-color:{strength_colors[0]};height:20px;border-radius:5px;"></div>', unsafe_allow_html=True)
    if score >= 1:
        col2.markdown(f'<div style="background-color:{strength_colors[1]};height:20px;border-radius:5px;"></div>', unsafe_allow_html=True)
    if score >= 2:
        col3.markdown(f'<div style="background-color:{strength_colors[2]};height:20px;border-radius:5px;"></div>', unsafe_allow_html=True)
    if score >= 3:
        col4.markdown(f'<div style="background-color:{strength_colors[3]};height:20px;border-radius:5px;"></div>', unsafe_allow_html=True)
    if score >= 4:
        col5.markdown(f'<div style="background-color:{strength_colors[4]};height:20px;border-radius:5px;"></div>', unsafe_allow_html=True)

else:
    st.warning("Enter a password to check its strength.")

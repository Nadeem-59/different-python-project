# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones (diff time zone hai isko hum apnay tymzone se match karay gay )
TIME_ZONES = ["🕰️", "⏰", "🌍", "🏙️", "🕓",
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]
# Apply Background Image Using Streamlit Components
def set_bg_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_url}) no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
set_bg_image("data:image/jpeg;base64,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")
# Custom CSS for Styling
st.markdown(
    """
    <style>
    /* Buttons */
        .stButton > button {
            background-color: red;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 20px;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: green;
            transform: scale(1.1);
             color: #ffffff;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }
    </style>
    """,
      unsafe_allow_html=True
)

# Create app title
st.title("Time Zone App 🕰️🌍🏙️")

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%H:%S %p")
    # Display timezone and its current time
    st.write(f"**{tz}**: {current_time}")

# Create section for time conversion
st.subheader("Convert Time Between Timezones")
# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("Convert Time"):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the converted time with success message
    st.success(f"Converted Time in {to_tz}: {converted_time}")
import streamlit as st
import base64

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to get BMI category and advice
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🍽️ You might need to increase your calorie intake. Consider a nutritious diet."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "✅ Great! Maintain a healthy lifestyle with a balanced diet and exercise."
    elif 25 <= bmi < 29.9:
        return "Overweight", "🏃 You should consider regular physical activity and mindful eating."
    else:
        return "Obese", "⚕️ A healthcare consultation is recommended to improve health."

# Function to generate a downloadable report
def generate_report(weight, height, bmi, category, advice):
    report = f"""BMI Report\n\nWeight: {weight} kg\nHeight: {height} m\nBMI: {bmi}\nCategory: {category}\nAdvice: {advice}\n"""
    return report

# Function to create a download link
def get_download_link(report):
    b64 = base64.b64encode(report.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="BMI_Report.txt">📥 Download BMI Report</a>'
    return href

# Set page config
st.set_page_config(page_title="🌟 Modern BMI Calculator", page_icon="⚕️", layout="wide")
# Custom CSS for stylish design with purple sidebar
st.markdown("""
    <style>
        body {
            background: #f5f5f5; /* Light gray background */
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
            max-width: 800px;
        }
        .stButton>button {
            background: #6a1b9a; /* Purple color */
            color: white;
            font-size: 18px;
            padding: 12px 24px;
            border-radius: 12px;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: #4a148c; /* Darker purple color */
            transform: scale(1.05);
        }
        .stNumberInput>div>input, .stRadio>div {
            border-radius: 12px;
            border: 1px solid #ddd;
            padding: 10px;
        }
        .stProgress>div>div>div {
            background: #6a1b9a; /* Purple color */
        }
        h1, h2, h3 {
            color: #6a1b9a; /* Purple for headings */
            text-align: center;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #6a1b9a; /* Purple for footer */
            margin-top: 30px;
        }
        .sidebar .sidebar-content {
            background: #6a1b9a; /* Purple background */
            color: purple;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            margin: 20px;
        }
        .sidebar .stRadio>div, .sidebar .stSelectbox>div {
            color: purple;
        }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("<h1 style='color: #6a1b9a;'>🌟 Modern BMI Calculator 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6a1b9a;'>📊 Calculate your BMI and get personalized health tips! 🩺</p>", unsafe_allow_html=True)

# Input fields in a container
with st.container():
    st.markdown("<h3 style='color: #6a1b9a;'>📊 Enter Your Details</h3>", unsafe_allow_html=True)
    weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, step=0.1)
    height = st.number_input("📏 Enter your height (m):", min_value=0.5, step=0.01)
    age = st.number_input("🎂 Enter your age:", min_value=1, step=1)
    gender = st.radio("🚻 Select your gender:", ("Male", "Female", "Other"))
    activity_level = st.selectbox("🏃 Select your activity level:",
                                  ["Sedentary (little to no exercise)", "Lightly active (1-3 days per week)",
                                   "Moderately active (3-5 days per week)", "Very active (6-7 days per week)"])

# Calculate BMI button
if st.button("💪 Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, advice = get_bmi_category(bmi)
        
        # Display BMI results
        st.markdown("<h2 style='color: #6a1b9a;'>📈 Your BMI Results</h2>", unsafe_allow_html=True)
        st.success(f"Your BMI: **{bmi}**")
        st.info(f"Category: **{category}**")
        st.warning(f"Advice: **{advice}**")
        
        # Visualize BMI status with a progress bar
        st.markdown("<h3 style='color: #6a1b9a;'>📊 BMI Progress</h3>", unsafe_allow_html=True)
        bmi_min = 0
        bmi_max = 40
        bmi_progress = (bmi - bmi_min) / (bmi_max - bmi_min)
        
        # Clamp the progress value between 0.0 and 1.0
        bmi_progress = max(0.0, min(1.0, bmi_progress))
        
        st.progress(bmi_progress)
        st.write(f"📊 BMI Progress: **{int(bmi_progress * 100)}%**")
        
        # Generate and download report
        report = generate_report(weight, height, bmi, category, advice)
        st.markdown(get_download_link(report), unsafe_allow_html=True)
        
        # Additional health tips
        st.markdown("<h3 style='color: #6a1b9a;'>🏋️ Suggested Health Tips</h3>", unsafe_allow_html=True)
        if bmi < 18.5:
            st.write("- 🥜 Increase calorie intake with healthy foods like nuts, dairy, and whole grains.")
            st.write("- 💪 Strength training can help build muscle mass.")
        elif 18.5 <= bmi < 24.9:
            st.write("- 🥗 Keep up the great work with a balanced diet and regular exercise! ✅")
        elif 25 <= bmi < 29.9:
            st.write("- 🏃 Incorporate cardio and strength training to maintain a healthy weight.")
            st.write("- 🚫 Reduce sugar and processed food intake.")
        else:
            st.write("- 🩺 Consider consulting a dietitian for personalized weight management.")
            st.write("- 🏋️‍♂️ A mix of cardio and strength training is recommended.")
    else:
        st.error("⚠️ Please enter valid weight and height values.")

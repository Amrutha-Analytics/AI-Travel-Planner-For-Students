# 🎒 AI Student Travel Budget Planner
page_title=" AI Student Travel Budget Planner"

This is a Streamlit-based AI web application that helps students
plan budget-friendly trips across Indian states. The app predicts
the total travel budget using a Machine Learning model and generates
a daily travel plan including cities, food, hotels, and student tips.

## ✨ Features

- AI-based travel budget prediction using a trained ML model
- Multi-page Streamlit application with session state
- State-wise cities, food, and hotel recommendations
- Daily itinerary generation
- Per-day budget calculation
- Budget split visualization using charts
- Downloadable travel plan in text format

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Joblib
- Altair
- HTML & CSS (for custom UI styling)
 
 ## ⚙️ How the Application Works

1. The user starts the application and clicks "Start Planning".
2. The user enters travel details such as age, state, interests,
   accommodation type, and number of days.
3. The ML model predicts the total travel budget.
4. The app displays:
   - Total budget
   - Per-day budget
   - Daily travel itinerary
   - Hotel and food suggestions
   - Budget split chart
5. The user can download the travel plan as a text file.
 
 ## 🤖 Machine Learning Model

The application uses a pre-trained Machine Learning model
(`model2.pkl`) loaded using Joblib. The model predicts the
total travel budget based on user inputs such as age, interests,
accommodation type, travel companion, and trip duration.

## 📂 Project Structure

AI-Student-Travel-Budget-Planner/
│
├── app.py               # Main Streamlit application
├── model2.pkl           # Trained ML model
├── README.md            # Project documentation
├── requirements.txt     # Required Python libraries
 
 ## ▶️ How to Run the Project

Live Demo: https://ai-travel-planner-for-students123aa.streamlit.app/

## 🧪 Example Use Case

- Age: 21
- State: Maharashtra
- Days: 5
- Gender: M
- Primary Interest: Beach
- Secondary Interest: Shopping
- Travel Companion: Solo
- Accommodation: Budget

Output:
- Total budget prediction
- Daily itinerary
- Budget Split visualization
- Popular Food recommandations on the particular place
- Per-day cost
- Downloadable travel plan

**Author:** Amrutha Ammuloju

import streamlit as st

st.set_page_config(
    page_title="Student Grade Application",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Grade Application")
st.write("Enter the student's details and marks below.")

# Student details
name = st.text_input("Student Name")
roll_no = st.text_input("Roll Number")

st.subheader("📚 Enter Marks")

maths = st.number_input("Mathematics", min_value=0, max_value=100, value=0)
science = st.number_input("Science", min_value=0, max_value=100, value=0)
english = st.number_input("English", min_value=0, max_value=100, value=0)
computer = st.number_input("Computer Science", min_value=0, max_value=100, value=0)
social = st.number_input("Social Science", min_value=0, max_value=100, value=0)

# Calculate button
if st.button("Calculate Grade"):
    
    if name.strip() == "" or roll_no.strip() == "":
        st.warning("Please enter the student's name and roll number.")
    
    else:
        marks = [maths, science, english, computer, social]

        total = sum(marks)
        percentage = total / len(marks)

        # Grade calculation
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        # Pass / Fail
        if all(mark >= 35 for mark in marks):
            result = "PASS"
        else:
            result = "FAIL"

        st.divider()

        st.subheader("📊 Student Result")

        st.write(f"**Student Name:** {name}")
        st.write(f"**Roll Number:** {roll_no}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Marks", f"{total}/500")

        with col2:
            st.metric("Percentage", f"{percentage:.2f}%")

        with col3:
            st.metric("Grade", grade)

        if result == "PASS":
            st.success(f"🎉 Result: {result}")
        else:
            st.error(f"❌ Result: {result}")

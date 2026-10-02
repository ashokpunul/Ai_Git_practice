import streamlit as st

st.title("Student Grade Manager")

# Store students in session state
if "students" not in st.session_state:
    st.session_state.students = [
        {"name": "Priya", "mark": 92},
        {"name": "Arun", "mark": 78},
        {"name": "Divya", "mark": 83}
    ]


# Grade calculation
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Input section
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    name = st.text_input("Name")

with col2:
    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0
    )

with col3:
    st.write("")
    st.write("")
    add = st.button("Add")


# Add student
if add:
    if name.strip() == "":
        st.warning("Please enter a student name.")
    else:
        st.session_state.students.append({
            "name": name,
            "mark": mark
        })
        st.rerun()


# Student table
st.subheader("Student Details")

marks = [student["mark"] for student in st.session_state.students]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

# Header
h1, h2, h3, h4, h5, h6 = st.columns(6)

h1.write("**Name**")
h2.write("**Mark**")
h3.write("**Grade**")
h4.write("**Average**")
h5.write("**Highest**")
h6.write("**Lowest**")

# Student rows
for index, student in enumerate(st.session_state.students):

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.write(student["name"])
    c2.write(student["mark"])
    c3.write(get_grade(student["mark"]))

    # Display average/highest/lowest only for first student
    if index == 0:
        c4.write(f"{average:.1f}")
        c5.write(highest)
        c6.write(lowest)

import streamlit as st
from random import randrange
from xfacts import all_facts

#st.sidebar.title("Navigate Pages")
#page = st.sidebar.radio("Go to:", ["Home🏠", "Original Calc👴", "New Calc incl. Year 3🤯"])

tabs = st.tabs(["Home🏠", "Original Calc👴", "New Calc incl. Year 3🤯"])

#if page == "Home🏠":
with tabs[0]:
    st.title("Welcome to the new and improved Calc 4 Psych 🧘")
    st.write("Please choose one of the tabs to get going 😼")
    st.write("")

    if st.button("Generate Fun Fact!", key = "fact_button"):
        random_number = randrange(len(all_facts))
        fact = (all_facts[random_number])

        if fact.endswith('.'):
            fact = fact[:-1] + '!'
        else:
            fact += '!'

        st.write(fact)

#elif page == "Original Calc👴":
with tabs[1]:
    st.title("Calc 4 Psych 🧘")
    st.write("Note that all inputs should be in the form of a percentage.")

    def grade_calc(fyp_grade, overall_grade):
        return 1.5*(overall_grade - fyp_grade/3)

    fyp_input = st.text_input("Please input the percentage received for the FYP.")
    overall_input = st.text_input("Please input the percentage received overall.")

    if st.button("Calculate Grade!", key = "og_button"):
        result = grade_calc(float(fyp_input), float(overall_input))
        st.write(f"The percentage received in the 40 non-FYP credits was **{result}**!")

#elif page == "New Calc incl. Year 3🤯":
with tabs[2]:
    st.title("New calc including grade from 3rd year! 🕺")
    st.write("Note that all inputs should be in the form of a percentage.")

    year3grade = st.text_input("3rd Year Grade:")
    st.caption("Your 3rd year grade accounts for 30% of your final grade.")

    year4grade = st.text_input("4th Year Grade:")
    st.caption("Your 4th year grade (excluding your FYP) accounts for ~46.67% of your final grade.")

    fyp = st.text_input("Your FYP Grade:")
    st.caption("Your final year project accounts for ~23.33% of your final grade.")

    if st.button("Calculate Grade!", key = "new_button"):
        result = (float(year3grade)*.3)+(float(year4grade)*.7*2/3)+(float(fyp)*.7*1/3)
        st.write(f"The projected result is **{result}**! Well done!")


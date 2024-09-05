import os
import google.generativeai as genai
import streamlit as st
from typing_extensions import TypedDict

api_key ='AIzaSyClnWNUlKao9KxSfEb3J-zCffWHS89kh5s'
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')


class State(TypedDict):
    skills: list


def get_job_role_and_pay(state: State) -> str:
    input_skills = ', '.join(state["skills"])
    prompt = f"Given the skills: {input_skills}, list the most relevant job role and its pay per hour. Provide only the job role and pay per hour in your response."
    
    try:
        
        response = model.generate_content(prompt)
        
        output = response.text.strip()
        return output
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "I'm having trouble connecting to the service. Please try again later."

def get_skills_by_job_role(job_role: str) -> str:
    prompt = f"Given the job role: {job_role}, list 5 essential skills for this role. Provide only the skills in your response."
    
    try:
        
        response = model.generate_content(prompt)
       
        output = response.text.strip()
        return output
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "I'm having trouble connecting to the service. Please try again later."

def main():
    logo='d2.jpeg'
    st.image(logo)
    st.title('Job Role and Skills Generator')
    app_mode = st.radio("Choose Mode", ["Get Job Role and Pay", "Get Skills by Job Role"])
    
    if app_mode == "Get Job Role and Pay":
        user_input = st.text_input("Enter Skills (comma-separated):", "")
        if st.button("Generate Job Role and Pay"):
            skills_list = user_input.split(',')
            job_and_pay = get_job_role_and_pay({"skills": skills_list})
            st.success(f"Job Role and Pay Per Hour: {job_and_pay}")
    elif app_mode == "Get Skills by Job Role":
        job_role_input = st.text_input("Enter Job Role:", "")
        if st.button("Generate Skills"):
            skills = get_skills_by_job_role(job_role_input)
            st.success(f"Essential Skills for {job_role_input}: {skills}")

if __name__ == "__main__":
    main()

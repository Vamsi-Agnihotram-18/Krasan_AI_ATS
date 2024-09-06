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
    prompt = f"""Train yourself with simple technical defination of each of these job roles: 
    
    Sr Data Conversion Specialist,
    Data Conversion Specialist,
    DataWarehouse Engineer,
    Data Analyst,
    Power BI Data Visualization expert,
    Database Administrator,
    SQL Developer,
    Sr Oracle DBA,
    MySQL Developer,
    .Net Developer,
    Software Developer,
    Oracle eBusiness HCM/BI Developer,
    Jitterbit Developer,
    Oracle Fusion SOA Developer,
    ADF Developer,
    Oracle EBS Support,
    MuleSoft Integration Developer,
    Integration Developer – Technical,
    Workday Integration Developer,
    Business Analyst (Functional),
    Functional Business Analyst,
    Sr. Business Analyst,
    Business Analyst,
    Proposal Analyst,
    Program Manager,
    Project Manager,
    Project Coordinator,
    Client Project Coordinator,
    Release Train Engineer,
    Manual Tester,
    QA Tester,
    Performance Tester,
    Automation Tester,
    Quality Analyst,
    Functional Tester,
    DCFS- Tester - Manual/Functional/Automation,
    Senior Security Specialist,
    AWS Specialized Architect,
    Sr. Technical Lead and APEX Architect Consultant,
    Architect, Developer,
    Business Object Consultant,
    Oracle PPM Consultant,
    SAP HANA/BI Consultant,
    Senior Consultant,
    Oracle HCM Benefits Consultant,
    HR Classification Analyst,
    Director, Talent Acquisition,
    US IT Recruiter - Internal,
    HR and Immigration Analyst,
    Fractional Staffing Consultant,
    Proposal Support - Non Billable,
    Proposal Support - Billable,
    SAP ERP Trainer,
    Training Developer,
    Internal – Non-Client Billable – Administrative,
    Marketing Services Coordinator - 01 Open Position,
    Product Owner,
    Oracle AP & Expenses Support Analyst,
    Core Financial Support Analyst,
    Manager - Finance,
    AP And Expenses Lead,
    Helpdesk Analyst,
    UI/Front-end Developer,
    CCC_UX Strategist,
    MS Dynamics 365 Developer,
    Dynamics 365 Developer,
    Lead Java Developer,
    Java Developer,
    PowerBI Developer,
    Account Manager,
    VP - Consulting Services,
    Senior Director, Consulting Services – Data Services,
    Solution Designer,
    HRIT/Manager,
    Oracle HCM Benefits Consultant,
    ADF Developer,
    Power BI Data Visualization expert,
    Jitterbit Developer,
    DCFS- Tester - Manual/Functional/Automation

Given these skills: {input_skills}, list 2-3 most relevant job roles from the above list of 79 roles. Research their average hourly pay in Chicago, US.

Criteria:

Match the skills with the most relevant job roles.
Understand the meaning of each role and skill set.
Choose based on dominant skills.

Response format:

[Role] (Role Match: %%) - Est Pay: $X-Y/hour

[Role] (Role Match: %%) - Est Pay: $X-Y/hour

Relevant skills that you considered for the match in short.
And, reason in 1 sentence including all technical details.


Please don't give any extra notes or anything after the response.

"""
    
    try:
        
        response = model.generate_content(prompt)
        
        output = response.text.strip()
        return output
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "I'm having trouble connecting to the service. Please try again later."

def get_skills_by_job_role(job_role: str) -> str:
    prompt = f"Given the job role: {job_role}, list 100 essential skills for this role. Provide only the skills in your response in an organized format. Please don't give any extra notes or anything asfter the response"
    
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

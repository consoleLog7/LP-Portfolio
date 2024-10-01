## Imports
import streamlit as st


## Page Setup
st.set_page_config(page_title="Logan Pugsley", page_icon="Profile_Image.jpeg")
st.write('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
st.markdown('''<style>
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    header {
        visibility: hidden;
    }
    </style>''', unsafe_allow_html=True)


## Navigation Bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('''
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #326fa8;">
        <a class="navbar-brand" href="https://www.linkedin.com/in/loganpugsley" target="_blank">Logan Pugsley</a>
    </nav>
    ''', unsafe_allow_html=True)


## Main Header
col1, col2 = st.columns([5, 2])
with col1:
    st.write('''
    # Logan Pugsley
    ###### *Business Technology Professional / Student*
    ''')
    st.markdown(":email: loganpugsley7@gmail.com")
    st.markdown(":phone: +1 (506) 863-4378")
    st.markdown(":link: www.linkedin.com/in/loganpugsley")
with col2:
    st.image("Profile_Image.jpeg")


## Summary
st.markdown("")
st.markdown('''## About''')
st.write('''
A highly motivated business technology professional that specializes in developing and implementing innovative solutions to help organizations adopt technology, mitigate risk, make data-driven decisions, automate processes, and reach strategic objectives. With a unique skillset, balancing both business expertise and technical skills, has a tremendous ability to solve complex problems and work as a team-player. Has a track-record of improving business outcomes, with specific industry experience in finance, telecommunications, and sports.

Currently working at Blue Cross Life Insurance Company of Canada as an Information Management & Technology Student on various strategic initiatives throughout the business, driving innovation and data-driven decision-making by building cloud solutions, integrating systems, improving processes, and enhancing information security initiatives. During the school year, a fourth-year student in the Gerald Schwartz School of Business at St. Francis Xavier University, working towards a Bachelor of Business Administration (BBA), Advanced Major in Enterprise Systems.
''')


## Education
st.markdown('''## Education''')
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1:
    st.image("STFX.png")
with col2:
    st.markdown('**Bachelor of Business Administration (BBA)**  \nSt. Francis Xavier University  \nAntigonish, NS')
with col3:
    st.markdown('<div style="text-align: right;">September 2021 - Present', unsafe_allow_html=True)
st.markdown('**Advanced Major:** Enterprise Systems  \n**Subsidiaries:** Computer Science, Public Policy and Governance')
st.markdown('''
    - 4th year student
    - Order of Merit Scholar at the Gerald Schwartz School of Business
    - Member of the Dean’s List (2022, 2023, 2024)
    - Service Learning Program Completion, 2023-2024
    - Full-time student athlete as skip of the men’s curling team
    - XREC Student Leadership Award, 2023-2024
    - Most Valuable Player StFX Men’s Curling, 2023-2024
''')
with st.expander("View Courses"):
    # Completed Courses
    st.markdown("### Completed:")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD101: Introduction to Business")
    with col2: st.markdown("BSAD102: Business Decision-Making")
    with col3: st.markdown("ECON101: Introductory Microeconomics")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("ECON102: Introductory Macroecnomics")
    with col2: st.markdown("MATH105: Business Mathematics")
    with col3: st.markdown("STAT101: Introductory Statistics")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("CSCI161: Intro to Programming")
    with col2: st.markdown("CSCI162: Programming & Data Structures")
    with col3: st.markdown("PGOV101: Public Policy & Governance")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("PHYS171: Intro to Astronomy I")
    with col2: st.markdown("BSAD221: Intro Financial Accounting")
    with col3: st.markdown("BSAD223: Intro Managerial Accounting")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD231: Foundations of Marketing")
    with col2: st.markdown("BSAD241: Financial Management I")
    with col3: st.markdown("BSAD261: Organizational Behaviour")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD281: Foundations of Information Technology")
    with col2: st.markdown("CSCI223: Introduction to Data Science")
    with col3: st.markdown("MATH382: Sports Analytics")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("PGOV201: Public Policy")
    with col2: st.markdown("PGOV202: Governance")
    with col3: st.markdown("BSAD321: Intermediate Managerial Accounting I")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD382: Introduction to Enterprise Systems and SAP")
    with col2: st.markdown("BSAD385: Business Programming and ABAP")
    with col3: st.markdown("BSAD386: Project Management and Practice")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("PGOV399: Local Government")
    with col2: st.markdown("BSAD322: Intermediate Managerial Accounting II")
    with col3: st.markdown("BSAD357: International Business")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD384: Data Management and Analytics")
    with col2: st.markdown("BSAD389: Technology and Innovation Management")
    with col3: st.markdown("IDS305: Immersion Service Learning")

    # Courses in Progress
    st.markdown("### In Progress:")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD450: Personal Taxation")
    with col2: st.markdown("BSAD483: Systems Analysis and Design")
    with col3: st.markdown("BSAD487: Advances in Technology and Innovation")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("ECON335: Money & Financial Markets I")
    with col2: st.markdown("CSCI225: Coding in Health Analytics")
    st.markdown("")


## Work Experience
st.markdown('''## Work Experience''')            
# BCL Internship
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("BCL.png")
with col2: st.markdown('''**Information Management & Technology Student**  \nBlue Cross Life Insurance Company of Canada  \nMoncton, NB & Remote''')
with col3: st.markdown('<div style="text-align: right;">May 2023 - Present', unsafe_allow_html=True)
st.markdown('''
    - Collaborated with the DevOps Engineering Lead to transform Blue Cross Life’s cybersecurity program, replacing legacy vendor processes by implementing cloud-native solutions powered by machine learning
    - Developed a business intelligence and analytical reporting system for the cybersecurity program, integrating data from cloud-native security solutions into a customized dashboard
    - Established a business process automation solution to streamline corporate accounts payable processes, automating the flow from invoice receipt, approval, and request for payment
    - Created a collection of SharePoint Sites and Power Automate processes to transform a process of auditing insurance claims for the Claims Management team and product distributors nationwide
    - Developed a systems integration API solution in partnership with one of Blue Cross Life’s insurance distributors, enabling a seamless flow of data between two project management systems
    - Led a project to develop a cloud-based configuration management database (CMDB) to record data about technology systems, vendors, and a software bill of materials within the organization
    - Supports technical work on a multi-year data warehouse project to integrate data from six insurance distributors into a single database for data-driven decision-making
''')
st.markdown("")

# CurlData
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("CurlData.png")
with col2: st.markdown('**Founder**  \nCurlData  \nMoncton, NB')
with col3: st.markdown('<div style="text-align: right;">July 2021 - Present', unsafe_allow_html=True)
st.markdown('''
    - Developed the world's first platform dedicated to data analytics in curling
    - Consults with curling teams to improve curling performance using data
    - Researches curling topics through blog posts and a proprietary curling analytics dashboard
    - Maintains an extensive database of relevant curling data spanning 30 years
''')
st.markdown("")

# MLT Part-Time
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('''**Data Analyst**  \nMissing Link Technologies  \nRemote''')
with col3: st.markdown('<div style="text-align: right;">September 2022 - April 2023', unsafe_allow_html=True)
st.markdown('''
    - While studying as a full-time student, transitioned to a part-time Data Analyst role
    - Improved data ETL processes and data quality for telecommunications field surveying and GPS data collection, reducing human error and to deliver better results for clients
    - Coordinated and implemented telecommunications fiber planning process automation projects
''')
st.markdown("")

# MLT Internship
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('''**Data Analyst Intern**  \nMissing Link Technologies  \nMoncton, NB''')
with col3: st.markdown('<div style="text-align: right;">May 2022 - August 2022</div>', unsafe_allow_html=True)
st.markdown('''
    - Established an innovative research program for implementing process automation solutions for Missing Link Technologies’ telecommunications planning division
    - Streamlined fiber planning processes, reducing manual effort in key business areas, saving enormous amounts of resource hours each year
''')
st.markdown("")

# MLT Co-Op
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data and Analytics Co-Op**  \nMissing Link Technologies  \nMoncton, NB')
with col3: st.markdown('<div style="text-align: right;">January 2021 - June 2021', unsafe_allow_html=True)
st.markdown('''
    - Developed technical, analytical, and project management skills by coordinating an innovative data science research project into sport, mentored by Missing Link Technologies’ Data & Analytics team
''')
st.markdown("")


## Volunteer Experience
st.markdown('''## Volunteer Experience''')       
# StFX Curling President
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("STFX_Curling.jpg")
with col2: st.markdown('''**President**  \nStFX Curling Club  \nAntigonish, NS''')
with col3: st.markdown('<div style="text-align: right;">April 2023 - Present', unsafe_allow_html=True)
st.markdown('''
    - Successfully re-established StFX’s curling program, after it had not existed for 5 years
    - Designed a program to select, develop, and compete for both men’s and women’s curling teams, ahead of annual competition at the Atlantic University Sport (AUS) Curling Championships
    - Collaborated with an Executive team to delegate and manage various projects and situations
''')
st.markdown("")

# Curling Society Treasurer
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("STFX_Curling.jpg")
with col2: st.markdown('''**Treasurer**  \nStFX Curling Society  \nAntigonish, NS''')
with col3: st.markdown('<div style="text-align: right;">September 2021 - April 2023', unsafe_allow_html=True)
st.markdown('''
    - Coordinated cash collections and disbursements for the student- managed curling society
    - Managed the society’s annual budgetary review process
''')
st.markdown("")


## Skills
st.markdown('''## Skills''')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Data Analytics & Business Intelligence**  \n`- Data Engineering`  \n`- Data Visualization`  \n`- Extract, Transform, Load (ETL)`')
with col2: st.markdown('**Cloud Computing**  \n`- Amazon Web Services (AWS)`  \n`- Microsoft Office 365`')
col1, col2 = st.columns([4, 4])
with col1: st. markdown('**Business Process Improvement**  \n`- Process Mapping and Analysis`  \n`- Automation`  \n`- Systems Integration`')
with col2: st.markdown('**Programming**  \n`- Python`  \n`- Javascript`  \n`- C++`  \n`- Java`  \n`- Visual Basic`  \n`- HTML`  \n`- ABAP`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Cybersecurity**  \n`- Cloud Security`  \n`- Day-to-Day Operations`  \n`- Incident Response`  \n`- Risk Mitigation`  \n`- Policy Compliance`')
with col2: st.markdown('**Databases**  \n`- SQL`  \n`- Oracle`  \n`- SAP S/4HANA`  \n`- SQLite`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Project Management**  \n`- Project Planning`  \n`- Agile PM`  \n`- Stakeholder Engagement`')
with col2: st.markdown('**IT Service Management**  \n`- Configuration Management Database (CMDB) Development`  \n`- Change Management`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Person Skills**  \n`- Critical Thinker`  \n`- Organized`  \n`- Communicator`  \n`- Polite`  \n`- Lifelong Learner`  \n`- Team Player`')


## Certifications and Professional Development
st.markdown('''## Certifications and Professional Development''')
# IBM Enterprise Design Thinking Practitioner
col1, col2, col3 = st.columns([1, 4, 2.2])
with col1: st.image("IBM_Design_Thinking.png")
with col2: st.markdown('**Enterprise Design Thinking Practitioner**  \nIBM')
with col3: st.markdown('Issued: September 2024', unsafe_allow_html=True)
st.markdown("") 

# AWS Certified Cloud Practitioner
col1, col2, col3 = st.columns([1, 4, 2.2])
with col1: st.image("AWS_CCP.png")
with col2: st.markdown('**AWS Certified Cloud Practitioner**  \nAmazon Web Services (AWS)')
with col3: st.markdown('Issued: April 2024', unsafe_allow_html=True)
st.markdown("")
# Professional Development Courses
with st.expander("View Professional Development Courses Completed"):
    # IBM Cybersecurity Fundamentals
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("IBM_Cybersecurity_Fundamentals.png")
    with col2: st.markdown('**IBM Cybersecurity Fundamentals**')
    with col3: st.markdown('<div style="text-align: right;">September 2024', unsafe_allow_html=True)
    st.markdown("") 

    # IBM Agile Explorer
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("IBM_Agile_Explorer.png")
    with col2: st.markdown('**IBM Agile Explorer**')
    with col3: st.markdown('<div style="text-align: right;">September 2024', unsafe_allow_html=True)
    st.markdown("") 

    # MS-900T01--A: Microsoft 365 Fundamentals
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("MS_Learn.png")
    with col2: st.markdown('**Microsoft 365 Fundamentals**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("") 

    # AWS Certified Cloud Practitioner Exam Prep Course
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Certified Cloud Practitioner Exam Prep Course**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("") 

    # Cloud Practitioner - Cloud Quest Completion Badge
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Cloud_Quest.png")
    with col2: st.markdown('**Cloud Practitioner - Cloud Quest Completion Badge**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("") 

    # AWS Technical Essentials
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Technical Essentials**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Getting Started with AWS Cloud Essentials
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Getting Started with AWS Cloud Essentials**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS Skills Centers: Becoming a Cloud Practitioner
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Skills Centers: Becoming a Cloud Practitioner**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS Skill Builder Learner Guide
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Skill Builder Learner Guide**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to AWS Marketplace
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to AWS Marketplace**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS Marketplace Overview
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Marketplace Overview**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

     # Decarbonization with AWS Introduction
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Decarbonization with AWS Introduction**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS Cloud Economics for Healthcare
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Cloud Economics for Healthcare**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS Cloud Economics for Banking
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Cloud Economics for Banking**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Cloud for CTOs
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Cloud for CTOs**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Cloud for CHROs
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Cloud for CHROs**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS Shared Responsibility Model
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Shared Responsibility Model**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Data for Executives
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Data for Executives**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Amazon Transcribe Getting Started
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Amazon Transcribe Getting Started**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to Amazon Athena
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to Amazon Athena**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Machine Learning Essentials for Business and Technical Decision Makers
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Machine Learning Essentials for Business and Technical Decision Makers**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Amazon Lex Getting Started
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Amazon Lex Getting Started**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to Machine Learning
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to Machine Learning**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Unleashing Innovation: The Generative AI Revolution
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Unleashing Innovation: The Generative AI Revolution**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Planning a Generative AI Project
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Planning a Generative AI Project**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to Generative AI
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to Generative AI**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Amazon Redshift Introduction
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Amazon Redshift Introduction**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # AWS for SAP Fundamentals
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS for SAP Fundamentals**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to Amazon Quicksight
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to Amazon Quicksight**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to Amazon Kinesis Analytics for Java Applications
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to Amazon Kinesis Analytics for Java Applications**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to Amazon Kinesis Analytics
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to Amazon Kinesis Analytics**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Introduction to AWS Data Pipeline
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Introduction to AWS Data Pipeline**')
    with col3: st.markdown('<div style="text-align: right;">April 2024', unsafe_allow_html=True)
    st.markdown("")

    # Google Generative AI Fundamentals
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("GoogleGenAIFundamentals.png")
    with col2: st.markdown('**Google Generative AI Fundamentals Certificate**')
    with col3: st.markdown('<div style="text-align: right;">December 2023', unsafe_allow_html=True)
    st.markdown("")

    # Google Introduction to Responsible AI
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("GoogleIntroResponsibleAI.png")
    with col2: st.markdown('**Google Introduction to Responsible AI Course**')
    with col3: st.markdown('<div style="text-align: right;">December 2023', unsafe_allow_html=True)
    st.markdown("")

    # Google Introduction to Large Language Models
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("GoogleIntroductionLLM.png")
    with col2: st.markdown('**Google Introduction to Large Language Models Course**')
    with col3: st.markdown('<div style="text-align: right;">December 2023', unsafe_allow_html=True)
    st.markdown("")

    # Google Introduction to Generative AI
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("GoogleIntroductionGenAI.png")
    with col2: st.markdown('**Google Introduction to Generative AI Course**')
    with col3: st.markdown('<div style="text-align: right;">December 2023', unsafe_allow_html=True)
    st.markdown("")

   # AWS Cloud Essentials - Badge
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Course.png")
    with col2: st.markdown('**AWS Cloud Essentials - Badge**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")

    # AWS Cloud Practitioner Essentials
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Cloud Practitioner Essentials**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")

    # Cloud Essentials - Knowledge Badge
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Cloud Essentials - Knowledge Badge**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")


    # Job Roles in the Cloud
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Job Roles in the Cloud**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")

    # Getting Started with Cloud Acquisition
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**Getting Started with Cloud Acquisition**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")

    # AWS Billing and Cost Management
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Billing and Cost Management**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")

    # AWS Foundations: Getting Started with the AWS Cloud
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWS_Learning.png")
    with col2: st.markdown('**AWS Foundations: Getting Started with the AWS Cloud**')
    with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
    st.markdown("")

    # IBM Introduction to Data Science
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("IBM_Data.png")
    with col2: st.markdown('**IBM Introduction to Data Science Certificate**')
    with col3: st.markdown('<div style="text-align: right;">January 2021', unsafe_allow_html=True)
    st.markdown("")

with st.expander("View Conferences and Professional Engagements"):
    # AWSome Day
    col1, col2, col3 = st.columns([1, 4, 2.2])
    with col1: st.image("AWSOMEDAY.jpeg")
    with col2: st.markdown('**AWSome Day Conference**')
    with col3: st.markdown('<div style="text-align: right;">February 2024', unsafe_allow_html=True)
    st.markdown("")


## Additional Resources
st.markdown('''## Additional Resources''')
st.write("[Resume](https://www.logan.pugsley.ca/resume)")
st.write("[Podcast Interview](https://www.curldata.ca/podcast)")
st.write("[CurlData](https://www.curldata.ca)")
st.write("[GitHub Profile](https://www.logan.pugsley.ca/git)")


## About this Portfolio
st.markdown('''## About this Portfolio''')
st.write("[About](https://www.logan.pugsley.ca/about)")
st.write("[Infrastructure Diagram](https://www.logan.pugsley.ca/diagram)")
st.write("[Source Code](https://github.com/consoleLog7/LP-Portfolio)")
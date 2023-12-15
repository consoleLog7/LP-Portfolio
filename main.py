## Imports
import streamlit as st


## Streamlit Page Setup
st.set_page_config(page_title="Logan Pugsley", page_icon="Profile_Image.jpeg")
st.write('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
hide_menu_style = '''
<style>
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    header {
        visibility: hidden;
    }
</style>
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)


## Streamlit Navigation Bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #326fa8;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/loganpugsley" target="_blank">Logan Pugsley</a>
</nav>
""", unsafe_allow_html=True)


### Main Header
col1, col2 = st.columns([5, 2])
with col1:
    st.write('''
    # Logan Pugsley
    ###### *Business Technology Professional / Student*
    ''')
    st.markdown(":email: logan@pugsley.ca")
    st.markdown(":link: https://ca.linkedin.com/in/loganpugsley")
    st.markdown(":phone: (506) 863-4378")
with col2:
    st.image("Profile_Image.jpeg")


### Summary
st.markdown("")
st.markdown('''## About''')
st.write('''
    A highly motivated business technology professional specializing in data analytics, process automation, cybersecurity, and systems integration. At twenty years old, experienced in multiple industries, including insurance, telecommunications, and sports. Focused on building an exciting and meaningful career while earning an education.

    Currently working at Blue Cross Life Insurance Company of Canada as an Information Management & Technology Student on various cybersecurity, systems integration, risk, compliance, and analytics initiatives. Proud to be a part of the team at Canada’s Most Respected Life Insurance Company!

    During the school year, a third-year student at St. Francis Xavier University working towards a Bachelor of Business Administration, Advanced Major in Enterprise Systems.
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
st.markdown('**Advanced Major:** Enterprise Systems  \n**Subsidiary:** Public Policy and Governance')
st.markdown('''
- 3rd Year Student
- Order of Merit Scholar at the Gerald Schwartz School of Business
- Member of the Dean's List (top 5% of class)
''')



## Work Experience
st.markdown('''## Work Experience''')
            
# BCL Internship
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("BCL.png")
with col2: st.markdown('''**Information Management and Technology Student**  \nBlue Cross Life Insurance Company of Canada  \nMoncton, NB''')
with col3: st.markdown('<div style="text-align: right;">May 2023 - Present', unsafe_allow_html=True)
st.markdown('''
''')
st.markdown("")

# CurlData
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("CurlData.png")
with col2: st.markdown('**Founder / Data Scientist**  \nCurlData  \nMoncton, NB')
with col3: st.markdown('<div style="text-align: right;">July 2021 - Present', unsafe_allow_html=True)
st.markdown('''
- Developed the world's first and only platform dedicated to data science and analytics in curling
- Conducts research and outreach through blog posts and team consulting
- Maintains an extensive database of relevant curling data dating back 25 years
- Developed a first-of-its-kind curling analytics dashboard available free to the curling community
''')
st.markdown("")

# MLT Part-Time
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('''**Data Analyst**  \nMissing Link Technologies  \nRemote''')
with col3: st.markdown('<div style="text-align: right;">September 2022 - April 2023', unsafe_allow_html=True)
st.markdown('''
- While studying as a full-time student, transitioned to a part-time Data Analyst role
- Improved data ETL processes for field surveying and GPS data collection
- Coordinated and implemented telecommunications data analytics and process automation projects
- Improved data quality by using technology to reduce human error, delivering improved value to clients
''')
st.markdown("")

# MLT Internship
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('''
                       **Data Analyst Intern**  \nMissing Link Technologies  \nMoncton, NB
                       ''')
with col3: st.markdown('<div style="text-align: right;">May 2022 - August 2022</div>', unsafe_allow_html=True)
st.markdown('''
- Coordinated and implemented data analytics projects by developing Python automation apps for MLT's telecommunications division
- Established an innovative research program for process automation in the telecommunications industry
- Streamlined fiber planning processes, reducing manual effort in key business areas, saving enormous amounts of resource hours each year
''')
st.markdown("")

# MLT Co-Op
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data and Analytics Co-Op**  \nMissing Link Technologies  \nMoncton, NB')
with col3: st.markdown('<div style="text-align: right;">January 2021 - June 2021', unsafe_allow_html=True)
st.markdown('''
- Through a daily Co-Op placement, was mentored by MLT's Data and Analytics team
- Developed technical, analytical, and project management skills by coordinating a data research project
- Reviewed projects completed for commercial clients
''')
st.markdown("")


## Certifications & Courses
st.markdown('''## Professional Certifications & Courses''')

# IBM Introduction to Data Science
col1, col2, col3 = st.columns([1, 4, 2.2])
with col1: st.image("AWS_Course.png")
with col2: st.markdown('**AWS Cloud Essentials Course**')
with col3: st.markdown('<div style="text-align: right;">May 2023', unsafe_allow_html=True)
st.markdown("")

# IBM Introduction to Data Science
col1, col2, col3 = st.columns([1, 4, 2.2])
with col1: st.image("IBM_Data.png")
with col2: st.markdown('**IBM Introduction to Data Science Certificate**')
with col3: st.markdown('<div style="text-align: right;">January 2021', unsafe_allow_html=True)
st.markdown("")


#####################
st.markdown('''
## Skills
''')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Data Analytics & Business Intelligence**  \n`- Data Engineering`  \n`- Data Visualization`  \n`- Extract, Transform, Load (ETL)`  \n`- Data Governance`  \n`- Process Automation`')
with col2: st.markdown('**Cybersecurity**  \n`- Day-to-Day Operations`  \n`- Event Log Monitoring`  \n`- Incident Response`  \n`- Vulnerability Management`  \n`- Risk Mitigation`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Programming**  \n`- Python`  \n`- Javascript`  \n`- C++`  \n`- Java`  \n`- Visual Basic`  \n`- HTML`  \n`- ABAP`')
with col2: st.markdown('**Databases**  \n`- SQL`  \n`- Oracle`  \n`- MySQL`  \n`- SQLite`  \n`- SAP S/4HANA`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Systems Integration**  \n`- Custom API Development`  \n`- REST API`  \n`- SAP Configuration`')
with col2: st.markdown('**IT Vendor Management**  \n`- Configuration Management Database (CMDB) Development`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Cloud Computing**  \n`- Amazon Web Services (AWS)`  \n`- Microsoft Office 365`')
with col2: st.markdown('**Project Management**  \n`- YouTrack`  \n`- Jira`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Regulatory Compliance**  \n`- Office of the Superintendent of Financial Institutions (OSFI)`')
with col2: st.markdown('**Person Skills**  \n`- Critical Thinker`  \n`- Organized`  \n`- Communicator`  \n`- Polite`  \n`- Lifelong Learner`  \n`- Team Player`')

#####################
st.markdown('''
## Additional Resources / Information
''')
st.write("[CurlData](https://www.curldata.ca)")
st.write("[Guest speaker on The Data Crunch podcast](https://www.curldata.ca/podcast)")
st.write("[Github Profile](https://github.com/consoleLog7)")

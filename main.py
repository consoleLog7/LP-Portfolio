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


###Main Header
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


##### Summary
# st.markdown('## Summary', unsafe_allow_html=True)
# st.info('''
# ''')


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
- Maintains an extensive database of relevant curling data dating back 20 years
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
- Coordinated and implemented telecommunications data analytics projects
- Improved data ETL processes for field surveying and GPS data collection
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
- During a summer internship, coordinated and implemented data analytics projects by developing Python automation apps for MLT's telecommunications division
- Streamlined fiber planning processes, reducing manual effort in key business processes
''')
st.markdown("")

# MLT Co-Op
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data and Analytics Co-Op**  \nMissing Link Technologies  \nMoncton, NB')
with col3: st.markdown('<div style="text-align: right;">January 2021 - June 2021', unsafe_allow_html=True)
st.markdown('''
- Worked with MLT's Data and Analytics team through a daily Co-Op placement
- Developed technical and analytical skills by working on a complete data research project
''')
st.markdown("")


## Certifications & Courses
st.markdown('''## Certifications & Courses''')

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
with col3: st.markdown('<div style="text-align: right;">December 2020', unsafe_allow_html=True)
st.markdown("")


#####################
st.markdown('''
## Skills
''')
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
with col1: st.markdown('**Cybersecurity**')
with col2: st.markdown('**Project Management**')
with col3: st.markdown('**Programming**  \n`Python`, `Javascript`, `C++`, `Java`, `Visual Basic`, `HTML`')
with col4: st.markdown('**Business Intelligence**')
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
with col1: st.markdown('**Process Automation**')
with col2: st.markdown('**Data & Analytics**  \n`SQL`, `pandas`, `numpy`, `Data Governance`')
with col3: st.markdown('**Telecom**  \n`AutoCAD`, `Trimble`, `Data Management`, `QGIS`')
with col4: st.markdown('**Person Skills**  \n`Polite`, `Lifelong Learner`, `Team Player`, `Critical Thinker`, `Organized`')
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
with col1: st.markdown('**Systems Integration**  \n`API Development`')
with col2: st.markdown('**IT Risk Management**')
with col3: st.markdown('**Regulatory Compliance**')
with col4: st.markdown('**Cloud Computing**  \n`AWS`')
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])



#####################
st.markdown('''
## Additional Resources / Information
''')
st.write("[CurlData](https://www.curldata.ca)")
st.write("[Guest speaker on The Data Crunch podcast](https://www.curldata.ca/podcast)")
st.write("[Github Profile](https://github.com/consoleLog7)")


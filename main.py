# Imports
import streamlit as st

# Streamlit Page Setup
st.set_page_config(page_title="Logan Pugsley", page_icon=r"https://media-exp1.licdn.com/dms/image/C4E03AQE3m1b8N94S4Q/profile-displayphoto-shrink_100_100/0/1651492727145?e=1665619200&v=beta&t=mF_H8aKHWI-0omiMUT42UuDMDOPkq9UDZEI8r5A5Shc")
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

# Streamlit Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #326fa8;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/loganpugsley" target="_blank">Logan Pugsley</a>
</nav>
""", unsafe_allow_html=True)







#### Main Header
col1, col2 = st.columns(2)
with col1:
    st.write('''
    # Logan Pugsley
    ##### *Data Analyst / Student* 
    ''')
    st.markdown(":email: loganpugsley7@gmail.com")
    st.markdown(":link: https://ca.linkedin.com/in/loganpugsley")
    st.markdown(":phone: (506) 863-4378")

with col2:
    st.image("Profile_Image.jpeg")


##### Summary
# st.markdown('## Summary', unsafe_allow_html=True)
# st.info("blabkabla")




##### Education
st.markdown('''## Education''')
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    st.image("STFX.png")
with col2:
    st.markdown('**Bachelor of Business Administration**, *St. Francis Xavier University*')
with col3:
    st.markdown("2021-Present")
st.markdown('Major: Enterprise Systems -  Subsidiary: Public Policy and Governance')
st.markdown('''
- 2nd Year Student
- Order of Merit Scholar in the Schwartz School of Business
- Member of the Dean's List
- Taking courses in Information Technology, Project Management, SAP, Accounting, Financial Management, Computer Science, etc.
''')



##### Work Experience

### MLT Part-Time
st.markdown('''
## Work Experience
''')
col1, col2, col3 = st.columns([1, 4, 1])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data Analyst**, Missing Link Technologies, Moncton, NB')
with col3: st.markdown('September 2022 - Present')
st.markdown('''
- While studying as a full-time student, transitioned to a part-time Data Analyst role
- Coordinated and implemented analytics projects for MLT’s telecommunications division to streamline OSP (Outside Plant) engineering and fibre planning processes.
- Specialized in telecom data analytics and process improvement related to AutoCAD, Trimble, QGIS, etc.
''')
st.markdown("")


### MLT Internship
col1, col2, col3 = st.columns([1, 4, 1])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data Analyst Intern**, Missing Link Technologies, Moncton, NB')
with col3: st.markdown('May 2022 - August 2022')
st.markdown('''
- Coordinated and implemented analytics projects for MLT’s telecommunications division to streamline OSP (Outside Plant) engineering and fibre planning processes.
- Specialized in telecom data analytics and process improvement related to AutoCAD, Trimble, QGIS, etc.
''')
st.markdown("")

### CurlData
col1, col2, col3 = st.columns([1, 4, 1])
with col1: st.image("CurlData.png")
with col2: st.markdown('**Founder / Data Scientist**, CurlData')
with col3: st.markdown('July 2021 - Present')
st.markdown('''
- Developed the world's first and only platform dedicated to promoting curling analytics through data-based research
- Continues research and outreach through blog posts and team consulting
- Maintains an extensive database of relevant curling data dating back 20 years
''')
st.markdown("")


# MLT Co-Op
col1, col2, col3 = st.columns([1, 4, 1])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data and Analytics Co-Op**, Missing Link Technologies, Moncton, NB')
with col3: st.markdown('January 2021 - June 2021')
st.markdown('''
- Worked with MLT's Data and Analytics team through a daily Co-Op placement
- Developed technical and analytical skills by working on a complete data research project
''')
st.markdown("")


#####################
# st.markdown('''
# ## Certifications
# ''')
# col1, col2 = st.columns([3,2])
# with col1: st.markdown('IBM Introduction to Data Science')
# with col2: st.markdown('https://www.edx.org/course/intro-to-data-science')


#####################
st.markdown('''
## Skills
''')
col1, col2 = st.columns([2, 3])
with col1: st.markdown('Programming')
with col2: st.markdown('`Python`, `Javascript`, `C++`, `Java`, `HTML`')
col1, col2 = st.columns([2, 3])
with col1: st.markdown('Business Intelligence')
with col2: st.markdown('`Process Improvement`, `Project Management`')
col1, col2 = st.columns([2, 3])
with col1: st.markdown('Data Analysis')
with col2: st.markdown('`SQL`, `pandas`, `numpy`')
col1, col2 = st.columns([2, 3])
with col1: st.markdown('Telecom')
with col2: st.markdown('`AutoCAD`, `Trimble`, `Data Management`, `QGIS`')
col1, col2 = st.columns([2, 3])
with col1: st.markdown('Person Skills')
with col2: st.markdown('`Polite`, `Lifelong Learner`, `Team Player`, `Critical Thinker`, `Organized`')



#####################
st.markdown('''
## Additional Resources / Information
''')
st.write("[CurlData](https://www.google.com)")
st.write("[Guest speaker on The Data Crunch podcast](https://www.google.com)")
st.write("[Github Profile](https://www.google.com)")


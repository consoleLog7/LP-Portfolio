## Imports
import streamlit as st


## Page Setup
st.set_page_config(page_title="Logan Pugsley", page_icon="Profile_Image.jpg")
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
    ###### *Business Analytics and Technology Professional*
    ''')
    st.markdown(":email: loganpugsley7@gmail.com")
    st.markdown(":phone: +1 (506) 863-4378")
    st.markdown(":link: www.linkedin.com/in/loganpugsley")
with col2:
    st.image("Profile_Image.jpeg")


## Summary
st.markdown("")
st.markdown('''## About''')
st.write('''Logan Pugsley is a Digital Risk Staff Consultant in the Risk Consulting practice at Ernst & Young LLP. He joined the firm in September 2025 after obtaining his BBA Advanced Major in Enterprise Systems at Saint Francis Xavier University. 
Logan has previously worked with organizations across several industries, including provincial and municipal governments, crown corporations, educational institutions, as well as various public and private organizations across financial services, insurance, telecommunications, automotive, retail, and mining. His experience has focused on data analytics, business process optimization, digital transformation, cybersecurity, internal audit, risk assessment, technology risk and compliance, and disaster recovery. 
Logan’s background allows him to balance both business expertise and technical abilities to advise organizations across various industries to identify opportunities for transformation.''')


## Education
st.markdown('''## Education''')
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1:
    st.image("STFX.png")
with col2:
    st.markdown('**Bachelor of Business Administration (BBA), Advanced Major with Distinction**  \nSt. Francis Xavier University  \nAntigonish, NS')
with col3:
    st.markdown('<div style="text-align: right;">September 2021 - May 2025', unsafe_allow_html=True)
st.markdown('**Advanced Major:** Enterprise Systems  \n**Subsidiaries:** Computer Science, Public Policy and Governance')
st.markdown('''
    - Order of Merit Scholar at the Gerald Schwartz School of Business
    - Member of the Dean’s List (2022, 2023, 2024, 2025)
    - Service Learning Program Completion, 2023-2024
    - Full-time student athlete as Skip of the X-Men Curling team
    - XREC Student Leadership Award, 2023-2024
    - Most Valuable Player StFX Men’s Curling, 2023-2024
''')
with st.expander("View Courses"):
    # Completed Courses
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
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD450: Personal Taxation")
    with col2: st.markdown("BSAD483: Systems Analysis and Design")
    with col3: st.markdown("BSAD487: Advances in Technology and Innovation")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("ECON335: Money & Financial Markets I")
    with col2: st.markdown("CSCI225: Coding in Health Analytics")
    with col3: st.markdown("BSAD471: Strategic Management")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD482: Decision Intelligence & Analytics")
    with col2: st.markdown("BSAD492: Advanced Majors Consulting Project")
    with col3: st.markdown("PGOV302: Public Management")
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1: st.markdown("BSAD495: Artificial Intelligence for Technology Management and Marketing")


## Work Experience
st.markdown('''## Work Experience''')            
# EY
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("EY.png")
with col2: st.markdown('''**Consultant, Digital Risk Consulting**  \nErnst & Young LLP (EY)  \nHalifax, Nova Scotia''')
with col3: st.markdown('<div style="text-align: right;">September 2025 - Present', unsafe_allow_html=True)
st.markdown('''
    - Provides technology and risk consulting services across provincial and municipal governments, crown corporations, educational institutions, financial services companies, automotive manufacturers, and mining companies, including Fortune 500 and publicly traded firms.
    - Performed data analytics and visualization on enterprise payroll datasets to identify overtime trends, policy compliance issues, and cost-reduction opportunities for a municipal government.
    - Provides data-driven internal audit services to organizations across multiple sectors to review business processes, governance, and technology solutions, and identify opportunities for business process improvement and digital transformation to senior management.
    - Conducted a fraud risk assessment and control design evaluation, identifying vulnerabilities and recommending mitigation strategies and technology solutions for a provincial government.
    - Executed assessments over Internal Controls over Financial Reporting (ICFR) and Information Technology General Controls (ITGC) to validate data accuracy, system integrity, and information security across multiple public and private sector organizations.
    ''')
st.markdown("")

# BCL Internship
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("BCL.png")
with col2: st.markdown('''**Information Management & Technology Student**  \nBlue Cross Life Insurance Company of Canada  \nMoncton, New Brunswick & Remote''')
with col3: st.markdown('<div style="text-align: right;">May 2023 - May 2025', unsafe_allow_html=True)
st.markdown('''
    - Transformed the national insurance claims management and auditing process by automating enterprise workflows, leveraging Power Platform, and reduced manual data processing and review by the claims management team by 80%.
    - Developed a custom business intelligence and analytics reporting system for the cybersecurity team, integrating data from cloud-native cybersecurity platforms into interactive dashboards for live cybersecurity operations monitoring and reporting.
    - Contributed to a multi-year enterprise cloud data warehouse initiative integrating data from six insurance distributors to support data-driven business decisions.
    - Implemented systems integrations and API solutions to automate data flows and improve extract, transform, and load processes across various technology systems.
    - Transformed the company's cybersecurity program by auditing and replacing legacy processes with cloud cybersecurity solutions powered by artificial intelligence.
''')
st.markdown("")

# MLT
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('''**Data Analyst**  \nMissing Link Technologies  \nMoncton, New Brunswick and Remote''')
with col3: st.markdown('<div style="text-align: right;">May 2022 - May 2023', unsafe_allow_html=True)
st.markdown('''
    - Developed Python automation tools to streamline telecommunications fiber planning workflows, reducing key operational hours spent on repetitive, manual engineering processes.
    - Improved ETL pipelines and data validation processes for telecommunications field GPS data collection, significantly reducing human error and improving dataset reliability.
    - Designed automation and analytics workflows to process and analyze large field-survey datasets used for telecommunications infrastructure planning, delivering enhanced accuracy for clients.
    - In collaboration with data scientists, established a process automation research program to identify analytics and automation opportunities within telecommunications fiber planning.
    ''')
st.markdown("")

# MLT Co-Op
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("MLT.png")
with col2: st.markdown('**Data and Analytics Co-Op**  \nMissing Link Technologies  \nMoncton, New Brunswick')
with col3: st.markdown('<div style="text-align: right;">February 2021 - June 2021', unsafe_allow_html=True)
st.markdown('''
    - Coordinated a data science research project analyzing sports performance datasets, applying statistical and analytical techniques under mentorship from the company's analytics team.
    - Developed foundational skills in data analysis, project management, business process improvement, and change management while collaborating with professional data scientists.
    - Evaluated prior client analytics projects to understand real-world data engineering and analytical solution delivery.
    ''')
st.markdown("")


## Skills
st.markdown('''## Skills''')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Data Analytics & Business Intelligence**  \n`- Data Engineering`  \n`- Data Visualization`  \n`- Extract, Transform, Load (ETL)` \n`- Tableau` \n`- Alteryx` \n`- Power BI`')
with col2: st.markdown('**Programming & Databases**  \n`- Python`  \n`- SQL` \n`- JavaScript` \n`- Others: C++, Java, HTML, Visual Basic, ABAP`')
col1, col2 = st.columns([4, 4])
with col1: st. markdown('**Cloud Computing**  \n`- Amazon Web Services`  \n`- Microsoft Azure`  \n`- Microsoft Office 365` \n`- Power Platform`')
with col2: st.markdown('**Process Improvmenet**  \n`- Process Automation`  \n`- Process Mapping`  \n`- Systems Integration`')
col1, col2 = st.columns([4, 4])
with col1: st.markdown('**Risk Management & Audit**  \n`- Internal Audit`  \n`- Process & Controls Evaluation`  \n`- Risk Assessment`')
with col2: st.markdown('**Person Skills**  \n`- Critical Thinker`  \n`- Organized`  \n`- Strong Communicator`')


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


## Volunteer Experience
st.markdown('''## Volunteer Experience''')       
# StFX Curling President
col1, col2, col3 = st.columns([1.5, 4, 2.2])
with col1: st.image("STFX_Curling.jpg")
with col2: st.markdown('''**President**  \nStFX Curling Club  \nAntigonish, NS''')
with col3: st.markdown('<div style="text-align: right;">April 2023 - May 2025', unsafe_allow_html=True)
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


## Additional Resources
st.markdown('''## Additional Resources''')
st.write("[Source Code](https://github.com/consoleLog7/LP-Portfolio)")
st.write("[GitHub Profile](https://www.logan.pugsley.ca/git)")
st.write("[Podcast Interview](https://www.curldata.ca/podcast)")
st.write("[CurlData](https://www.curldata.ca)")

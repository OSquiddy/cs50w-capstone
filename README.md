# Requirements

The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be entirely up to you, albeit subject to the staff’s approval.

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

- Your web application must utilize at least two of Python, JavaScript, and SQL.
- Your web application must be mobile-responsive.
- In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project.
- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!

Beyond these requirements, the design, look, and feel of the website are up to you!

<br>

# Introduction

My final project started off as an Electronic Medical Record (EMR) System, but then I got too ambitious and thought I'd go ahead and create a whole clinic/hospital management system. The basic idea was that I should have a platform where both doctors and patients can sign in and do some specific tasks:

- *Patient:*
  - *Sign up for the app*
  - *View a directory of doctor profiles (including information about their qualifications, work timings etc)*
  - *Book an appointment with a doctor of their choice*
  - *Update their histories of illnesses and operations*
  - *Upload medical reports/tests for their doctors to view*
  - *Keep track of all appointments they have*
  - *Pay for their appointments*

- *Doctor:*
  - *View upcoming appointments*
  - *Create new appointments*
  - *Add any walk-in patients to the platform* 
  - *Create entries for each patient visit/appointment.* 
  - *The information entered by the doctor would automatically be stored as a PDF report, which could be viewed/printed by either the doctor or the patient themselves.*
  - *A doctor would also be able to view the patient's history of past illnesses (family/personal), which would make prescribing non-conflicting medicines easier, since the doctor would also be aware of other parallel treatments/medications that the patient was undergoing.*

As I said, I got a bit too ambitious. Shortly after I started this project I was able to land a full time job in Web Development, which did not leave me with a lot of time to spend on this project. A few months later, I've finally decided to get off the couch in my free time and complete what I had started earlier. Due to time constraints, I haven't been able to add everything I wanted to, but I am reasonably happy with the final product. It works as a proof of concept for what I had earlier imagined.

<br>

# *Electronic Medical Record / Hospital Management System*

This project was built using Django + Django Rest Framework (DRF) as the backend, with Vue.js (Vue 2) as the frontend. All generated information is stored in the default SQLite database. If I am able to host this site on a platform, like my other CS50W projects I'll probably go ahead with PostgreSQL. 

## Installation

**Initial Steps:**
- Clone the repository using the command `git clone https://github.com/OSquiddy/cs50w-capstone.git` and move into the **cs50w-capstone** directory using the command `cd cs50w-capstone`. *This step is not needed for instructors*
- *(Optional Step)* Create a virtual environment for the project using the command `python3 -m venv .myenv` or `python -m venv .myenv`, where **.myenv** is the name of the virtual environment. You can put any name you want.
- To activate the virtual env on Windows, type: `.myenv\Scripts\activate`
- To activate the virtual env on Mac/Unix: `source .myenv/bin/activate`

**Note: You will need to run 2 terminals in parallel. One for the frontend, and the other for the backend**

Once this repository has been cloned, you can do the following:

**Backend Installation:**
- Navigate to the backend directory by running the command `cd capstone/backend`
- Install backend dependencies by running `pip install -r requirements.txt`. The main dependencies are Django *(main backend)*, Pillow *(Allows work with images)*, ReportLab *(Used to generate the PDF reports)* and Djoser *(authentication endpoints)*
- Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`
- Run the server using `python manage.py runserver 5500`

**Note: It is important to run the backend server on port 5500**

**Frontend Installation:**
You need to have NPM and Node installed on your machine for the following commands

- Navigate to the frontend directory by running the command `cd capstone/frontend`
- Install frontend dependencies by running `npm i`
- Start the dev server by running `npm run serve`

**Signing In:**
You can sign in to the system by using the doctor's credentials:
- Username: severusSnape
- Password: 1234

# Distinctiveness and Complexity

Complexity for this project can be argued in a few different ways. 

The first complexity I'd say came from learning how to integrate Django with a frontend framework like Vue. There were a lot of different approaches available, and I was very keen on being able to implement one that would allow me to keep the Django templating engine, alongside whatever frontend framework I was using. I grew somewhat attached to the simplicity of Django's frontend management, and felt that keeping Django as just a backend would be limiting its potential.

I read quite a few different articles and blogs to find out if there was a way to get the behaviour I wanted, and there *was* one person who did it... but unfortunately, their method did not work for me. I've included a link though. Maybe someone else will be able to figure out something. I will definitely be revisiting that method later.

What I finally settled with was the Django Rest Framework (DRF), where Django is used only for the API endpoints. The frontend is completely managed by Vue.

Coming to the application itself, it has all the basic requirements of a complex web app. User authentication/authorization, CRUD functionilities etc. A few app specific areas of complexity include learning D3.js for the generation of the charts on the overwiew page, as well as ReportLab, to generate PDF reports of patient appointments.

D3 was something I learned at work, and I wanted a way to improve my command over it, so I integrated it into this project. The parts where I've been able to add transitions to the charts were something I've never done anywhere else. Learned it while working on this.

Similarly, I've learned the basics of the ReportLab library just for this project, and will be exploring it a lot more. It's a very useful and powerful tool to have in your belt.

Another 

# Detailed Summary of the Files and Directories

## Backend

- **capstone** - main application directory
  - **backend** - contains all the Django related code for the backend
    - **capstone** - the django project directory (Contains all configuration files for the backend)
      - **settings.py**
      - **urls.py**
      - **wsgi.py**
      - **asgi.py**
    - **emrsystem** - the app created for this project
      - **migrations** - contains the migration data for the app
      - **admin.py** - contains the admin panel related code
      - **apps.py**
      - **models.py** - contains all the models for the app
      - **serializers.py** - contains all the serializers for the models *(JSON)*. This is needed for communication with the frontend using the Rest Framework
      - **urls.py** - contains the urls for the app
      - **utils.py** - contains the utility functions for the app. (Report generation and appointment list filtering functions)
      - **views.py** - contains all the logic for the APIs of the app

## Frontend

- **capstone** - main application directory
  - **frontend** - contains the Vue code for the frontend
  - **build** - contains the files built for serving in a production environment
  - **node_modules** - contains all the dependencies and sub-dependencies installed through npm
  - **public** - contains all public assets *This mainly contains the reports generated through the ReportLab library*
  - **src** - contains the source code for the Vue app
    - **assets** - contains the static data that needs to be served on the app using the **development server**
    - **components** - contains all the reusable Vue components created for the app
      - **CustomCalendar.vue** - Code for the daily upcoming appointments viewer. The doctor can view all upcoming appointments for a certain day by clicking on it's date. This components only shows the doctor the appointments for the current month. For the rest of the appointments the doctor can visit the dedicated Appointments page.
      - **DonutChart.vue** - contains the code for the donut chart found on the Overview page. The chart is generated using the *D3.js* library. It shows the genderwise distribution of patients in the database.
      - **EarningsBarChart.vue** - contains the code for the barchart found on the Overview page. The chart is generated using the *D3.js* library. It shows the month-wise earnings of the establishment.
      - **EarningsLineChart.vue** - contains the code for the line chart found on the Overview page. The chart is generated using the *D3.js* library. It shows the total earnings of the establishment, from the first appointment. Hovering over the data will show the earnings from and data of each appointment recorded.
      - **Layout.vue** - contains the layout for the Desktop site. All other components/views are nested within this component
      - **LayoutMobile.vue** - contains the layout for the Mobile site. All other components/views are nested within this component
      - **LocalTabs.vue** - contains the code for the local navigation bar found on the patient information pages
      - **LoginPage.vue** - contains the code for the login page
      - **NoDataContainer.vue** - contains the code for the container that shows up when there is no data to be displayed
      - **PatientHeader.vue** - contains the code for the Patient information header shown on any of the patient related pages in the Desktop view. 
      - **PatientSmall.vue** - contains the code for the miniature patient header shown on any of the patient related pages in the Mobile view.
      - **SearchableDropdown.vue** - contains the code for the searchable dropdown found on the New Appointment page
      - **SearchContainer.vue** - contains the code for the live filtering, when a keyword is entered into any searchbar
    - **router**
      - **index.js** - contains the routes served by Vue on the frontend
    - **store**
      - **index.js** - contains the data and methods that are stored in the Vuex store. These variables/methods and their states are globally available throughout the app  
      - **search.js** - contains the vuex data related to the live search functionality. This module is appended to the index.js file at compile time
    - **util** - contains some utility functions 
      - **tooltip.js** - contains the code used to render the custom tooltip for the D3 charts
      - **util.js** - contain a utility function for the vue app. *(Debounce, Snackbar, defaultPic)*
    - **views**
      - **AppointmentEntry** - contains the code/view for form in which the doctor enters all appointment related data/observations
        - **AppointmentEntry.vue**
      - **Appointments** - contains the code for viewing all appointments in the app. (Dedicated appointments page)
        - **Appointments.vue**
        - **AppointmentsMobile.vue**
      - **MainPage** - contains the code for the Main/Overview page. This page contains a sort of dashboard for the doctor
        - **MainContainer.vue**
        - **MainContainerMobile.vue**
      - **NewAppointment** - contains the code for the page that allows you to create a new appointment
        - **NewAppointment.vue**
        - **NewAppointmentMobile.vue**
      - **NewPatient** - contains the code for the page that allows you to add a patient to the database
        - **NewPatient.vue**
        - **NewPatientMobile.vue**
      - **PatientDirectory** - contains the code for the page that allows you to view the patient database
        - **PatientDirectory.vue**
        - **PatientDirectoryMobile.vue**
      - **PatientInfo** - contains the code that allows you to view detailed information about a patient (History, Reports, Overview etc)
        - **PatientHistory.vue**
        - **PatientMain.vue**
        - **PatientMainMobile.vue**
        - **PatientOverview.vue**
      - **Reports** - contains the code that allows you to view/download the PDF reports of the patient
        - **Report.vue**
        - **ReportMobile.vue**
      - **App.scss** - contains the styling that is common throughout the site
      - **App.vue** - is the parent component for any Vue application
      - **main.js** - JS file which mounts the Vue application onto the website
    - **package.json** - Contains dependancy information
  - **.gitignore** - Contains a list of files/folders that are not tracked by Git 

# Areas for improvement

- The search functionality on the Mobile Appointments page can be made more powerful. Currently it recognizes IDs, partial dates (Numbers can either be the days of the month, or the number of the month itself), partial names and full dates (ISO format - *YYYY-MM-DD*). It would be helpful if we could search for dates like *'2020-08'*, which would filter all results from August, or even dates in string formats, like *'21st July'*.
- Add in a dark mode theme
- Finish the Patients module
- Serve static files through a CDN instead of hosting them on the main server
- Forms currently do not have a error messages show up per input. If the form submission fails as a whole, then a small message shows up, but there are no specific messages. Need to add that later.
- Add some code for better patient confidentiality. Currently any doctor who signs in has full access to the entire patient database. We could write some conditions to make sure that doctors are only able to access the information of patients that they are treating, unless they're given some sort of permission.
- Need to show the Past History in Mobile mode.
- Need to update the Report PDF to take in the Past History information
# Avicenna

An Electronic Medical Record and clinic management platform. Doctors manage appointments, record patient visits, and generate PDF reports. Patients book appointments, maintain their medical history, and upload test results.

**[Live demo](https://avicenna.omarsiddiqui.dev)** · **[Video walkthrough](https://youtu.be/4SJu4Y8Bu18)**

Built with Django REST Framework and Vue.js. The overview dashboard uses custom D3.js charts that update as patients and appointments are added.

### Demo account

| | |
|---|---|
| Username | `severusSnape` |
| Password | *(see note below)* |

The demo instance holds seeded test data only. There is no real patient information in it.

<!--
TODO before sharing this link widely:
1. Rotate this password to something non-trivial and put the new one here.
2. Add 3 or 4 screenshots to a /screenshots directory and embed them below.
   The overview dashboard with the D3 charts should be the first one.
-->

<br>

## What it does

**Doctor**

- View upcoming appointments on a monthly calendar, or through a dedicated appointments page with live search
- Create appointments and add walk-in patients directly
- Record observations for each visit, which are automatically written to a PDF report that either the doctor or the patient can view and print
- View a patient's history of personal and family illnesses, so prescriptions can account for treatments already underway
- An overview dashboard showing patient demographics and earnings over time

**Patient**

- Sign up, then browse a directory of doctor profiles with qualifications and working hours
- Book an appointment with a doctor of their choice
- Maintain a history of illnesses and operations
- Upload medical reports and test results for their doctor to see
- Track all of their appointments

The interface is fully responsive, with separate desktop and mobile layouts rather than a single design that reflows.

<br>

## Stack

| Layer | Technology |
|---|---|
| Backend | Django, Django REST Framework |
| Frontend | Vue.js (Vue 2), Vuex, Vue Router |
| Charts | D3.js |
| PDF generation | ReportLab |
| Authentication | Djoser |
| Image handling | Pillow |
| Database | SQLite in local development. <!-- CONFIRM what Render is actually running and state it here --> |
| Hosting | Render. Originally deployed on a VM I managed myself with Nginx. |

<br>

## Architecture

Django serves API endpoints only. Vue owns the entire frontend and talks to the backend over REST. The two run as separate applications.

```
Browser
   |
   |  Vue SPA (Vue Router handles all client-side routing)
   |
   |  REST over HTTP
   v
Django REST Framework
   |
   +-- emrsystem app
   |     models.py       patients, doctors, appointments, visit records
   |     serializers.py  JSON representation for every model
   |     views.py        API logic
   |     utils.py        PDF report generation, appointment filtering
   |
   +-- Djoser            authentication endpoints
   |
   v
Database
```

I did not start here. See the engineering notes below for how I arrived at it.

<br>

## Running it locally

You will need two terminals, one for the backend and one for the frontend.

**Clone**

```bash
git clone https://github.com/OSquiddy/cs50w-capstone.git
cd cs50w-capstone
```

**Backend**

```bash
cd capstone/backend

# optional but recommended
python3 -m venv .myenv
source .myenv/bin/activate        # Windows: .myenv\Scripts\activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 5500
```

The backend has to run on port 5500. The frontend expects it there.

If `migrate` reports that no migrations were applied or no changes were detected, that is fine. It means the SQLite file is already present.

**Frontend**

```bash
cd capstone/frontend
npm i
npm run serve
```

<br>

## Engineering notes

### Getting Django and Vue to work together

The first real problem was integration. There were a lot of approaches available, and I was keen on one that would let me keep Django's templating engine alongside whatever frontend framework I used. I had grown somewhat attached to the simplicity of Django's frontend management, and it felt like reducing Django to a pure backend was limiting what it could do.

I read quite a few articles and blog posts looking for a way to get the behaviour I wanted. There *was* one person who had done it, but their method did not work in my setup, and I spent longer than I should have trying to make it work anyway.

Eventually I accepted that the approach was wrong for this project and rebuilt around Django REST Framework, with Django handling only the API endpoints and Vue owning the frontend completely. The decoupled version was simpler, easier to reason about, and made the mobile and desktop layouts far more manageable.

The lesson I took from it was about the cost of staying attached to an approach. I was protecting a preference that was not actually load bearing.

### The D3 charts

I learned D3 at work and wanted a way to push my command of it further, so I built the overview dashboard around it rather than reaching for a chart library.

There are three charts, all in `src/components`:

- `DonutChart.vue` shows the gender distribution across the patient database
- `EarningsBarChart.vue` shows month by month earnings
- `EarningsLineChart.vue` shows cumulative earnings from the first appointment onward, with hover detail on each data point

They regenerate as patients are added, appointments are created, and visits are completed. The transitions were new to me, I had not built animated D3 anywhere else before this, and getting them working properly took a fair bit of experimentation. `src/util/tooltip.js` holds the custom tooltip logic shared across all three.

### PDF report generation

The doctor's visit observations get written to a PDF automatically, using ReportLab. I learned the library specifically for this project. The generation logic sits in `emrsystem/utils.py`.

<br>

## Project structure

```
capstone/
├── backend/
│   ├── capstone/            Django project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── emrsystem/           the application
│       ├── models.py        patients, doctors, appointments, visits
│       ├── serializers.py   JSON serialization for the REST API
│       ├── views.py         API logic
│       ├── utils.py         PDF generation, appointment filtering
│       ├── urls.py
│       ├── admin.py
│       └── migrations/
│
└── frontend/
    ├── public/              static assets and generated reports
    └── src/
        ├── components/      reusable components, including the three D3 charts
        │   ├── DonutChart.vue
        │   ├── EarningsBarChart.vue
        │   ├── EarningsLineChart.vue
        │   ├── CustomCalendar.vue     monthly appointment viewer
        │   ├── SearchableDropdown.vue
        │   ├── SearchContainer.vue    live filtering for every search bar
        │   ├── Layout.vue             desktop shell
        │   └── LayoutMobile.vue       mobile shell
        ├── views/           one directory per page, desktop and mobile variants
        │   ├── MainPage/              overview dashboard
        │   ├── Appointments/
        │   ├── NewAppointment/
        │   ├── AppointmentEntry/      visit observation form
        │   ├── NewPatient/
        │   ├── PatientDirectory/
        │   ├── PatientInfo/           history, reports, overview
        │   └── Reports/               PDF viewer
        ├── store/           Vuex state, with live search in its own module
        ├── router/
        └── util/            tooltip logic for the D3 charts, debounce, snackbar
```

Most pages exist as both a desktop and a mobile component rather than one responsive component, which was a deliberate choice given how differently the two layouts needed to behave.

<br>

## Known limitations

These are known and unaddressed, not oversights. Listing them here because the alternative is someone finding them and assuming I did not know.

- **Authorization is not scoped per doctor.** Any signed in doctor can currently access the full patient database. The correct behaviour is for a doctor to see only the patients they are treating, unless explicitly granted access. This is the first thing I would fix, and it is the most important item on this list.
- **Form validation is form level, not field level.** A failed submission shows one message rather than highlighting the specific input that caused it.
- **No appointment time slot checking.** Nothing currently prevents two appointments being booked in the same slot with the same doctor.
- **Past medical history is missing from the mobile view**, and is not yet included in the generated PDF reports.
- **The Patients module is incomplete.**
- **Static files are served from the application server** rather than a CDN.
- **Mobile appointment search is limited.** It handles IDs, partial names, partial dates, and full ISO dates. It does not yet handle month level queries like `2020-08` or natural formats like `21st July`.

<br>

## What I would do differently

- **Scope the authorization from the start.** Retrofitting per doctor access control onto views that were written assuming full access is more work than building it in would have been, and on a medical records system it should never have been deferred.
- **Decide on the Django and Vue integration earlier.** I spent real time trying to preserve Django templating before accepting a decoupled architecture, and the decoupled version turned out to be the better design regardless.
- **Use PostgreSQL from the beginning.** Starting on SQLite meant a migration later that would not have been necessary.
- **Write tests.** There are none, and the PDF generation and appointment filtering logic in `utils.py` are exactly the kind of code that should have them.

<br>

## Background

This started as my capstone for CS50W, Harvard's Web Programming with Python and JavaScript. The original brief was an Electronic Medical Record system, and I widened it into a fuller clinic management platform, which put it well beyond what the course required.

I began it shortly before starting my first full time web development job, which meant it sat unfinished for several months before I came back and completed it. I have continued to extend and maintain it since.
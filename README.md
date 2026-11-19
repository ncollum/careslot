# CareSlot

CareSlot is a clinic appointment booking site. Patients can find a doctor, see open time slots and book a visit online. It is our group project for COMP 8347 at the University of Windsor. 
> My contributions: the doctors module, including doctor data models, fixtures, and the list, search, and detail pages.

## Running it on your computer

You need Python 3.14 and Git.

1. Clone the repo and go into the folder.

   ```
   git clone https://github.com/Tashdidtrdb/CareSlot.git
   cd CareSlot
   ```

2. Create a virtual environment and install the packages.

   Mac:

   ```
   python3.14 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows:

   ```
   py -3.14 -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the database and start the server.

   ```
   python manage.py migrate
   python manage.py runserver
   ```

4. Open http://127.0.0.1:8000 in your browser.

To use the admin site, create an account with `python manage.py createsuperuser` and go to http://127.0.0.1:8000/admin.

## Project layout

| Folder | What goes in it |
|---|---|
| `careslot/` | Project settings and the main `urls.py` |
| `core/` | Home page, About, Contact, FAQ, Privacy, user history |
| `accounts/` | Register, login, logout, password reset, patient profile |
| `doctors/` | Clinics, specialties, doctors, doctor search |
| `appointments/` | Time slots, booking, rescheduling, cancelling, patient dashboard |
| `records/` | Medical document uploads and doctor reviews |
| `articles/` | Health articles |

## Working on the code

Open the repo folder in PyCharm. The `.editorconfig` file and the shared settings in `.idea/inspectionProfiles/` set up indentation and warnings for you.

Built with Django 5.2 and Bootstrap 5.3.

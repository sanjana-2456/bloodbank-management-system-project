🩸 BloodBank Management System (Django)
A fully functional Blood Bank Management System built using Django, designed to help hospitals and blood banks manage donors, blood stock, and blood requests efficiently.
This project includes user authentication, donor management, blood stock tracking, request handling, and a beautiful red-themed responsive UI.

🚀 Features
🔐 User Authentication


User Register / Login / Logout


Custom authentication views


Protected dashboard after login


🧑‍🤝‍🧑 Donor Management


Add new donors


View full donor list


Record blood donations


Track last donation date


Auto-update stock based on donations


🩸 Blood Stock Management


See available units for each blood group


Stock auto-updates on:


Donation record


Fulfilling requests




🏥 Blood Request Handling


Add blood requests


View pending requests


Fulfill a request (stock auto-decreases)


🎨 Beautiful UI (Red BloodBank Theme)


Fully responsive Bootstrap 5 design


Clean and modern card-based dashboard


Custom red theme for branding



🛠️ Tech Stack
TechnologyDescriptionPythonBackend languageDjangoWeb frameworkSQLite3Default DB for easy setupBootstrap 5Frontend stylingHTML, CSS, JSUI BuildingFont AwesomeIcons

📸 Screenshots
(Add these once deployed or after taking screenshots)


Dashboard


Add Donor


Add Request


Login / Register


Donor List


Stock Overview



📂 Project Structure
bloodbank_project/
│
├── bloodbank/               # Main application
│   ├── models.py            # Database models
│   ├── views.py             # Application logic
│   ├── urls.py              # Routing
│   ├── templates/           # HTML templates
│   └── static/              # CSS/JS files
│
├── bloodbank_project/       # Project settings folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3               # Database
└── manage.py                # Django management script


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/sanjana-2456/bloodbank-management-system-project.git
cd bloodbank-management-system-project

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment
Windows:
venv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Start Server
python manage.py runserver

Then open:
👉 http://127.0.0.1:8000/

🔰 Default Pages
URLDescription/login/User Login/register/New user registration/Dashboard/donors/Donor list/requests/Blood requests

❤️ Contribution
Pull Requests are welcome! Feel free to fork the repository and submit improvements.



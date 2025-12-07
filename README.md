<h1> Wagtail CMS </h1>
<p><h4>Wagtail is a modern, open-source CMS built on Django, known for its clean and intuitive editor interface. It offers the speed, flexibility, and scalability needed for building robust, content-rich websites, and is trusted by developers and editorial teams worldwide.</h4></p>

<h2>📝 Wagtail Checklist</h2>
<img width="1920" height="1080" alt="Screenshot 2025-12-07 043510" src="https://github.com/user-attachments/assets/2b37544d-8699-4d41-b272-a8caed13e6d9" />


Wagtail Checklist is a lightweight extension built on top of the powerful and flexible Wagtail CMS
 — an open-source Django-based content management system known for its clean interface and excellent editor experience.

This project introduces a custom Checklist System that enhances Wagtail’s editorial workflow by allowing editors to manage page-specific tasks with clarity and efficiency.
Each page has its own checklist dashboard, where users can add tasks, edit or delete them, and mark items as approved or rejected.
Built using Django + Wagtail, the system focuses on clean UI, seamless integration, and simple workflow improvement.

For more about Wagtail and its ecosystem:
📖 Wagtail Documentation: https://docs.wagtail.org/en/stable/

🏢 Wagtail Organization: https://github.com/wagtail

-----

Features
Core Features

Add checklist tasks linked to Wagtail pages

Dedicated checklist dashboard for each page

Approve or reject tasks

Edit or delete tasks

Clean UI integrated into the Wagtail editor

Powered by Django models, views, and templates

Benefits of Wagtail CMS
--
Fast, user-friendly editor interface

Scales to large websites with many pages

StreamField for flexible content creation

Strong image and document library

Excellent search (PostgreSQL / Elasticsearch)

Multi-site and multi-language support

Built on Django — secure, robust, and extensible

Learn more: https://wagtail.org
-----

## 📥 Getting Started (Local Development)

Follow these steps to set up the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/rishab938/Wagtail--Checklist-.git
cd Wagtail--Checklist-
```
# 2️⃣  (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```
# 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
# 4️⃣  Run database migrations
```bash
python manage.py migrate
```
# 5️⃣  Collect static files (if needed)
```bash
python manage.py collectstatic
```
# 6️⃣  Create a superuser for Wagtail admin
```bash
python manage.py createsuperuser
```
# 7️⃣  Start the development server
```bash
python manage.py runserver
```

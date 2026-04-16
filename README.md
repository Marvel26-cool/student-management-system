🎓 AI-Based Student Management System (Django)
📌 Project Overview

This project is a Student Management System developed using Django (Python). It provides a centralized platform for managing student data, attendance, marks, and assignments with separate portals for Admin, Teacher, and Student.

The system also includes a basic AI chatbot and a dashboard with data visualization, making it modern and user-friendly.

🚀 Features
👤 Role-Based Access
Admin Portal
Manage users (students & teachers)
View system data
Teacher Portal
Manage attendance
Assign marks
Student Portal
View attendance
View marks and assignments
📊 Dashboard
Displays attendance percentage
Shows average marks
Interactive charts using Chart.js
🤖 AI Chatbot
Basic chatbot to answer student queries
Can be extended using NLP models
🌙 UI/UX Features
Clean dashboard interface
Sidebar navigation
Responsive design using Bootstrap
Dark mode support (in advanced versions)
🛠️ Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Charts: Chart.js
⚙️ Installation & Setup
Clone the repository:
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py makemigrations
python manage.py migrate
Create superuser:
python manage.py createsuperuser
Run the server:
python manage.py runserver
Open in browser:
http://127.0.0.1:8000/
🔐 Login Details (Example)
Role	Username	Password
Admin	admin	admin123
Teacher	teacher1	teacher123
Student	student1	student123
📈 Future Enhancements
Real-time notifications
Advanced AI chatbot using NLP
File upload for assignments
Mobile app integration
Email/SMS alerts
🎯 Conclusion

This project demonstrates how a Django-based system can efficiently manage academic activities with role-based access, data visualization, and AI integration.

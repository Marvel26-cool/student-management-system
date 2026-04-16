import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduportal.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Student, Teacher, Subject, Grade, Attendance, Class
from notes.models import FileUpload
from doubt.models import DoubtQuestion
from datetime import date

def create_users():
    # Student disha
    if not User.objects.filter(username='disha').exists():
        user = User.objects.create_user('disha', password='disha123', first_name='Disha')
        student = Student.objects.create(user=user, roll_number='S001', gpa=0.0)
    else:
        user = User.objects.get(username='disha')
        student = Student.objects.get(user=user)

    # Teacher
    if not User.objects.filter(username='teacher').exists():
        teacher_user = User.objects.create_user('teacher', password='teacher123', first_name='Prof.', last_name='Smith')
        Teacher.objects.create(user=teacher_user, employee_id='T001', department='Science')

    # Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

    # Subjects
    subjects_data = [
        {'name': 'Mathematics', 'code': 'MATH101', 'credit': 4},
        {'name': 'Physics', 'code': 'PHY101', 'credit': 3},
        {'name': 'Chemistry', 'code': 'CHEM101', 'credit': 3},
        {'name': 'Biology', 'code': 'BIO101', 'credit': 3},
        {'name': 'Computer Science', 'code': 'CS101', 'credit': 4},
    ]
    for sub in subjects_data:
        Subject.objects.get_or_create(**sub)

    # Grades
    grade_data = [
        {'code': 'MATH101', 'marks': 50.0, 'grade': 'D'},
        {'code': 'PHY101', 'marks': 1.0, 'grade': 'D'},
        {'code': 'CHEM101', 'marks': 25.0, 'grade': 'D'},
        {'code': 'BIO101', 'marks': 10.0, 'grade': 'D'},
        {'code': 'CS101', 'marks': 100.0, 'grade': 'A+'},
        {'code': 'MATH101', 'marks': 70.0, 'grade': 'B'},
    ]
    for g in grade_data:
        subject = Subject.objects.get(code=g['code'])
        Grade.objects.get_or_create(student=student, subject=subject, defaults={'marks': g['marks'], 'grade': g['grade']})

    # Attendance
    Attendance.objects.get_or_create(student=student, subject=Subject.objects.get(code='MATH101'), date=date.today(), status='Present')
    Attendance.objects.get_or_create(student=student, subject=Subject.objects.get(code='PHY101'), date=date.today(), status='Present')

    # Classes
    Class.objects.get_or_create(student=student, name='Mathematics', day='Monday', time='10:00-11:00')
    Class.objects.get_or_create(student=student, name='Physics', day='Wednesday', time='14:00-15:00')

    # File uploads
    FileUpload.objects.get_or_create(student=student, file='notes/student_21_20251104_112603.txt', subject='Mathematics')
    FileUpload.objects.get_or_create(student=student, file='notes/student_21_20251103_220344.pdf', subject='Physics')

    # Doubts
    DoubtQuestion.objects.get_or_create(student=student, question='How to solve quadratic equations?', answer='Use formula: x = [-b ± √(b²-4ac)]/(2a)')
    DoubtQuestion.objects.get_or_create(student=student, question="Explain Newton's laws", answer='1) Inertia, 2) F=ma, 3) Action-reaction')

if __name__ == '__main__':
    create_users()
    print("Sample data created.")
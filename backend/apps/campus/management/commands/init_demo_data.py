from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.authentication.models import UserRole
from apps.campus.models import Department, FacultyMember, Student, Course, Enrollment

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds initial demo data for campus management system.'

    def handle(self, *args, **kwargs):
        self.stdout.write('==> Initializing Demo Campus Data...')

        # 1. Create Superuser / Admin
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@campus.edu',
                'first_name': 'Admin',
                'last_name': 'Director',
                'role': UserRole.ADMIN,
                'is_staff': True,
                'is_superuser': True,
                'department_name': 'Campus Administration'
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user (admin / admin123)'))

        # 2. Create Departments
        departments_data = [
            {'code': 'CS', 'name': 'Computer Science & Engineering', 'established_year': 1995, 'description': 'Algorithms, Artificial Intelligence, and Software Engineering.'},
            {'code': 'EE', 'name': 'Electrical & Electronics Engineering', 'established_year': 1990, 'description': 'Robotics, VLSI, and Power Systems.'},
            {'code': 'ME', 'name': 'Mechanical Engineering', 'established_year': 1988, 'description': 'Thermodynamics, CAD/CAM, and Automotives.'},
            {'code': 'BA', 'name': 'Business Administration', 'established_year': 2002, 'description': 'Marketing, Finance, and Enterprise Management.'},
            {'code': 'BIO', 'name': 'Biotechnology & Bioengineering', 'established_year': 2010, 'description': 'Genetics, Bioinformatics, and Cellular Engineering.'},
        ]
        dept_map = {}
        for d_data in departments_data:
            dept, _ = Department.objects.get_or_create(code=d_data['code'], defaults=d_data)
            dept_map[d_data['code']] = dept
        self.stdout.write(self.style.SUCCESS(f'Created/verified {len(dept_map)} departments.'))

        # 3. Create Faculty Users & Profiles
        faculty_data = [
            {'username': 'prof_smith', 'first_name': 'Alan', 'last_name': 'Smith', 'email': 'alan.smith@campus.edu', 'dept': 'CS', 'designation': 'Professor & Chair', 'spec': 'Machine Learning', 'room': 'CS-301'},
            {'username': 'prof_elena', 'first_name': 'Elena', 'last_name': 'Rostova', 'email': 'elena.rostova@campus.edu', 'dept': 'CS', 'designation': 'Associate Professor', 'spec': 'Cloud Computing & Distributed Systems', 'room': 'CS-204'},
            {'username': 'prof_rajesh', 'first_name': 'Rajesh', 'last_name': 'Kumar', 'email': 'rajesh.kumar@campus.edu', 'dept': 'EE', 'designation': 'Professor', 'spec': 'Microprocessors & Embedded Systems', 'room': 'EE-105'},
            {'username': 'prof_sara', 'first_name': 'Sara', 'last_name': 'Vance', 'email': 'sara.vance@campus.edu', 'dept': 'BA', 'designation': 'Assistant Professor', 'spec': 'Strategic Financial Management', 'room': 'BA-402'},
        ]
        faculty_map = {}
        for f_data in faculty_data:
            user, u_created = User.objects.get_or_create(
                username=f_data['username'],
                defaults={
                    'email': f_data['email'],
                    'first_name': f_data['first_name'],
                    'last_name': f_data['last_name'],
                    'role': UserRole.FACULTY,
                    'is_staff': True,
                    'department_name': dept_map[f_data['dept']].name
                }
            )
            if u_created:
                user.set_password('faculty123')
                user.save()
            fac_member, _ = FacultyMember.objects.get_or_create(
                user=user,
                defaults={
                    'department': dept_map[f_data['dept']],
                    'designation': f_data['designation'],
                    'specialization': f_data['spec'],
                    'office_room': f_data['room']
                }
            )
            faculty_map[f_data['username']] = fac_member
        self.stdout.write(self.style.SUCCESS(f'Created/verified {len(faculty_map)} faculty members.'))

        # 4. Create Students
        students_data = [
            {'username': 'student', 'first_name': 'Alex', 'last_name': 'Johnson', 'email': 'student@campus.edu', 'dept': 'CS', 'sid': 'STU-2026-001', 'sem': 4, 'gpa': 3.85},
            {'username': 'stu_maya', 'first_name': 'Maya', 'last_name': 'Patel', 'email': 'maya.p@campus.edu', 'dept': 'CS', 'sid': 'STU-2026-002', 'sem': 4, 'gpa': 3.92},
            {'username': 'stu_david', 'first_name': 'David', 'last_name': 'Lee', 'email': 'david.lee@campus.edu', 'dept': 'EE', 'sid': 'STU-2026-003', 'sem': 6, 'gpa': 3.45},
            {'username': 'stu_sophia', 'first_name': 'Sophia', 'last_name': 'Martinez', 'email': 'sophia.m@campus.edu', 'dept': 'BA', 'sid': 'STU-2026-004', 'sem': 2, 'gpa': 3.78},
            {'username': 'stu_liam', 'first_name': 'Liam', 'last_name': 'O\'Connor', 'email': 'liam.oc@campus.edu', 'dept': 'ME', 'sid': 'STU-2026-005', 'sem': 3, 'gpa': 3.60},
        ]
        student_objs = []
        for s_data in students_data:
            user, u_created = User.objects.get_or_create(
                username=s_data['username'],
                defaults={
                    'email': s_data['email'],
                    'first_name': s_data['first_name'],
                    'last_name': s_data['last_name'],
                    'role': UserRole.STUDENT,
                    'department_name': dept_map[s_data['dept']].name
                }
            )
            if u_created:
                user.set_password('student123')
                user.save()
            stu, _ = Student.objects.get_or_create(
                user=user,
                defaults={
                    'student_id': s_data['sid'],
                    'department': dept_map[s_data['dept']],
                    'semester': s_data['sem'],
                    'gpa': s_data['gpa']
                }
            )
            student_objs.append(stu)
        self.stdout.write(self.style.SUCCESS(f'Created/verified {len(student_objs)} students.'))

        # 5. Create Courses
        courses_data = [
            {'code': 'CS-101', 'title': 'Data Structures & Algorithms', 'dept': 'CS', 'instructor': faculty_map['prof_smith'], 'credits': 4, 'capacity': 60, 'semester': 'Fall 2026'},
            {'code': 'CS-204', 'title': 'Distributed Cloud Architectures', 'dept': 'CS', 'instructor': faculty_map['prof_elena'], 'credits': 3, 'capacity': 45, 'semester': 'Fall 2026'},
            {'code': 'EE-201', 'title': 'Embedded Microcontroller Systems', 'dept': 'EE', 'instructor': faculty_map['prof_rajesh'], 'credits': 4, 'capacity': 40, 'semester': 'Fall 2026'},
            {'code': 'BA-102', 'title': 'Corporate Finance & Analytics', 'dept': 'BA', 'instructor': faculty_map['prof_sara'], 'credits': 3, 'capacity': 50, 'semester': 'Fall 2026'},
        ]
        course_map = {}
        for c_data in courses_data:
            course, _ = Course.objects.get_or_create(
                code=c_data['code'],
                defaults={
                    'title': c_data['title'],
                    'department': dept_map[c_data['dept']],
                    'instructor': c_data['instructor'],
                    'credits': c_data['credits'],
                    'capacity': c_data['capacity'],
                    'semester_offered': c_data['semester']
                }
            )
            course_map[c_data['code']] = course
        self.stdout.write(self.style.SUCCESS(f'Created/verified {len(course_map)} courses.'))

        # 6. Create Enrollments
        enrollments = [
            (student_objs[0], course_map['CS-101'], Enrollment.GradeChoices.A, 94.5),
            (student_objs[0], course_map['CS-204'], Enrollment.GradeChoices.A_PLUS, 98.0),
            (student_objs[1], course_map['CS-101'], Enrollment.GradeChoices.A_PLUS, 96.2),
            (student_objs[2], course_map['EE-201'], Enrollment.GradeChoices.B_PLUS, 88.0),
            (student_objs[3], course_map['BA-102'], Enrollment.GradeChoices.A, 92.0),
        ]
        for stu, crs, grd, att in enrollments:
            Enrollment.objects.get_or_create(
                student=stu,
                course=crs,
                defaults={'grade': grd, 'attendance_percentage': att}
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded all initial demo data!'))

from datetime import date, timedelta
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.accounts.models import UserRole, UserStatus
from apps.departments.models import Department
from apps.faculty.models import Faculty, FacultyStatus
from apps.students.models import Student, StudentStatus
from apps.courses.models import Course, Enrollment
from apps.attendance.models import AttendanceSession, AttendanceRecord, SessionType, AttendanceStatus
from apps.examinations.models import Exam, ExamResult, ExamType
from apps.fees.models import FeeCategory, FeeStructure, FeePayment, PaymentMethod, PaymentStatus
from apps.assignments.models import Assignment, AssignmentSubmission, SubmissionStatus
from apps.library.models import Book, BookIssue, IssueStatus
from apps.placements.models import Company, PlacementDrive, JobApplication, DriveStatus, ApplicationStatus
from apps.complaints.models import Complaint, ComplaintCategory, ComplaintPriority, ComplaintStatus
from apps.events.models import Event, EventRegistration, EventType
from apps.notifications.models import Notification, NotificationType

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds database with institutional roles and 15 module records.'

    def handle(self, *args, **kwargs):
        self.stdout.write('==> Starting Institutional Schema Data Seeding...')

        # 1. Departments (CSE, ECE, EEE, MECH, CIVIL)
        depts_data = [
            {'code': 'CSE', 'name': 'Computer Science & Engineering', 'established_year': 1995, 'head_of_department': 'Dr. Alan Smith', 'building_block': 'Turing Block A'},
            {'code': 'ECE', 'name': 'Electronics & Communication Engineering', 'established_year': 1998, 'head_of_department': 'Dr. Marcus Vance', 'building_block': 'Shannon Block B'},
            {'code': 'EEE', 'name': 'Electrical & Electronics Engineering', 'established_year': 1992, 'head_of_department': 'Dr. Rajesh Kumar', 'building_block': 'Tesla Block C'},
            {'code': 'MECH', 'name': 'Mechanical Engineering', 'established_year': 1988, 'head_of_department': 'Dr. Robert Ford', 'building_block': 'Watt Block D'},
            {'code': 'CIVIL', 'name': 'Civil Engineering', 'established_year': 1985, 'head_of_department': 'Dr. Arthur Dent', 'building_block': 'Smeaton Block E'},
        ]
        dept_map = {}
        for d in depts_data:
            obj, _ = Department.objects.get_or_create(code=d['code'], defaults=d)
            dept_map[d['code']] = obj

        # 2. Institutional Role Users
        role_users = [
            ('admin', 'admin@campus.edu', 'Admin', 'Officer', UserRole.ADMIN, '+1 (555) 100-0001'),
            ('hod_cs', 'hod.cs@campus.edu', 'Alan', 'Smith', UserRole.HOD, '+1 (555) 100-0002'),
            ('prof_elena', 'elena.r@campus.edu', 'Elena', 'Rostova', UserRole.FACULTY, '+1 (555) 100-0003'),
            ('student', 'student@campus.edu', 'Alex', 'Johnson', UserRole.STUDENT, '+1 (555) 100-0004'),
            ('placement_officer', 'placement@campus.edu', 'Marcus', 'Vance', UserRole.PLACEMENT_OFFICER, '+1 (555) 100-0005'),
            ('accountant', 'accounts@campus.edu', 'Clara', 'Oswald', UserRole.ACCOUNTANT, '+1 (555) 100-0006'),
            ('librarian', 'library@campus.edu', 'Arthur', 'Dent', UserRole.LIBRARIAN, '+1 (555) 100-0007'),
        ]
        user_map = {}
        for uname, email, fname, lname, role, phone in role_users:
            u, _ = User.objects.get_or_create(
                username=uname,
                defaults={
                    'email': email,
                    'first_name': fname,
                    'last_name': lname,
                    'role': role,
                    'phone': phone,
                    'status': UserStatus.ACTIVE,
                    'is_staff': role in [UserRole.ADMIN, UserRole.HOD, UserRole.PLACEMENT_OFFICER, UserRole.ACCOUNTANT, UserRole.LIBRARIAN],
                    'is_superuser': role == UserRole.ADMIN,
                }
            )
            u.set_password('password123')
            u.save()
            user_map[uname] = u
        self.stdout.write(self.style.SUCCESS('1. Initialized 7 institutional role user accounts.'))

        # 3. Faculty
        faculty_data = [
            {'fid': 'FAC-CS-001', 'name': 'Dr. Alan Smith', 'email': 'hod.cs@campus.edu', 'phone': '+1 (555) 100-0002', 'dept': 'CS', 'desig': 'Professor & HOD', 'user': user_map['hod_cs']},
            {'fid': 'FAC-CS-002', 'name': 'Dr. Elena Rostova', 'email': 'elena.r@campus.edu', 'phone': '+1 (555) 100-0003', 'dept': 'CS', 'desig': 'Associate Professor', 'user': user_map['prof_elena']},
            {'fid': 'FAC-EE-001', 'name': 'Dr. Rajesh Kumar', 'email': 'rajesh.k@campus.edu', 'phone': '+1 (555) 100-0010', 'dept': 'EE', 'desig': 'Professor & HOD', 'user': None},
            {'fid': 'FAC-BA-001', 'name': 'Dr. Sara Vance', 'email': 'sara.v@campus.edu', 'phone': '+1 (555) 100-0011', 'dept': 'BA', 'desig': 'Assistant Professor', 'user': None},
        ]
        faculty_map = {}
        for f in faculty_data:
            fac, _ = Faculty.objects.get_or_create(
                faculty_id=f['fid'],
                defaults={
                    'name': f['name'],
                    'email': f['email'],
                    'phone': f['phone'],
                    'department': dept_map[f['dept']],
                    'designation': f['desig'],
                    'user': f['user'],
                    'status': FacultyStatus.ACTIVE
                }
            )
            faculty_map[f['fid']] = fac
        self.stdout.write(self.style.SUCCESS('2. Initialized Faculty records.'))

        # 4. Students
        students_data = [
            {'sid': 'STU-2026-001', 'name': 'Alex Johnson', 'email': 'student@campus.edu', 'phone': '+1 (555) 100-0004', 'dept': 'CS', 'year': 2, 'sec': 'A', 'sem': 4, 'gpa': Decimal('3.85'), 'user': user_map['student']},
            {'sid': 'STU-2026-002', 'name': 'Maya Patel', 'email': 'maya.p@campus.edu', 'phone': '+1 (555) 100-0020', 'dept': 'CS', 'year': 2, 'sec': 'A', 'sem': 4, 'gpa': Decimal('3.92'), 'user': None},
            {'sid': 'STU-2026-003', 'name': 'David Lee', 'email': 'david.l@campus.edu', 'phone': '+1 (555) 100-0021', 'dept': 'EE', 'year': 3, 'sec': 'B', 'sem': 6, 'gpa': Decimal('3.45'), 'user': None},
            {'sid': 'STU-2026-004', 'name': 'Sophia Martinez', 'email': 'sophia.m@campus.edu', 'phone': '+1 (555) 100-0022', 'dept': 'BA', 'year': 1, 'sec': 'A', 'sem': 2, 'gpa': Decimal('3.78'), 'user': None},
            {'sid': 'STU-2026-005', 'name': 'Liam O\'Connor', 'email': 'liam.o@campus.edu', 'phone': '+1 (555) 100-0023', 'dept': 'ME', 'year': 2, 'sec': 'C', 'sem': 3, 'gpa': Decimal('3.60'), 'user': None},
        ]
        student_objs = []
        for s in students_data:
            stu, _ = Student.objects.get_or_create(
                student_id=s['sid'],
                defaults={
                    'name': s['name'],
                    'email': s['email'],
                    'phone': s['phone'],
                    'department': dept_map[s['dept']],
                    'year': s['year'],
                    'section': s['sec'],
                    'semester': s['sem'],
                    'gpa': s['gpa'],
                    'status': StudentStatus.ACTIVE,
                    'user': s['user']
                }
            )
            student_objs.append(stu)
        self.stdout.write(self.style.SUCCESS('3. Initialized Student records.'))

        # 4. Courses (CSE curriculum: Data Structures, DBMS, Operating Systems, Computer Networks, Machine Learning)
        courses_data = [
            {'code': 'CSE-101', 'title': 'Data Structures & Algorithms', 'credits': 4, 'semester': 3, 'course_type': 'THEORY', 'department': dept_map.get('CSE'), 'instructor': faculty_objs[0] if faculty_objs else None},
            {'code': 'CSE-202', 'title': 'Database Management Systems (DBMS)', 'credits': 4, 'semester': 4, 'course_type': 'THEORY', 'department': dept_map.get('CSE'), 'instructor': faculty_objs[1] if len(faculty_objs) > 1 else None},
            {'code': 'CSE-301', 'title': 'Operating Systems', 'credits': 4, 'semester': 5, 'course_type': 'THEORY', 'department': dept_map.get('CSE'), 'instructor': faculty_objs[0] if faculty_objs else None},
            {'code': 'CSE-302', 'title': 'Computer Networks', 'credits': 3, 'semester': 6, 'course_type': 'THEORY', 'department': dept_map.get('CSE'), 'instructor': faculty_objs[1] if len(faculty_objs) > 1 else None},
            {'code': 'CSE-401', 'title': 'Machine Learning & Neural Networks', 'credits': 4, 'semester': 7, 'course_type': 'ELECTIVE', 'department': dept_map.get('CSE'), 'instructor': faculty_objs[0] if faculty_objs else None},
            {'code': 'ECE-201', 'title': 'Digital Signal Processing', 'credits': 4, 'semester': 4, 'course_type': 'THEORY', 'department': dept_map.get('ECE'), 'instructor': None},
            {'code': 'EEE-201', 'title': 'Embedded Microcontroller Systems', 'credits': 4, 'semester': 4, 'course_type': 'THEORY', 'department': dept_map.get('EEE'), 'instructor': None},
            {'code': 'MECH-301', 'title': 'Thermodynamics & Heat Transfer', 'credits': 4, 'semester': 5, 'course_type': 'THEORY', 'department': dept_map.get('MECH'), 'instructor': None},
            {'code': 'CIVIL-201', 'title': 'Structural Analysis & Mechanics', 'credits': 4, 'semester': 4, 'course_type': 'THEORY', 'department': dept_map.get('CIVIL'), 'instructor': None},
        ]
        course_map = {}
        for c in courses_data:
            course_obj, _ = Course.objects.get_or_create(
                code=c['code'],
                defaults={
                    'title': c['title'],
                    'department': c['department'],
                    'instructor': c['instructor'],
                    'credits': c['credits'],
                    'semester': c['semester'],
                    'course_type': c['course_type'],
                }
            )
            course_map[c['code']] = course_obj

        for stu in student_objs[:3]:
            Enrollment.objects.get_or_create(student=stu, course=course_map['CSE-101'], defaults={'final_grade': 'A'})
            Enrollment.objects.get_or_create(student=stu, course=course_map['CSE-202'], defaults={'final_grade': 'A+'})

        # 6. Attendance
        session, _ = AttendanceSession.objects.get_or_create(
            course=course_map['CSE-101'],
            date=date.today() - timedelta(days=2),
            defaults={'faculty': faculty_map['FAC-CS-001'], 'session_type': SessionType.LECTURE, 'topic_covered': 'Binary Search Trees'}
        )
        for stu in student_objs[:3]:
            AttendanceRecord.objects.get_or_create(session=session, student=stu, defaults={'status': AttendanceStatus.PRESENT})

        # 7. Exams
        exam, _ = Exam.objects.get_or_create(
            name='Midterm Assessment 2026',
            course=course_map['CSE-101'],
            defaults={'exam_type': ExamType.MIDTERM, 'date': date.today() + timedelta(days=14), 'max_marks': Decimal('100.00'), 'passing_marks': Decimal('40.00')}
        )
        ExamResult.objects.get_or_create(exam=exam, student=student_objs[0], defaults={'marks_obtained': Decimal('94.50'), 'grade': 'A+'})

        # 8. Fees
        fee_cat, _ = FeeCategory.objects.get_or_create(name='Semester Tuition Fee', defaults={'description': 'Standard semester academic fee.'})
        fee_struct, _ = FeeStructure.objects.get_or_create(
            title='Fall 2026 CS Tuition',
            category=fee_cat,
            department=dept_map['CS'],
            defaults={'semester': 4, 'amount': Decimal('4500.00'), 'due_date': date.today() + timedelta(days=30)}
        )
        FeePayment.objects.get_or_create(
            student=student_objs[0],
            fee_structure=fee_struct,
            defaults={'amount_paid': Decimal('4500.00'), 'payment_method': PaymentMethod.ONLINE, 'status': PaymentStatus.SUCCESS, 'transaction_id': 'TXN-CAMPUS-982347'}
        )

        # 9. Assignments
        assignment, _ = Assignment.objects.get_or_create(
            course=course_map['CS-101'],
            title='Assignment 1: Graph Traversal Algorithms',
            defaults={'faculty': faculty_map['FAC-CS-001'], 'deadline': timezone.now() + timedelta(days=7), 'max_score': Decimal('50.00')}
        )
        AssignmentSubmission.objects.get_or_create(
            assignment=assignment,
            student=student_objs[0],
            defaults={'submission_text': 'Submitted GitHub repository link.', 'score': Decimal('48.50'), 'status': SubmissionStatus.GRADED}
        )

        # 10. Library
        book1, _ = Book.objects.get_or_create(
            isbn='978-0131103627',
            defaults={'title': 'The C Programming Language', 'author': 'Kernighan & Ritchie', 'category': 'Computer Science', 'total_copies': 10, 'available_copies': 8}
        )
        BookIssue.objects.get_or_create(book=book1, user=user_map['student'], defaults={'due_date': date.today() + timedelta(days=14), 'status': IssueStatus.ISSUED})

        # 11. Placements
        company, _ = Company.objects.get_or_create(name='Google Cloud', defaults={'industry': 'Cloud & AI Computing', 'website': 'https://cloud.google.com'})
        drive, _ = PlacementDrive.objects.get_or_create(
            company=company,
            job_role='Associate Cloud Solutions Engineer',
            defaults={'title': 'Google Cloud Campus Recruitment 2026', 'package_lpa': Decimal('24.50'), 'eligibility_gpa': Decimal('3.50'), 'drive_date': date.today() + timedelta(days=25), 'application_deadline': timezone.now() + timedelta(days=15), 'status': DriveStatus.UPCOMING}
        )
        JobApplication.objects.get_or_create(drive=drive, student=student_objs[0], defaults={'status': ApplicationStatus.SHORTLISTED})

        # 12. Complaints
        Complaint.objects.get_or_create(
            title='Wi-Fi Signal in Lab 3',
            submitted_by=user_map['student'],
            defaults={'category': ComplaintCategory.INFRASTRUCTURE, 'description': 'Slow Wi-Fi in Lab 3.', 'priority': ComplaintPriority.MEDIUM, 'status': ComplaintStatus.OPEN}
        )

        # 13. Events
        event, _ = Event.objects.get_or_create(
            title='Annual International Hackathon 2026',
            defaults={'organizer': user_map['admin'], 'event_type': EventType.HACKATHON, 'venue': 'Innovation Arena', 'start_time': timezone.now() + timedelta(days=10), 'end_time': timezone.now() + timedelta(days=12), 'capacity': 250}
        )
        EventRegistration.objects.get_or_create(event=event, user=user_map['student'])

        # 14. Notifications
        Notification.objects.get_or_create(
            recipient=user_map['student'],
            title='Midterm Schedule Announced',
            defaults={'message': 'Your Fall 2026 exam schedule has been published.', 'notification_type': NotificationType.ACADEMIC}
        )

        self.stdout.write(self.style.SUCCESS('==> Institutional database seeded successfully!'))

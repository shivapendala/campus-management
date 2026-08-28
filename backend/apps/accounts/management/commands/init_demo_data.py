from datetime import date, timedelta
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.accounts.models import UserRole
from apps.departments.models import Department
from apps.faculty.models import Faculty
from apps.students.models import Student
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
    help = 'Seeds initial comprehensive demo data across all 15 independent campus modules.'

    def handle(self, *args, **kwargs):
        self.stdout.write('==> Starting Full 15-Module Campus Data Initialization...')

        # 1. Accounts: Admin & Staff
        admin_user, _ = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@campus.edu',
                'first_name': 'System',
                'last_name': 'Administrator',
                'role': UserRole.ADMIN,
                'is_staff': True,
                'is_superuser': True,
                'department_name': 'Administration'
            }
        )
        admin_user.set_password('admin123')
        admin_user.save()

        staff_user, _ = User.objects.get_or_create(
            username='staff_john',
            defaults={
                'email': 'staff.john@campus.edu',
                'first_name': 'John',
                'last_name': 'Wick',
                'role': UserRole.STAFF,
                'is_staff': True,
                'department_name': 'Operations'
            }
        )
        staff_user.set_password('staff123')
        staff_user.save()
        self.stdout.write(self.style.SUCCESS('1. Admin & Staff accounts initialized.'))

        # 2. Departments
        depts_data = [
            {'code': 'CS', 'name': 'Computer Science & Engineering', 'established_year': 1995, 'head_of_department': 'Dr. Alan Smith', 'building_block': 'Turing Block A'},
            {'code': 'EE', 'name': 'Electrical & Electronics Engineering', 'established_year': 1992, 'head_of_department': 'Dr. Rajesh Kumar', 'building_block': 'Tesla Block B'},
            {'code': 'ME', 'name': 'Mechanical Engineering', 'established_year': 1988, 'head_of_department': 'Dr. Robert Ford', 'building_block': 'Watt Block C'},
            {'code': 'BA', 'name': 'Business Administration', 'established_year': 2004, 'head_of_department': 'Dr. Sara Vance', 'building_block': 'Drucker Block D'},
            {'code': 'BIO', 'name': 'Biotechnology & Bioinformatics', 'established_year': 2012, 'head_of_department': 'Dr. Rosalind Franklin', 'building_block': 'Curie Block E'},
        ]
        dept_map = {}
        for d in depts_data:
            obj, _ = Department.objects.get_or_create(code=d['code'], defaults=d)
            dept_map[d['code']] = obj
        self.stdout.write(self.style.SUCCESS('2. 5 Departments initialized.'))

        # 3. Faculty
        faculty_users_data = [
            {'username': 'prof_smith', 'first_name': 'Alan', 'last_name': 'Smith', 'email': 'alan.smith@campus.edu', 'dept': 'CS', 'fid': 'FAC-CS-001', 'desig': 'Professor & Chair', 'spec': 'Artificial Intelligence'},
            {'username': 'prof_elena', 'first_name': 'Elena', 'last_name': 'Rostova', 'email': 'elena.rostova@campus.edu', 'dept': 'CS', 'fid': 'FAC-CS-002', 'desig': 'Associate Professor', 'spec': 'Distributed Cloud Architectures'},
            {'username': 'prof_rajesh', 'first_name': 'Rajesh', 'last_name': 'Kumar', 'email': 'rajesh.kumar@campus.edu', 'dept': 'EE', 'fid': 'FAC-EE-001', 'desig': 'Professor', 'spec': 'Embedded Microcontroller Systems'},
            {'username': 'prof_sara', 'first_name': 'Sara', 'last_name': 'Vance', 'email': 'sara.vance@campus.edu', 'dept': 'BA', 'fid': 'FAC-BA-001', 'desig': 'Assistant Professor', 'spec': 'Corporate Finance & Valuation'},
        ]
        faculty_map = {}
        for f in faculty_users_data:
            u, _ = User.objects.get_or_create(
                username=f['username'],
                defaults={
                    'email': f['email'],
                    'first_name': f['first_name'],
                    'last_name': f['last_name'],
                    'role': UserRole.FACULTY,
                    'is_staff': True,
                    'department_name': dept_map[f['dept']].name
                }
            )
            u.set_password('faculty123')
            u.save()
            fac, _ = Faculty.objects.get_or_create(
                user=u,
                defaults={
                    'faculty_id': f['fid'],
                    'department': dept_map[f['dept']],
                    'designation': f['desig'],
                    'specialization': f['spec'],
                    'office_room': f"{f['dept']}-20{len(faculty_map)+1}"
                }
            )
            faculty_map[f['username']] = fac
        self.stdout.write(self.style.SUCCESS('3. 4 Faculty members initialized.'))

        # 4. Students
        students_users_data = [
            {'username': 'student', 'first_name': 'Alex', 'last_name': 'Johnson', 'email': 'student@campus.edu', 'dept': 'CS', 'sid': 'STU-2026-001', 'sem': 4, 'gpa': Decimal('3.85')},
            {'username': 'stu_maya', 'first_name': 'Maya', 'last_name': 'Patel', 'email': 'maya.p@campus.edu', 'dept': 'CS', 'sid': 'STU-2026-002', 'sem': 4, 'gpa': Decimal('3.92')},
            {'username': 'stu_david', 'first_name': 'David', 'last_name': 'Lee', 'email': 'david.lee@campus.edu', 'dept': 'EE', 'sid': 'STU-2026-003', 'sem': 6, 'gpa': Decimal('3.45')},
            {'username': 'stu_sophia', 'first_name': 'Sophia', 'last_name': 'Martinez', 'email': 'sophia.m@campus.edu', 'dept': 'BA', 'sid': 'STU-2026-004', 'sem': 2, 'gpa': Decimal('3.78')},
            {'username': 'stu_liam', 'first_name': 'Liam', 'last_name': 'O\'Connor', 'email': 'liam.oc@campus.edu', 'dept': 'ME', 'sid': 'STU-2026-005', 'sem': 3, 'gpa': Decimal('3.60')},
        ]
        student_objs = []
        for s in students_users_data:
            u, _ = User.objects.get_or_create(
                username=s['username'],
                defaults={
                    'email': s['email'],
                    'first_name': s['first_name'],
                    'last_name': s['last_name'],
                    'role': UserRole.STUDENT,
                    'department_name': dept_map[s['dept']].name
                }
            )
            u.set_password('student123')
            u.save()
            stu, _ = Student.objects.get_or_create(
                user=u,
                defaults={
                    'student_id': s['sid'],
                    'department': dept_map[s['dept']],
                    'semester': s['sem'],
                    'gpa': s['gpa'],
                    'guardian_name': f"Parent of {s['first_name']}",
                    'guardian_phone': '+1 (555) 019-2834'
                }
            )
            student_objs.append(stu)
        self.stdout.write(self.style.SUCCESS('4. 5 Student profiles initialized.'))

        # 5. Courses & Enrollments
        courses_data = [
            {'code': 'CS-101', 'title': 'Data Structures & Algorithms', 'dept': 'CS', 'instructor': faculty_map['prof_smith'], 'credits': 4, 'capacity': 60},
            {'code': 'CS-204', 'title': 'Distributed Cloud Architectures', 'dept': 'CS', 'instructor': faculty_map['prof_elena'], 'credits': 3, 'capacity': 45},
            {'code': 'EE-201', 'title': 'Embedded Microcontroller Systems', 'dept': 'EE', 'instructor': faculty_map['prof_rajesh'], 'credits': 4, 'capacity': 40},
            {'code': 'BA-102', 'title': 'Corporate Finance & Analytics', 'dept': 'BA', 'instructor': faculty_map['prof_sara'], 'credits': 3, 'capacity': 50},
        ]
        course_map = {}
        for c in courses_data:
            course_obj, _ = Course.objects.get_or_create(
                code=c['code'],
                defaults={
                    'title': c['title'],
                    'department': dept_map[c['dept']],
                    'instructor': c['instructor'],
                    'credits': c['credits'],
                    'capacity': c['capacity']
                }
            )
            course_map[c['code']] = course_obj

        for stu in student_objs[:3]:
            Enrollment.objects.get_or_create(student=stu, course=course_map['CS-101'], defaults={'final_grade': 'A'})
            Enrollment.objects.get_or_create(student=stu, course=course_map['CS-204'], defaults={'final_grade': 'A+'})
        self.stdout.write(self.style.SUCCESS('5. Courses & Enrollments initialized.'))

        # 6. Attendance Sessions & Records
        session, _ = AttendanceSession.objects.get_or_create(
            course=course_map['CS-101'],
            date=date.today() - timedelta(days=2),
            defaults={
                'faculty': faculty_map['prof_smith'],
                'session_type': SessionType.LECTURE,
                'topic_covered': 'Binary Search Trees and AVL Trees'
            }
        )
        for stu in student_objs[:3]:
            AttendanceRecord.objects.get_or_create(session=session, student=stu, defaults={'status': AttendanceStatus.PRESENT})
        self.stdout.write(self.style.SUCCESS('6. Attendance sessions initialized.'))

        # 7. Examinations & Results
        exam, _ = Exam.objects.get_or_create(
            name='Midterm Assessment 2026',
            course=course_map['CS-101'],
            defaults={
                'exam_type': ExamType.MIDTERM,
                'date': date.today() + timedelta(days=14),
                'max_marks': Decimal('100.00'),
                'passing_marks': Decimal('40.00'),
                'venue': 'Auditorium Hall 1'
            }
        )
        ExamResult.objects.get_or_create(
            exam=exam,
            student=student_objs[0],
            defaults={'marks_obtained': Decimal('94.50'), 'grade': 'A+', 'remarks': 'Excellent mastery of tree data structures.'}
        )
        self.stdout.write(self.style.SUCCESS('7. Examinations initialized.'))

        # 8. Fees
        fee_cat, _ = FeeCategory.objects.get_or_create(name='Semester Tuition Fee', defaults={'description': 'Standard semester academic tuition fee.'})
        fee_struct, _ = FeeStructure.objects.get_or_create(
            title='Fall 2026 Engineering Tuition',
            category=fee_cat,
            department=dept_map['CS'],
            defaults={'semester': 4, 'amount': Decimal('4500.00'), 'due_date': date.today() + timedelta(days=30)}
        )
        FeePayment.objects.get_or_create(
            student=student_objs[0],
            fee_structure=fee_struct,
            defaults={'amount_paid': Decimal('4500.00'), 'payment_method': PaymentMethod.ONLINE, 'status': PaymentStatus.SUCCESS, 'transaction_id': 'TXN-CAMPUS-982347'}
        )
        self.stdout.write(self.style.SUCCESS('8. Fees & Payments initialized.'))

        # 9. Assignments
        assignment, _ = Assignment.objects.get_or_create(
            course=course_map['CS-101'],
            title='Assignment 1: Graph Traversal Algorithms',
            defaults={
                'faculty': faculty_map['prof_smith'],
                'description': 'Implement BFS and DFS algorithms in Python and analyze complexity.',
                'deadline': timezone.now() + timedelta(days=7),
                'max_score': Decimal('50.00')
            }
        )
        AssignmentSubmission.objects.get_or_create(
            assignment=assignment,
            student=student_objs[0],
            defaults={'submission_text': 'Submitted GitHub repository link.', 'score': Decimal('48.50'), 'status': SubmissionStatus.GRADED}
        )
        self.stdout.write(self.style.SUCCESS('9. Assignments & Submissions initialized.'))

        # 10. Library
        book1, _ = Book.objects.get_or_create(
            isbn='978-0131103627',
            defaults={'title': 'The C Programming Language', 'author': 'Brian W. Kernighan, Dennis M. Ritchie', 'category': 'Computer Science', 'total_copies': 10, 'available_copies': 8, 'rack_number': 'CS-01'}
        )
        BookIssue.objects.get_or_create(
            book=book1,
            user=student_objs[0].user,
            defaults={'due_date': date.today() + timedelta(days=14), 'status': IssueStatus.ISSUED}
        )
        self.stdout.write(self.style.SUCCESS('10. Library books & issue records initialized.'))

        # 11. Placements
        company, _ = Company.objects.get_or_create(
            name='Google Cloud',
            defaults={'industry': 'Cloud & AI Computing', 'website': 'https://cloud.google.com', 'contact_person': 'Campus Talent Lead'}
        )
        drive, _ = PlacementDrive.objects.get_or_create(
            company=company,
            job_role='Associate Cloud Solutions Engineer',
            defaults={
                'title': 'Google Cloud Campus Recruitment 2026',
                'package_lpa': Decimal('24.50'),
                'eligibility_gpa': Decimal('3.50'),
                'drive_date': date.today() + timedelta(days=25),
                'application_deadline': timezone.now() + timedelta(days=15),
                'status': DriveStatus.UPCOMING
            }
        )
        JobApplication.objects.get_or_create(
            drive=drive,
            student=student_objs[0],
            defaults={'status': ApplicationStatus.SHORTLISTED}
        )
        self.stdout.write(self.style.SUCCESS('11. Placements initialized.'))

        # 12. Complaints
        Complaint.objects.get_or_create(
            title='Wi-Fi Signal Strength in Computer Lab 3',
            submitted_by=student_objs[0].user,
            defaults={
                'category': ComplaintCategory.INFRASTRUCTURE,
                'description': 'Frequent disconnects during practical exams in Turing Lab 3.',
                'priority': ComplaintPriority.MEDIUM,
                'status': ComplaintStatus.OPEN
            }
        )
        self.stdout.write(self.style.SUCCESS('12. Complaints initialized.'))

        # 13. Events
        event, _ = Event.objects.get_or_create(
            title='Annual International Hackathon 2026',
            defaults={
                'organizer': admin_user,
                'event_type': EventType.HACKATHON,
                'venue': 'Innovation Hub Arena',
                'start_time': timezone.now() + timedelta(days=10),
                'end_time': timezone.now() + timedelta(days=12),
                'capacity': 250
            }
        )
        EventRegistration.objects.get_or_create(event=event, user=student_objs[0].user)
        self.stdout.write(self.style.SUCCESS('13. Events initialized.'))

        # 14. Notifications
        Notification.objects.get_or_create(
            recipient=student_objs[0].user,
            title='Midterm Schedule Announced',
            defaults={
                'message': 'Your Fall 2026 midterm examination schedule has been published.',
                'notification_type': NotificationType.ACADEMIC,
                'is_read': False
            }
        )
        self.stdout.write(self.style.SUCCESS('14. Notifications initialized.'))
        self.stdout.write(self.style.SUCCESS('==> Successfully loaded comprehensive demo data across all 15 modules!'))

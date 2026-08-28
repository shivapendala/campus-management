import React, { useState, useEffect } from 'react';
import StatCard from '../../components/StatCard';
import { facultyService } from '../../services';
import { useNotification } from '../../context/NotificationContext';
import { Link } from 'react-router-dom';

export const FacultyDashboard = ({ user }) => {
  const { showSuccess } = useNotification();
  const [data, setData] = useState({
    my_classes: [
      { id: 1, name: 'Year 2 — Section A', department: 'Computer Science & Engineering', students_count: 60, course_code: 'CS-101', course_name: 'Data Structures & Algorithms', room: 'Turing-101' },
      { id: 2, name: 'Year 2 — Section B', department: 'Computer Science & Engineering', students_count: 45, course_code: 'CS-204', course_name: 'Distributed Cloud Architectures', room: 'Tesla-204' },
      { id: 3, name: 'Year 3 — Section A', department: 'Computer Science & Engineering', students_count: 40, course_code: 'CS-305', course_name: 'AI Foundations', room: 'Curie-301' },
    ],
    my_subjects: [
      { code: 'CS-101', title: 'Data Structures & Algorithms', credits: 4, enrolled_students: 60, syllabus_completed: 78, avg_attendance: 94.5 },
      { code: 'CS-204', title: 'Distributed Cloud Architectures', credits: 3, enrolled_students: 45, syllabus_completed: 85, avg_attendance: 92.0 },
      { code: 'CS-305', title: 'Artificial Intelligence Foundations', credits: 4, enrolled_students: 40, syllabus_completed: 65, avg_attendance: 91.2 },
    ],
    todays_schedule: [
      { period: 'Period 1', time: '09:00 AM - 10:30 AM', course: 'CS-101 Data Structures', room: 'Turing-101', status: 'COMPLETED', attendance_marked: true },
      { period: 'Period 3', time: '02:00 PM - 03:30 PM', course: 'CS-204 Cloud Architectures', room: 'Cloud Lab 2', status: 'IN_PROGRESS', attendance_marked: false },
      { period: 'Period 4', time: '04:00 PM - 05:00 PM', course: 'Student Mentoring & Consultation', room: 'Faculty Room 204', status: 'UPCOMING', attendance_marked: false },
    ],
    attendance_summary: {
      overall_rate: 92.6,
      total_sessions_conducted: 34,
      present_today: 98,
      absent_today: 7,
    },
    assignments_summary: {
      total_published: 6,
      pending_grading_count: 12,
      graded_count: 133,
      avg_submission_score: 44.8,
    },
    exams_summary: {
      upcoming_exam: 'Midterm Assessment 2026',
      exam_date: '2026-09-15',
      question_paper_status: 'APPROVED',
      pass_rate: 96.2,
    },
    student_performance: {
      grade_distribution: { A_plus: 38, A: 52, B_plus: 34, B: 15, C: 6 },
      top_students: ['Maya Patel (3.92 GPA)', 'Alex Johnson (3.85 GPA)', 'Sophia Martinez (3.78 GPA)'],
      mentoring_alerts: 3,
    },
  });

  const [scheduleList, setScheduleList] = useState(data.todays_schedule);

  useEffect(() => {
    facultyService
      .getDashboardStats()
      .then((res) => {
        if (res) {
          setData(res);
          if (res.todays_schedule) setScheduleList(res.todays_schedule);
        }
      })
      .catch(() => {});
  }, []);

  const handleMarkAttendance = (idx) => {
    const updated = [...scheduleList];
    updated[idx].attendance_marked = true;
    updated[idx].status = 'COMPLETED';
    setScheduleList(updated);
    showSuccess(`Attendance recorded for ${updated[idx].course} (58 Present, 2 Absent).`);
  };

  return (
    <div className="container-fluid p-4">
      {/* Faculty Header Banner */}
      <div
        className="campus-card p-4 mb-4 text-white border-0 shadow-md"
        style={{ background: 'linear-gradient(135deg, #1e1b4b 0%, #4338ca 60%, #6366f1 100%)' }}
      >
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-primary text-white mb-2 fw-bold px-3 py-1">
              👨‍🏫 Faculty Professor & Instructor Portal
            </span>
            <h2 className="fw-bold mb-1">
              Welcome, Prof. {user?.first_name || user?.username || 'Elena'}!
            </h2>
            <p className="mb-0 text-white-50 small">
              Department: <strong>{user?.department_name || 'Computer Science & Engineering'}</strong> • Term: Fall 2026
            </p>
          </div>
          <div className="d-flex gap-2">
            <Link to="/courses" className="btn btn-light btn-sm fw-semibold text-primary px-3">
              <i className="bi bi-journal-bookmark me-1"></i> Course Catalog
            </Link>
          </div>
        </div>
      </div>

      {/* KPI Cards Row */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Assigned Subjects"
            value={data.my_subjects.length}
            change="CS-101, CS-204, CS-305"
            isPositive={true}
            icon="bi-journal-code"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Total Students Taught"
            value="145"
            change="Across 3 Sections"
            isPositive={true}
            icon="bi-people"
            gradientClass="bg-gradient-cyan"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Class Avg Attendance"
            value={`${data.attendance_summary.overall_rate}%`}
            change="34 Sessions Conducted"
            isPositive={true}
            icon="bi-check-circle-fill"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Pending Submissions"
            value={data.assignments_summary.pending_grading_count}
            change="Need Grade Review"
            isPositive={false}
            icon="bi-inbox-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
      </div>

      {/* Row 1: 1. My Classes & 2. My Subjects */}
      <div className="row g-4 mb-4">
        {/* 1. My Classes */}
        <div className="col-12 col-lg-6">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">
                  <i className="bi bi-building text-primary me-2"></i>
                  My Classes & Batches
                </h5>
                <p className="text-muted small mb-0">Assigned academic sections & room allocations</p>
              </div>
              <span className="badge bg-primary px-3 py-1">3 Classes</span>
            </div>

            <div className="d-flex flex-column gap-3">
              {data.my_classes.map((cls) => (
                <div key={cls.id} className="p-3 bg-light rounded-3 border d-flex justify-content-between align-items-center">
                  <div>
                    <h6 className="fw-bold text-dark mb-1">{cls.name}</h6>
                    <small className="text-muted d-block">
                      {cls.course_code}: {cls.course_name}
                    </small>
                    <small className="text-secondary">
                      <i className="bi bi-geo-alt me-1"></i> {cls.room}
                    </small>
                  </div>
                  <div className="text-end">
                    <span className="badge bg-white text-primary border fw-bold px-3 py-2">
                      {cls.students_count} Students
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* 2. My Subjects & Syllabus Progress */}
        <div className="col-12 col-lg-6">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">
                  <i className="bi bi-book-half text-info me-2"></i>
                  My Subjects & Syllabus Progress
                </h5>
                <p className="text-muted small mb-0">Course curriculum completion & attendance</p>
              </div>
              <span className="badge bg-info text-dark px-3 py-1">Fall 2026</span>
            </div>

            <div className="d-flex flex-column gap-3">
              {data.my_subjects.map((sub) => (
                <div key={sub.code} className="p-3 bg-light rounded-3 border">
                  <div className="d-flex justify-content-between align-items-center mb-1">
                    <strong className="text-dark">{sub.code}: {sub.title}</strong>
                    <span className="badge bg-light text-secondary border">{sub.credits} Credits</span>
                  </div>
                  <div className="d-flex justify-content-between small text-muted mb-2">
                    <span>Syllabus Covered: <strong>{sub.syllabus_completed}%</strong></span>
                    <span>Class Attendance: <strong>{sub.avg_attendance}%</strong></span>
                  </div>
                  <div className="progress" style={{ height: '8px' }}>
                    <div
                      className={`progress-bar ${sub.syllabus_completed > 80 ? 'bg-success' : 'bg-primary'}`}
                      style={{ width: `${sub.syllabus_completed}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Row 2: 3. Today's Schedule & 4. Attendance Action */}
      <div className="row g-4 mb-4">
        {/* 3. Today's Schedule */}
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">
                  <i className="bi bi-clock-history text-warning me-2"></i>
                  Today's Lecture Schedule
                </h5>
                <p className="text-muted small mb-0">Real-time daily class timetable and roll-call</p>
              </div>
              <span className="badge bg-warning text-dark fw-bold px-3 py-1">Live Timetable</span>
            </div>

            <div className="d-flex flex-column gap-3">
              {scheduleList.map((slot, idx) => (
                <div
                  key={idx}
                  className="p-3 bg-light rounded-3 border d-flex flex-column flex-sm-row justify-content-between align-items-sm-center gap-2"
                >
                  <div>
                    <div className="d-flex align-items-center gap-2 mb-1">
                      <span className="badge bg-secondary text-white">{slot.period}</span>
                      <strong className="text-dark">{slot.time}</strong>
                    </div>
                    <span className="fw-semibold text-primary d-block">{slot.course}</span>
                    <small className="text-muted"><i className="bi bi-geo-alt me-1"></i> {slot.room}</small>
                  </div>
                  <div>
                    {slot.attendance_marked ? (
                      <span className="badge bg-success-subtle text-success py-2 px-3 fw-bold">
                        <i className="bi bi-check-circle-fill me-1"></i> Roll-Call Taken
                      </span>
                    ) : (
                      <button
                        className="btn btn-sm btn-primary py-2 px-3 fw-semibold shadow-sm"
                        onClick={() => handleMarkAttendance(idx)}
                      >
                        <i className="bi bi-calendar-check me-1"></i> Take Attendance
                      </button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* 4. Attendance Statistics Widget */}
        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <h5 className="fw-bold text-dark mb-1">
              <i className="bi bi-pie-chart-fill text-success me-2"></i>
              Attendance Overview
            </h5>
            <p className="text-muted small mb-3">Live daily class presence counts</p>

            <div className="p-4 bg-light rounded-3 text-center mb-3">
              <span className="display-6 fw-bold text-success d-block mb-1">
                {data.attendance_summary.overall_rate}%
              </span>
              <small className="text-muted fw-semibold">Aggregate Faculty Attendance Rate</small>
            </div>

            <div className="row g-2 text-center">
              <div className="col-6">
                <div className="p-2 bg-white rounded border">
                  <small className="text-muted d-block">Present Today</small>
                  <strong className="text-success fs-5">{data.attendance_summary.present_today}</strong>
                </div>
              </div>
              <div className="col-6">
                <div className="p-2 bg-white rounded border">
                  <small className="text-muted d-block">Absent Today</small>
                  <strong className="text-danger fs-5">{data.attendance_summary.absent_today}</strong>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Row 3: 5. Assignments, 6. Exams & 7. Student Performance */}
      <div className="row g-4">
        {/* 5. Assignments */}
        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h5 className="fw-bold text-dark mb-0">
                <i className="bi bi-file-earmark-code text-primary me-2"></i>
                Assignments Queue
              </h5>
              <span className="badge bg-warning text-dark">{data.assignments_summary.pending_grading_count} Pending</span>
            </div>
            <ul className="list-group list-group-flush small">
              <li className="list-group-item px-0 d-flex justify-content-between align-items-center">
                <span>CS-101 Assignment 1 (Trees)</span>
                <span className="badge bg-success">Graded (60/60)</span>
              </li>
              <li className="list-group-item px-0 d-flex justify-content-between align-items-center">
                <span>CS-204 Kubernetes Assignment</span>
                <span className="badge bg-warning text-dark">12 to Grade</span>
              </li>
              <li className="list-group-item px-0 d-flex justify-content-between align-items-center">
                <span>CS-305 AI Neural Net Mini-Project</span>
                <span className="badge bg-light text-secondary border">Due in 4 Days</span>
              </li>
            </ul>
          </div>
        </div>

        {/* 6. Exams */}
        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h5 className="fw-bold text-dark mb-0">
                <i className="bi bi-award-fill text-danger me-2"></i>
                Examinations
              </h5>
              <span className="badge bg-success">Approved</span>
            </div>
            <div className="p-3 bg-light rounded-3 border mb-3">
              <strong className="text-dark d-block mb-1">{data.exams_summary.upcoming_exam}</strong>
              <small className="text-muted d-block mb-2">Scheduled: {data.exams_summary.exam_date} • Auditorium Hall 1</small>
              <div className="d-flex justify-content-between small">
                <span>Question Paper:</span>
                <span className="badge bg-success">{data.exams_summary.question_paper_status}</span>
              </div>
            </div>
            <small className="text-muted">Historical Pass Rate: <strong>{data.exams_summary.pass_rate}%</strong></small>
          </div>
        </div>

        {/* 7. Student Performance */}
        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h5 className="fw-bold text-dark mb-0">
                <i className="bi bi-graph-up-arrow text-emerald me-2"></i>
                Student Performance
              </h5>
              <span className="badge bg-success-subtle text-success">Top GPA 3.92</span>
            </div>

            <div className="mb-3">
              <small className="text-secondary fw-semibold d-block mb-2">Top Class Performers:</small>
              {data.student_performance.top_students.map((stu, i) => (
                <div key={i} className="p-2 bg-light rounded mb-1 small d-flex justify-content-between">
                  <span>🏆 {stu}</span>
                </div>
              ))}
            </div>

            <div className="p-2 bg-warning-subtle text-warning-emphasis rounded small d-flex align-items-center gap-2">
              <i className="bi bi-exclamation-triangle-fill"></i>
              <span>{data.student_performance.mentoring_alerts} students flagged for academic mentoring</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FacultyDashboard;

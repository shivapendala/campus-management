import React, { useState, useEffect } from 'react';
import api from '../api/axios';

export const Courses = () => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  const defaultCourses = [
    { id: 1, code: 'CS-101', title: 'Data Structures & Algorithms', department_detail: { name: 'Computer Science' }, instructor_detail: { user: { first_name: 'Alan', last_name: 'Smith' } }, credits: 4, capacity: 60, enrolled_count: 54 },
    { id: 2, code: 'CS-204', title: 'Distributed Cloud Architectures', department_detail: { name: 'Computer Science' }, instructor_detail: { user: { first_name: 'Elena', last_name: 'Rostova' } }, credits: 3, capacity: 45, enrolled_count: 42 },
    { id: 3, code: 'EE-201', title: 'Embedded Microcontroller Systems', department_detail: { name: 'Electrical Eng.' }, instructor_detail: { user: { first_name: 'Rajesh', last_name: 'Kumar' } }, credits: 4, capacity: 40, enrolled_count: 36 },
    { id: 4, code: 'BA-102', title: 'Corporate Finance & Analytics', department_detail: { name: 'Business Admin' }, instructor_detail: { user: { first_name: 'Sara', last_name: 'Vance' } }, credits: 3, capacity: 50, enrolled_count: 48 },
  ];

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const res = await api.get('/campus/courses/');
        if (res.data.results && res.data.results.length > 0) {
          setCourses(res.data.results);
        } else {
          setCourses(defaultCourses);
        }
      } catch (err) {
        setCourses(defaultCourses);
      } finally {
        setLoading(false);
      }
    };
    fetchCourses();
  }, []);

  return (
    <div className="container-fluid p-4">
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Course Catalog</h2>
          <p className="text-muted mb-0">Overview of courses, credit allocations, and enrollment capacities</p>
        </div>
        <button className="btn btn-primary btn-sm d-flex align-items-center gap-2">
          <i className="bi bi-plus-circle-fill"></i>
          <span>Create New Course</span>
        </button>
      </div>

      <div className="row g-4">
        {courses.map((c) => (
          <div className="col-12 col-md-6 col-xl-3" key={c.id || c.code}>
            <div className="campus-card campus-card-interactive p-4 h-100 d-flex flex-column justify-content-between">
              <div>
                <div className="d-flex justify-content-between align-items-start mb-2">
                  <span className="badge bg-primary-subtle text-primary fw-bold px-2 py-1">
                    {c.code}
                  </span>
                  <span className="badge bg-light text-secondary border">
                    {c.credits} Credits
                  </span>
                </div>
                <h5 className="fw-bold text-dark mb-2">{c.title}</h5>
                <p className="text-muted small mb-3">
                  <i className="bi bi-building me-1"></i>
                  {c.department_detail?.name || 'Academic Dept'}
                </p>
                <div className="p-2 bg-light rounded-3 mb-3 small">
                  <span className="text-muted d-block" style={{ fontSize: '0.75rem' }}>Lead Instructor</span>
                  <span className="fw-semibold text-dark">
                    Prof. {c.instructor_detail?.user?.first_name || 'Alan'} {c.instructor_detail?.user?.last_name || 'Smith'}
                  </span>
                </div>
              </div>

              <div>
                <div className="d-flex justify-content-between text-muted small mb-1">
                  <span>Enrolled Capacity</span>
                  <span className="fw-semibold text-dark">{c.enrolled_count || 45} / {c.capacity || 50}</span>
                </div>
                <div className="progress" style={{ height: '6px' }}>
                  <div
                    className="progress-bar bg-primary"
                    role="progressbar"
                    style={{ width: `${Math.min(100, ((c.enrolled_count || 45) / (c.capacity || 50)) * 100)}%` }}
                  ></div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Courses;

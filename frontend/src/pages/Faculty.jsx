import React, { useState, useEffect } from 'react';
import api from '../api/axios';

export const Faculty = () => {
  const [faculty, setFaculty] = useState([]);
  const [loading, setLoading] = useState(true);

  const defaultFaculty = [
    { id: 1, user: { first_name: 'Alan', last_name: 'Smith', email: 'alan.smith@campus.edu' }, department_detail: { name: 'Computer Science' }, designation: 'Professor & Chair', specialization: 'Machine Learning', office_room: 'CS-301' },
    { id: 2, user: { first_name: 'Elena', last_name: 'Rostova', email: 'elena.rostova@campus.edu' }, department_detail: { name: 'Computer Science' }, designation: 'Associate Professor', specialization: 'Distributed Cloud Systems', office_room: 'CS-204' },
    { id: 3, user: { first_name: 'Rajesh', last_name: 'Kumar', email: 'rajesh.kumar@campus.edu' }, department_detail: { name: 'Electrical Eng.' }, designation: 'Professor', specialization: 'Embedded Microcontrollers', office_room: 'EE-105' },
    { id: 4, user: { first_name: 'Sara', last_name: 'Vance', email: 'sara.vance@campus.edu' }, department_detail: { name: 'Business Admin' }, designation: 'Assistant Professor', specialization: 'Strategic Finance & Analytics', office_room: 'BA-402' },
  ];

  useEffect(() => {
    const fetchFaculty = async () => {
      try {
        const res = await api.get('/faculty/');
        if (res.data.results && res.data.results.length > 0) {
          setFaculty(res.data.results);
        } else {
          setFaculty(defaultFaculty);
        }
      } catch (err) {
        setFaculty(defaultFaculty);
      } finally {
        setLoading(false);
      }
    };
    fetchFaculty();
  }, []);

  return (
    <div className="container-fluid p-4">
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Faculty & Academic Staff</h2>
          <p className="text-muted mb-0">List of campus professors, research specializations, and departmental chairs</p>
        </div>
        <button className="btn btn-primary btn-sm d-flex align-items-center gap-2">
          <i className="bi bi-person-plus-fill"></i>
          <span>Add Faculty Member</span>
        </button>
      </div>

      <div className="row g-4">
        {faculty.map((f) => (
          <div className="col-12 col-md-6 col-xl-3" key={f.id || f.user?.email}>
            <div className="campus-card campus-card-interactive p-4 text-center h-100">
              <div
                className="bg-gradient-primary rounded-circle mx-auto d-flex align-items-center justify-content-center text-white fw-bold mb-3 shadow-sm"
                style={{ width: '64px', height: '64px', fontSize: '1.25rem' }}
              >
                {f.user?.first_name ? f.user.first_name[0] : 'P'}
              </div>
              <h5 className="fw-bold text-dark mb-1">
                Prof. {f.user?.first_name} {f.user?.last_name}
              </h5>
              <span className="badge bg-primary-subtle text-primary mb-2">
                {f.designation || 'Professor'}
              </span>
              <p className="text-muted small mb-2">
                <i className="bi bi-building me-1"></i> {f.department_detail?.name || 'Computer Science'}
              </p>
              <p className="text-secondary small mb-3">
                <i className="bi bi-journal-text me-1"></i> {f.specialization || 'Academic Research'}
              </p>
              <div className="border-top pt-3 text-muted small d-flex justify-content-between">
                <span>Room: <strong className="text-dark">{f.office_room || 'N/A'}</strong></span>
                <a href={`mailto:${f.user?.email}`} className="text-primary text-decoration-none" title="Send Email">
                  <i className="bi bi-envelope-fill me-1"></i>Contact
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Faculty;

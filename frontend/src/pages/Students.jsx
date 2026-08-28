import React, { useState, useEffect } from 'react';
import api from '../api/axios';

export const Students = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  // Fallback demo data if API is loading or empty
  const defaultStudents = [
    { id: 1, student_id: 'STU-2026-001', user: { first_name: 'Alex', last_name: 'Johnson', email: 'alex.j@campus.edu' }, department_detail: { name: 'Computer Science' }, semester: 4, gpa: 3.85 },
    { id: 2, student_id: 'STU-2026-002', user: { first_name: 'Maya', last_name: 'Patel', email: 'maya.p@campus.edu' }, department_detail: { name: 'Computer Science' }, semester: 4, gpa: 3.92 },
    { id: 3, student_id: 'STU-2026-003', user: { first_name: 'David', last_name: 'Lee', email: 'david.l@campus.edu' }, department_detail: { name: 'Electrical Eng.' }, semester: 6, gpa: 3.45 },
    { id: 4, student_id: 'STU-2026-004', user: { first_name: 'Sophia', last_name: 'Martinez', email: 'sophia.m@campus.edu' }, department_detail: { name: 'Business Admin' }, semester: 2, gpa: 3.78 },
    { id: 5, student_id: 'STU-2026-005', user: { first_name: 'Liam', last_name: 'O\'Connor', email: 'liam.o@campus.edu' }, department_detail: { name: 'Mechanical Eng.' }, semester: 3, gpa: 3.60 },
  ];

  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const res = await api.get('/campus/students/');
        if (res.data.results && res.data.results.length > 0) {
          setStudents(res.data.results);
        } else {
          setStudents(defaultStudents);
        }
      } catch (err) {
        setStudents(defaultStudents);
      } finally {
        setLoading(false);
      }
    };
    fetchStudents();
  }, []);

  const filtered = students.filter(
    (s) =>
      s.student_id?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.user?.first_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.user?.last_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.department_detail?.name?.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="container-fluid p-4">
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Student Directory</h2>
          <p className="text-muted mb-0">Manage enrolled student records, GPA standings, and academic departments</p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-primary btn-sm d-flex align-items-center gap-2">
            <i className="bi bi-person-plus-fill"></i>
            <span>Register New Student</span>
          </button>
        </div>
      </div>

      <div className="campus-card mb-4">
        <div className="p-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <div className="input-group" style={{ maxWidth: '350px' }}>
            <span className="input-group-text bg-light border-end-0 text-muted">
              <i className="bi bi-search"></i>
            </span>
            <input
              type="text"
              className="form-control bg-light border-start-0"
              placeholder="Search by ID, name, or department..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          <div className="d-flex gap-2">
            <button className="btn btn-sm btn-outline-secondary">Filter by Dept</button>
            <button className="btn btn-sm btn-outline-secondary">Export CSV</button>
          </div>
        </div>

        <div className="table-responsive">
          <table className="custom-table">
            <thead>
              <tr>
                <th>Student ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Department</th>
                <th>Semester</th>
                <th>GPA</th>
                <th className="text-end">Actions</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((s) => (
                <tr key={s.id || s.student_id}>
                  <td>
                    <span className="fw-bold text-primary">{s.student_id}</span>
                  </td>
                  <td>
                    <div className="d-flex align-items-center gap-2">
                      <div className="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center fw-bold" style={{ width: '32px', height: '32px', fontSize: '0.8rem' }}>
                        {s.user?.first_name ? s.user.first_name[0] : 'S'}
                      </div>
                      <span className="fw-semibold text-dark">
                        {s.user ? `${s.user.first_name} ${s.user.last_name}` : 'Alex Johnson'}
                      </span>
                    </div>
                  </td>
                  <td className="text-muted">{s.user?.email || 'student@campus.edu'}</td>
                  <td>
                    <span className="badge bg-secondary-subtle text-secondary border">
                      {s.department_detail?.name || 'Computer Science'}
                    </span>
                  </td>
                  <td>Sem {s.semester || 1}</td>
                  <td>
                    <span className="badge bg-success-subtle text-success fw-bold">
                      {s.gpa || '3.50'}
                    </span>
                  </td>
                  <td className="text-end">
                    <button className="btn btn-sm btn-light me-1" title="View Profile">
                      <i className="bi bi-eye"></i>
                    </button>
                    <button className="btn btn-sm btn-light text-primary me-1" title="Edit">
                      <i className="bi bi-pencil"></i>
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Students;

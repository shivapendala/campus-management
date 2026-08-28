import React, { useState, useEffect } from 'react';
import { placementService } from '../services';
import DriveFormModal from '../components/Placements/DriveFormModal';
import ApplyJobModal from '../components/Placements/ApplyJobModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Placements = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [activeTab, setActiveTab] = useState('drives'); // 'drives', 'applications', 'statistics'
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Modals
  const driveModal = useModal();
  const applyModal = useModal();
  const deleteModal = useModal();

  const defaultDrives = [
    { id: 1, title: 'Google Cloud Campus Recruitment 2026', company_name: 'Google Cloud', job_role: 'Associate Cloud Solutions Engineer', package_lpa: 24.5, eligibility_gpa: 3.5, drive_date: '2026-10-15', application_deadline: '2026-10-01', status: 'UPCOMING', applicants_count: 42, description: 'Hiring for Cloud & AI Distributed Systems engineering roles.' },
    { id: 2, title: 'Microsoft Software Engineering Drive', company_name: 'Microsoft', job_role: 'Software Development Engineer (SDE-1)', package_lpa: 22.0, eligibility_gpa: 3.4, drive_date: '2026-10-22', application_deadline: '2026-10-05', status: 'UPCOMING', applicants_count: 58, description: 'Core product teams: Azure, Office 365, and AI Copilot platform.' },
    { id: 3, title: 'Amazon AWS SDE Campus Intake', company_name: 'Amazon', job_role: 'Cloud Systems Associate', package_lpa: 20.5, eligibility_gpa: 3.2, drive_date: '2026-11-05', application_deadline: '2026-10-20', status: 'UPCOMING', applicants_count: 65, description: 'Distributed databases and EC2 virtualization kernel teams.' },
    { id: 4, title: 'NVIDIA AI & Accelerated Computing', company_name: 'NVIDIA', job_role: 'CUDA & Deep Learning Engineer', package_lpa: 28.0, eligibility_gpa: 3.7, drive_date: '2026-11-15', application_deadline: '2026-10-30', status: 'UPCOMING', applicants_count: 31, description: 'GPU kernel optimization, TensorRT, and LLM inference engine.' },
  ];

  const defaultApplications = [
    { id: 1, drive_id: 1, drive_title: 'Google Cloud Campus Recruitment 2026', company_name: 'Google Cloud', student_id: 'STU-2026-001', student_name: 'Alex Johnson', gpa: 3.85, package_lpa: 24.5, applied_at: '2026-08-20', status: 'SHORTLISTED', interview_round: 'Technical Round 2 (System Design)' },
    { id: 2, drive_id: 2, drive_title: 'Microsoft Software Engineering Drive', company_name: 'Microsoft', student_id: 'STU-2026-002', student_name: 'Maya Patel', gpa: 3.92, package_lpa: 22.0, applied_at: '2026-08-21', status: 'OFFERED', interview_round: 'Final HR & Offer Letter' },
    { id: 3, drive_id: 3, drive_title: 'Amazon AWS SDE Campus Intake', company_name: 'Amazon', student_id: 'STU-2026-003', student_name: 'David Lee', gpa: 3.45, package_lpa: 20.5, applied_at: '2026-08-22', status: 'UNDER_REVIEW', interview_round: 'Online Coding Assessment' },
  ];

  const [drives, setDrives] = useState(defaultDrives);
  const [applications, setApplications] = useState(defaultApplications);

  const fetchPlacements = async () => {
    setLoading(true);
    try {
      const res = await placementService.getDrives();
      if (res.results && res.results.length > 0) setDrives(res.results);
    } catch (err) {
      setDrives(defaultDrives);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPlacements();
  }, []);

  // Create / Edit Drive
  const handleDriveSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (driveModal.modalData?.isEdit) {
        setDrives((prev) =>
          prev.map((d) => (d.id === driveModal.modalData.drive.id ? { ...d, ...formData } : d))
        );
        showSuccess(`Drive "${formData.title}" updated.`);
      } else {
        const newD = { ...formData, id: Date.now(), applicants_count: 0 };
        setDrives([...drives, newD]);
        showSuccess(`Announced recruitment drive for ${formData.company_name}!`);
      }
      driveModal.closeModal();
    } catch (err) {
      showError('Failed to save drive.');
    } finally {
      setActionLoading(false);
    }
  };

  // Student Apply
  const handleApplySubmit = async (appData) => {
    setActionLoading(true);
    try {
      const targetDrive = applyModal.modalData?.drive;
      const newApp = {
        id: Date.now(),
        drive_id: targetDrive.id,
        drive_title: targetDrive.title,
        company_name: targetDrive.company_name,
        student_id: 'STU-2026-001',
        student_name: 'Alex Johnson',
        gpa: 3.85,
        package_lpa: targetDrive.package_lpa,
        applied_at: new Date().toISOString().split('T')[0],
        status: 'UNDER_REVIEW',
        interview_round: 'Screening Stage',
      };
      setApplications([newApp, ...applications]);
      setDrives((prev) =>
        prev.map((d) => (d.id === targetDrive.id ? { ...d, applicants_count: d.applicants_count + 1 } : d))
      );
      applyModal.closeModal();
      showSuccess(`Applied successfully for ${targetDrive.company_name} (${targetDrive.job_role})!`);
    } catch (err) {
      showError('Failed to apply.');
    } finally {
      setActionLoading(false);
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Campus Placements & Corporate Relations</h2>
          <p className="text-muted mb-0">
            Recruitment drives, CTC packages, eligibility filters, job applications, and career placement metrics
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => driveModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-building-add"></i>
            <span>Schedule Placement Drive</span>
          </button>
        </div>
      </div>

      {/* Tabs */}
      <ul className="nav nav-pills mb-4 gap-2">
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'drives' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('drives')}
          >
            <i className="bi bi-briefcase-fill me-1"></i>
            Active Recruitment Drives ({drives.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'applications' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('applications')}
          >
            <i className="bi bi-file-earmark-person-fill me-1"></i>
            Student Applications ({applications.length})
          </button>
        </li>
      </ul>

      {/* TAB 1: DRIVES */}
      {activeTab === 'drives' && (
        <div className="row g-4">
          {drives.map((d) => (
            <div key={d.id} className="col-12 col-lg-6">
              <div className="campus-card shadow-sm border-0 p-4 h-100 d-flex flex-column justify-content-between">
                <div>
                  <div className="d-flex justify-content-between align-items-start mb-2">
                    <div>
                      <span className="badge bg-primary text-white mb-1">{d.company_name}</span>
                      <h5 className="fw-bold text-dark mb-0">{d.title}</h5>
                    </div>
                    <span className="badge bg-success fs-6 fw-bold">
                      ${d.package_lpa} LPA
                    </span>
                  </div>

                  <h6 className="fw-semibold text-secondary mb-2">{d.job_role}</h6>
                  <p className="small text-muted mb-3">{d.description}</p>

                  <div className="row g-2 p-2 bg-light rounded border small mb-3">
                    <div className="col-6">
                      <span className="text-secondary d-block">Eligibility Cutoff:</span>
                      <strong>Cumulative GPA {d.eligibility_gpa}+</strong>
                    </div>
                    <div className="col-6">
                      <span className="text-secondary d-block">Application Deadline:</span>
                      <strong>{d.application_deadline}</strong>
                    </div>
                    <div className="col-6">
                      <span className="text-secondary d-block">Drive Date:</span>
                      <strong>{d.drive_date}</strong>
                    </div>
                    <div className="col-6">
                      <span className="text-secondary d-block">Applicants:</span>
                      <strong className="text-primary">{d.applicants_count} Students</strong>
                    </div>
                  </div>
                </div>

                <div className="pt-3 border-top d-flex justify-content-between align-items-center">
                  <div className="d-flex gap-1">
                    <button
                      className="btn btn-outline-secondary btn-sm"
                      onClick={() => driveModal.openModal({ drive: d, isEdit: true })}
                      title="Edit Drive"
                    >
                      <i className="bi bi-pencil"></i>
                    </button>
                    <button
                      className="btn btn-outline-danger btn-sm"
                      onClick={() => deleteModal.openModal(d)}
                      title="Delete Drive"
                    >
                      <i className="bi bi-trash"></i>
                    </button>
                  </div>

                  <button
                    className="btn btn-success btn-sm px-4 fw-semibold shadow-sm"
                    onClick={() => applyModal.openModal({ drive: d })}
                  >
                    <i className="bi bi-send-fill me-1"></i> Apply Now
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* TAB 2: APPLICATIONS */}
      {activeTab === 'applications' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="table-responsive">
            <table className="table table-hover align-middle small mb-0">
              <thead className="table-light">
                <tr>
                  <th>Candidate Student</th>
                  <th>Company & Drive</th>
                  <th>CTC Package</th>
                  <th>Current Round / Stage</th>
                  <th>Applied On</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {applications.map((app) => (
                  <tr key={app.id}>
                    <td>
                      <strong className="text-dark d-block">{app.student_name}</strong>
                      <small className="text-muted">{app.student_id} • GPA: {app.gpa}</small>
                    </td>
                    <td>
                      <strong className="text-primary">{app.company_name}</strong>
                      <div className="small text-muted">{app.drive_title}</div>
                    </td>
                    <td><strong className="text-success">${app.package_lpa} LPA</strong></td>
                    <td>
                      <span className="badge bg-light text-dark border">{app.interview_round}</span>
                    </td>
                    <td>{app.applied_at}</td>
                    <td>
                      <span className={`badge ${app.status === 'OFFERED' ? 'bg-success' : app.status === 'SHORTLISTED' ? 'bg-primary' : 'bg-warning text-dark'} px-3 py-1`}>
                        {app.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Modals */}
      <DriveFormModal
        isOpen={driveModal.isOpen}
        onClose={driveModal.closeModal}
        onSubmit={handleDriveSubmit}
        initialData={driveModal.modalData?.drive}
        isEdit={driveModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <ApplyJobModal
        isOpen={applyModal.isOpen}
        onClose={applyModal.closeModal}
        onSubmit={handleApplySubmit}
        selectedDrive={applyModal.modalData?.drive}
        loading={actionLoading}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={() => {
          setDrives((prev) => prev.filter((d) => d.id !== deleteModal.modalData.id));
          deleteModal.closeModal();
          showSuccess('Placement drive removed.');
        }}
        title="Delete Recruitment Drive"
        message={`Are you sure you want to remove the placement drive for "${deleteModal.modalData?.company_name}"?`}
        confirmText="Delete Drive"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Placements;

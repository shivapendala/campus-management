import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const BiometricAttendanceReconciler = () => {
  const [studentId, setStudentId] = useState('');
  const [deviceLogs, setDeviceLogs] = useState([
    { id: 'LOG-1001', student: 'Amit Kumar', roll: '2024CS08', type: 'CARD_SWIPE', location: 'Lab Block A Entry', time: '09:02 AM', status: 'OK' },
    { id: 'LOG-1002', student: 'Rohan Sharma', roll: '2023ME45', type: 'WIFI_LOGIN', location: 'AP-Hostel-3-Floor2', time: '09:15 AM', status: 'OK' },
    { id: 'LOG-1003', student: 'Sneha Reddy', roll: '2025EC12', type: 'CARD_SWIPE', location: 'ECE Seminar Hall', time: '09:05 AM', status: 'OK' },
    { id: 'LOG-1004', student: 'Vikram Singh', roll: '2023CE19', type: 'WIFI_LOGIN', location: 'AP-Central-Library-G', time: '09:45 AM', status: 'OK' }
  ]);
  const [discrepancies, setDiscrepancies] = useState([
    { id: 'DIS-001', student: 'Amit Kumar', roll: '2024CS08', description: 'Card swiped but no Wi-Fi signature detected during class hours', severity: 'MEDIUM', action: 'PENDING_PROCTOR_APPROVAL' }
  ]);

  const logColumns = [
    { key: 'id', label: 'Log ID', render: (val) => <strong className="text-secondary">{val}</strong> },
    { key: 'student', label: 'Student' },
    { key: 'roll', label: 'Roll Number' },
    { key: 'type', label: 'Log Signature', render: (val) => <span className="badge bg-dark">{val}</span> },
    { key: 'location', label: 'Device / AP Name' },
    { key: 'time', label: 'Timestamp' }
  ];

  const discColumns = [
    { key: 'id', label: 'Alert ID', render: (val) => <strong className="text-danger">{val}</strong> },
    { key: 'student', label: 'Student Name' },
    { key: 'description', label: 'Anomaly Details' },
    { key: 'severity', label: 'Alert Level', render: (val) => <span className={`badge ${val === 'HIGH' ? 'bg-danger' : 'bg-warning text-dark'}`}>{val}</span> },
    { key: 'action', label: 'Required Action', render: (val) => <span className="text-muted small">{val}</span> }
  ];

  const handleResolveAlert = (alertId) => {
    setDiscrepancies((prev) => prev.filter((d) => d.id !== alertId));
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-fingerprint me-2"></i>Biometric Attendance & Geofence Sync
          </h2>
          <p className="text-muted mb-0">
            Reconcile physical card swipes with campus Wi-Fi network logs and geofencing coordinates to audit proxies.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-6">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-broadcast me-2"></i>Raw Access Activity Logs</h5>
            <AdvancedDataTable columns={logColumns} data={deviceLogs} searchPlaceholder="Search device logs..." />
          </div>
        </div>

        <div className="col-lg-6">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-danger"><i className="bi bi-exclamation-triangle-fill me-2"></i>Active Attendance Anomalies</h5>
            {discrepancies.length > 0 ? (
              <div className="table-responsive">
                <table className="table table-hover align-middle">
                  <thead>
                    <tr>
                      <th className="small fw-bold">Alert ID</th>
                      <th className="small fw-bold">Student</th>
                      <th className="small fw-bold">Description</th>
                      <th className="small fw-bold">Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    {discrepancies.map((d) => (
                      <tr key={d.id}>
                        <td><strong className="text-danger">{d.id}</strong></td>
                        <td>{d.student}</td>
                        <td className="small text-muted">{d.description}</td>
                        <td>
                          <button className="btn btn-sm btn-outline-success" onClick={() => handleResolveAlert(d.id)}>
                            Approve Present
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <div className="text-center py-5 text-muted">
                <i className="bi bi-check-circle fs-3 text-success mb-2 d-block"></i>
                All swipes match active network signatures. No anomalies registered.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default BiometricAttendanceReconciler;

import React, { useState } from 'react';
import Modal from '../common/Modal';

export const ImportStudentsModal = ({ isOpen, onClose, onImport, loading = false }) => {
  const [csvText, setCsvText] = useState(
`student_id,name,email,phone,year,section,semester,gpa
STU-2026-101,Daniel Craig,d.craig@campus.edu,+1 555-0101,1,A,1,3.75
STU-2026-102,Rachel Weisz,r.weisz@campus.edu,+1 555-0102,2,B,3,3.90
STU-2026-103,Tom Hiddleston,t.hiddleston@campus.edu,+1 555-0103,3,A,5,3.62`
  );

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setCsvText(event.target.result);
      };
      reader.readAsText(file);
    }
  };

  const handleImport = () => {
    onImport(csvText);
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Batch Import Students via CSV"
      size="lg"
    >
      <div className="mb-3">
        <label className="form-label small fw-semibold text-secondary">
          Upload .CSV File or Paste CSV Data
        </label>
        <input
          type="file"
          accept=".csv"
          className="form-control mb-3"
          onChange={handleFileUpload}
        />
      </div>

      <div className="mb-3">
        <label className="form-label small fw-semibold text-secondary">
          CSV Content Editor (Headers: <code>student_id, name, email, phone, year, section, semester, gpa</code>)
        </label>
        <textarea
          rows={7}
          className="form-control font-monospace small"
          value={csvText}
          onChange={(e) => setCsvText(e.target.value)}
        ></textarea>
      </div>

      <div className="alert alert-info py-2 px-3 small d-flex align-items-center gap-2 mb-4">
        <i className="bi bi-info-circle-fill"></i>
        <div>Existing student IDs will be updated; new IDs will be enrolled automatically.</div>
      </div>

      <div className="d-flex justify-content-end gap-2 pt-3 border-top">
        <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
          Cancel
        </button>
        <button
          type="button"
          disabled={loading || !csvText.trim()}
          className="btn btn-success btn-sm px-4 fw-semibold d-flex align-items-center gap-2"
          onClick={handleImport}
        >
          {loading && <span className="spinner-border spinner-border-sm" role="status"></span>}
          <span>Run Batch Import</span>
        </button>
      </div>
    </Modal>
  );
};

export default ImportStudentsModal;

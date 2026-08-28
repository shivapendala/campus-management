import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const LibraryInventoryAuditor = () => {
  const [accessionNumber, setAccessionNumber] = useState('');
  const [shelfNumber, setShelfNumber] = useState('');
  const [bookCondition, setBookCondition] = useState('GOOD');
  const [inventoryIssues, setInventoryIssues] = useState([]);

  const initialAudits = [
    { id: 'AUD-001', date: '2026-08-25', auditor: 'Mrs. L. Janaki', totalCatalog: 5000, scanned: 4982, missing: 18, status: 'COMPLETED' },
    { id: 'AUD-002', date: '2026-08-28', auditor: 'Mr. P. Murugan', totalCatalog: 12000, scanned: 11985, missing: 15, status: 'IN_PROGRESS' }
  ];

  const columns = [
    { key: 'id', label: 'Audit Run Code', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'date', label: 'Date Triggered' },
    { key: 'auditor', label: 'Lead Auditor' },
    { key: 'totalCatalog', label: 'Registered Catalog Size' },
    { key: 'scanned', label: 'Scanned Counts' },
    { key: 'missing', label: 'Flagged Missing' },
    { key: 'status', label: 'Audit Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleScanSubmit = (e) => {
    e.preventDefault();
    if (!accessionNumber || !shelfNumber) return;
    
    // Simulate catalog lookup discrepancy check
    const isMisplaced = shelfNumber !== 'SHELF-621.3';
    const newIssue = {
      id: `ISS-${Date.now()}`,
      accessionNumber: accessionNumber,
      scannedShelf: shelfNumber,
      expectedShelf: 'SHELF-621.3',
      issueType: isMisplaced ? 'MISPLACED' : 'INTACT',
      condition: bookCondition
    };
    
    setInventoryIssues((prev) => [newIssue, ...prev]);
    setAccessionNumber('');
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-journal-album me-2"></i>Library Stock & Inventory Auditor
          </h2>
          <p className="text-muted mb-0">
            Compare active shelf scans with registered Dewey Decimal catalog indexes to detect missing or misplaced assets.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-upc-scan me-2"></i>Shelf Scanner Input</h5>
            <form onSubmit={handleScanSubmit}>
              <div className="mb-3">
                <label className="form-label small fw-bold">Book Accession Number</label>
                <input
                  type="text"
                  className="form-control"
                  value={accessionNumber}
                  onChange={(e) => setAccessionNumber(e.target.value)}
                  placeholder="e.g. ACC-10934"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Shelf Scanned Code</label>
                <input
                  type="text"
                  className="form-control"
                  value={shelfNumber}
                  onChange={(e) => setShelfNumber(e.target.value)}
                  placeholder="e.g. SHELF-620.1"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Physical Condition</label>
                <select className="form-select" value={bookCondition} onChange={(e) => setBookCondition(e.target.value)}>
                  <option value="GOOD">Good / Intact</option>
                  <option value="WORN">Worn / Needs Binding</option>
                  <option value="DAMAGED">Damaged / Page Mismatch</option>
                </select>
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-plus-circle me-1"></i>Record Physical Scan
              </button>
            </form>

            {inventoryIssues.length > 0 && (
              <div className="mt-4">
                <h6 className="fw-bold mb-2 text-danger">Verification Realtime Alerts:</h6>
                <div style={{ maxHeight: '200px', overflowY: 'auto' }}>
                  {inventoryIssues.map((issue) => (
                    <div key={issue.id} className={`p-2 mb-2 rounded-3 small border-start border-4 ${issue.issueType === 'MISPLACED' ? 'bg-warning-subtle border-warning' : 'bg-success-subtle border-success'}`}>
                      <strong>{issue.accessionNumber}</strong>: {issue.issueType === 'MISPLACED' ? `Misplaced (Expected ${issue.expectedShelf})` : 'Catalog match OK'}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-card-list me-2"></i>Stock Verification Registers</h5>
            <AdvancedDataTable columns={columns} data={initialAudits} searchPlaceholder="Search verification cycles..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default LibraryInventoryAuditor;

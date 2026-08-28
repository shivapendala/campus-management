import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const AssetInventoryStudio = () => {
  const [showAssetModal, setShowAssetModal] = useState(false);
  const [assetName, setAssetName] = useState('');
  const [assetCategory, setAssetCategory] = useState('COMPUTING_HARDWARE');
  const [roomNumber, setRoomNumber] = useState('');

  const initialAssets = [
    { id: 'AST-2026-001', name: 'Dell PowerEdge R740 Server', category: 'COMPUTING_HARDWARE', location: 'Server Room A', status: 'ACTIVE', custodian: 'Mr. P. Murugan' },
    { id: 'AST-2026-002', name: 'CISCO Catalyst 9300 Switch', category: 'NETWORKING_EQUIPMENT', location: 'Lab Block 3 Rack A', status: 'ACTIVE', custodian: 'Mr. P. Murugan' },
    { id: 'AST-2026-003', name: 'HP LaserJet Enterprise Printer', category: 'OFFICE_AUTOMATION', location: 'Dean Office Reception', status: 'MAINTENANCE', custodian: 'Mrs. L. Janaki' },
    { id: 'AST-2026-004', name: 'Optiplex 7090 Workstations (x30)', category: 'LAB_EQUIPMENT', location: 'Central Computer Lab 2', status: 'ACTIVE', custodian: 'Dr. Sunita Murthy' },
    { id: 'AST-2026-005', name: 'Rigol DS1054Z Oscilloscope', category: 'LAB_EQUIPMENT', location: 'VLSI Design Lab', status: 'ACTIVE', custodian: 'Dr. Meenakshi Sundaram' }
  ];

  const columns = [
    { key: 'id', label: 'Asset Code', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'name', label: 'Asset Description' },
    { key: 'category', label: 'Asset Category', render: (val) => <span className="badge bg-secondary">{val}</span> },
    { key: 'location', label: 'Physical Location / Room' },
    { key: 'status', label: 'Operational Status', render: (val) => <StatusBadge status={val} size="small" /> },
    { key: 'custodian', label: 'Designated Custodian' }
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-cpu-fill me-2"></i>Campus Asset & Inventory Audit Studio
          </h2>
          <p className="text-muted mb-0">
            Lifecycle monitoring, custody transfers, physical audit reconciliations, and maintenance calendars for university assets.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary" onClick={() => setShowAssetModal(true)}>
            <i className="bi bi-plus-circle-fill me-1"></i>Provision New Asset
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-arrow-repeat me-1"></i>Run Depreciation Audit
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Registered Assets"
            value="1,420 Items"
            icon="bi-box-seam"
            variant="primary"
            subtitle="Valued at Rs. 4.2 Cr"
            delta="100% Tracked"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Assets in Active Use"
            value="1,385 Items"
            icon="bi-check-circle-fill"
            variant="success"
            subtitle="97.5% Operational Rate"
            delta="Healthy"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Under Maintenance"
            value="35 Items"
            icon="bi-tools"
            variant="warning"
            subtitle="Avg. Turnaround: 4.8 Days"
            delta="Normal"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Pending Decommission"
            value="12 Items"
            icon="bi-trash-fill"
            variant="danger"
            subtitle="E-waste disposal queue"
            delta="Action Required"
            deltaType="negative"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4 mb-4">
        <h5 className="fw-bold mb-3"><i className="bi bi-search me-2 text-primary"></i>Asset Registry Index</h5>
        <AdvancedDataTable columns={columns} data={initialAssets} searchPlaceholder="Search assets by code, description, custodian, or location..." />
      </div>

      {showAssetModal && (
        <div className="modal show d-block" tabIndex="-1" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content border-0 shadow rounded-3">
              <div className="modal-header border-0 bg-light p-3">
                <h5 className="modal-title fw-bold text-primary">Provision New Campus Asset</h5>
                <button type="button" className="btn-close" onClick={() => setShowAssetModal(false)}></button>
              </div>
              <div className="modal-body p-4">
                <div className="mb-3">
                  <label className="form-label small fw-bold">Asset Name / Description</label>
                  <input type="text" className="form-control" value={assetName} onChange={(e) => setAssetName(e.target.value)} placeholder="e.g. Dell Latitude 5420 Laptop" />
                </div>
                <div className="mb-3">
                  <label className="form-label small fw-bold">Asset Category</label>
                  <select className="form-select" value={assetCategory} onChange={(e) => setAssetCategory(e.target.value)}>
                    <option value="COMPUTING_HARDWARE">Computing Hardware</option>
                    <option value="NETWORKING_EQUIPMENT">Networking Equipment</option>
                    <option value="LAB_EQUIPMENT">Laboratory Equipment</option>
                    <option value="OFFICE_AUTOMATION">Office Automation</option>
                  </select>
                </div>
                <div className="mb-3">
                  <label className="form-label small fw-bold">Assigned Physical Location</label>
                  <input type="text" className="form-control" value={roomNumber} onChange={(e) => setRoomNumber(e.target.value)} placeholder="e.g. Lab 3, Ground Floor" />
                </div>
              </div>
              <div className="modal-footer border-0 p-3 bg-light d-flex justify-content-end gap-2">
                <button className="btn btn-outline-secondary" onClick={() => setShowAssetModal(false)}>Cancel</button>
                <button className="btn btn-primary" onClick={() => setShowAssetModal(false)}>Register Asset</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AssetInventoryStudio;

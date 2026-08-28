import React from 'react';

const PlacementPipelineKanban = () => {
  const stages = [
    { name: 'Applied Pool', count: 180, variant: 'secondary' },
    { name: 'Online Assessment (OA)', count: 95, variant: 'info' },
    { name: 'Technical Interview', count: 32, variant: 'warning' },
    { name: 'HR / Final Round', count: 18, variant: 'primary' },
    { name: 'Offers Extended', count: 14, variant: 'success' },
  ];

  return (
    <div className="kanban-pipeline-wrapper d-flex gap-3 overflow-auto pb-3">
      {stages.map((stage, idx) => (
        <div
          key={idx}
          className="kanban-column card border-0 shadow-sm rounded-3 p-3 flex-fill"
          style={{ minWidth: '220px', background: '#f8f9fa' }}
        >
          <div className="d-flex justify-content-between align-items-center mb-3">
            <h6 className="fw-bold text-dark mb-0 small text-uppercase">{stage.name}</h6>
            <span className={`badge bg-${stage.variant} rounded-pill`}>{stage.count}</span>
          </div>

          <div className="d-flex flex-column gap-2">
            <div className="card p-2 border shadow-xs bg-white">
              <div className="fw-bold small">Rahul Sharma</div>
              <small className="text-muted">23CSE01042 • CGPA 8.42</small>
            </div>
            <div className="card p-2 border shadow-xs bg-white">
              <div className="fw-bold small">Priya Verma</div>
              <small className="text-muted">23CSE01088 • CGPA 8.90</small>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default PlacementPipelineKanban;

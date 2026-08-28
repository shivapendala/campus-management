import React from 'react';

const TimelineView = ({ items = [] }) => {
  // items: [{ title: '...', timestamp: '...', description: '...', icon: 'bi-check', variant: 'primary' }]
  return (
    <div className="timeline-container position-relative ps-4 border-start ms-2">
      {items.map((item, idx) => (
        <div key={idx} className="timeline-item mb-4 position-relative">
          {/* Bullet node */}
          <div
            className={`position-absolute top-0 start-0 translate-middle rounded-circle d-flex align-items-center justify-content-center bg-${
              item.variant || 'primary'
            } text-white shadow-sm`}
            style={{ width: '28px', height: '28px', left: '-25px' }}
          >
            <i className={`bi ${item.icon || 'bi-circle-fill'} small`}></i>
          </div>

          <div className="ps-2">
            <div className="d-flex justify-content-between align-items-baseline">
              <h6 className="fw-bold mb-1 text-dark">{item.title}</h6>
              <span className="text-muted small">{item.timestamp}</span>
            </div>
            {item.description && <p className="text-muted small mb-0">{item.description}</p>}
            {item.metadata && (
              <div className="mt-2 p-2 bg-light rounded small text-secondary">
                {typeof item.metadata === 'string' ? item.metadata : JSON.stringify(item.metadata)}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default TimelineView;

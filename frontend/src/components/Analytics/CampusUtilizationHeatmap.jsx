import React from 'react';

const CampusUtilizationHeatmap = () => {
  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  const periods = ['09:00', '10:00', '11:30', '01:30', '02:30', '03:30'];

  const getHeatColor = (val) => {
    if (val >= 90) return 'bg-danger text-white';
    if (val >= 75) return 'bg-warning-subtle text-dark';
    if (val >= 50) return 'bg-success-subtle text-dark';
    return 'bg-light text-muted';
  };

  const heatmapMatrix = [
    [95, 92, 88, 85, 78, 45], // Mon
    [90, 94, 86, 82, 70, 40], // Tue
    [92, 90, 89, 88, 75, 50], // Wed
    [88, 85, 90, 78, 65, 35], // Thu
    [85, 80, 75, 70, 55, 30], // Fri
  ];

  return (
    <div className="table-responsive">
      <table className="table table-bordered text-center align-middle mb-0">
        <thead className="table-light">
          <tr>
            <th>Day / Period</th>
            {periods.map((p, idx) => (
              <th key={idx} className="small">{p}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {days.map((d, rIdx) => (
            <tr key={rIdx}>
              <td className="fw-bold text-start table-light">{d}</td>
              {heatmapMatrix[rIdx].map((val, cIdx) => (
                <td key={cIdx} className={getHeatColor(val)}>
                  <span className="fw-semibold small">{val}%</span>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CampusUtilizationHeatmap;

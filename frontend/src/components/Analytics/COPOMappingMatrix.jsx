import React from 'react';

const COPOMappingMatrix = ({ matrix = [] }) => {
  return (
    <div className="table-responsive">
      <table className="table table-bordered text-center align-middle">
        <thead className="table-light">
          <tr>
            <th className="text-start">Course Outcome (CO)</th>
            <th>PO1</th>
            <th>PO2</th>
            <th>PO3</th>
            <th>PO4</th>
            <th>PO5</th>
            <th>PO6</th>
            <th>PO7</th>
            <th>PO8</th>
            <th>PO9</th>
            <th>PO10</th>
            <th>PO11</th>
            <th>PO12</th>
            <th>PSO1</th>
            <th>PSO2</th>
          </tr>
        </thead>
        <tbody>
          {matrix.map((row, idx) => (
            <tr key={idx}>
              <td className="text-start fw-bold text-primary">{row.co}</td>
              {[...Array(12)].map((_, pIdx) => {
                const val = row[`po${pIdx + 1}`] || '-';
                return (
                  <td key={pIdx}>
                    {val !== '-' ? <span className="badge bg-primary">{val}</span> : '-'}
                  </td>
                );
              })}
              <td><span className="badge bg-success">{row.pso1 || '-'}</span></td>
              <td><span className="badge bg-success">{row.pso2 || '-'}</span></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default COPOMappingMatrix;

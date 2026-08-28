import React from 'react';
import { Line } from 'react-chartjs-2';

const AcademicProgressionChart = ({ semesterScores = [8.10, 8.35, 8.50, 8.25, 8.65] }) => {
  const data = {
    labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5'],
    datasets: [
      {
        label: 'Semester SGPA Progression',
        data: semesterScores,
        borderColor: '#0d6efd',
        backgroundColor: 'rgba(13, 110, 253, 0.1)',
        tension: 0.3,
        fill: true,
        pointBackgroundColor: '#0d6efd',
        pointRadius: 5,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: { min: 6.0, max: 10.0, ticks: { stepSize: 1.0 } },
    },
  };

  return (
    <div style={{ height: '220px' }}>
      <Line data={data} options={options} />
    </div>
  );
};

export default AcademicProgressionChart;

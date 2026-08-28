import React from 'react';
import { Line } from 'react-chartjs-2';

const CohortRetentionChart = ({ cohortYear = 2023 }) => {
  const data = {
    labels: ['Year 1 (Freshman)', 'Year 2 (Sophomore)', 'Year 3 (Junior)', 'Year 4 (Senior / Graduation)'],
    datasets: [
      {
        label: `Cohort of ${cohortYear} Retention %`,
        data: [100.0, 96.5, 93.8, 91.2],
        borderColor: '#0d6efd',
        backgroundColor: 'rgba(13, 110, 253, 0.15)',
        tension: 0.3,
        fill: true,
        pointBackgroundColor: '#0d6efd',
        pointRadius: 5,
      },
      {
        label: `Cohort of ${cohortYear - 1} Benchmark %`,
        data: [100.0, 94.2, 91.0, 88.5],
        borderColor: '#6c757d',
        borderDash: [5, 5],
        tension: 0.3,
        pointRadius: 4,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'top' },
      tooltip: {
        callbacks: {
          label: (context) => `${context.dataset.label}: ${context.parsed.y}%`,
        },
      },
    },
    scales: {
      y: {
        min: 80,
        max: 100,
        ticks: { stepSize: 5 },
      },
    },
  };

  return (
    <div className="cohort-retention-chart-wrapper" style={{ height: '280px' }}>
      <Line data={data} options={options} />
    </div>
  );
};

export default CohortRetentionChart;

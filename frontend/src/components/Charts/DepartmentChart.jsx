import React from 'react';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export const DepartmentChart = ({ chartData }) => {
  const defaultData = {
    labels: ['Computer Science', 'Electrical Eng.', 'Mechanical Eng.', 'Business Admin', 'Biotechnology'],
    datasets: [
      {
        label: 'Students Enrolled',
        data: [420, 310, 260, 290, 180],
        backgroundColor: [
          '#4f46e5',
          '#06b6d4',
          '#10b981',
          '#f59e0b',
          '#ec4899'
        ],
        borderWidth: 2,
        borderColor: '#ffffff',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '70%',
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          font: { family: 'Plus Jakarta Sans', size: 12 },
          color: '#64748b',
          padding: 14,
        },
      },
      tooltip: {
        padding: 10,
        backgroundColor: '#0f172a',
      },
    },
  };

  return (
    <div style={{ height: '300px', width: '100%' }}>
      <Doughnut data={chartData || defaultData} options={options} />
    </div>
  );
};

export default DepartmentChart;

import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export const PlacementPieChart = () => {
  const data = {
    labels: ['Dream Super Tier (>20 LPA)', 'Dream Tier (10-20 LPA)', 'Core Engineering (5-10 LPA)'],
    datasets: [
      {
        data: [42, 68, 35],
        backgroundColor: [
          '#6366f1', // Indigo
          '#0ea5e9', // Sky
          '#10b981', // Emerald
        ],
        borderWidth: 2,
        borderColor: '#ffffff',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          boxWidth: 12,
          padding: 12,
          font: {
            size: 11,
          },
        },
      },
    },
  };

  return (
    <div style={{ height: '240px' }}>
      <Pie data={data} options={options} />
    </div>
  );
};

export default PlacementPieChart;

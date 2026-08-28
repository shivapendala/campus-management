import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export const ComplaintsDoughnutChart = () => {
  const data = {
    labels: ['Infrastructure & Wi-Fi', 'Academic & Exams', 'Hostel & Mess', 'Fee/Finance', 'Other'],
    datasets: [
      {
        data: [10, 6, 4, 3, 2],
        backgroundColor: [
          '#f59e0b', // Amber
          '#6366f1', // Indigo
          '#ec4899', // Pink
          '#0ea5e9', // Sky
          '#94a3b8', // Slate
        ],
        borderWidth: 2,
        borderColor: '#ffffff',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '65%',
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          boxWidth: 10,
          padding: 8,
          font: {
            size: 10,
          },
        },
      },
    },
  };

  return (
    <div style={{ height: '240px' }}>
      <Doughnut data={data} options={options} />
    </div>
  );
};

export default ComplaintsDoughnutChart;

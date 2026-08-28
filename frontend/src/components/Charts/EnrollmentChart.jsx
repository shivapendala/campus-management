import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

export const EnrollmentChart = ({ chartData }) => {
  const defaultData = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [
      {
        label: 'Active Enrollments',
        data: [120, 180, 240, 310, 290, 350, 420, 580, 750, 810, 890, 950],
        borderColor: '#4f46e5',
        backgroundColor: 'rgba(79, 70, 229, 0.12)',
        fill: true,
        tension: 0.35,
        pointBackgroundColor: '#4f46e5',
        pointBorderColor: '#fff',
        pointHoverRadius: 6,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
        labels: {
          font: { family: 'Plus Jakarta Sans', size: 12 },
          color: '#64748b',
        },
      },
      tooltip: {
        padding: 10,
        backgroundColor: '#0f172a',
        titleFont: { size: 13, family: 'Plus Jakarta Sans' },
        bodyFont: { size: 12, family: 'Plus Jakarta Sans' },
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { color: '#94a3b8' },
      },
      y: {
        grid: { color: '#f1f5f9' },
        ticks: { color: '#94a3b8' },
      },
    },
  };

  return (
    <div style={{ height: '300px', width: '100%' }}>
      <Line data={chartData || defaultData} options={options} />
    </div>
  );
};

export default EnrollmentChart;

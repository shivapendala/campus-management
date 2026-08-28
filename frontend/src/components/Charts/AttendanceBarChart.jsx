import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const AttendanceBarChart = () => {
  const data = {
    labels: ['CS & Eng.', 'Electrical', 'Mechanical', 'Business', 'Biotech'],
    datasets: [
      {
        label: 'Attendance Rate (%)',
        data: [95.4, 93.8, 92.6, 96.1, 94.0],
        backgroundColor: [
          'rgba(99, 102, 241, 0.85)',
          'rgba(14, 165, 233, 0.85)',
          'rgba(245, 158, 11, 0.85)',
          'rgba(16, 185, 129, 0.85)',
          'rgba(168, 85, 247, 0.85)',
        ],
        borderRadius: 8,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        callbacks: {
          label: (ctx) => ` Attendance: ${ctx.raw}%`,
        },
      },
    },
    scales: {
      y: {
        min: 80,
        max: 100,
        ticks: {
          stepSize: 5,
          callback: (val) => `${val}%`,
        },
        grid: {
          color: 'rgba(226, 232, 240, 0.6)',
        },
      },
      x: {
        grid: {
          display: false,
        },
      },
    },
  };

  return (
    <div style={{ height: '260px' }}>
      <Bar data={data} options={options} />
    </div>
  );
};

export default AttendanceBarChart;

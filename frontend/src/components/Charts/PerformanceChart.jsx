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

export const PerformanceChart = ({ chartData }) => {
  const defaultData = {
    labels: ['A+ (90-100)', 'A (80-89)', 'B+ (75-79)', 'B (70-74)', 'C (60-69)', 'D (50-59)', 'F (<50)'],
    datasets: [
      {
        label: 'Grade Distribution',
        data: [45, 68, 52, 38, 22, 10, 4],
        backgroundColor: '#3b82f6',
        borderRadius: 6,
        hoverBackgroundColor: '#2563eb',
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
        padding: 10,
        backgroundColor: '#0f172a',
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
      <Bar data={chartData || defaultData} options={options} />
    </div>
  );
};

export default PerformanceChart;

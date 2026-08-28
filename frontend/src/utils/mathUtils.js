/**
 * Mathematical and statistical utility functions for institutional analytics.
 */

export const calculateMean = (numbers = []) => {
  if (!numbers.length) return 0;
  const sum = numbers.reduce((acc, val) => acc + val, 0);
  return Number((sum / numbers.length).toFixed(2));
};

export const calculateStandardDeviation = (numbers = []) => {
  if (numbers.length < 2) return 0;
  const mean = calculateMean(numbers);
  const variance = numbers.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / numbers.length;
  return Number(Math.sqrt(variance).toFixed(2));
};

export const calculatePercentile = (arr = [], p = 50) => {
  if (!arr.length) return 0;
  const sorted = [...arr].sort((a, b) => a - b);
  const index = (p / 100) * (sorted.length - 1);
  const lower = Math.floor(index);
  const upper = Math.ceil(index);
  const weight = index - lower;
  return Number((sorted[lower] * (1 - weight) + sorted[upper] * weight).toFixed(2));
};

export const formatCurrencyINR = (amount = 0) => {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(amount);
};

export default {
  calculateMean,
  calculateStandardDeviation,
  calculatePercentile,
  formatCurrencyINR,
};

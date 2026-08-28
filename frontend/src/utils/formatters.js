/**
 * Utility formatters for dates, currencies, GPA, and numbers.
 */

export const formatDate = (dateString, options = {}) => {
  if (!dateString) return 'N/A';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    ...options,
  });
};

export const formatDateTime = (dateString) => {
  if (!dateString) return 'N/A';
  const date = new Date(dateString);
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
};

export const formatCurrency = (amount, currency = 'USD') => {
  if (amount === undefined || amount === null) return '$0.00';
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
    minimumFractionDigits: 2,
  }).format(amount);
};

export const formatGPA = (gpa) => {
  if (gpa === undefined || gpa === null) return '0.00';
  return parseFloat(gpa).toFixed(2);
};

export const formatPercentage = (val) => {
  if (val === undefined || val === null) return '0%';
  return `${parseFloat(val).toFixed(1)}%`;
};

export const truncateText = (text, maxLength = 60) => {
  if (!text) return '';
  return text.length > maxLength ? `${text.substring(0, maxLength)}...` : text;
};

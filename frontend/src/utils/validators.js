/**
 * Form input validators.
 */

export const isValidEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(String(email).toLowerCase());
};

export const isValidPassword = (password, minLength = 6) => {
  return typeof password === 'string' && password.length >= minLength;
};

export const isValidPhone = (phone) => {
  if (!phone) return true; // optional
  const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
  return re.test(String(phone));
};

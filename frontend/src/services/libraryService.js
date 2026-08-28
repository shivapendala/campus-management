import apiClient from './apiClient';

export const libraryService = {
  getBooks: async (params = {}) => {
    const res = await apiClient.get('/library/books/', { params });
    return res.data;
  },
  createBook: async (data) => {
    const res = await apiClient.post('/library/books/', data);
    return res.data;
  },
  updateBook: async (id, data) => {
    const res = await apiClient.put(`/library/books/${id}/`, data);
    return res.data;
  },
  deleteBook: async (id) => {
    const res = await apiClient.delete(`/library/books/${id}/`);
    return res.data;
  },
  getIssues: async (params = {}) => {
    const res = await apiClient.get('/library/issues/', { params });
    return res.data;
  },
  issueBook: async (data) => {
    const res = await apiClient.post('/library/issues/', data);
    return res.data;
  },
  returnBook: async (issueId, payload = {}) => {
    const res = await apiClient.post(`/library/issues/${issueId}/return-book/`, payload);
    return res.data;
  },
};

export default libraryService;

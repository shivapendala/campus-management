import apiClient from './apiClient';

export const examService = {
  getExams: async (params = {}) => {
    const res = await apiClient.get('/examinations/exams/', { params });
    return res.data;
  },
  getExamById: async (id) => {
    const res = await apiClient.get(`/examinations/exams/${id}/`);
    return res.data;
  },
  createExam: async (data) => {
    const res = await apiClient.post('/examinations/exams/', data);
    return res.data;
  },
  updateExam: async (id, data) => {
    const res = await apiClient.put(`/examinations/exams/${id}/`, data);
    return res.data;
  },
  deleteExam: async (id) => {
    const res = await apiClient.delete(`/examinations/exams/${id}/`);
    return res.data;
  },
  submitMarks: async (examId, payload) => {
    const res = await apiClient.post(`/examinations/exams/${examId}/submit-marks/`, payload);
    return res.data;
  },
  verifyByHOD: async (examId) => {
    const res = await apiClient.post(`/examinations/exams/${examId}/verify-by-hod/`);
    return res.data;
  },
  publishResults: async (examId) => {
    const res = await apiClient.post(`/examinations/exams/${examId}/publish-results/`);
    return res.data;
  },
  getResults: async (params = {}) => {
    const res = await apiClient.get('/examinations/results/', { params });
    return res.data;
  },
  getStudentGradeCard: async (studentId = 'STU-2026-001') => {
    const res = await apiClient.get('/examinations/results/student-grade-card/', {
      params: { student_id: studentId },
    });
    return res.data;
  },
};

export default examService;

import apiClient from './apiClient';

export const curriculumService = {
  getCoursePrerequisites: (courseId) => apiClient.get(`/courses/${courseId}/prerequisites/`),
  getCOPOMatrix: (courseId) => apiClient.get(`/courses/${courseId}/copo-matrix/`),
  getSyllabusUnits: (courseId) => apiClient.get(`/courses/${courseId}/syllabus/`),
  verifyCurriculumCredits: (deptId) => apiClient.get(`/departments/${deptId}/curriculum-credits/`),
};

export default curriculumService;

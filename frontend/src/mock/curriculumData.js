/**
 * Canonical Curriculum & Syllabi Data Store for Multi-Department Engineering Programs
 */

export const engineeringCurriculumData = {
  CSE: {
    department_name: 'Computer Science & Engineering',
    hod_name: 'Dr. Rajesh Raman, Ph.D. (IIT Delhi)',
    total_credits: 160,
    regulations: 'R23 Autonomous',
    semesters: [
      {
        semester: 1,
        courses: [
          { code: 'MA101', title: 'Linear Algebra & Calculus', type: 'BS', credits: 4, hours: 4 },
          { code: 'PH101', title: 'Engineering Physics & Quantum Mechanics', type: 'BS', credits: 3, hours: 3 },
          { code: 'CS101', title: 'Problem Solving & Python Programming', type: 'ES', credits: 3, hours: 3 },
          { code: 'ME101', title: 'Engineering Graphics & 3D Modeling', type: 'ES', credits: 3, hours: 4 },
          { code: 'PH102', title: 'Physics Laboratory', type: 'BS', credits: 1.5, hours: 3 },
          { code: 'CS102', title: 'Python Programming Laboratory', type: 'ES', credits: 1.5, hours: 3 },
        ],
      },
      {
        semester: 2,
        courses: [
          { code: 'MA201', title: 'Differential Equations & Numerical Methods', type: 'BS', credits: 4, hours: 4 },
          { code: 'CH201', title: 'Engineering Chemistry & Material Science', type: 'BS', credits: 3, hours: 3 },
          { code: 'EE201', title: 'Basic Electrical & Electronics Engineering', type: 'ES', credits: 3, hours: 3 },
          { code: 'CS201', title: 'Programming in C & Data Structures', type: 'PC', credits: 4, hours: 4 },
          { code: 'CH202', title: 'Chemistry Laboratory', type: 'BS', credits: 1.5, hours: 3 },
          { code: 'CS202', title: 'Data Structures Laboratory in C', type: 'PC', credits: 1.5, hours: 3 },
        ],
      },
      {
        semester: 3,
        courses: [
          { code: 'MA301', title: 'Discrete Mathematics & Graph Theory', type: 'BS', credits: 4, hours: 4 },
          { code: 'CS301', title: 'Database Management Systems', type: 'PC', credits: 4, hours: 4 },
          { code: 'CS302', title: 'Design & Analysis of Algorithms', type: 'PC', credits: 4, hours: 4 },
          { code: 'CS303', title: 'Digital Logic & Computer Architecture', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS304', title: 'Object-Oriented Programming with Java', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS305', title: 'Database Management Systems Lab', type: 'PC', credits: 1.5, hours: 3 },
          { code: 'CS306', title: 'Java Programming & Software Studio Lab', type: 'PC', credits: 1.5, hours: 3 },
        ],
      },
      {
        semester: 4,
        courses: [
          { code: 'MA401', title: 'Probability, Statistics & Stochastic Processes', type: 'BS', credits: 4, hours: 4 },
          { code: 'CS401', title: 'Operating Systems & Kernel Architecture', type: 'PC', credits: 4, hours: 4 },
          { code: 'CS402', title: 'Theory of Computation & Automata', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS403', title: 'Software Engineering & Agile DevOps', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS404', title: 'Web Technologies & RESTful Microservices', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS405', title: 'Operating Systems & Linux Shell Lab', type: 'PC', credits: 1.5, hours: 3 },
          { code: 'CS406', title: 'Web Development & Full-Stack Studio Lab', type: 'PC', credits: 1.5, hours: 3 },
        ],
      },
      {
        semester: 5,
        courses: [
          { code: 'CS501', title: 'Computer Networks & Internet Protocols', type: 'PC', credits: 4, hours: 4 },
          { code: 'CS502', title: 'Compiler Design & Lexical Analysis', type: 'PC', credits: 4, hours: 4 },
          { code: 'CS503', title: 'Artificial Intelligence & Knowledge Systems', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS_PE1', title: 'Professional Elective I: Cloud Computing Architecture', type: 'PE', credits: 3, hours: 3 },
          { code: 'OE101', title: 'Open Elective I: Operations Research & Optimization', type: 'OE', credits: 3, hours: 3 },
          { code: 'CS504', title: 'Computer Networks & Packet Sniffing Lab', type: 'PC', credits: 1.5, hours: 3 },
          { code: 'CS505', title: 'Artificial Intelligence & Machine Learning Lab', type: 'PC', credits: 1.5, hours: 3 },
        ],
      },
      {
        semester: 6,
        courses: [
          { code: 'CS601', title: 'Machine Learning & Statistical Pattern Recognition', type: 'PC', credits: 4, hours: 4 },
          { code: 'CS602', title: 'Cryptography & Network Security', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS_PE2', title: 'Professional Elective II: Big Data Analytics & Spark', type: 'PE', credits: 3, hours: 3 },
          { code: 'CS_PE3', title: 'Professional Elective III: Natural Language Processing', type: 'PE', credits: 3, hours: 3 },
          { code: 'OE201', title: 'Open Elective II: Intellectual Property Rights (IPR)', type: 'OE', credits: 3, hours: 3 },
          { code: 'CS603', title: 'Machine Learning Studio & Deep Learning Lab', type: 'PC', credits: 1.5, hours: 3 },
          { code: 'CS604', title: 'Security Auditing & Penetration Testing Lab', type: 'PC', credits: 1.5, hours: 3 },
        ],
      },
      {
        semester: 7,
        courses: [
          { code: 'CS701', title: 'Deep Learning & Neural Network Architectures', type: 'PC', credits: 3, hours: 3 },
          { code: 'CS_PE4', title: 'Professional Elective IV: Distributed Systems & Blockchain', type: 'PE', credits: 3, hours: 3 },
          { code: 'CS_PE5', title: 'Professional Elective V: Edge Computing & IoT Systems', type: 'PE', credits: 3, hours: 3 },
          { code: 'OE301', title: 'Open Elective III: Environmental Sustainability & ESG', type: 'OE', credits: 3, hours: 3 },
          { code: 'CS702', title: 'Summer Internship & Industrial Training Seminar', type: 'EEC', credits: 3, hours: 6 },
          { code: 'CS703', title: 'Capstone Design Project Phase I', type: 'EEC', credits: 3, hours: 6 },
        ],
      },
      {
        semester: 8,
        courses: [
          { code: 'CS_PE6', title: 'Professional Elective VI: Quantum Computing Foundations', type: 'PE', credits: 3, hours: 3 },
          { code: 'OE401', title: 'Open Elective IV: Engineering Economics & Management', type: 'OE', credits: 3, hours: 3 },
          { code: 'CS801', title: 'Capstone Design Project Phase II & Viva Voce', type: 'EEC', credits: 10, hours: 20 },
        ],
      },
    ],
  },
};

export default engineeringCurriculumData;

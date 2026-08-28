/**
 * Comprehensive Campus Entity Graph & Telemetry Mock Store
 */

export const comprehensiveCampusStore = {
  institution_metadata: {
    institution_id: 'INST-EDUCORE-001',
    name: 'EduCore University of Science and Technology',
    established_year: 1998,
    chancellor: 'Dr. Vikramaditya Singhania',
    vice_chancellor: 'Prof. K. R. Narayanan, Ph.D. (Stanford)',
    registrar: 'Dr. P. S. Ramanujan',
    campus_area_acres: 120,
    built_up_area_sqft: 850000,
    statutory_approvals: ['AICTE (F.No. South-West/1-9842100)', 'UGC 2(f) & 12(B)', 'NAAC Grade A++', 'NBA Tier-1 Accredited'],
  },
  department_summary: [
    { code: 'CSE', name: 'Computer Science & Engineering', intake: 180, enrolled: 720, faculty_count: 48, labs: 8, student_faculty_ratio: '15:1' },
    { code: 'ECE', name: 'Electronics & Communication Engineering', intake: 120, enrolled: 480, faculty_count: 32, labs: 6, student_faculty_ratio: '15:1' },
    { code: 'EEE', name: 'Electrical & Electronics Engineering', intake: 60, enrolled: 240, faculty_count: 16, labs: 5, student_faculty_ratio: '15:1' },
    { code: 'MECH', name: 'Mechanical Engineering', intake: 120, enrolled: 480, faculty_count: 32, labs: 7, student_faculty_ratio: '15:1' },
    { code: 'CIVIL', name: 'Civil Engineering', intake: 60, enrolled: 240, faculty_count: 16, labs: 5, student_faculty_ratio: '15:1' },
    { code: 'AIML', name: 'Artificial Intelligence & Data Science', intake: 60, enrolled: 240, faculty_count: 16, labs: 4, student_faculty_ratio: '15:1' },
  ],
  campus_buildings: [
    { code: 'AB-1', name: 'Aryabhatta Academic Block 1 (CSE & AIML)', floors: 5, classrooms: 24, labs: 12, capacity: 1500 },
    { code: 'AB-2', name: 'Ramanujan Academic Block 2 (ECE & EEE)', floors: 4, classrooms: 18, labs: 10, capacity: 1200 },
    { code: 'AB-3', name: 'Visvesvaraya Engineering Block 3 (MECH & CIVIL)', floors: 4, classrooms: 18, labs: 14, capacity: 1200 },
    { code: 'CENTRAL_LIB', name: 'Dr. APJ Abdul Kalam Central Library', floors: 3, seating_capacity: 800, volumes: 45200 },
    { code: 'AUD_MAIN', name: 'Tagore Memorial Central University Auditorium', capacity: 1200, air_conditioned: true },
    { code: 'HOSTEL_M1', name: 'Homi Bhabha Boys Residence Block A', capacity: 450, rooms: 225 },
    { code: 'HOSTEL_M2', name: 'C.V. Raman Boys Residence Block B', capacity: 450, rooms: 225 },
    { code: 'HOSTEL_F1', name: 'Kalpana Chawla Girls Residence Block C', capacity: 400, rooms: 200 },
    { code: 'HOSTEL_F2', name: 'Sarojini Naidu Girls Residence Block D', capacity: 400, rooms: 200 },
  ],
  statutory_committees: [
    { name: 'Internal Quality Assurance Cell (IQAC)', chair: 'Prof. K. R. Narayanan (Vice Chancellor)', coordinator: 'Dr. Rajesh Raman' },
    { name: 'Internal Complaints Committee (ICC / POSH)', chair: 'Dr. Sunita Murthy (Presiding Officer)', external_member: 'Adv. Pratibha Rao (High Court)' },
    { name: 'Anti-Ragging Flying Squad & Committee', chair: 'Dr. Ramesh Chandra (Convener)', members_count: 12 },
    { name: 'Institute Innovation Council (IIC - MHRD)', chair: 'Dr. Meenakshi Sundaram', president: 'Dr. Rajesh Raman' },
    { name: 'Board of Studies (BOS) - Computing', chair: 'Dr. Rajesh Raman (Dean Academics)', external_experts: ['Prof. IIT Madras', 'Principal Architect, Microsoft'] },
  ],
};

export default comprehensiveCampusStore;

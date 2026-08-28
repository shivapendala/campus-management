/**
 * Comprehensive Institutional Reports Mock Store
 * Mapped to NAAC and NIRF statutory reporting criteria.
 */

export const comprehensiveInstitutionalReports = {
  nirf_tlr: {
    student_strength: [
      { program: "B.Tech (CSE)", intake: 180, first_year: 180, second_year: 178, third_year: 175, fourth_year: 172, total_enrolled: 705, boys: 480, girls: 225, within_state: 512, outside_state: 185, outside_country: 8, economically_backward: 110, socially_challenged: 240 },
      { program: "B.Tech (ECE)", intake: 120, first_year: 120, second_year: 118, third_year: 115, fourth_year: 112, total_enrolled: 465, boys: 310, girls: 155, within_state: 360, outside_state: 102, outside_country: 3, economically_backward: 75, socially_challenged: 180 },
      { program: "B.Tech (MECH)", intake: 120, first_year: 120, second_year: 115, third_year: 112, fourth_year: 110, total_enrolled: 457, boys: 420, girls: 37, within_state: 380, outside_state: 75, outside_country: 2, economically_backward: 90, socially_challenged: 195 },
      { program: "B.Tech (CIVIL)", intake: 60, first_year: 60, second_year: 58, third_year: 55, fourth_year: 54, total_enrolled: 227, boys: 195, girls: 32, within_state: 190, outside_state: 35, outside_country: 2, economically_backward: 45, socially_challenged: 110 },
      { program: "B.Tech (EEE)", intake: 60, first_year: 60, second_year: 59, third_year: 56, fourth_year: 55, total_enrolled: 230, boys: 180, girls: 50, within_state: 185, outside_state: 42, outside_country: 3, economically_backward: 50, socially_challenged: 115 },
      { program: "B.Tech (AIML)", intake: 60, first_year: 60, second_year: 60, third_year: 58, fourth_year: 58, total_enrolled: 236, boys: 160, girls: 76, within_state: 165, outside_state: 68, outside_country: 3, economically_backward: 35, socially_challenged: 95 }
    ],
    faculty_details: [
      { dept: "CSE", total_faculty: 48, phd_qualified: 32, masters_qualified: 16, professors: 8, associate_professors: 16, assistant_professors: 24, average_experience_years: 11.2 },
      { dept: "ECE", total_faculty: 32, phd_qualified: 20, masters_qualified: 12, professors: 5, associate_professors: 10, assistant_professors: 17, average_experience_years: 10.5 },
      { dept: "MECH", total_faculty: 32, phd_qualified: 18, masters_qualified: 14, professors: 5, associate_professors: 9, assistant_professors: 18, average_experience_years: 12.1 },
      { dept: "CIVIL", total_faculty: 16, phd_qualified: 10, masters_qualified: 6, professors: 2, associate_professors: 5, assistant_professors: 9, average_experience_years: 9.8 },
      { dept: "EEE", total_faculty: 16, phd_qualified: 9, masters_qualified: 7, professors: 2, associate_professors: 4, assistant_professors: 10, average_experience_years: 10.2 },
      { dept: "AIML", total_faculty: 16, phd_qualified: 11, masters_qualified: 5, professors: 2, associate_professors: 5, assistant_professors: 9, average_experience_years: 8.9 }
    ]
  },
  nirf_rpc: {
    publications: [
      { year: 2021, journal_papers: 98, conference_proceedings: 120, book_chapters: 15, total_citations: 920 },
      { year: 2022, journal_papers: 105, conference_proceedings: 135, book_chapters: 18, total_citations: 1120 },
      { year: 2023, journal_papers: 118, conference_proceedings: 150, book_chapters: 22, total_citations: 1340 },
      { year: 2024, journal_papers: 132, conference_proceedings: 168, book_chapters: 25, total_citations: 1590 },
      { year: 2025, journal_papers: 142, conference_proceedings: 185, book_chapters: 28, total_citations: 1840 },
      { year: 2026, journal_papers: 168, conference_proceedings: 210, book_chapters: 35, total_citations: 2150 }
    ],
    sponsored_research: [
      { agency: "DST-SERB", project_count: 5, total_funding_inr: 18500000.0, status: "ACTIVE" },
      { agency: "AICTE", project_count: 8, total_funding_inr: 11000000.0, status: "ACTIVE" },
      { agency: "DRDO", project_count: 2, total_funding_inr: 9500000.0, status: "ACTIVE" },
      { agency: "ISRO", project_count: 3, total_funding_inr: 6400000.0, status: "ACTIVE" },
      { agency: "Private Sector Industry", project_count: 12, total_funding_inr: 14500000.0, status: "ACTIVE" }
    ],
    consultancy_projects: [
      { client: "L&T Construction", service: "Structural Concrete Integrity Analysis", revenue_inr: 1200000.0 },
      { client: "Cognizant Technology Solutions", service: "Edge AI Algorithm Benchmark Audit", revenue_inr: 1800000.0 },
      { client: "Robert Bosch Engineering", service: "Embedded Controller Calibration Models", revenue_inr: 2500000.0 },
      { client: "Simplex Infrastructure Ltd", service: "Soil Dynamics Shear Mapping", revenue_inr: 850000.0 },
      { client: "Schneider Electric", service: "Smart Metering Protocol Compliance", revenue_inr: 1500000.0 }
    ]
  },
  nirf_go: {
    graduation_outcomes: [
      { program: "B.Tech (CSE)", total_graduates: 168, placed_count: 162, higher_education_count: 4, median_ctc_lpa: 12.5, min_ctc_lpa: 5.5, max_ctc_lpa: 32.5 },
      { program: "B.Tech (ECE)", total_graduates: 108, placed_count: 98, higher_education_count: 8, median_ctc_lpa: 8.5, min_ctc_lpa: 4.8, max_ctc_lpa: 22.0 },
      { program: "B.Tech (MECH)", total_graduates: 105, placed_count: 82, higher_education_count: 12, median_ctc_lpa: 6.2, min_ctc_lpa: 4.0, max_ctc_lpa: 12.0 },
      { program: "B.Tech (CIVIL)", total_graduates: 52, placed_count: 38, higher_education_count: 10, median_ctc_lpa: 5.8, min_ctc_lpa: 3.6, max_ctc_lpa: 9.5 },
      { program: "B.Tech (EEE)", total_graduates: 54, placed_count: 46, higher_education_count: 6, median_ctc_lpa: 7.2, min_ctc_lpa: 4.2, max_ctc_lpa: 15.0 },
      { program: "B.Tech (AIML)", total_graduates: 55, placed_count: 53, higher_education_count: 1, median_ctc_lpa: 14.0, min_ctc_lpa: 6.0, max_ctc_lpa: 30.0 }
    ],
    historical_graduation_trends: [
      { year: "2020", graduates: 420, placement_pct: 78.5, higher_ed_pct: 12.0, median_package: 4.5 },
      { year: "2021", graduates: 450, placement_pct: 80.2, higher_ed_pct: 11.5, median_package: 4.8 },
      { year: "2022", graduates: 480, placement_pct: 82.5, higher_ed_pct: 10.8, median_package: 5.2 },
      { year: "2023", graduates: 510, placement_pct: 84.1, higher_ed_pct: 9.5, median_package: 5.8 },
      { year: "2024", graduates: 540, placement_pct: 86.8, higher_ed_pct: 8.2, median_package: 6.4 },
      { year: "2025", graduates: 570, placement_pct: 89.2, higher_ed_pct: 7.5, median_package: 7.2 },
      { year: "2026", graduates: 600, placement_pct: 91.5, higher_ed_pct: 6.8, median_package: 8.5 }
    ]
  },
  naac_ssr_criterions: {
    criterion_1_curricular_aspects: {
      percent_revision_last_5_years: 32.5,
      new_courses_introduced: 84,
      bos_resolution_references: [
        { id: "BOS-CSE-2025-01", date: "2025-05-12", changes: "Introduction of Generative AI Electives in Sem 7" },
        { id: "BOS-ECE-2025-02", date: "2025-06-15", changes: "Inclusion of ARM System architecture and Edge computing lab" },
        { id: "BOS-MECH-2025-01", date: "2025-05-20", changes: "Electric vehicle powertrain modeling included in automotive design stream" }
      ]
    },
    criterion_2_teaching_learning_evaluation: {
      average_enrollment_pct: 97.8,
      seats_reserved_sc_st_obc: 420,
      seats_filled_sc_st_obc: 412,
      student_satisfaction_survey_avg: 4.42, // scale of 5
      revaluation_turnaround_days_avg: 18.2
    },
    criterion_4_infrastructure_learning_resources: {
      total_classrooms: 98,
      ict_enabled_classrooms: 98,
      total_computers_for_students: 840,
      wifi_bandwidth_mbps: 1000,
      library_e_journals_subscribed: 12000,
      annual_expenditure_books_inr: 2450000.0
    }
  }
};

export default comprehensiveInstitutionalReports;

/**
 * Comprehensive Institutional Fee Structure & Concession Matrix Store
 */

export const comprehensiveFeeStructuresStore = {
  academic_year: '2026-27',
  tuition_fee_schedule: [
    { program: 'B.Tech (CSE / AIML)', quota: 'GOVERNMENT_MERIT', annual_tuition_inr: 85000.0, dev_fee: 15000.0, total_annual: 100000.0 },
    { program: 'B.Tech (CSE / AIML)', quota: 'MANAGEMENT_QUOTA', annual_tuition_inr: 165000.0, dev_fee: 25000.0, total_annual: 190000.0 },
    { program: 'B.Tech (ECE / EEE)', quota: 'GOVERNMENT_MERIT', annual_tuition_inr: 75000.0, dev_fee: 15000.0, total_annual: 90000.0 },
    { program: 'B.Tech (MECH / CIVIL)', quota: 'GOVERNMENT_MERIT', annual_tuition_inr: 65000.0, dev_fee: 15000.0, total_annual: 80000.0 },
    { program: 'M.Tech (All Specializations)', quota: 'GATE_QUALIFIED', annual_tuition_inr: 50000.0, dev_fee: 10000.0, total_annual: 60000.0 },
  ],
  hostel_fee_schedule: [
    { room_type: 'Single Room (AC with Attached Bath)', annual_rent_inr: 65000.0, mess_advance_inr: 45000.0, total_hostel: 110000.0 },
    { room_type: 'Double Sharing (Non-AC)', annual_rent_inr: 42000.0, mess_advance_inr: 42000.0, total_hostel: 84000.0 },
    { room_type: 'Triple Sharing (Non-AC)', annual_rent_inr: 32000.0, mess_advance_inr: 42000.0, total_hostel: 74000.0 },
  ],
  transport_bus_fee_schedule: [
    { zone: 'Zone 1 (< 10 KM from Campus)', annual_bus_fee_inr: 18000.0 },
    { zone: 'Zone 2 (10 - 25 KM from Campus)', annual_bus_fee_inr: 24000.0 },
    { zone: 'Zone 3 (25 - 45 KM City Limits)', annual_bus_fee_inr: 30000.0 },
  ],
};

export default comprehensiveFeeStructuresStore;

/**
 * Campus Physical Infrastructure & Facility Equipment Mock Data Store
 */

export const campusInfrastructureStore = {
  classrooms: [
    { room_id: "CR-101", building: "Aryabhatta Academic Block 1", floor: 1, capacity: 60, projector: "EPSON-3LCD", audio_system: "JBL-Enterprise", status: "AVAILABLE" },
    { room_id: "CR-102", building: "Aryabhatta Academic Block 1", floor: 1, capacity: 60, projector: "EPSON-3LCD", audio_system: "JBL-Enterprise", status: "AVAILABLE" },
    { room_id: "CR-201", building: "Aryabhatta Academic Block 1", floor: 2, capacity: 60, projector: "EPSON-3LCD", audio_system: "JBL-Enterprise", status: "OCCUPIED" },
    { room_id: "CR-202", building: "Aryabhatta Academic Block 1", floor: 2, capacity: 60, projector: "EPSON-3LCD", audio_system: "JBL-Enterprise", status: "AVAILABLE" },
    { room_id: "LH-101", building: "Ramanujan Academic Block 2", floor: 1, capacity: 120, projector: "SONY-Laser-4K", audio_system: "BOSE-Surround", status: "OCCUPIED" },
    { room_id: "LH-102", building: "Ramanujan Academic Block 2", floor: 1, capacity: 120, projector: "SONY-Laser-4K", audio_system: "BOSE-Surround", status: "AVAILABLE" }
  ],
  laboratories: [
    { lab_id: "LAB-1", name: "Advanced Computing & Database Lab", department: "CSE", capacity: 40, work_stations: 42, server_node: "Dell-PowerEdge-T440", status: "OPERATIONAL" },
    { lab_id: "LAB-2", name: "AI & Neural Networks Research Lab", department: "CSE", capacity: 30, work_stations: 30, server_node: "NVIDIA-DGX-Station", status: "OPERATIONAL" },
    { lab_id: "LAB-3", name: "Microprocessors & VLSI Lab", department: "ECE", capacity: 40, work_stations: 40, server_node: "Intel-Xeon-Edge", status: "OPERATIONAL" },
    { lab_id: "LAB-4", name: "Power Systems & Machines Lab", department: "EEE", capacity: 30, work_stations: 15, server_node: "None", status: "OPERATIONAL" },
    { lab_id: "LAB-5", name: "CFD & CAD/CAM Simulation Lab", department: "MECH", capacity: 40, work_stations: 40, server_node: "HP-Z8-G4-Workstation", status: "OPERATIONAL" }
  ],
  biometric_terminals: [
    { terminal_id: "BIO-AB1-G1", model: "ZKTeco-UFace800", ip: "192.168.10.21", location: "Aryabhatta Block Entrance", status: "ONLINE" },
    { terminal_id: "BIO-AB2-G1", model: "ZKTeco-UFace800", ip: "192.168.10.22", location: "Ramanujan Block Entrance", status: "ONLINE" },
    { terminal_id: "BIO-LIB-G1", model: "Matrix-COSEC-PATH", ip: "192.168.10.25", location: "Central Library Entrance", status: "ONLINE" },
    { terminal_id: "BIO-HOST-M1", model: "eSSL-MB20", ip: "192.168.20.10", location: "Boys Hostel Block A Gate", status: "ONLINE" },
    { terminal_id: "BIO-HOST-F1", model: "eSSL-MB20", ip: "192.168.20.11", location: "Girls Hostel Block C Gate", status: "ONLINE" }
  ]
};

export default campusInfrastructureStore;

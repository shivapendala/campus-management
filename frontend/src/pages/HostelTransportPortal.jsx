import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const HostelTransportPortal = () => {
  const [activeTab, setActiveTab] = useState('hostel');

  const hostelRooms = [
    { block: 'Block A (Boys)', room: 'A-101', type: 'DOUBLE', occupants: 'Rahul Sharma, Aditya Deshmukh', available: '0 Beds', status: 'OCCUPIED' },
    { block: 'Block A (Boys)', room: 'A-102', type: 'DOUBLE', occupants: 'Chirag Sen', available: '1 Bed', status: 'AVAILABLE' },
    { block: 'Block C (Girls)', room: 'C-201', type: 'SINGLE', occupants: 'Ananya Iyer', available: '0 Beds', status: 'OCCUPIED' },
    { block: 'Block C (Girls)', room: 'C-202', type: 'DOUBLE', occupants: 'Bhavna Reddy, Divya Pillai', available: '0 Beds', status: 'OCCUPIED' },
  ];

  const busRoutes = [
    { route_no: 1, name: 'Central Station Express', bus_reg: 'KA-01-F-4210', driver: 'S. Murugesan (9842100001)', capacity: '50 Seats', enrolled: '46 Students', status: 'ON_ROUTE' },
    { route_no: 2, name: 'Airport Road Metro Feeder', bus_reg: 'KA-01-F-4211', driver: 'K. Rajendran (9842100002)', capacity: '50 Seats', enrolled: '42 Students', status: 'ON_ROUTE' },
    { route_no: 3, name: 'Tech Park / Electronic City', bus_reg: 'KA-01-F-4212', driver: 'M. Anand (9842100003)', capacity: '50 Seats', enrolled: '48 Students', status: 'ON_ROUTE' },
  ];

  const hostelCols = [
    { key: 'block', label: 'Hostel Block' },
    { key: 'room', label: 'Room No.', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'type', label: 'Type', render: (val) => <span className="badge bg-light text-dark">{val}</span> },
    { key: 'occupants', label: 'Current Occupant(s)' },
    { key: 'available', label: 'Available Vacancy' },
    { key: 'status', label: 'Status', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  const busCols = [
    { key: 'route_no', label: 'Route #', render: (val) => <strong className="text-primary">Route {val}</strong> },
    { key: 'name', label: 'Route Name' },
    { key: 'bus_reg', label: 'Bus Registration' },
    { key: 'driver', label: 'Driver & Contact' },
    { key: 'enrolled', label: 'Pass Holders' },
    { key: 'status', label: 'GPS Telemetry', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-houses-fill me-2"></i>Campus Living, Residential & Transit Studio
          </h2>
          <p className="text-muted mb-0">
            Hostel room allocation matrix, biometric curfew gatepasses, bus fleet route tracking, and GPS geofence telemetry.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-qr-code-scan me-1"></i>Scan Gatepass QR
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-plus-circle me-1"></i>Issue New Bus Pass
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Hostel Residents"
            value="1,420"
            icon="bi-people-fill"
            variant="primary"
            subtitle="94.5% Capacity Occupancy"
            delta="94.5%"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Curfew Gatepasses"
            value="38 Active"
            icon="bi-door-open-fill"
            variant="warning"
            subtitle="Expected Return < 09:30 PM"
            delta="Normal"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Operational Bus Fleet"
            value="18 Buses"
            icon="bi-bus-front-fill"
            variant="success"
            subtitle="850 Commuter Students"
            delta="All Active"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Mess Meals Served Daily"
            value="4,250 Meals"
            icon="bi-cup-hot-fill"
            variant="info"
            subtitle="Breakfast, Lunch, Dinner"
            delta="100% Quality Pass"
            deltaType="positive"
          />
        </div>
      </div>

      <ul className="nav nav-pills mb-4 gap-2 border-bottom pb-3">
        <li className="nav-item">
          <button className={`nav-link ${activeTab === 'hostel' ? 'active' : ''}`} onClick={() => setActiveTab('hostel')}>
            <i className="bi bi-building me-1"></i>Hostel Room Allotments
          </button>
        </li>
        <li className="nav-item">
          <button className={`nav-link ${activeTab === 'transport' ? 'active' : ''}`} onClick={() => setActiveTab('transport')}>
            <i className="bi bi-geo-alt-fill me-1"></i>Bus Fleet & Transit Routes
          </button>
        </li>
      </ul>

      {activeTab === 'hostel' && (
        <div className="card border-0 shadow-sm rounded-3 p-4">
          <h5 className="fw-bold mb-3"><i className="bi bi-door-closed me-2 text-primary"></i>Room Inventory & Student Occupancy</h5>
          <AdvancedDataTable columns={hostelCols} data={hostelRooms} searchPlaceholder="Search room, student, or block..." />
        </div>
      )}

      {activeTab === 'transport' && (
        <div className="card border-0 shadow-sm rounded-3 p-4">
          <h5 className="fw-bold mb-3"><i className="bi bi-signpost-2 me-2 text-primary"></i>Campus Bus Fleet Schedule & Live Telemetry</h5>
          <AdvancedDataTable columns={busCols} data={busRoutes} searchPlaceholder="Search route, driver, or stop..." />
        </div>
      )}
    </div>
  );
};

export default HostelTransportPortal;

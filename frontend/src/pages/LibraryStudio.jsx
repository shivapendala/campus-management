import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const LibraryStudio = () => {
  const books = [
    { acc_no: 'ACC-2026-001', isbn: '978-0134685991', title: 'Effective Java (3rd Edition)', author: 'Joshua Bloch', ddc: '005.133', copies: '4 / 5 Available', status: 'AVAILABLE' },
    { acc_no: 'ACC-2026-002', isbn: '978-0262033848', title: 'Introduction to Algorithms (CLRS)', author: 'Cormen, Leiserson, Rivest', ddc: '005.1', copies: '1 / 10 Available', status: 'AVAILABLE' },
    { acc_no: 'ACC-2026-003', isbn: '978-0078022159', title: 'Database System Concepts (7th Edition)', author: 'Silberschatz, Korth, Sudarshan', ddc: '005.74', copies: '0 / 8 Available', status: 'RESERVED' },
  ];

  const columns = [
    { key: 'acc_no', label: 'Accession No.', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'title', label: 'Title & Edition' },
    { key: 'author', label: 'Author(s)' },
    { key: 'ddc', label: 'DDC Class', render: (val) => <span className="badge bg-light text-dark">{val}</span> },
    { key: 'copies', label: 'Circulation Availability' },
    { key: 'status', label: 'Status', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-book-half me-2"></i>Library Catalog & Circulation Studio
          </h2>
          <p className="text-muted mb-0">
            Dewey Decimal Classification (DDC) catalog indexing, RFID checkout tracking, overdue fine calculation, and priority hold queues.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-upc-scan me-1"></i>Barcode Scanner Check-in
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-journal-plus me-1"></i>Add Book Accession
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Catalog Volumes"
            value="45,200"
            icon="bi-bookshelf"
            variant="primary"
            subtitle="8,500 Unique Titles"
            delta="Catalog Indexed"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Books in Loan"
            value="3,420"
            icon="bi-journal-arrow-up"
            variant="info"
            subtitle="7.5% Inventory in Circulation"
            delta="Normal"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Overdue Returns"
            value="42 Books"
            icon="bi-clock-history"
            variant="warning"
            subtitle="Automated Reminders Dispatched"
            delta="Under Control"
            deltaType="neutral"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="E-Journal Downloads"
            value="1,240 / Week"
            icon="bi-cloud-download-fill"
            variant="success"
            subtitle="IEEE Xplore & ScienceDirect"
            delta="+18% YoY"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-search me-2 text-primary"></i>Catalog Search & Stock Position
        </h5>
        <AdvancedDataTable
          columns={columns}
          data={books}
          searchPlaceholder="Search catalog by title, author, ISBN, or DDC classification..."
        />
      </div>
    </div>
  );
};

export default LibraryStudio;

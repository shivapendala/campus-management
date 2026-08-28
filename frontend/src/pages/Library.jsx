import React, { useState, useEffect } from 'react';
import { libraryService } from '../services';
import BookFormModal from '../components/Library/BookFormModal';
import IssueBookModal from '../components/Library/IssueBookModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Library = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [activeTab, setActiveTab] = useState('catalog'); // 'catalog', 'circulation', 'fines'
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('ALL');

  // Modals
  const bookModal = useModal();
  const issueModal = useModal();
  const deleteModal = useModal();

  const defaultBooks = [
    { id: 1, title: 'Introduction to Algorithms (CLRS)', author: 'Cormen, Leiserson, Rivest, Stein', isbn: '978-0262046305', category: 'Computer Science', publisher: 'MIT Press', total_copies: 15, available_copies: 11, shelf_location: 'Stack CS-04' },
    { id: 2, title: 'Database System Concepts', author: 'Silberschatz, Korth, Sudarshan', isbn: '978-0078022159', category: 'Computer Science', publisher: 'McGraw-Hill', total_copies: 12, available_copies: 8, shelf_location: 'Stack CS-02' },
    { id: 3, title: 'Modern Operating Systems', author: 'Andrew S. Tanenbaum, Herbert Bos', isbn: '978-0133591620', category: 'Computer Science', publisher: 'Pearson', total_copies: 10, available_copies: 6, shelf_location: 'Stack CS-03' },
    { id: 4, title: 'Computer Networking: A Top-Down Approach', author: 'Kurose & Ross', isbn: '978-0136681557', category: 'Computer Science', publisher: 'Pearson', total_copies: 14, available_copies: 9, shelf_location: 'Stack CS-05' },
    { id: 5, title: 'Pattern Recognition and Machine Learning', author: 'Christopher M. Bishop', isbn: '978-0387310732', category: 'Computer Science', publisher: 'Springer', total_copies: 8, available_copies: 4, shelf_location: 'Stack AI-01' },
    { id: 6, title: 'Microelectronic Circuits', author: 'Sedra & Smith', isbn: '978-0190853464', category: 'Electronics', publisher: 'Oxford Press', total_copies: 10, available_copies: 7, shelf_location: 'Stack EC-01' },
  ];

  const defaultIssues = [
    { id: 1, book_id: 1, book_title: 'Introduction to Algorithms (CLRS)', student_id: 'STU-2026-001', student_name: 'Alex Johnson', issue_date: '2026-08-15', due_date: '2026-08-29', status: 'ISSUED', fine_accrued: 0 },
    { id: 2, book_id: 2, book_title: 'Database System Concepts', student_id: 'STU-2026-002', student_name: 'Maya Patel', issue_date: '2026-08-10', due_date: '2026-08-24', status: 'OVERDUE', fine_accrued: 4.0 },
    { id: 3, book_id: 3, book_title: 'Modern Operating Systems', student_id: 'STU-2026-003', student_name: 'David Lee', issue_date: '2026-08-01', due_date: '2026-08-15', status: 'RETURNED', fine_accrued: 0 },
  ];

  const [books, setBooks] = useState(defaultBooks);
  const [issues, setIssues] = useState(defaultIssues);

  const fetchLibraryData = async () => {
    setLoading(true);
    try {
      const res = await libraryService.getBooks();
      if (res.results && res.results.length > 0) setBooks(res.results);
    } catch (err) {
      setBooks(defaultBooks);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLibraryData();
  }, []);

  const filteredBooks = books.filter((b) => {
    const matchesSearch =
      b.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      b.author.toLowerCase().includes(searchTerm.toLowerCase()) ||
      b.isbn.includes(searchTerm);
    const matchesCategory = selectedCategory === 'ALL' || b.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  // Handle Book CRUD
  const handleBookSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (bookModal.modalData?.isEdit) {
        setBooks((prev) =>
          prev.map((b) => (b.id === bookModal.modalData.book.id ? { ...b, ...formData } : b))
        );
        showSuccess(`Book "${formData.title}" updated.`);
      } else {
        const newB = { ...formData, id: Date.now() };
        setBooks([...books, newB]);
        showSuccess(`Added "${formData.title}" to library catalog.`);
      }
      bookModal.closeModal();
    } catch (err) {
      showError('Failed to save book.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Book Checkout
  const handleIssueSubmit = async (issueData) => {
    setActionLoading(true);
    try {
      const targetBook = issueModal.modalData?.book;
      const newIssue = {
        id: Date.now(),
        ...issueData,
        fine_accrued: 0,
      };
      setIssues([newIssue, ...issues]);
      setBooks((prev) =>
        prev.map((b) => (b.id === targetBook.id ? { ...b, available_copies: Math.max(0, b.available_copies - 1) } : b))
      );
      issueModal.closeModal();
      showSuccess(`Issued "${targetBook.title}" to ${issueData.student_name}!`);
    } catch (err) {
      showError('Failed to checkout book.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Book Return
  const handleReturnBook = (issue) => {
    setIssues((prev) =>
      prev.map((i) => (i.id === issue.id ? { ...i, status: 'RETURNED' } : i))
    );
    setBooks((prev) =>
      prev.map((b) => (b.id === issue.book_id ? { ...b, available_copies: b.available_copies + 1 } : b))
    );
    showSuccess(`Book "${issue.book_title}" returned successfully.`);
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Library & Digital Learning Commons</h2>
          <p className="text-muted mb-0">
            Book catalog, ISBN indexation, circulation desk, lending records, and automated fine calculations
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => bookModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-plus-circle-fill"></i>
            <span>Add Catalog Book</span>
          </button>
        </div>
      </div>

      {/* Tabs */}
      <ul className="nav nav-pills mb-4 gap-2">
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'catalog' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('catalog')}
          >
            <i className="bi bi-book-half me-1"></i>
            Book Catalog ({filteredBooks.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'circulation' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('circulation')}
          >
            <i className="bi bi-arrow-left-right me-1"></i>
            Circulation & Active Checkouts ({issues.filter((i) => i.status !== 'RETURNED').length})
          </button>
        </li>
      </ul>

      {/* TAB 1: BOOK CATALOG */}
      {activeTab === 'catalog' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="d-flex flex-wrap align-items-center justify-content-between gap-3 mb-4">
            <div className="d-flex align-items-center gap-2 flex-grow-1" style={{ maxWidth: '400px' }}>
              <i className="bi bi-search text-muted"></i>
              <input
                type="text"
                className="form-control form-control-sm"
                placeholder="Search by title, author, or ISBN..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <select
              className="form-select form-select-sm"
              style={{ width: '200px' }}
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
            >
              <option value="ALL">All Categories</option>
              <option value="Computer Science">Computer Science</option>
              <option value="Electronics">Electronics</option>
              <option value="Mechanical">Mechanical</option>
            </select>
          </div>

          <div className="table-responsive">
            <table className="table table-hover align-middle small mb-0">
              <thead className="table-light">
                <tr>
                  <th>Title & Authors</th>
                  <th>ISBN</th>
                  <th>Category</th>
                  <th>Shelf Location</th>
                  <th>Availability</th>
                  <th className="text-end">Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredBooks.map((b) => (
                  <tr key={b.id}>
                    <td>
                      <strong className="text-dark d-block fs-6">{b.title}</strong>
                      <small className="text-muted">{b.author}</small>
                    </td>
                    <td><code>{b.isbn}</code></td>
                    <td><span className="badge bg-light text-secondary border">{b.category}</span></td>
                    <td><span className="badge bg-secondary-subtle text-secondary">{b.shelf_location}</span></td>
                    <td>
                      <span className={`badge ${b.available_copies > 0 ? 'bg-success' : 'bg-danger'} px-3 py-1`}>
                        {b.available_copies} / {b.total_copies} Available
                      </span>
                    </td>
                    <td className="text-end">
                      <div className="d-flex justify-content-end gap-1">
                        <button
                          disabled={b.available_copies === 0}
                          className="btn btn-primary btn-sm fw-semibold"
                          onClick={() => issueModal.openModal({ book: b })}
                        >
                          <i className="bi bi-person-check me-1"></i> Issue
                        </button>
                        <button
                          className="btn btn-outline-secondary btn-sm"
                          onClick={() => bookModal.openModal({ book: b, isEdit: true })}
                        >
                          <i className="bi bi-pencil"></i>
                        </button>
                        <button
                          className="btn btn-outline-danger btn-sm"
                          onClick={() => deleteModal.openModal(b)}
                        >
                          <i className="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB 2: CIRCULATION & CHECKOUTS */}
      {activeTab === 'circulation' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="table-responsive">
            <table className="table table-hover align-middle small mb-0">
              <thead className="table-light">
                <tr>
                  <th>Book Title</th>
                  <th>Borrower Student</th>
                  <th>Issue Date</th>
                  <th>Due Date</th>
                  <th>Status & Fines</th>
                  <th className="text-end">Action</th>
                </tr>
              </thead>
              <tbody>
                {issues.map((issue) => (
                  <tr key={issue.id}>
                    <td><strong className="text-dark">{issue.book_title}</strong></td>
                    <td>
                      <strong className="text-primary">{issue.student_name}</strong>
                      <small className="d-block text-muted">{issue.student_id}</small>
                    </td>
                    <td>{issue.issue_date}</td>
                    <td>
                      <span className={issue.status === 'OVERDUE' ? 'text-danger fw-bold' : 'text-muted'}>
                        {issue.due_date}
                      </span>
                    </td>
                    <td>
                      <div className="d-flex align-items-center gap-2">
                        <span className={`badge ${issue.status === 'RETURNED' ? 'bg-secondary' : issue.status === 'OVERDUE' ? 'bg-danger' : 'bg-primary'}`}>
                          {issue.status}
                        </span>
                        {issue.fine_accrued > 0 && (
                          <span className="badge bg-danger-subtle text-danger fw-bold">
                            Fine: ${issue.fine_accrued.toFixed(2)}
                          </span>
                        )}
                      </div>
                    </td>
                    <td className="text-end">
                      {issue.status !== 'RETURNED' && (
                        <button
                          className="btn btn-success btn-sm fw-semibold"
                          onClick={() => handleReturnBook(issue)}
                        >
                          <i className="bi bi-box-arrow-in-left me-1"></i> Return Book
                        </button>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Modals */}
      <BookFormModal
        isOpen={bookModal.isOpen}
        onClose={bookModal.closeModal}
        onSubmit={handleBookSubmit}
        initialData={bookModal.modalData?.book}
        isEdit={bookModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <IssueBookModal
        isOpen={issueModal.isOpen}
        onClose={issueModal.closeModal}
        onSubmit={handleIssueSubmit}
        selectedBook={issueModal.modalData?.book}
        loading={actionLoading}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={() => {
          setBooks((prev) => prev.filter((b) => b.id !== deleteModal.modalData.id));
          deleteModal.closeModal();
          showSuccess('Book removed from catalog.');
        }}
        title="Remove Book from Catalog"
        message={`Are you sure you want to remove "${deleteModal.modalData?.title}" from the catalog?`}
        confirmText="Remove Book"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Library;

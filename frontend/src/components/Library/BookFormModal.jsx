import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const BookFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Introduction to Algorithms (CLRS)',
    author: 'Cormen, Leiserson, Rivest, Stein',
    isbn: '978-0262046305',
    category: 'Computer Science',
    publisher: 'MIT Press',
    edition: '4th Edition',
    total_copies: 15,
    shelf_location: 'Stack CS-04',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        author: initialData.author || '',
        isbn: initialData.isbn || '',
        category: initialData.category || 'Computer Science',
        publisher: initialData.publisher || 'MIT Press',
        edition: initialData.edition || '4th Edition',
        total_copies: initialData.total_copies || 15,
        shelf_location: initialData.shelf_location || 'Stack CS-04',
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      total_copies: Number(formData.total_copies),
      available_copies: Number(formData.total_copies),
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Book — ${formData.title}` : 'Catalog New Library Book'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-8">
            <FormField
              label="Book Title"
              name="title"
              placeholder="e.g. Operating System Concepts"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="ISBN Number"
              name="isbn"
              placeholder="978-..."
              value={formData.isbn}
              onChange={(e) => setFormData({ ...formData, isbn: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Primary Author(s)"
              name="author"
              placeholder="e.g. Silberschatz, Galvin, Gagne"
              value={formData.author}
              onChange={(e) => setFormData({ ...formData, author: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Academic Discipline / Category"
              type="select"
              name="category"
              value={formData.category}
              options={[
                { value: 'Computer Science', label: 'Computer Science & AI' },
                { value: 'Electronics', label: 'Electronics & VLSI' },
                { value: 'Electrical', label: 'Electrical & Power' },
                { value: 'Mechanical', label: 'Mechanical & Robotics' },
                { value: 'Civil', label: 'Civil & Structural' },
                { value: 'Mathematics', label: 'Mathematics & Statistics' },
              ]}
              onChange={(e) => setFormData({ ...formData, category: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Publisher"
              name="publisher"
              value={formData.publisher}
              onChange={(e) => setFormData({ ...formData, publisher: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Total Physical Copies"
              type="number"
              name="total_copies"
              value={formData.total_copies}
              onChange={(e) => setFormData({ ...formData, total_copies: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Shelf / Stack Location"
              name="shelf_location"
              placeholder="e.g. Rack B2-04"
              value={formData.shelf_location}
              onChange={(e) => setFormData({ ...formData, shelf_location: e.target.value })}
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Save Changes' : 'Add to Catalog'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default BookFormModal;

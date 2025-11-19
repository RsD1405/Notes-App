// NoteModal.jsx
import React from 'react';
import './NoteModal.css';

const NoteModal = ({ note, onClose }) => {
  if (!note) return null; // Don't render if no note

  return (
    <div className="modalOverlay" onClick={onClose}>
      <div className="modalContent" onClick={(e) => e.stopPropagation()}>
        <button className="closeButton" onClick={onClose}>×</button>
        <h2>{note.title}</h2>
        <p>{note.content}</p>
        <small>
          Created: {note.created_at} <br />
          Updated: {note.updated_at}
        </small>
      </div>
    </div>
  );
};

export default NoteModal;

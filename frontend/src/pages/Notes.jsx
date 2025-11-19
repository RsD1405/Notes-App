import React, { useState, useEffect } from "react";
import "./Notes.css";
import NoteModal from "../components/NoteModal";

const testDb = [
    {
        id: "1",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "2",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdghhhhhhhhsdfghsdgfhdghsdghzfadgfhadfhhadfhadhdfDfDfDFhDgjsfgjdtyjdyhjdyjsyjsyjjdgfhzdgjzadghDGhdgh",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "3",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "4",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "5",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "6",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "7",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    },
    {
        id: "8",
        title: "dfgdfg",
        content: "sdgasdgasdfgasfdg",
        created_at: "test",
        updated_at: "test"
    }
]

function Notes() {
    const [notes, setNotes] = useState([]);
    const [selectedNote, setSelectedNote] = useState(null);

    function truncate(text, maxLength) {
        if (!text) return '';
        return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
    }

    useEffect(() => {
        setNotes(testDb);
    }, []);

    return (
        <div id="pageContainer">
            <header className="pageHeader">
                <h1 className="pageTitle">Notes App</h1>
            </header>
            <div id="notesGridDiv">
                {notes.map((note) => (
                    <div
                        key={note.id}
                        className="notesCard"
                        onClick={() => setSelectedNote(note)}>
                        <h3>{truncate(note.title, 10)}</h3>
                        <p>{truncate(note.content, 20)}</p>
                        <small>
                            Created: {note.created_at}
                            <br />
                            Updated: {note.updated_at}
                        </small>
                    </div>
                ))}
            </div>
            {
                selectedNote && (
                    <NoteModal note={selectedNote} onClose={() => setSelectedNote(null)} />
                )
            }
        </div>
    );
}

export default Notes
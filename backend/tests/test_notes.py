# tests/test_notes.py
def test_create_note(client):
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note"
    assert "id" in data

def test_read_notes(client):
    response = client.get("/notes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_update_note(client):
    create_resp = client.post("/notes/", json={"title": "Old Title", "content": "Old content"})
    note_id = create_resp.json()["id"]
    update_resp = client.patch(f"/notes/{note_id}", json={"title": "New Title", "content": "Updated content"})
    assert update_resp.status_code == 200
    data = update_resp.json()
    assert data["title"] == "New Title"
    assert data["content"] == "Updated content"

def test_delete_note(client):
    create_resp = client.post("/notes/", json={"title": "Delete Me", "content": "To be deleted"})
    note_id = create_resp.json()["id"]
    delete_resp = client.delete(f"/notes/{note_id}")
    assert delete_resp.status_code == 204
    get_resp = client.get("/notes/")
    ids = [note["id"] for note in get_resp.json()]
    assert note_id not in ids


"""
Running:
cd backend
python -m pytest -v

no need to run main backend server
"""
## -------------------- Emil Ferent, Sep 2024 ---------------------

import pytest
from app import app
from models import db, Idea

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_submit_idea(client):
    response = client.post('/ideas', json={
        'title': 'New Windmill Virtual Reality Training',
        'description': 'A new idea about how we can help the Engineering team and CAD design.',
        'category': 'wind',
        'submitter': 'Anders'
    }, headers={"API-Key": "your-api-key"})
    
    assert response.status_code == 201
    assert b'Idea submitted successfully' in response.data

def test_get_ideas(client):
    response = client.get('/ideas', headers={"API-Key": "your-api-key"})
    assert response.status_code == 200

def test_update_idea_status(client):
    idea = Idea(title="New Idea on IoT", description="IoT Sensors on blade tips", category="wind", submitter="Christina")
    db.session.add(idea)
    db.session.commit()

    response = client.put(f'/ideas/{idea.id}', json={"status": "in development"}, headers={"API-Key": "your-api-key"})
    assert response.status_code == 200
    assert b'Idea status updated successfully' in response.data

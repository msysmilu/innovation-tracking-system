## -------------------- Emil Ferent, Sep 2024 ---------------------

# Innovation Tracking System API

This API allows employees to submit, track, and collaborate on innovative ideas related to renewable energy technologies.

## Authentication
All requests must include an `API-Key` in the headers.

## Endpoints

### 1. Submit a New Idea

**POST /ideas**

Request Body:
```json
{
  "title": "New Windmill Augmented Reality Service Process",
  "description": "A new idea for improving the way service workers use manuals for the maintenance tasks.",
  "category": "wind",
  "submitter": "Sofia"
}
```

Response:
```json
{
  "message": "Idea submitted successfully",
  "idea": 1
}
```

### 2. Retrieve Ideas

**GET /ideas**

Optional query parameters:
- `category`: Filter by category (e.g., solar, wind)
- `status`: Filter by status (e.g., under review, in development)

Response:
```json
[
  {
    "id": 1,
    "title": "New Windmill Augmented Reality Service Process",
    "description": "A new idea for improving the way service workers use manuals for the maintenance tasks.",
    "category": "wind",
    "status": "under review",
    "submitter": "Sofia",
    "created_at": "2024-09-12T10:00:00"
  }
]
```

### 3. Update Idea Status

**PUT /ideas/{id}**

Request Body:
```json
{
  "status": "in development"
}
```

Response:
```json
{
  "message": "Idea status updated successfully",
  "idea": 1
}
```

### 4. Add Comment to an Idea

**POST /ideas/{id}/comments**

Request Body:
```json
{
  "content": "Great idea!",
  "author": "Christian"
}
```

Response:
```json
{
  "message": "Comment added successfully",
  "comment_id": 1
}
```

### How to Run the Application

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize the database: `python db_init.py`
4. Run the application: `python app.py`
5. Run tests: `pytest`

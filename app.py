## -------------------- Emil Ferent, Sep 2024 ---------------------

from flask import Flask, jsonify, request
from models import db, Idea, Comment
from auth import require_api_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
db.init_app(app)

@app.route('/ideas', methods=['POST'])
@require_api_key
def submit_idea():
    data = request.json
    new_idea = Idea(
        title=data['title'],
        description=data['description'],
        category=data['category'],
        submitter=data['submitter']
    )
    db.session.add(new_idea)
    db.session.commit()
    return jsonify({"message": "Idea submitted successfully", "idea": new_idea.id}), 201

@app.route('/ideas', methods=['GET'])
@require_api_key
def get_ideas():
    category = request.args.get('category')
    status = request.args.get('status')

    #build the filtering system
    ideas_query = Idea.query
    if category:
        ideas_query = ideas_query.filter_by(category=category)
    if status:
        ideas_query = ideas_query.filter_by(status=status)

    ideas = ideas_query.all()
    return jsonify([{
        "id": idea.id,
        "title": idea.title,
        "description": idea.description,
        "category": idea.category,
        "status": idea.status,
        "submitter": idea.submitter,
        "created_at": idea.created_at
    } for idea in ideas])

@app.route('/ideas/<int:id>', methods=['PUT'])
@require_api_key
def update_idea_status(id):
    data = request.json
    idea = Idea.query.get_or_404(id)

    # todo: add a default status mechanism (maybe 'under review')
    if 'status' not in data:
        return jsonify({"error": "Status is required"}), 400

    if data['status'] not in ['under review', 'in development', 'implemented']:
        return jsonify({"error": "Invalid status"}), 400

    idea.status = data['status']
    db.session.commit()

    return jsonify({"message": "Idea status updated successfully", "idea": idea.id})

@app.route('/ideas/<int:id>/comments', methods=['POST'])
@require_api_key
def add_comment(id):
    data = request.json
    idea = Idea.query.get_or_404(id)
    
    new_comment = Comment(
        idea_id=idea.id,
        content=data['content'],
        author=data['author']
    )
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"message": "Comment added successfully", "comment_id": new_comment.id})

if __name__ == '__main__':
    app.run(debug=True)

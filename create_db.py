from web_api import app, db

with app.app_context():
    db.create_all()
    print("Database created successfully!")
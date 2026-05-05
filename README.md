# candidates-web-api
Web API to keep track of Candidates applying for IT Job

<!-- Creating Virtual Env -->
python -m virtualenv nameofenv
<!-- Example -->
<!-- python -m virtualenv flaskcrudenv -->

<!-- Enable ENV -->
<!-- In Powershell -->
.\env\Scripts\activate.ps1
<!-- In Command Prompt -->
env\Scripts\activate.bat


<!-- Deactivate ENV -->
deactivate

pip3 install flask, flask_sqlalchemy

<!-- RUN APP -->
python .\web_api.py

<!-- Set up database in terminal -->
<!-- Make sure env is acivated -->
python create_db.py

pip3 install gunicorn
pip3 freeze > requirements.txt
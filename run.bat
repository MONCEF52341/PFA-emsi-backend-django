call .\.env\Scripts\activate
cd AbsenceManager
start firefox "http://127.0.0.1:8000/"
python manage.py runserver
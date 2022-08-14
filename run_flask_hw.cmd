cd ..

call env/Scripts/activate.bat

call Homeworks

set FLASK_APP=hw_flask
flask run --host=0.0.0.0

cmd
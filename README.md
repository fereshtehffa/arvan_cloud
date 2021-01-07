# Arvan cloud sample middleware

This project uses django as the framework, sqlite as the database, openresty as the web server.

## How to run

1. Install the python requirements:
```sh 
pip3 install -r requirements.txt
```

2. Create the necessary database tables 
```sh
python3 manage.py migrate
```

3. Create superuser to access the admin panel
```sh
python3 manage.py createsuperuser
```


4. Run the server
```sh 
python3 manage.py runserver
```

5. Open the below usr to access tables such as name exceptions for prefix
```
http://127.0.0.1:8000/admin/
```

6. Set bucket access credentials in `openresty/app.lua:36-43`

7. Build the docker image
```sh
cd openresty
docker build -t openresty .
```

8. Run an instance of the image
```sh 
docker run -it --net=host -p 8080:8080  openresty
```

9. send POST requests like the below form:
```
{"username": "YOUR_USERNAME", "prefix": "SAMPLE", "name": "SAMPLESAMPLE"}
```
> Create YOUR_USERNAME user in admin panel explained on step 5
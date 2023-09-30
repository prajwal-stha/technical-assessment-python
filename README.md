# Inroduction

Hazesoft Form is a Django based application where one can fill form and save it.

## Task Breakdown
- Form for user has been created
- Written backend code for form
- Created UI for superuser for CRUD operation
- Backend core has been packaged for pip install in private repository
- Refactored the code
- Created docker compose and dockerfile
- Tested

## Tech Used
- Python
- Django
- Docker
- Github

## Installation
- Clone repository from [github](https://github.com/prajwal-stha/technical-assessment-python.git)
- Go to cloned directory where docker compose file is
- Now build the docker compose using 
```bash
docker compose up webb
```
- Now you will see link http://0.0.0.0:8000/
- Docker compose is bind to above link, after seeing above link, now go to the browser and write http://127.0.0.1:8000/user/login/
- You will see login page for superuser admin, use username: hazesoft and password: hazesoft@123
- You can create form by clicking create form in login page


## License

[MIT](https://choosealicense.com/licenses/mit/)
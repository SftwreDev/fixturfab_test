# FixturFab Test API

This project is built with FastAPI.


## Installation

1. Clone the repository: 
```code
git clone https://github.com/SftwreDev/fixturfab_test.git
```
2. Change into the app directory: 
```code
cd app
```
3. Install the requirements: 
```code
pip install -r requirements.txt
```

4. Run Alembic to create the database tables: 
```code
alembic upgrade head
```

## Running the App

To start the application, run the following command:

```code
uvicorn main:app --reload
```

This will start the application on `http://localhost:8000/`.

## API Documentation

The API documentation can be found at `http://localhost:8000`. The documentation provides a user-friendly interface to explore the API endpoints and their parameters.

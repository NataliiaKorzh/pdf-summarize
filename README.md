# PDF Summary API

## Description

This API allows users to upload a one-page PDF file and get a summary of its content using the OpenAI API. The application is containerized using Docker.

## Technologies Used
- FastAPI
- OpenAI API
- Docker

## Setup and Usage

### Prerequisites

- Docker
- OpenAI API Key
- Python 3.8+ (if not using Docker)

### Installing using GitHub

Clone the repository:

```shell
git clone https://github.com/your_username/pdf_summary_api.git
cd pdf_summarize
```

Create and activate virtual environment:

```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```

Install the required packages:
```shell
pip install -r requirements.txt
```

Create .env file and fill it like in .env_sample

### Run server
Start the server using Uvicorn:

```shell
uvicorn main:app --reload
```


## Run with Docker

Docker should be installed

Build and Run the Docker container:

```shell

docker-compose build
docker-compose up
```

## Accessing the API
For testing summarize endpoint open a browser and enter url

http://0.0.0.0:8000/docs/

POST /summarize
Upload a 1-page PDF file and get a summary of its content.

### Request:

- Method: POST
- Endpoint: /summarize
- Content-Type: multipart/form-data
- File: 1-page PDF file (must have .pdf extension)

### Response:

- Status Code: 200
- Content-Type: application/json
- Body: JSON object containing the summary of the PDF content.

Example response:
```
{
  "summary": "This is a summarized content of the uploaded PDF."
}

```
## Project Structure
- main.py: Initializes the FastAPI application.
- app/: Contains application files. Includes routers,can be expanded with DB models, Pydantic schemas, crud, utils, etc.
- Dockerfile: Docker configuration file.
- docker-compose.yml: Docker Compose configuration file.
- .env: Environment variables file (not included in the repository, you need to create it).
- requirements.txt: List of Python dependencies.

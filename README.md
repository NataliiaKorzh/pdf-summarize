# PDF Summary API

## Description

This API allows users to upload a PDF file and get a summary of its content using the OpenAI API. The application is containerized using Docker.

## Setup and Usage

### Prerequisites

- Docker
- OpenAI API Key

### Installing using GitHub

Clone the repository:

```shell
git clone https://github.com/your_username/pdf_summary_api.git
cd pdf_summarize
```

Create virtual environment:

```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt

set OPENAI_API_KEY=<your_openai_api_key>

```

### Run server

```shell
uvicorn main:app --reload
```


## Run with Docker

```shell

docker-compose build
docker-compose up
```

For testing summarize endpoint open a browser and enter url

http://0.0.0.0:8000/docs/

- POST request
![DB structure](Request_examp.png)

- Response

```shell
{
  "summary": "string"
}
```

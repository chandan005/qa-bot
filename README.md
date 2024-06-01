# Question-Answering Bot API

## Introduction

This project implements a backend API for a Question-Answering bot using FastAPI and Langchain. The bot leverages the capabilities of a large language model to answer questions based on the content of a document. It supports input files in JSON and PDF formats and returns a structured JSON blob with answers to each question.

## Tools and Technologies Used

- FastAPI: API Framework.
- Langchain: Framework for building natural language processing applications
- PyPDFLoader: Module for loading and extracting text from PDF files
- Chroma: Vector database for similarity search
- OpenAI: Large language model for generating answers to questions
- Python-dotenv: Library for loading environment variables from .env files
- Pipenv: Dependency Management

## Steps to Run, Test, and Deploy

### Prerequisites

- Python 3.9 or higher installed
- Docker installed (optional, for containerization)

1. Clone the Repository

   ```bash
   git clone <repository-url>
   cd qa-bot
   ```

2. Install Dependencies

   ```bash
   pip install pipenv
   pipenv install --dev
   ```

3. Set Environment Variables

Create a `.env.dev` file for development environment and `.env.prod` file for production environment. Set the required environment variables including PINECONE_API_KEY, OPENAI_API_KEY, and PINECONE_INDEX_NAME.

4. Run the Application Locally

   ```bash
   pipenv run uvicorn app.main --reload
   ```

5. Test the API

You can use tools like curl or Postman to test the API endpoints. Refer to the provided test cases for different scenarios to test.

6. Dockerize the Application (Optional)

   ```bash
   docker build -t qa-bot -f Dockerfile .
   docker run -p 8000:8000 qa-bot
   ```

7. Deploy to Production

Deploy the application to a production server using your preferred hosting provider. Make sure to set the environment variables for the production environment and configure the server accordingly.

```bash
    docker build -t qa-bot -f Dockerfile.prod .
    docker run -p 8000:8000 qa-bot
```

## API Documentation

The API documentation can be accessed at `http://localhost:8000/docs` when running the application locally. It provides detailed information about the available endpoints, request parameters, and response formats.
"""

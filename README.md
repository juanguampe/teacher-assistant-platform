# Teacher Assistant Platform

A web-based platform for teachers to interact with an AI assistant that has access to custom instructions and documents.

## Features

- Chat-based interface similar to ChatGPT
- Custom instructions for the AI assistant
- Document upload functionality for reference knowledge
- Persistent chat history
- Multiple conversation threads

## Setup and Installation

### Prerequisites

- Python 3.9+
- OpenAI API key

### Local Development

1. Clone this repository
   ```
   git clone https://github.com/juanguampe/teacher-assistant-platform.git
   cd teacher-assistant-platform
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your OpenAI API key
   ```
   OPENAI_API_KEY=your_api_key_here
   FLASK_APP=run.py
   FLASK_DEBUG=1
   SECRET_KEY=some_random_string
   ```

5. Initialize the database
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application
   ```
   flask run
   ```

7. Access the application at http://localhost:5000

## Project Structure

- `app/`: Main application package
  - `static/`: Static files (CSS, JS, etc.)
  - `templates/`: HTML templates
  - `uploads/`: Directory for uploaded documents
  - `__init__.py`: Application factory
  - `config.py`: Configuration settings
  - `models.py`: Database models
  - `openai_service.py`: OpenAI API integration
  - `routes.py`: Application routes
  - `utils.py`: Utility functions
- `migrations/`: Database migrations
- `run.py`: Application entry point

## License

MIT

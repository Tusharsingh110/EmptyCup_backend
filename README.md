# Empty Cup Assignment backend
# Flask MongoDB Backend

This is a simple Flask backend that connects to a MongoDB database and serves data through a RESTful API. The backend is designed to be deployed on platforms like Vercel.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Tusharsingh110/EmptyCup_backend.git
```
2. Navigate to the project directory:

```bash
cd EmptyCup_backend
```
3. Install dependencies:
4. Configuration
Create a .env file in the root directory:
```
env
MONGODB_URI=mongodb+srv://your-username:your-password@cluster0.your.mongodb.net/your-database
```
#Replace your-username, your-password, and your-database with your MongoDB credentials.

5. Save the .env file.
6. Run the Flask application:

```bash
python app.py
```
The application will run on http://localhost:5000/.

7. API Endpoints
GET /: Data from the MongoDB database.

8. Deployment
This backend is deployed on Vercel.

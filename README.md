# Full-Stack Web Application Starter Template

A simple, modern full-stack web application template that uses **Next.js** on the frontend and **Python + FastAPI** on the backend.  
Instructions on customizing the template for a new project can be found in [NEW_PROJECT_GUIDE.md](./NEW_PROJECT_GUIDE.md).  
Created/organized by [Drew Peterson](https://github.com/drewpeterson99).  

## 🏗️ Architecture

- **Frontend**: Next.js 16 with TypeScript, Tailwind CSS, and Shadcn UI
- **Backend**: FastAPI (Python) with Pydantic for validation
- **Monorepo Structure**: Isolated frontend and backend folders for separate deployment

## 📁 Project Structure

```
.
├── backend/          # FastAPI backend
│   ├── api/         # API versioning
│   ├── app/         # business logic that is imported/used by the routers
│   ├── routers/     # Route handlers/API endpoints
│   ├── config.py    # Environment configuration
│   └── main.py      # Application entry point
├── frontend/         # Next.js frontend
│   ├── app/         # Next.js app router pages
│   ├── components/   # React components (Shadcn UI)
│   └── lib/         # Utilities and API client
└── .gitignore       # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites installed on your local machine
- Python 3.8+ (for backend)
- Node.js 18+ (for frontend)

### Backend Setup

1. Navigate to backend folder:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Mac/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file (copy from `.env.example`):
   ```bash
   # Copy .env.example to .env and configure
   ```

5. Run the server:
   ```bash
   python main.py
   # Or: uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

Backend will run on `http://127.0.0.1:8000` by default

### Frontend Setup

1. Navigate to frontend folder:
   ```bash
   cd frontend
   ```

2. Install dependencies (reads from the `package.json` file):
   ```bash
   npm install
   ```

3. Create `.env.local` file (copy from `.env.example`):
   ```bash
   # Copy .env.example to .env.local and configure API URL
   ```

4. Run development server:
   ```bash
   npm run dev
   ```

Frontend will run on `http://localhost:3000` by default

## 🔧 Configuration

### Backend Environment Variables

Create `backend/.env`:
```env
ENVIRONMENT=development
HOST=127.0.0.1
PORT=8000
CORS_ORIGINS=http://localhost:3000
API_V1_PREFIX=/api/v1
```

### Frontend Environment Variables

Create `frontend/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## 📚 Key Features

- ✅ Type-safe API with Pydantic models
- ✅ Environment variable management
- ✅ CORS configured for frontend-backend communication
- ✅ API versioning structure (`/api/v1`)
- ✅ Health check endpoints
- ✅ Shadcn UI component library
- ✅ Tailwind CSS for styling
- ✅ TypeScript throughout

## 🛠️ Development

### Backend
- API Documentation: `http://127.0.0.1:8000/docs` (Swagger UI)
- Health Check: `http://127.0.0.1:8000/api/v1/health` - Comprehensive health check endpoint for monitoring and deployment verification. Returns status, timestamp, environment, API version, service name, and system checks.
- Liveness Probe: `http://127.0.0.1:8000/api/v1/health/live` - Indicates the service is running. Used by Kubernetes and container orchestration.
- Readiness Probe: `http://127.0.0.1:8000/api/v1/health/ready` - Indicates the service is ready to accept traffic. Can be expanded to check database connections, external services, etc.

### Frontend
- Development server with hot reload
- TypeScript for type safety
- Tailwind CSS for styling
- **Home Page** (`/`): Landing page for the Real Estate Investment App featuring navigation to the properties page and API documentation, along with feature cards highlighting the app's capabilities (Browse Properties, Screen Investments, Make Decisions).
- **Properties Page** (`/properties`): Displays a grid of available real estate investment opportunities (sample data) fetched from the backend API. Shows property details including address, price, bedrooms, bathrooms, square feet, property type, and year built. Includes error handling for API connection issues.

## 📦 Dependencies

### Backend
- FastAPI - Web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- python-dotenv - Environment variables

### Frontend
- Next.js - React framework
- React - UI library
- TypeScript - Type safety
- Tailwind CSS - Styling
- Shadcn UI - Component library

## 🚢 Deployment

This template is designed for separate deployment:
- **Backend**: Deploy FastAPI to any Python hosting (Railway, Render, AWS, etc.)
- **Frontend**: Deploy Next.js to Vercel, Netlify, or any static hosting

Update CORS origins in backend `.env` to match your frontend URL in production.

## 📝 License

[Drew Peterson - 2026]
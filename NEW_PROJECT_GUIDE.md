# Customization Guide

This guide helps you customize this template for your new project.

## Step 1: Create a Copy of the Template Repository

Use GitHub's "Import repository" feature to create a copy of this repository under your own account:
   - Go to GitHub and click the "+" icon in the top right, then select "Import repository"
   - Enter the URL of this template repository
   - Choose a name for your new repository
   - Note: This process is different from forking, as the new repository will have no link to the original. Also note that you can't fork your own repository in GitHub anyway.

## Step 2: Initial Repo Setup

Follow instructions in [README.md](./README.md)

## Step 3: Update Project Information

- Rename the project folder to your project name
- Update `frontend/package.json`:
   - Change `name` and `version` if needed
- Update `backend/main.py`:
   - Change API `title`, `description` and `version` if needed
- Update `README.md` with your project-specific information

## Step 4: Customize Backend

- Add your routes in `routers/` folder (create new files like `routers/users.py`, etc.)
- Update `config.py` - Add new environment variables if needed
- Remove sample routes (`routers/properties.py`)
- Update `api/v1/router.py` - Remove sample router includes, add your own

## Step 5: Customize Frontend

- Update `app/layout.tsx` - Change metadata (title, description)
- Update `app/page.tsx` - Customize home page content
- Remove sample pages (`app/properties/`)
- Update `lib/api.ts` - Remove sample API functions, add your own
- Add new pages in `app/` folder as needed

## Step 6: Clean Up Template Documentation

After customizing, you may want to:
- Replace `TEMPLATE_README.md` with your own `README.md` (copy and customize)
- Remove `CUSTOMIZATION_GUIDE.md` if not needed for your project

## Step 7: Environment Configuration

### Backend
Update `backend/.env` with your specific values:
- `ENVIRONMENT` - Set to `production` when deploying
- `CORS_ORIGINS` - Add your production frontend URL(s)
- Add any additional environment variables your app needs

### Frontend
Update `frontend/.env.local`:
- `NEXT_PUBLIC_API_URL` - Point to your production backend URL when deploying

## Next Steps

- Set up database (if needed)
- Add authentication
- Configure deployment
- Set up CI/CD

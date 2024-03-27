#!/bin/bash

# Change directory to Dynamic_Web_Application/
cd ..

# Set up virtual environment
python3 -m venv venv
echo ""
echo "Virtual environment is created: venv"

# Activate virtual environment
source venv/bin/activate
echo ""

# Verify if the virtual environment is activated
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment is activated: $VIRTUAL_ENV"
else
    echo "Virtual environment is not activated."
fi
echo ""

# Install Django
echo "Installing django:"
echo ""
pip install django
echo ""

# Navigate to the Dynamic_Web_Application/Project directory
cd Project/ || { echo "Project directory not found"; exit 1; }

# Create migration file
echo "Creating migration file:"
echo ""
python3 manage.py makemigrations website
echo ""

# Apply migrations
echo "Applying migrations:"
echo ""
python3 manage.py migrate
echo ""
#!/bin/bash

# Change directory to Dynamic_Web_Application/
cd ..

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

# Navigate to the Dynamic_Web_Application/Project directory
cd Project/ || { echo "Project directory not found"; exit 1; }

# Start Django server
echo "Starting Django server:"
echo ""
python3 manage.py runserver
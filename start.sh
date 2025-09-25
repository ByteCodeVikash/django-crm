#!/bin/bash

# Run migrations
python manage.py migrate --noinput

# Collect static files  
python manage.py collectstatic --noinput

# Create superuser if environment variables are set
if [ "$CREATE_SUPERUSER" = "true" ]; then
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"
fi

# Start gunicorn server
exec gunicorn --bind 0.0.0.0:$PORT webcrm.wsgi:application

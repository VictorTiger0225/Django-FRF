##Django Cloud Messaging App

This Django application provides a cloud messaging solution for sending push notifications and messages to users on various platforms. With this app, you can easily integrate cloud messaging capabilities into your Django project and send targeted notifications to your users.

###Features

- Send push notifications to iOS and Android devices
- Send SMS messages to mobile numbers
- Web-based dashboard for managing notifications and users
- Targeted messaging based on user segments or custom filters
- Easy integration with existing Django projects

###Installation

#Clone the repository:

git clone https://github.com/VictorTiger0225/Django-FRF.git

#Change into the project directory:

cd Django-FR

#Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

#Install the required dependencies:

pip install -r requirements.txt

#Set up the database:

python manage.py migrate

#Start the development server:

python manage.py runserver
Access the web-based dashboard at http://localhost:8000/admin and log in with your superuser credentials.

##Usage

- Create a new project in the dashboard and configure the necessary settings, such as API keys for push notifications and SMS gateways.
- Create user segments or custom filters to target specific groups of users for notifications.
- Use the provided APIs or admin interface to send push notifications or SMS messages to your users.
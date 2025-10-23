# Monthly Coffee Club

A Django web application that helps you discover and track your monthly coffee roaster subscriptions. The app randomly selects a coffee roaster each month based on weighted tags, allows you to rate and review your coffee experiences, and maintains a gallery of all available roasters.

## Features

- **Random Roaster Selection**: Uses a weighted algorithm to randomly pick your next monthly coffee roaster
- **Rating System**: Rate and review each roaster after trying their coffee
- **Coffee Roaster Gallery**: Browse all available roasters with images and details
- **Tag-Based Weighting**: Roasters are weighted by tags (Premium, Local, etc.) to influence selection probability
- **Admin Interface**: Easy management of roasters, ratings, and tags through Django admin
- **Responsive Design**: Beautiful, mobile-friendly interface with smooth animations

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/monthlyCoffee.git
cd monthlyCoffee
```

### 2. Create a Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
cd coffeeclub
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
# Run migrations to create database tables
python manage.py migrate

# Create a superuser account (for admin access)
python manage.py createsuperuser
```

Follow the prompts to create your admin username and password.

### 5. Add Coffee Roasters (Required)

Before using the app, you need to add at least one coffee roaster and the "Last Time" tag through the admin interface.

```bash
# Start the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

**Required Setup:**
1. **Create Tags**: Add a tag called "Last Time" with value `1.0` (required for tracking current roaster)
2. **Add Roasters**: Add your favorite coffee roasters with names, websites, and images
3. **Assign Tags**: Give each roaster at least one tag, and assign "Last Time" to one roaster to get started

Optional tags you can create:
- Premium (value: 3.0) - Higher chance of selection
- Local (value: 2.5) - Medium-high chance
- Standard (value: 1.5) - Medium chance

Higher tag values = higher probability of being selected.

## Usage

### Running the Application

```bash
cd coffeeclub
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### Choosing Your Monthly Coffee

1. **View Current Month**: The homepage shows your current monthly roaster (tagged with "Last Time")
2. **Rate Previous Coffee**: Click "Rate the Coffee" to leave a score and review
3. **Choose Next Roaster**: Click "Choose Next Roaster!" to randomly select next month's coffee
4. **Browse Gallery**: Scroll down to see all available roasters in the gallery

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` to:
- Add/edit/delete coffee roasters
- Manage tags and their weights
- View all ratings and reviews
- Upload roaster images

## Project Structure

```
monthlyCoffee/
├── coffeeclub/                 # Django project root
│   ├── coffeeclub/            # Project configuration
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py            # Main URL configuration
│   │   └── wsgi.py            # WSGI configuration
│   ├── monthlycoffee/         # Main application
│   │   ├── models/            # Database models
│   │   │   ├── coffee_roaster.py
│   │   │   ├── rating.py
│   │   │   └── tag.py
│   │   ├── templates/         # HTML templates
│   │   ├── static/            # CSS, JS, images
│   │   ├── views.py           # View functions
│   │   ├── urls.py            # App URL patterns
│   │   └── admin.py           # Admin configuration
│   ├── manage.py              # Django management script
│   └── requirements.txt       # Python dependencies
└── README.md
```

## Technologies Used

- **Django 5.2.4**: Web framework
- **SQLite**: Database
- **Pillow**: Image processing
- **Gunicorn**: Production WSGI server
- **HTML5 UP Story**: Frontend template

## How the Random Selection Works

The app uses a weighted random selection algorithm:

1. Each roaster has tags with numeric values (e.g., Premium = 3.0, Local = 2.5)
2. A roaster's total weight is the sum of all its tag values
3. Higher weights = higher probability of being selected
4. The "Last Time" tag is transferred to the newly selected roaster

## Troubleshooting

### Page is blank
- Make sure you've added at least one roaster through the admin panel
- Ensure at least one roaster has the "Last Time" tag
- Check that static files are loading (CSS/JS)

### Images not displaying
- Verify images are uploaded through the admin interface
- Check file permissions in the static/images directory

### Database errors
- Run `python manage.py migrate` to ensure all migrations are applied
- If using the provided db.sqlite3, make sure it's in the coffeeclub directory

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Frontend template by [HTML5 UP](https://html5up.net)
- Built with Django

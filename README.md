# TaskFlow - Modern Django Todo App 🎯

A beautiful, modern todo list application built with Django 4.2 and Tailwind CSS 3.x. Features a sleek UI, email notifications, and guest login functionality.

![Django](https://img.shields.io/badge/Django-4.2.16-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-38bdf8.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎨 **Modern UI** - Beautiful gradient design with Tailwind CSS 3.x
- 📧 **Email Notifications** - Automated password delivery and reset emails with HTML templates
- 👤 **Guest Login** - Try the app without signing up
- ✅ **Task Management** - Create, complete, and delete tasks
- 📱 **Responsive Design** - Works seamlessly on all devices
- 🔒 **Secure Authentication** - User registration with email verification
- 🎯 **Task Statistics** - View active tasks and productivity metrics
- 🌊 **Masonry Layout** - Dynamic card layout that adapts to content

## � Quick Start

### Prerequisites

- Python 3.11+
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Amaan6674/To-Do-List.git
cd To-Do-List
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your email credentials
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser!

## 📧 Email Configuration

The app uses Maileroo for sending emails. Update your `.env` file:

```env
EMAIL_HOST_USER=your_maileroo_username
EMAIL_HOST_PASSWORD=your_maileroo_api_key
EMAIL_FROM=noreply@yourdomain.maileroo.org
```

## 🎮 Guest Login

Try the app without creating an account:

- Click "Continue as Guest" on the login page
- Username: `guest_demo`
- Password: `demo123`

## 🌐 Deployment

### Railway / Render / PythonAnywhere

1. **Set environment variables:**

   - `SECRET_KEY` - Django secret key
   - `DEBUG` - Set to `False` in production
   - `ALLOWED_HOSTS` - Your domain
   - `EMAIL_HOST_USER` - Maileroo username
   - `EMAIL_HOST_PASSWORD` - Maileroo API key
   - `EMAIL_FROM` - Sender email
   - `DATABASE_URL` - PostgreSQL connection string (auto-provided)

2. **Deploy:**
   - Connect your GitHub repository
   - Set environment variables
   - Deploy!

## 📁 Project Structure

```
todo-webapp/
├── auapp/              # Authentication app
│   ├── templates/      # Login, signup, password reset
│   └── views.py        # Auth logic & email handling
├── eoapp/              # Todo app
│   ├── templates/      # Task views
│   ├── models.py       # Task model
│   └── views.py        # Task logic
├── templates/          # Base template
├── todo_project/       # Project settings
├── requirements.txt    # Dependencies
├── Procfile           # Production server config
└── runtime.txt        # Python version
```

## �️ Tech Stack

- **Backend:** Django 4.2.16 LTS
- **Frontend:** Tailwind CSS 3.x, Font Awesome 6.4.0
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Email:** Maileroo SMTP
- **Deployment:** Gunicorn, WhiteNoise

## 📝 Features in Detail

### Task Management

- Create tasks with rich text descriptions
- Mark tasks as complete/incomplete (toggle)
- Delete tasks with confirmation
- View task creation time
- Masonry grid layout for optimal space usage

### Authentication

- User registration with auto-generated passwords
- Beautiful HTML email templates
- Password reset functionality
- Remember me (30-day sessions)
- Guest login for demo

### UI/UX

- Gradient backgrounds and hover effects
- Responsive mobile menu
- Sticky navigation
- Empty state illustrations
- Loading animations
- Modern card designs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## � Author

**Amaan**

- GitHub: [@Amaan6674](https://github.com/Amaan6674)
- LinkedIn: [Amaan](https://linkedin.com/in/amaan6674)

## 🙏 Acknowledgments

- Built with Django
- Styled with Tailwind CSS
- Icons by Font Awesome
- Email service by Maileroo

---

Made with ❤️ by Amaan

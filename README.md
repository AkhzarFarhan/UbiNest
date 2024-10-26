# UbiNest - Family Task and Finance Management System

UbiNest is a web application designed to enhance family organization and productivity. It offers tools for managing tasks, finances, goals, and communications all in one place. Perfect for families who want a streamlined approach to organizing shared responsibilities and financial tracking.

## Features

- **User Profiles**: Each family member can set up a profile with a custom role and bio, and add an avatar for easy identification.
- **Task Management**: Assign, track, and update tasks for each family member. Task details include title, description, assigned person, status, due date, and reward.
- **Financial Tracking**: Log income and expenses, and view recent transactions to monitor family finances.
- **Savings Goals**: Set up and monitor savings goals, track progress, and visualize how close you are to achieving family financial goals.
- **Group & Individual Chat**: Send messages to the family group or start one-on-one chats to keep everyone in sync.
- **Event Calendar**: Manage family events with a shared calendar, listing important dates and event details.
  
## Getting Started

### Prerequisites
- **Python 3.8+**
- **Django 4.x**
- **SQLite** (default database; can be configured for PostgreSQL/MySQL)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/UbiNest.git
   cd UbiNest
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create the database:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```bash
   python manage.py runserver

   ```
6. Access the application at:
   ```
   http://127.0.0.1:8000
   ```


### Usage
- **Login:** Log in with your superuser or registered account.
- **Dashboard:** View and manage your tasks, transactions, goals, events, and messages.
- **Task Management:** Assign tasks, update status, and set rewards for completion.
- **Finance:** Log transactions, set savings goals, and monitor financial health.
- **Messaging:** Communicate within the family through group or private chat.


### Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your updates.

- Fork the repository.
- Create a new branch: git checkout -b feature/YourFeature
- Commit your changes: git commit -m 'Add some feature'
- Push to the branch: git push origin feature/YourFeature
- Open a pull request.
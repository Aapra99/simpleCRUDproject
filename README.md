# Simple CRUD Project with Django

1. **Clone the repo:**
      ```bash
      git clone https://github.com/Aapra99/simpleCRUDproject.git
      cd simpleCRUDproject
      
2. **Install dependencies:**
      ```bash
      pip install -r requirements.txt

3. **Edit settings.py file:**
      ```bash
      DB_NAME=formkodata
      DB_USER=your_username
      DB_PASSWORD=your_password
      DB_HOST=localhost
      DB_PORT=port_number
      
4. **Run the server:**
      ```bash
      python manage.py runserver
     
This project uses environment variables for Database credentials.

All sensitive data is stored in `.env` (ignored by Git).


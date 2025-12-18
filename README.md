<p align="center">
  <h2 align="center">DJecommerce – Django E-Commerce Website</h2>
  <p align="center">
    A simple and functional e-commerce web application built using Django.
  </p>
</p>

---

## 📌 Project Overview

DJecommerce is a full-stack e-commerce web application developed using Django.  
The project allows users to browse products, filter them by category, add items to a cart, and complete purchases using Stripe payment integration.  
It is built as a learning and internship-level project to understand real-world Django development.

---

## 🚀 Features

- User authentication (Login / Signup) using Django Allauth  
- Product listing with category-wise filtering  
- Add to cart and remove from cart functionality  
- Quantity management for cart items  
- Checkout and payment integration using Stripe  
- Admin panel for managing products, categories, and orders  
- Responsive UI built with Bootstrap  

---

## 🛠 Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **Authentication:** Django Allauth  
- **Forms:** Django Crispy Forms  
- **Payments:** Stripe  

---

## 📂 Project Structure
djecommerce/
├── core/
├── djecommerce/
│ └── settings/
├── templates/
├── static_in_env/
├── manage.py
├── requirements.txt
└── db.sqlite3


## ⚙️ Installation & Setup

Make sure Python is installed on your system.

### 1️⃣ Clone the repository
```bash
git clone https://github.com/devpatel1849/ecommerce-master.git
cd ecommerce-master

###2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver

📚 Learning Outcomes

Understanding Django project structure and settings management

Working with Django ORM and model relationships

Implementing authentication using Django Allauth

Integrating third-party services like Stripe

Handling real-world debugging and dependency issues

🔮 Future Improvements

Product reviews and ratings

Wishlist functionality

Order tracking system

Deployment on cloud platforms (Render / AWS)

👨‍💻 Author

Dev Patel
Computer Engineering Student
GitHub: https://github.com/devpatel1849

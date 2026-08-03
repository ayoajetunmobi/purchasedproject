# 🛒 Purchased — E-Commerce & Service Marketplace Platform

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Redis](https://img.shields.io/badge/Redis-7.0+-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![Celery](https://img.shields.io/badge/Celery-5.3+-37814A?style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

> **A feature-rich e-commerce and classified advertising platform that allows sellers to list products/services via integrated payments, communicate directly with customers, and leverage automated background email marketing.**

---

## 📖 Overview

**Purchased** is a modern e-commerce marketplace platform built to connect sellers, service providers, and buyers. The platform allows users to post advertisements and product listings by securely checking out through an integrated **Payment Gateway**. 

To drive user engagement and recurring traffic, **Purchased** features a powerful background messaging engine powered by **Celery**, **Redis**, and **SMTP**, which automatically schedules and dispatches targeted email marketing campaigns without interrupting the user browsing experience.

---

## ✨ Key Features

### 📣 1. Ad & Product Listing Engine
* **Ad Submission & Management:** Users can post their products, services, descriptions, pricing, and media assets.
* **Integrated Payment Gateway:** Secure payment processing requiring users to pay listing fees or boost ads before publication.
* **Category & Service Filtering:** Seamless discovery tools allowing buyers to search and filter through listed services and physical goods.

### 🤝 2. Direct Buyer-to-Seller Communication
* **Service Inquiries:** Integrated messaging and contact options allowing buyers to reach sellers directly for quotes or service details.
* **User Accounts & Portals:** Merchant and buyer dashboards to manage posted ads, track active listings, and review account activity.

### 📧 3. Automated Background Email Marketing
* **Asynchronous Campaign Execution:** Uses **Celery** and **Redis** to send high-volume email marketing campaigns via **SMTP** in the background.
* **Automated Customer Engagement:** Periodic background tasks send newsletter updates, ad performance summaries, and promotional notifications.

---

## 🏗 System Architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│                       Frontend Interface                        │
│                (HTML5 / CSS3 / JavaScript / UI)                 │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 v  (HTTP / HTTPS)
┌────────────────────────────────┴────────────────────────────────┐
│                        Django Web Engine                        │
│        (Routing, Auth, Business Logic & Payment Handlers)       │
└──────────────┬─────────────────┬──────────────────┬─────────────┘
               │                 │                  │
               v                 v                  v
┌──────────────────────┐ ┌───────────────┐ ┌──────────────────────┐
│   Payment Gateway    │ │  PostgreSQL / │ │    Celery Worker     │
│ (Ad Listing Checkout)│ │  SQLite DB    │ │  (Background Tasks)  │
└──────────────────────┘ └───────────────┘ └──────────┬───────────┘
                                                      │
                                                      v
                                           ┌──────────────────────┐
                                           │     Redis Broker     │
                                           │  (Queue / Scheduler) │
                                           └──────────┬───────────┘
                                                      │
                                                      v
                                           ┌──────────────────────┐
                                           │    SMTP Email Server │
                                           │ (Marketing Campaigns)│
                                           └──────────────────────┘


| Domain | Technologies Used |
| :--- | :--- |
| **Backend** | Python, Django |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Task Queue & Caching** | Celery, Redis |
| **Email Services** | SMTP Integration |
| **Database** | SQLite (Development) / PostgreSQL |
| **Payments** | External Payment Gateway API |

### Flow Breakdown
1. **Ad Creation:** The seller creates an ad, processes payment via the integrated payment gateway, and upon verification, the ad goes live.
2. **Product Browsing & Inquiry:** Visitors search products and send inquiries directly to the listing owner.
3. **Automated Marketing:** Asynchronous tasks are pushed to **Redis** and picked up by **Celery workers**, which handle mass email communications without blocking main request threads.

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites

Ensure you have the following installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [Redis Server](https://redis.io/download/)
- Git

---

### Installation Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ayoajetunmobi/purchasedproject.git
   cd purchasedproject


# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

SECRET_KEY=your_django_secret_key
DEBUG=True

# Database Settings (if applicable)
DATABASE_URL=sqlite:///db.sqlite3

# Payment Gateway Settings
PAYMENT_GATEWAY_PUBLIC_KEY=your_public_key
PAYMENT_GATEWAY_SECRET_KEY=your_secret_key

# Redis & Celery Config
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# SMTP Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

⚙️ Running the Application

To run the full stack including background tasks, execute the following commands in separate terminal windows:
1. Start Redis Server
redis-server
celery -A purchasedproject worker --loglevel=info
python manage.py runserver
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

👤 Author
    Ayomide Ajetunmobi - GitHub Profile

📄 License

This project is licensed under the MIT License.




![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![API](https://img.shields.io/badge/API-FF6C37?style=for-the-badge&logo=fastapi&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

# Khetsing Market API: Local Produce & Gig Marketplace

![Data Source](https://img.shields.io/badge/Data%20Source-Khetsi%20Market%20API-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

A Django-powered API platform for authentic local goods (farm produce, crafts) and quick gig opportunities in Lesotho to help during hard times.

---

## Key Features

- **Real-Time Price Fetching**: Automated API calls to Khetsi Market’s endpoints.

### For Sellers
- **Produce Listings**: Sell homegrown crops, handmade goods.
- **Gig Hub**: Offer services (plumbing, deliveries, etc.).
- **Trust System**: Verified seller badges + reviews (WIP).

### For Buyers
- **Hyperlocal Discovery**: Find fresh produce within 5km (WIP).
- **Gig Matching**: Hire help for short-term tasks.

### For All
- **Mobile-First**: Accessible via low-bandwidth.
- **Cashless Payments**: Mobile money integration (WIP, Mpesa djara integration soon).

---

## Technologies Used

### Core Stack
- **Backend**: Python 3.10+, Django 4.2
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: 
  - `allauth` (Google OAuth, email/password)
  - JWT via `rest_framework.authtoken`
- **Database**: PostgreSQL (production), SQLite (development)
- **Data Tools**: Pandas, NumPy, SQLAlchemy

### APIs & Integrations
- **Internal**: RESTful endpoints with DRF
- **External**: Requests, WebSocket (live updates)
- **CORS**: `django-cors-headers` for cross-origin requests

### Infrastructure
- **Version Control**: GitHub (CI/CD via Actions)
- **Security**: CSRF middleware, `django-security`

### Key Django Modules
```python
INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
    'allauth',  # Multi-auth (Google + email)
    'api',      # Custom user model (KhetsingUser)
]

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/khetsi-market-api.git
cd khetsi-market-api

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env  # Add your API keys

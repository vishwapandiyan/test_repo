"""Application configuration - contains security issues."""

import os

# SECURITY ISSUE: Hardcoded credentials
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "admin123",  # Weak password
    "database": "production_db"
}

# SECURITY ISSUE: API keys in source code
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "your_stripe_secret_key_here")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "your_sendgrid_api_key_here")

# SECURITY ISSUE: Weak encryption key
ENCRYPTION_KEY = "1234567890123456"  # Too short and predictable

def get_database_connection():
    """Get database connection with hardcoded credentials."""
    import psycopg2
    return psycopg2.connect(**DATABASE_CONFIG)


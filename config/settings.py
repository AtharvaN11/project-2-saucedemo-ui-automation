"""
Environment configuration.

Real projects test the same app in several places (dev, staging, prod).
Here we keep each environment's settings in one dictionary so tests never
hard-code a URL. Choose one with:  pytest --env staging
"""

ENVIRONMENTS = {
    "prod": {"base_url": "https://www.saucedemo.com"},
    # Same site used as a stand-in so you can see how switching works.
    "staging": {"base_url": "https://www.saucedemo.com"},
}

DEFAULT_ENV = "prod"

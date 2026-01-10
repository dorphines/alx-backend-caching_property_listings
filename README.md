# ALX Backend Caching Property Listings

This project implements a Django-based property listing application with Redis caching strategies.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repo_url>
    cd alx-backend-caching_property_listings
    ```

2.  **Environment Setup**:
    Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Docker Services**:
    Start PostgreSQL and Redis:
    ```bash
    docker-compose up -d
    ```

4.  **Database Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

## Caching Strategies implemented

### 1. View-Level Caching
-   **File**: `properties/views.py`
-   **Method**: Used `@cache_page(60 * 15)` decorator on `property_list` view.
-   **Effect**: Caches the entire HTTP response for 15 minutes.

### 2. Low-Level Queryset Caching
-   **File**: `properties/utils.py`
-   **Method**: `get_all_properties()` checks Redis for 'all_properties' key.
-   **Logic**: If cache miss, fetches from DB, forces evaluation (list conversion), and sets cache for 1 hour.
-   **Usage**: The view uses this utility to fetch data.

### 3. Cache Invalidation
-   **File**: `properties/signals.py`
-   **Method**: Uses `post_save` and `post_delete` signals on `Property` model.
-   **Effect**: Deletes 'all_properties' key from cache whenever a property is added, updated, or deleted.

### 4. Metrics
-   **File**: `properties/utils.py`
-   **Method**: `get_redis_cache_metrics()` retrieves hits/misses from Redis INFO and logs them.

## Configuration
-   **Database**: PostgreSQL (via `psycopg2-binary`)
-   **Cache Backend**: `django-redis`
# alx-backend-caching_property_listings

# Django Loan PDF Generator

This is a Django REST Framework project that allows users to submit loan details via an API and generates a PDF report using **wkhtmltopdf**.

## Features
- **REST API** for loan submission
- **PDF Generation** using `pdfkit`
- **Django Rest Framework (DRF)**
- **SQLite Database** for storing loan records

## Installation

### 1. Clone the Repository
```bash
 git clone https://github.com/your-repo.git
 cd project
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install wkhtmltopdf
- Download `wkhtmltopdf` from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
- Install and locate the binary path
- Update `settings.py` with the correct path:
```python
PDFKIT_CONFIG = pdfkit.configuration(
    wkhtmltopdf=r"C:\\path\\to\\wkhtmltopdf.exe"
)
```

## Database Migration
```bash
python manage.py migrate
```

## Running the Server
```bash
python manage.py runserver
```

## API Endpoints
### Submit Loan & Generate PDF
**POST** `/api/generate-pdf/`
#### Request Body (JSON):
```json
{
    "name": " john",
    "email": "john@example.com",
    "loan_amount": 5000.00
}
```
#### Response:
- Success: Returns a PDF file
- Error: Returns validation errors

## Project Structure
```
project/
│── pdf_generator/
│   ├── migrations/
│   ├── templates/
│   │   ├── pdf_template.html
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── project/
│   ├── settings.py
│   ├── urls.py
│── db.sqlite3
│── manage.py
│── requirements.txt
│── README.md
```




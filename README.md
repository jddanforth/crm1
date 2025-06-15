# Simple CRM

This repository contains a minimal web-based CRM using Flask and SQLite.
It supports viewing and adding contacts. Email fetching and AI-based contact
parsing can be added via `crm/email_utils.py`.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python run.py
   ```
3. Open `http://localhost:5000` in your browser.

Configuration for IMAP email integration can be set via environment variables or
Flask configuration (see `crm/email_utils.py`).

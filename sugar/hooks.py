# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "sugar"
app_title = "Erpnext Sugar Mill Cane Crushing Ledger"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Sugar Mill Cane Crushing Ledger for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/sugar/css/sugar.bundle.css"
app_include_js = "/assets/sugar/js/sugar.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "sugar.engine.on_document_submit",
        "on_cancel": "sugar.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "sugar.engine.daily_scheduled_sync"
    ]
}

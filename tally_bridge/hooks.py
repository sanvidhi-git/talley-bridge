app_name = "tally_bridge"
app_title = "Tally Bridge"
app_publisher = "Sanvidhi Technologies"
app_description = "Configurable ERPNext to TallyPrime integration with live sync and period export."
app_email = "info@sanvidhi.example"
app_license = "MIT"
app_version = "2.0.0"

required_apps = ["frappe", "erpnext"]

# V16: app_icon / app_color removed; icon set via Workspace fixture

doc_events = {
    "Customer": {
        "after_insert": "tally_bridge.sync.enqueue.on_document_event",
        "on_update": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Supplier": {
        "after_insert": "tally_bridge.sync.enqueue.on_document_event",
        "on_update": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Item": {
        "after_insert": "tally_bridge.sync.enqueue.on_document_event",
        "on_update": "tally_bridge.sync.enqueue.on_document_event",
    },
    "UOM": {
        "after_insert": "tally_bridge.sync.enqueue.on_document_event",
        "on_update": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Account": {
        "after_insert": "tally_bridge.sync.enqueue.on_document_event",
        "on_update": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Address": {
        "on_update": "tally_bridge.sync.enqueue.on_address_update",
    },
    "Sales Invoice": {
        "on_submit": "tally_bridge.sync.enqueue.on_document_event",
        "on_cancel": "tally_bridge.sync.enqueue.on_document_event",
        "on_update_after_submit": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Purchase Invoice": {
        "on_submit": "tally_bridge.sync.enqueue.on_document_event",
        "on_cancel": "tally_bridge.sync.enqueue.on_document_event",
        "on_update_after_submit": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Payment Entry": {
        "on_submit": "tally_bridge.sync.enqueue.on_document_event",
        "on_cancel": "tally_bridge.sync.enqueue.on_document_event",
    },
    "Journal Entry": {
        "on_submit": "tally_bridge.sync.enqueue.on_document_event",
        "on_cancel": "tally_bridge.sync.enqueue.on_document_event",
    },
}

after_sync = "tally_bridge.sync.service.after_sync"

fixtures = [
    {
        "doctype": "Workspace",
        "filters": [["name", "=", "Tally Bridge"]],
    },
]

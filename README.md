# Tally Bridge

ERPNext v16 custom app to sync accounting vouchers and master data to TallyPrime via its local XML/TDL gateway.

## Features

- **Live sync** — Sales Invoices, Purchase Invoices, Payment Entries, Journal Entries are queued and pushed to Tally on submit/cancel
- **Master sync** — Customers, Suppliers, Items, UOMs, Accounts synced as Tally Ledgers/Stock Items/Units with idempotent remote-ID tracking
- **Queue-based** — Never blocks ERPNext submit; background agent polls the queue; automatic retry with exponential back-off (5 attempts max)
- **Period export** — Bulk backfill date ranges via Tally Export Job
- **Reconciliation** — Compare ERPNext and Tally records via Tally Reconciliation Job
- **Console page** — Live dashboard at `/tally-bridge-console`

## Installation

```bash
# From your frappe-bench directory
bench get-app https://github.com/sanvidhi-git/talley-bridge
bench install-app tally_bridge
```

## Setup

1. Go to **Tally Bridge → Tally Connection Settings**
2. Set your Tally host URL (e.g. `http://localhost:9000`), company name, and ERPNext company
3. Enable the connection
4. Start the agent: `python agent/main.py --config agent/config.yaml`

## ERPNext v16

This app targets ERPNext/Frappe v16. Key V16 changes applied:
- `pyproject.toml` with `flit_core` build backend (PEP 517)
- `Python >=3.14,<3.15`
- `[tool.bench.frappe-dependencies]` for Frappe/ERPNext deps
- DocType JSON: `doctype_version: 2`, `migration_hash: ""`; `engine` field removed
- Module icon via **Workspace** JSON fixture (not `app_icon` in hooks.py)

## Architecture

```
ERPNext event (on_submit/on_cancel)
  └─► enqueue.py — snapshot doc, insert Tally Sync Queue record
         └─► agent/main.py — polls queue, builds XML payload, POSTs to Tally
                  └─► Tally Sync Log — audit record per attempt
```

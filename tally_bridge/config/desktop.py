from frappe import _


def get_data():
    return [
        {
            "module_name": "tally_bridge",
            "category": "Modules",
            "label": _("Tally Bridge"),
            "color": "#2490EF",
            "icon": "octicon octicon-sync",
            "type": "module",
            "hidden": 0,
        }
    ]

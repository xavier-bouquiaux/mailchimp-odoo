# Copyright 2021 Xavier Bouquiaux
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Odoo-Campaign",
    "summary": (
        "Sync your mailchimp campaigns in your odoo database "
    ),
    "author": "Xavier Bouquiaux",
    "website": "https://https://github.com/xavier-bouquiaux/mailchimp-odoo",
    "version": "14.0.1.0.1",
    "development_status": "Production/Stable",
    "license": "AGPL-3",
    "installable": True,
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/odoo-campaign.xml",
        "wizards/credential_wizard.xml",
    ],
    "external_dependencies": {
        "python": [
            "mailchimp_marketing",
        ],
    },
    "maintainers": ["xavier-bouquiaux"],
}
.. _resource-serviceescalation:

serviceescalation
===================

.. csv-table::
   :header: "Parameter", "Type", "Required", "Default", "Data relation"

   "use", "objectid", "", "", ":ref:`serviceescalation <resource-serviceescalation>`"
   "name", "string", "", "", ""
   "definition_order", "integer", "", "100", ""
   "contacts", "objectid", "", "", ":ref:`contact <resource-contact>`"
   "last_notification_time", "integer", "", "", ""
   "escalation_options", "list", "", "['d', 'u', 'r', 'w', 'c']", ""
   "register", "boolean", "", "True", ""
   "contact_groups", "objectid", "", "", ":ref:`contactgroup <resource-contactgroup>`"
   "notification_interval", "integer", "", "30", ""
   "hostgroup_name", "string", "", "", ""
   "escalation_period", "string", "", "", ""
   "host_name", "string", "", "", ""
   "first_notification_time", "integer", "", "", ""
   "service_description", "string", "", "", ""
   "first_notification", "integer", "", "", ""
   "last_notification", "integer", "", "", ""
   "imported_from", "string", "", "unknown", ""

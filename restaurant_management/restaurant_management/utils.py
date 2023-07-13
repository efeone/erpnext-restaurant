import frappe

@frappe.whitelist()
def update_customer_in_table_order(table_order, customer):
    if frappe.db.exists('Table Order', table_order):
        frappe.db.set_value('Table Order', table_order, 'customer', customer)
        frappe.db.commit()

@frappe.whitelist()
def create_new_customer(customer_name, mobile_number=None):
    customer_doc = frappe.new_doc('Customer')
    customer_doc.customer_name = customer_name
    if mobile_number:
        customer_doc.mobile_number = mobile_number
    customer_doc.insert(ignore_permissions=True)
    return customer_doc.name

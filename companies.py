
import webbrowser

class Company():
	def __init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent):
		self.description = company_description
		self.street = company_address_street
		self.city = company_address_city
		self.suite = company_address_suite
		self.zip = company_address_zip
		self.state = company_address_state
		self.url = company_url
		self.logo = company_logo
		self.billing_type = billing_type
		self.retainage_percent = retainage_percent
		
	
	BILLING_TYPE = ["requisition", "invoice", "other"]
	
	def show_website(self):
		webbrowser.open(self.url)
		

class Subcontractor(Company):
	def __init__(self, project_manager, trade):
		Company.__init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent)
		self.project_manager = project_manager
		self.trade = trade


class Material_Supplier(Company):
	def __init__(self, material_type, deposit_required, primary_contact):
		Company.__init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent)
		self.material_type = material_type
		self.deposit_required = deposit_required
		self.primary_contact = primary_contact
		
class Consultant(Company):
	def __init__(self, professional_service_type, primary_contact, project_billing_phase):
		Company.__init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent)
		self.professional_service_type = professional_service_type
		self.primary_contact = primary_contact
		self.project_billing_phase = project_billing_phase
	
	

import webbrowser


"""
Add following functions to Company class--
1. print_all_attributes
2. open company url
3. display company logo if available
4. print key billing information (billing_type, retainage percent, company name)
5. print company profile (with company name, description, company_logo, company_url)
"""

class Company():
	def __init__(self, name, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent):
		self.name = name
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
		if hasattr(self, 'url') and self.url != "":
			webbrowser.open(self.url)
		else: 
			print "PLEASE provide website address"
			web_address = raw_input("Type address here: ")
			webbrowser.open(web_address)
		
	
	def company_profile(self):
		print self.name + " specializes in " + self.description +". " + "Find more information at the following link:  " + self.url
	
	def print_all_attributes(self):
		if hasattr(self, 'name'):
			print self.name
		if hasattr(self, 'description'):
			print self.description
		if hasattr(self, 'street'):
			print self.street
		if hasattr(self, 'city'):
			print self.city
		if hasattr(self, 'suite'):
			print self.suite
		if hasattr(self, 'zip'):
			print self.zip
		if hasattr(self, 'state'):
			print self.state
		if hasattr(self, 'url'):
			print self.url
		if hasattr(self, 'logo'):
			print self.logo
		if hasattr(self, 'billing_type'):
			print self.billing_type
		if hasattr(self, 'retainage_percent'):
			print self.retainage_percent
		if hasattr(self, 'project_manager'):
			print self.project_manager
		if hasattr(self, 'trade'):
			print self.trade
		if hasattr(self, 'material_type'):
			print self.material_type
		if hasattr(self, 'deposit_required'):
			print self.deposit_required
		if hasattr(self, 'primary_contact'):
			print self.primary_contact
		if hasattr(self, 'project_billing_phase'):
			print self.project_billing_phase
		if hasattr(self, 'professional_service_type'):
			print self.professional_service_type
		print '\n'


class Subcontractor(Company):
	def __init__(self, name, project_manager, trade, description, street, city, suite, zip, state, url, logo, billing_type, retainage_percent):
		Company.__init__(self, name, description, street, city, suite, zip, state, url, logo, billing_type, retainage_percent)
		self.project_manager = project_manager
		self.trade = trade
	


class Material_Supplier(Company):
	def __init__(self, name, material_type, deposit_required, primary_contact, description, street, city, suite, zip, state, url, logo, billing_type, retainage_percent):
		#Company.__init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent)
		Company.__init__(self, name, description, street, city, suite, zip, state, url, logo, billing_type, retainage_percent)
		self.material_type = material_type
		self.deposit_required = deposit_required
		self.primary_contact = primary_contact
		
class Consultant(Company):
	def __init__(self, name, professional_service_type, primary_contact, project_billing_phase, description, street, city, suite, zip, state, url, logo, billing_type, retainage_percent):
		#Company.__init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo, billing_type, retainage_percent)
		Company.__init__(self, name, description, street, city, suite, zip, state, url, logo, billing_type, retainage_percent)
		self.professional_service_type = professional_service_type
		self.primary_contact = primary_contact
		self.project_billing_phase = project_billing_phase
	
	

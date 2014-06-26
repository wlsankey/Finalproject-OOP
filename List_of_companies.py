import companies

##Almar = companies.Subcontractor(project_manager = "Mike Capala", trade = "plumbing")
##
##print Almar.project_manager


#Almar = companies.Subcontractor(company_description = "plumbing / heating", 
#company_address_street = "680 Madison Ave",
#company_address_city = "New York", 
#company_address_suite = "", 
#company_address_zip = "11238",  
#company_address_state = "New York",
#company_url = "https://www.facebook.com/pages/Almar-Plumbing-Heating-Corp/143200015725831",
#company_logo = "http://media.merchantcircle.com/16422355/Logo8-24_full.jpeg", 
#billing_type = "Requisition", 
#retainage_percent = "ten",
#trade = "plumbing and waste",
#project_manager = "Ian Gray"
#)

Almar = companies.Subcontractor(name = "Almar", description = "plumbing / heating", 
street = "680 Madison Ave",
city = "New York", 
suite = "", 
zip = "11238",  
state = "New York",
url = "https://www.facebook.com/pages/Almar-Plumbing-Heating-Corp/143200015725831",
logo = "http://media.merchantcircle.com/16422355/Logo8-24_full.jpeg", 
billing_type = "Requisition", 
retainage_percent = "ten",
trade = "plumbing and waste",
project_manager = "Ian Gray"
)

Goodman_Architects = companies.Consultant(name = "Goodman Architects", description = "plumbing / heating", 
street = "123 5th Ave",
city = "New York", 
suite = "12000", 
zip = "10001",  
state = "New York",
url = "http://fagoodman.com/",
logo = "http://fagoodman.com/wp-content/gallery/renderings/renderings-11.jpg", 
billing_type = BILLING_TYPE[0], 
retainage_percent = 0.10,
primary_contact = "Jonathan Goodman", 
professional_service_type = "Architect",
project_billing_phase = "Design Development"
)



#Almar = companies.Company("plumbing / heating", 
#"680 Madison Ave",
#"New York", 
#"", 
#"11238",  
#"New York",
#"https://www.facebook.com/pages/Almar-Plumbing-Heating-Corp/143200015725831",
#"http://media.merchantcircle.com/16422355/Logo8-24_full.jpeg", 
#"Requisition", 
#"ten"
#)

#ADDED instance with Subcontractor and its attributes
#Almar = companies.Subcontractor("Joe Doe", "plumbing")

#self.description = company_description
#		self.street = company_address_street
#		self.city = company_address_city
#		self.suite = company_address_suite
#		self.zip = company_address_zip
#		self.state = company_address_state
#		self.url = company_url
#		self.logo = company_logo
#		self.billing_type = billing_type
#		self.retainage_percent = retainage_percent
		
#print Almar.description
#print Almar.street
#print Almar.city
#print Almar.suite
#print Almar.zip
#print Almar.state
#print Almar.url
#print Almar.logo

#ADDED code to test subclass Subcontrator instance
#print Almar.trade
#print Almar.project_manager

Almar.print_all_attributes()
Almar.company_profile()

#companies.Company.show_website(Almar)
#
#if hasattr(Almar, 'city'):
#    if Almar.city == "Texas":
#        print "True"
#else:
#    print "False"

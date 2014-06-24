import companies

Almar = companies.Subcontractor(project_manager = "Mike Capala", trade = "plumbing")

print Almar.project_manager

"""
Almar = companies.Company(company_description = "plumbing / heating", 
company_address_street = "680 Madison Ave",
company_address_city = "New York", 
company_address_suite = "", 
company_address_zip = "11238",  
company_address_state = "New York",
company_url = "https://www.facebook.com/pages/Almar-Plumbing-Heating-Corp/143200015725831",
company_logo = "http://media.merchantcircle.com/16422355/Logo8-24_full.jpeg", 
billing_type = "Requisition", 
retainage_percent = "ten",
)
"""

#
#print Almar.description
#print Almar.street
#print Almar.city
#print Almar.suite
#print Almar.zip
#print Almar.state
#print Almar.url
#print Almar.logo


companies.Company.show_website(Almar)

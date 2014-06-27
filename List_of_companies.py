import companies


Almar = companies.Subcontractor(name = "Almar", description = "plumbing / heating", 
street = "680 Madison Ave",
city = "New York", 
suite = "", 
zip = "11238",  
state = "New York",
url = "https://www.facebook.com/pages/Almar-Plumbing-Heating-Corp/143200015725831",
logo = "http://media.merchantcircle.com/16422355/Logo8-24_full.jpeg", 
billing_type = companies.Company.BILLING_TYPE[0], 
retainage_percent = "ten",
trade = "plumbing and waste",
project_manager = "Ian Gray"
)

Goodman_Architects = companies.Consultant(name = "Goodman Architects", description = "arhitecture and design", 
street = "123 5th Ave",
city = "New York", 
suite = "12000", 
zip = "10001",  
state = "New York",
url = "http://fagoodman.com/",
logo = "http://fagoodman.com/wp-content/gallery/renderings/renderings-11.jpg", 
billing_type = companies.Company.BILLING_TYPE[1], 
retainage_percent = 0.10,
primary_contact = "Jonathan Goodman", 
professional_service_type = "Architect",
project_billing_phase = "Design Development"
)


Almar.print_all_attributes()
Almar.company_profile()

Goodman_Architects.print_all_attributes()
Goodman_Architects.company_profile()
Goodman_Architects.show_website()



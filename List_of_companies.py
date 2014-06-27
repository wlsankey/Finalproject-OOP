import companies

# DATA -- Creation of class instances and population of attributes
""" Here I have created three instances of the various classes creates in companies.py. These instances allow me to test the classes,
their definitions and methods, and ensure that they function appropriately when interpreted."""


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
url = "",
logo = "http://fagoodman.com/wp-content/gallery/renderings/renderings-11.jpg", 
billing_type = companies.Company.BILLING_TYPE[1], 
retainage_percent = 0.10,
primary_contact = "Jonathan Goodman", 
professional_service_type = "Architect",
project_billing_phase = "Design Development"
)


RG_New_York_Tile = companies.Material_Supplier(name = "R.G. New York Tile, Inc.", 
description = "marble supply", 
street = "22 W 29thh Street",
city = "New York", 
suite = "", 
zip = "10021",  
state = "New York",
url = "http://www.rgnytiles.com/",
logo = "", 
billing_type = companies.Company.BILLING_TYPE[1], 
retainage_percent = 0.15,
primary_contact = "Rob DiCarpala", 
deposit_required = "Yes, 30% deposit",
material_type = "stone and flooring"
)



#TEST FOR SUBCONTRACTOR class
Almar.print_all_attributes()
Almar.company_profile()
Almar.show_website()

#TEST FOR CONSULTANT class
Goodman_Architects.print_all_attributes()
Goodman_Architects.company_profile()
Goodman_Architects.show_website()

#TEST FOR MATERIAL SUPPLIER class
RG_New_York_Tile.print_all_attributes()
RG_New_York_Tile.company_profile()
RG_New_York_Tile.show_website()


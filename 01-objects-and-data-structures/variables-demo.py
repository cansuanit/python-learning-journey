"""
Programming Fundamentals - Variables Demo 
1- Create variables for the following customer information:
- Customer's Name
- Customer's Surname
- Customer's Name + Customer's Surname 
- Customer's Gender
- Customer's ID Number
- Customer's Birthday Year
- Customer's Address
- Customer's Age 

"""

customerName = "John"
customerSurname = "Doe"     
customerFullName = customerName + " " + customerSurname
print(customerFullName)
customerGender = "Male" 
customerIDNumber = "123456789"
customerBirthdayYear = 1990
customerAddress = "123 Main St, Anytown, USA"
customerAge = 2026 - customerBirthdayYear  # Assuming the current year is 2026

print(customerAge)

"""2- Calculate the total information for the following orders
- Order 1 => 110 $
- Order 2 => 1100.5 $
- Order 3 => 365.95 $
"""
order1 = 110
order2 = 1100.5
order3 = 365.95

total = order1 + order2 + order3
print("Total Order Amount:", total, "$")

print(order1 + order2 + order3)
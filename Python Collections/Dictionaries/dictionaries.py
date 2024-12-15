config = {
    "keys": "12b23ga",
    "debug": True,
    "max connection": 23
}

print(config)



user_information = {
    "john_23": {"Full Name": "John wick", "Email": "joen@gmail.com", "phone": "093241235344"},
    "user_no2": {"Full Name": "Ceasar Montano", "Email": "ceasar@gmail.com", "phone": "092313548475"}
}

print(user_information["john_23"])


user_preferences = { 'theme':  'dark', 'Notifications': True}
print(user_preferences)




#BEST PRACTICES FOR USING DICTIONARIES

#Use Immutable Types for Keys:


my_prac_dict = {1: 'preferred one', (2,3): 'tuples keys', 'name': 'may'}

print(my_prac_dict) 

#Readable dictioanries

products = {'product_name': 'shoes', 'price': 1200, 'quantity': 230}
products["price"] = 450 #update the price
products["quality"]  = 'new' #adding new pair of keys and values
print(products)
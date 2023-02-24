#!/bin/env python3


import os
import csv

products_list = []
for dir in os.listdir('/OneDrive/'):
    full_path_name = os.path.join(dir, '/OneDrive/')
    if os.path.isdir(full_path_name):
        products_list.append(dir)
print(products_list)

products_path = '/OneDrive'

def product_list(products_path):
    products_list = []
    for dir in os.listdir(products_path):
        full_path_name = os.path.join(dir, products_path)
        if os.path.isdir(full_path_name):
            products_list.append(dir)
    return products_list

extension_list= ['txt','S4P','cir','zip','docx','ibs','msg','log','prm','S2P','s4p','pdf','doc','xls','xlsx']
extension_dict = { i:'No' for i in extension_list}
csv_header_rows = extension_list.insert(0, 'Product Name')

def generate_csv_header(poducts_list,csv_header_rows):
    with open(Required_Product_List.csv,'w') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=csv_header_rows)
        writer.writeheader()
        writer.writerows()



# In the future where there are unknown extensions, iterate through list using regex to generate extensions
# def generate_extensions(products_list):
#     for product in products_list:
#         os.path.join(product,products_path)
#         regex = r"*[.][a-z]$"
#         re.findall(regex)





def copy_file_url(file, filename):
    needed_url = os.path.join(file,filename)
    for ext in extension_list:
        if file.endswith('.' + ext) & extension_dict1[ext] == 'No':
            extension_dict1[ext] = needed_url
         #change dictionary value
         # go to next file or extension 
    return extension_dict1
    
    

['txt','S4P','cir','zip','docx','ibs','msg','log','prm','S2P','s4p','pdf','doc','xls','xlsx']   
        



def iteration():
    extension_dict1 = extension_dict
    for product in product_list:
        filename = os.path.join(product,products_path)
        #run extension/ get url
        for file in filename:
            if os.path.join(file,filename) == False:
                dx = copy_file_url(file,filename)
        
        #write into csv
        dx ={'Product Name':file}.update(dx)
        writing_dict_rows(dx) 


def writing_dict_rows(dict):
    # Import DictWriter class from CSV module
    from csv import DictWriter
    with open('event.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=csv_header_rows)
        dictwriter_object.writerow(dict)
        f_object.close()

 
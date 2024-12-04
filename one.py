json1 = [
    {"name": "john doe", "email": "JOHN@example.com", "phone_number": "123-456-7890", "address": "123 Main St, New York, NY 10001"},
    {"name": "jane smith", "email": "Jane.Smith@Email.com", "phone_number": "(123) 456 7890", "address": "456 Elm St, Los Angeles, CA 90001"},
    {"name": "john doe", "email": "john@example.com", "phone_number": "1234567890", "address": "123 Main St, New York, NY 10001"},
    {"name": "emma brown", "email": "emma_brown@hotmail.com", "phone_number": "+1 321-654-9870", "address": "789 Pine Ave, Chicago, IL 60601"},
    {"name": "liam jones", "email": "liam.j@domain.org", "phone_number": "(321) 654 9870", "address": "321 Oak St, Houston, TX 77001"},
    {"name": "olivia johnson", "email": "olivia.johnson@gmail.com", "phone_number": "3216549870", "address": "654 Maple Dr, Miami, FL 33101"},
    {"name": "noah williams", "email": "noah.williams@yahoo.com", "phone_number": "987-654-3210", "address": "987 Cedar St, Seattle, WA 98101"},
    {"name": "ava taylor", "email": "ava.t@company.com", "phone_number": "(987) 654 3210", "address": "654 Birch Rd, Boston, MA 02101"},
    {"name": "sophia harris", "email": "sophia.harris@email.org", "phone_number": "+1 (789) 456-1230", "address": "123 Aspen Ln, Denver, CO 80201"},
    {"name": "william moore", "email": "william.moore@service.net", "phone_number": "789-456-1230", "address": "456 Willow Way, San Francisco, CA 94101"},
    {"name": "isabella white", "email": "isabella.white@gmail.com", "phone_number": "4567891230", "address": "789 Cypress Ct, Portland, OR 97201"},
    {"name": "james thomas", "email": "james.thomas@email.com", "phone_number": "456-789-1230", "address": "123 Redwood Ave, Austin, TX 73301"},
    {"name": "mia martin", "email": "mia.martin@domain.com", "phone_number": "+1 456-789-1230", "address": "456 Spruce St, Atlanta, GA 30301"},
    {"name": "Emily Davis", "email": "emily.davis@sample.com", "phone_number": "987-654-3210", "address": "789 Pine St, Chicago, IL 60601"},
    {"name": "john doe", "email": "JOHN@example.com", "phone_number": "+1-123-456-7890", "address": "123 Main St, New York, NY 10001"},  
    {"name": "Michael Brown", "email": "michael_brown@domain.com", "phone_number": "9876543210", "address": "101 Oak St, Houston, TX 77001"},
    {"name": "Jane Smith", "email": "jane.smith@email.com", "phone_number": "123.456.7890", "address": "456 Elm St, Los Angeles, CA 90001"},  
    {"name": "Anna Taylor", "email": "annataylor@example.org", "phone_number": "456-789-1234", "address": "202 Maple St, Phoenix, AZ 85001"},
    {"name": "Chris Green", "email": "chris.green@domain.com", "phone_number": "+1 (456) 789-1234", "address": "303 Birch St, Miami, FL 33101"},
    {"name": "Michael Brown", "email": "michael_brown@DOMAIN.com", "phone_number": "9876543210", "address": "101 Oak St, Houston, TX 77001"},
    {"name": "john doe", "email": "JOHN@example.com", "phone_number": "123-456-7890", "address": "123 Main St, New York, NY 10001"},
    {"name": "john doe", "email": "JOHN@example.com", "phone_number": "+1-123-456-7890", "address": "123 Main St, New York, NY 10001"}
]
print(len(json1))


removedDuplicates = list({frozenset(i.items()):
                          i for i in json1}.values())
for i in removedDuplicates:
    print(i)



import re
for i in removedDuplicates:
    i['name']=i['name'].capitalize()
    i['email']=i['email'].lower()
    n=i['phone_number']
    n = re.sub(r'\D', '', n)
    clean_phone_number = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', n)
    i['phone_number']=clean_phone_number
    print(i)





def address_method(address):
    temp_data=address.split(',')
    l2=temp_data[2].split(' ')
    temp_data=temp_data[:2]
    for i in range(1,3):
        temp_data.append(l2[i])
    return temp_data
d=['City','State','abbrevation','zipcode']
for i in removedDuplicates:
    d2=dict(zip(d,address_method(i['address'])))
    i.update(d2)
for i in removedDuplicates:
    print(i)



import json
with open("details.json", "w") as file:
    json.dump(removedDuplicates, file, indent=6)  
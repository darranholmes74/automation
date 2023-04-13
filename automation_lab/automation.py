import re

with open('automation_lab/assets/potential-contacts.txt', 'r') as file:
    contents = file.read()
    # print(contents)

with open('automation_lab/assets/existing-contacts.txt', 'r') as file:
    contents2 = file.read()

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', contents)

email_set = set()
phone_set = set()



phone_numbers = re.findall(r'\d{3}[.\-\s]?\d{3}[.\-\s]?\d{4}', contents)
formatted_numbers = [re.sub(r'[.\-\s]', '-', num) for num in phone_numbers]


for email in emails:
    email_set.add(email)

for phone_number in formatted_numbers:
    for number in phone_number:
        cleaned_number = re.sub(r'\D', '', phone_number)
        new_formatted_num = re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', cleaned_number)
        phone_set.add(new_formatted_num)

print("Unique emails:")
for email in email_set:
    print(email)

print("Unique phone numbers:")
for phone in phone_set:
    print(phone)



with open('email.txt', 'w') as file:
    for email in email_set:
        file.write(email + '\n')

with open('phone.txt', 'w') as file:
    for phone in phone_set:
        file.write(phone + '\n')

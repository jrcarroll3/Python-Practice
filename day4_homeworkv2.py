import re

#Establish patterns to identify email addresses and phone numbers from files.
email_pattern = r'\S+@\S+' 
phone_pattern = r'\(?[\d]{3}\)?[\D{0,3}][\d]{3}[\D{0,3}][\d]{4}' 

#Initialize variables
formatted_numbers = []
email = ()

#Function to extract emails and phone numbers
def extract_emails_and_phones(file_path):
    emails = set()
    phones = set()
#Open file (using with open automatically closes the file when done)
    try:
        with open(file_path, 'r') as file:
            text = file.read()
#Find all emails and phone numbers using the established patterns
            emails = set(re.findall(email_pattern, text))
            phones = set(re.findall(phone_pattern, text))

#Exception handling if specified file is not found        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
 #Return all emails and phone numbers found   
    return emails, phones

#Function to standardize the format of any phone number found
def format_phone_numbers(phone_numbers):
    
    for number in phone_numbers:
#Strips all characters except numbers
        cleaned_number = re.sub(r'\D', '', number)
#Verified stripped phone number is 10 digits
        if len(cleaned_number) == 10:
#Formats valid phone numbers as: (NNN) NNN-NNNN
            formatted_number = f'({cleaned_number[:3]}) {cleaned_number[3:6]}-{cleaned_number[6:]}'
            formatted_numbers.append(formatted_number)
            #print(cleaned_number)
#Error handling for non-valid phone numbers identified
        else:
            print(f"Invalid phone number: {number}")


#Function to print to console unique email addresses and phone numbers
def print_unique_contacts(emails, phones):
    print(" ")
    print("Unique Email Addresses:")
    print("-----------------------")
    for email in emails:
        print(email)
    print(" ")
    print("Unique Phone Numbers:")
    print("-----------------------")
    for phone in formatted_numbers:
        print(phone)
#Establish source file location
file_path = ("c:\\temp\letter.txt")

#Call functions to execute
email_addresses, phone_numbers = extract_emails_and_phones(file_path)
format_phone_numbers(phone_numbers)
print_unique_contacts(email_addresses, formatted_numbers)

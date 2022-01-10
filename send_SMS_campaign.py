#!/usr/bin/python3
import bulk_sms

ACCOUNT_SSID_TWILIO = "XX"
AUTH_TOKEN_TWILIO = "YY"
TELEPHONE_FROM = "+11234"
CUSTOMERS_LIST = "input/list_of_customers.csv"
SMS_MESSAGE = "input/message.txt"
SMS_CR_PRICE = 0.04
# CUSTOMERS_LIST format:
# customer_name, Phone_number
# Olger Gerardo Zamora Bolaños,+50688366367

# Create object (Credentials)
sms = bulk_sms.BulkSMS(ACCOUNT_SSID_TWILIO, AUTH_TOKEN_TWILIO, TELEPHONE_FROM)

# Read and store the message
sms.read_txt(SMS_MESSAGE)
print("This is the text to send: \n")
print(sms.output_message)
print(f"\nThe message wil take: {sms.sms_quantity} SMS\n")
approve_text = input("It's the text approved? Y/N: ")
if approve_text == "Y":
    print("Text approved.\n")
    sms.read_customer_list(CUSTOMERS_LIST)
    approve_list = input(f"You will send it to {sms.number_lines} contact(s)\n"
                         f"It will approximately cost ${sms.number_lines * SMS_CR_PRICE}\n"
                         f"Would you like to send the SMS bulk campaign? Y/N  ")
    if approve_list == "Y":
        print("\nList approved, ready to send.")
        sms.send_message()
    else:
        print("\nList not approved.")

else:
    print("\nText not approved.")
# Send text to list








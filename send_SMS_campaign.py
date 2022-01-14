#!/usr/bin/python3
import bulk_sms
import os

# # sms_bulk_messaging
# Send SMS to a list of contacts
#
#
# # List of contacts in a csv format:
# File name: "input/list_of_customers.csv"
#
# Column format
# customer_name, Phone_number
#
# Example:
# Jon Doe,+50688361234
#
# # Message format
# File name: "input/message.txt"
# Use {name} tag to identify first name
#
# Example:
# Hi {name}, greetings today
#
# Notes:
# Unicode create larges SMSs
# Price based con Jan, 2021 $0.04 to Costa Rica

# ACCOUNT_SSID_TWILIO = "ACa32b39ef481f4b2bdede12fb9318485c"
# AUTH_TOKEN_TWILIO = "10613e143211bf17643aea7dfb83e6a6"
# TELEPHONE_FROM = "+17404818099"

ACCOUNT_SSID_TWILIO = os.environ['ACCOUNT_SSID_TWILIO']
AUTH_TOKEN_TWILIO = os.environ['AUTH_TOKEN_TWILIO']
TELEPHONE_FROM = os.environ['TELEPHONE_FROM']
CUSTOMERS_LIST = "input/list_of_customers.csv"
SMS_MESSAGE = "input/message.txt"
SMS_CR_PRICE = 0.04

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

    # Read contact list
    sms.read_customer_list(CUSTOMERS_LIST)
    approve_list = input(f"You will send it to {sms.number_lines} contact(s)\n"
                         f"It will approximately cost ${sms.number_lines * SMS_CR_PRICE}\n"
                         f"Would you like to send the SMS bulk campaign? Y/N  ")
    if approve_list == "Y":
        print("\nList approved, ready to send.")

        # Send SMS  the campaign
        print("Send message")
        # sms.send_message()
    else:
        print("\nList not approved.")

else:
    print("\nText not approved.")

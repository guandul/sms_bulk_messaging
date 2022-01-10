import csv
from twilio.rest import Client
import unidecode
import traceback


class BulkSMS:
    def __init__(self, account_id, auth_token, telephone_number):
        self.account_id = account_id
        self.auth_token = auth_token
        self.telephone_number = telephone_number
        self.output_message = ""
        self.sms_quantity = 0
        self.number_lines = 0
        self.list_contacts = []

    def read_txt(self, input_file):
        with open(input_file) as file:
            text_message = file.readlines()
        self.output_message = " ".join(text_message)
        is_unicode = False
        for char in self.output_message:
            if ord(char) > 127:
                is_unicode = True
        message_length = len(self.output_message) + 3
        if is_unicode:
            if message_length < 70:
                self.sms_quantity = 1
            else:
                self.sms_quantity = round(message_length / 67)
        else:
            if message_length < 160:
                self.sms_quantity = 1
            else:
                self.sms_quantity = round( message_length / 153 )

    def send_sms(self, telephone_to, text_to_send):
        client = Client(self.account_id, self.auth_token)
        message = client.messages \
            .create(
                body=text_to_send,
                from_=self.telephone_number,
                to=telephone_to
            )
        print(message.status)

    def read_customer_list(self, customer_list):

        file = open(customer_list)
        reader = csv.reader(file)
        for row in reader:
            self.number_lines += 1
            self.list_contacts.append(row)

    def send_message(self):
        for row in self.list_contacts:
            # Find first name and remove special characters
            first_name = unidecode.unidecode(row[0].split()[0]).capitalize()
            phone_number = row[1]
            message_formatted = self.output_message.format(name=first_name)
            try:
                print(f"Sending twilio to {phone_number}.")
                self.send_sms(phone_number, message_formatted)
            except Exception:
                traceback.print_exc()
                with open("output/error.csv", "a") as error:
                    error.write(",".join(row))
            else:
                print(message_formatted)

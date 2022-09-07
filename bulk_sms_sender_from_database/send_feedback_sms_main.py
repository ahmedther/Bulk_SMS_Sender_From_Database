from send_bulk_sms import SendSms
from support import PatientsValueAssignment
from oracle_config import Ora
from postgress_config import PostgressDB


# This Script has three different part and functions

# Part 1

# Retrieve Data from the database and filter the phone number as per requirements
pva = PatientsValueAssignment()

patients_list = pva.get_filtered_patients_values()

# ---------------------------------------------------------------------------------------------------------------------------------------#

# Part 2

# Extract Phone number to send SMS in bulk
extracted_phone_number = []
for i in list(patients_list.keys()):
    #     print(patients_list[i]['phone_number'])
    extracted_phone_number.append(patients_list[i]["phone_number"])


# Temproary "Remove in production"
extracted_phone_number1 = ["8767861216", "8080513540","9820580481"]  # "9004579961"

# Send Bulk SMS
SendSms(number=",".join(extracted_phone_number1))

# ---------------------------------------------------------------------------------------------------------------------------------------#

# Part 3 Save the data in a temporary table so that it can be viewed later
post_db = PostgressDB()

post_db.send_patient_data_to_postgres_database(patients_list)

post_db.delete_patient_above_24hr()

post_db.connection_close()

from send_bulk_sms import SendSms
from support import PatientsValueAssignment


# This Script has three different part and functions

#Part 1

#Retrieve Data from the database and filter the phone number as per requirements
con_db = PatientsValueAssignment()

patients_list = con_db.get_filtered_patients_values()



# Part 2

# Extract Phone number to send SMS in bulk
extracted_phone_number = []
for i in list(patients_list.keys()):
#     print(patients_list[i]['phone_number'])
    extracted_phone_number.append(patients_list[i]['phone_number'])



#Temproary "Remove in production"
extracted_phone_number1 = ["8767861216","9004579961","8080513540"]

#Send Bulk SMS
#SendSms(number=','.join(extracted_phone_number1))



# Part 3 Save the data in a temporary table so that it can be viewed later

con_db.send_patient_data_to_database(patients_list)

con_db.close_database_connection()
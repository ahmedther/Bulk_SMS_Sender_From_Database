from oracle_config import Ora


class PatientsValueAssignment:

    def __init__(self):
        db = Ora()
        discharge_patients_in_last_hour = db.get_discharge_patients_in_last_hour()
        db.close_database_connection()
        self.patients_list = {}
        for index, patients in enumerate(discharge_patients_in_last_hour):
            self.patients_list[index] = {
                "patient_id": patients[0],
                "encounter_id" : patients[1],
                "patient_name":patients[2],
                "phone_number": patients[3],
                "gender":patients[4],
                "bed_number": patients[5],
                "location": patients[6],
                "admission_datetime": patients[7],
                "discharge_datetime" : patients[8]
                }

        # Filtering patients phone numbers to remove country code.
        for index, patients in enumerate(self.patients_list):

            if len(self.patients_list[patients]["phone_number"]) > 10:
                number_with_country_code = self.patients_list[patients]["phone_number"]
                
                #Remove charactes from index 0 to 1 i.e 9 and 1 from begining
                number_without_country_code = number_with_country_code[0: 0:] + number_with_country_code[1 + 1::]
                self.patients_list[patients]["phone_number"] = number_without_country_code
            
            # Filter M to Male and F to Female
            try : 
                if self.patients_list[patients]["gender"] == "M":
                    self.patients_list[patients]["gender"] = "Male"

                if self.patients_list[patients]["gender"] == "F":
                    self.patients_list[patients]["gender"] = "Female"
            except:
                pass
        
        

        
        # Filtering and removing phonenumbers which are less then 10 digit
        for i in list(self.patients_list.keys()):
            

            if len(self.patients_list[i]["phone_number"]) < 10:
                    self.patients_list.pop(i)

                    
        
    def get_filtered_patients_values(self):
        return self.patients_list







import urllib,urllib.request,urllib.parse



class SendSms:


    def __init__(self,message ="Total Bill amount of f as on date 10-Jan-2022 is Rs 100 balance deposit is Rs 0 Kokilaben Dhirubhai Ambani Hospital KINDLY SUBMIT THE PAN CARD NUMBER OF THE PATIENT BEFORE DISCHARGE,IN THE ABSENCE OF THE PAN CARD NUMBER FORM 60 TO BE FILLED MANDATORY.",number='8767861216,9004579961,8080513540'):
        url = "http://www.smscountry.com/smscwebservice_bulk.aspx"
        values = {'user' : 'kdah',
                    'passwd' : 'kdah@1234',
                    'message' : message,
                    'mobilenumber':number,
                    'mtype':'N',
                    'SID':"KDAHOS",
                    'DR':'Y'
                    }
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        request = urllib.request.Request(url,data)
        #print(request.data)
        response = urllib.request.urlopen(request)
        #print (response.read().decode('utf-8'))


message="Total Bill amount of f as on date 10-Jan-2022 is Rs 100 balance deposit is Rs 0 Kokilaben Dhirubhai Ambani Hospital KINDLY SUBMIT THE PAN CARD NUMBER OF THE PATIENT BEFORE DISCHARGE,IN THE ABSENCE OF THE PAN CARD NUMBER FORM 60 TO BE FILLED MANDATORY."

number = ("8767861216,9004579961,8080513540")

if __name__ == "__main__":

    test = SendSms(message,number)
    print(test)



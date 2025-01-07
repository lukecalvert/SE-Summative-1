import requests
import pandas as pd

initialRequest = requests.get("https://members-api.parliament.uk/api/Members/Search?House=1&IsEligible=true&skip=0&take=20")

responseItems = initialRequest.json()

maxRecords = responseItems['totalResults']
counter = 0

df1 = df = pd.DataFrame({"MP ID":[],
                        "Name":[],
                        "Full title":[],
                        "Address as":[],
                        "Constituency ID":[],
                        "Constituency":[],
                        "email":[]
                        })


while counter < maxRecords:
    response = requests.get("https://members-api.parliament.uk/api/Members/Search?House=1&IsEligible=true&skip="+str(counter)+"&take=20")
    
    items = response.json()
    
    for item in items['items']:
        MPid = item['value']['id']
        nameDisplayAs = item['value']['nameDisplayAs']
        nameFullTitle = item['value']['nameFullTitle']
        nameAddressAs = item['value']['nameAddressAs']
        
        constituencyName = item['value']['latestHouseMembership']['membershipFrom']
        constituencyID = item['value']['latestHouseMembership']['membershipFromId']
        house = item['value']['latestHouseMembership']['house']

        statusDescription = item['value']['latestHouseMembership']['membershipStatus']['statusDescription']

        contactInformation = item['links'][3]['href']

        contactRequest = requests.get("https://members-api.parliament.uk/api"+contactInformation)

        contactResponse = contactRequest.json()
        try: 
            email = contactResponse['value'][0]['email']
        except:
            email = "Null"

        counter += 1
        

        df2 = pd.DataFrame({"MP ID": [int(MPid)], 
                            "Name": [nameDisplayAs], 
                            "Full title": [nameFullTitle], 
                            "Address as": [nameAddressAs], 
                            "Constituency ID": [int(constituencyID)], 
                            "Constituency": [constituencyName], 
                            "email": [email]})
        df1 = pd.concat([df1, df2], axis=0)
        pComplete = str(round(counter/maxRecords * 100,2))
    print("\rCompleted: "+pComplete+"%")
    
df1.to_excel("output.xlsx", index=False)
print('output file created')
# Import libraries
import requests
import pandas as pd

# Define the initial API request
initialRequest = requests.get("https://members-api.parliament.uk/api/Location/Constituency/Search?name=?&skip=0&take=20")

# Get the total number of records
responseItems = initialRequest.json()
maxRecords = responseItems['totalResults']

# Initialize an empty DataFrame to store the data
df1 = pd.DataFrame({"MP ID":[],
                    "Name":[],
                    "Full title":[],
                    "Address as":[],
                    "Constituency ID":[],
                    "Constituency":[],
                    "email":[],
                    "Party": []
                    })

# Initialize an empty list to store the records
records = []

# Define a function to fetch data from the API
def fetch_data(counter):
    try:
        response = requests.get(f"https://members-api.parliament.uk/api/Location/Constituency/Search?name=?&skip={counter}&take=20")
        items = response.json()
        for item in items['items']:
            MPid = item['value']['currentRepresentation']['member']['value']['id']
            nameDisplayAs = item['value']['currentRepresentation']['member']['value']['nameDisplayAs']
            nameFullTitle = item['value']['currentRepresentation']['member']['value']['nameFullTitle']
            nameAddressAs = item['value']['currentRepresentation']['member']['value']['nameAddressAs']
            constituencyName = item['value']['name']
            constituencyID = item['value']['id']
            party = item['value']['currentRepresentation']['member']['value']['latestParty']['name']
            # tweak the below
            contactRequest = requests.get("https://members-api.parliament.uk/api/Members/"+str(MPid)+"/Contact")
            contactResponse = contactRequest.json()
            try: 
                email = contactResponse['value'][0]['email']
            except:
                email = "Null"
            records.append({"MP ID": int(MPid), 
                            "Name": nameDisplayAs, 
                            "Full title": nameFullTitle, 
                            "Address as": nameAddressAs, 
                            "Constituency ID": int(constituencyID), 
                            "Constituency": constituencyName, 
                            "email": email,
                            "Party": party})
    except Exception as e:
        print(f"Error: {e}")

for counter in range(0, maxRecords, 20):
    fetch_data(counter)


# Convert the records to a DataFrame
df1 = pd.DataFrame(records)

# Write the DataFrame to a CSV file
df1.to_csv("output.csv", index=False)
print('output file created')
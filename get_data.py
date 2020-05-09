import requests
import json


def get_data():
    with open("dataurl.txt") as f:
        data_url = f.read()
    
    with open("strucurl.txt") as f:
        struc_url = f.read()

    print(len(data_url))
    print(len(struc_url))

    if len(data_url) <= 1000:
        data = requests.get(data_url)
        printResults(data)

    if len(struc_url) <= 1000:
        struc = requests.get(struc_url)
        printResults(struc)

    # Use the built-in JSON function to return parsed data
    # data = data.text.json()
    # print(json.dumps(data,indent=4))

    # print(dataobj['slideshow']['title'])
    # print("There are {0} slides".format(len(dataobj['slideshow']['slides'])))

def printResults(results):
    print(f"Result code: {results.status_code}")
    print("\n")
    
    print("Headers: --------------------")
    print(results.headers)
    print("\n")
            
    print("Returned data: --------------------")
    print(results.text)


if __name__ == "__main__":
    get_data()


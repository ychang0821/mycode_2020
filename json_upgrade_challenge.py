import requests
def main():
    
    r = requests.get('http://api.open-notify.org/astros.json')
    for x in r.json()["people"]:
        print(f"{x['name']} is on the {x['craft']}")
main()

import secrets
import requests

def get_data():
    all_data=[]
    for page in range(5):g
        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.name,2013.student.size&api_key=I2z7eyUxvuqaGCtTM5STN5aN29XW0fV1P1dxd8dy")
        if response.status.status_code !=200:
            print("error while getting data")
            exit(-1)
        page_of_data=response.json()
        page_of_school_data= page_of_data['results']
        all_data.extend(page_of_school_data)
    return all_data


def main():
    demo_data = get_data()

if __name__ '__main__':
    main()
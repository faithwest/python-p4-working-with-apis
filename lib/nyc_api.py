import requests
import json

class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        
        if response.status_code == 200:
            return response.text  
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    def program_schools(self):
        programs_list = []
        programs_json = json.loads(self.get_programs()) if self.get_programs() else None

        if programs_json and isinstance(programs_json, list):
            for program in programs_json:
                school = program.get("school")
                if school is not None:
                    programs_list.append(school)

        return programs_list

programs = GetPrograms()

schools = programs.program_schools()

if schools:
    for school in set(schools):
        print(school)
else:
    print("No schools found or an error occurred.")

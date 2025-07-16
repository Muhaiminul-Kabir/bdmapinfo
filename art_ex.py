import re
import json
import os

def extract_art(link):
    



    with open("data/output.txt", "r", encoding="utf-8") as file:
        text = file.read()
    #  List of 64 districts (Bangladesh)
    districts_list = [
        "Bagerhat", "Bandarban", "Barguna", "Barisal", "Bhola", "Bogra", "Brahmanbaria", "Chandpur", "Chapai Nawabganj", "Chattogram",
        "Chuadanga", "Comilla", "Cox's Bazar", "Dhaka", "Dinajpur", "Faridpur", "Feni", "Gaibandha", "Gazipur", "Gopalganj",
        "Habiganj", "Jamalpur", "Jashore", "Jhalokathi", "Jhenaidah", "Joypurhat", "Khagrachari", "Khulna", "Kishoreganj", "Kurigram",
        "Kushtia", "Lakshmipur", "Lalmonirhat", "Madaripur", "Magura", "Manikganj", "Meherpur", "Moulvibazar", "Munshiganj", "Mymensingh",
        "Naogaon", "Narail", "Narayanganj", "Narsingdi", "Natore", "Netrokona", "Nilphamari", "Noakhali", "Pabna", "Panchagarh",
        "Patuakhali", "Pirojpur", "Rajbari", "Rajshahi", "Rangamati", "Rangpur", "Satkhira", "Shariatpur", "Sherpur", "Sirajganj",
        "Sunamganj", "Sylhet", "Tangail", "Thakurgaon"
    ]
    
    
    
    paths = {
        "Bagerhat":"path7070", "Bandarban":"path7308", "Barguna":"path2245", "Barisal":"path4189",
        "Bhola":"path5169", "Bogra":"path2184", "Brahmanbaria":"path4177", "Chandpur":"path5150",
        "Chapai Nawabganj":"path2180","Chattogram":"path2440","Chuadanga":"path6105", "Comilla":"path4179",
        "Cox's Bazar":"path5364", "Dhaka":"path4160", "Dinajpur":"path2174", "Faridpur":"path5128",
        "Feni":"path7138","Gaibandha":"path2177", "Gazipur":"path2229", "Gopalganj":"path6099",
        "Habiganj":"path3203", "Jamalpur":"path8041", "Jashore":"path2204", "Jhalokathi":"path3218", 
        "Jhenaidah":"path7082","Joypurhat":"path3152", "Khagrachari":"path4391", "Khulna":"path3186",
        "Kishoreganj":"path5143", "Kurigram":"path3151","Kushtia":"path3188", "Lakshmipur":"path6121", 
        "Lalmonirhat":"path2175","Madaripur":"path6102", "Magura":"path8053", "Manikganj":"path3189",
        "Meherpur":"path5134", "Moulvibazar":"path4174", "Munshiganj":"path2235", "Mymensingh":"path4172",
        "Naogaon":"path2179","Narail":"path2205", "Narayanganj":"path3206", "Narsingdi":"path2231",
        "Natore":"path3179", "Netrokona":"path6116", "Nilphamari":"path4167", "Noakhali":"path6152", 
        "Pabna":"path5240", "Panchagarh":"path2169","Patuakhali":"path3216", "Pirojpur":"path2242",
        "Rajbari":"path4163", "Rajshahi":"path3168", "Rangamati":"path8281", "Rangpur":"path2176", 
        "Satkhira":"path2206","Shariatpur":"path5131", "Sherpur":"path3201", "Sirajganj":"path4248",
        "Sunamganj":"path2228", "Sylhet":"path2230", "Tangail":"path2215", "Thakurgaon":"path2192"
    }

    #  Count victim keywords
    fatalities = len(re.findall(r'\b(died|passed away|dead|deceased|murdered|killed|throat slit|slain)\b', text.lower()))
    injured = len(re.findall(r'\b(injured|critical condition|admitted|hospitalised|wounded|serious injuries)\b', text.lower()))
    total_victims = fatalities + injured


    if total_victims == 0:
        print("Not a accident report")
    else:


        #  Extract victim names and ages
        names_ages = re.findall(r'([A-Z][a-z]+\s[A-Z][a-z]+),?\s*\(?(\d{1,2})\)?', text)
        victims = [{"name": name.strip(), "age": int(age)} for name, age in names_ages]

        #  Extract locations: village, upazila, etc.
        locations = re.findall(r'\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s(?:village|upazila|area|school|college))', text)
        location_list = list(set(locations))

        #  Extract hospitals
        hospitals = re.findall(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*\sHospital)', text)

        #  Extract doctors
        doctors = re.findall(r'Dr\.?\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)', text)
        
        #  Match districts from master list
        matched_districts = [d for d in districts_list if re.search(fr'\b{re.escape(d)}\b', text)]
        
        path_data = []
        
        for x in matched_districts:
            path_data.append(paths[x])
        
        
        json_path = 'data/db.json'

        # Ensure data is in correct format
        victim_details = [f"{v['name']}({v['age']})" for v in victims] if victims else []
        hurt = len(victims)

        # Construct the new entry as a dictionary
        new_entry = {
            "path_data": path_data if path_data else [],
            "victims": victim_details,
            "hurt": str(hurt),
            "locations": location_list if location_list else [],
            "hospitals": hospitals if hospitals else [],
            "doctors": doctors if doctors else [],
            "districts": matched_districts if matched_districts else [],
            "link": link
        }

        # Step 1: Load existing entries
        existing_entries = []
        if os.path.exists(json_path):
            with open(json_path, mode='r', encoding='utf-8') as file:
                try:
                    existing_entries = json.load(file)
                except json.JSONDecodeError:
                    existing_entries = []

        # Step 2: Check for duplicate and save if new
        if new_entry not in existing_entries:
            existing_entries.append(new_entry)
            with open(json_path, mode='w', encoding='utf-8') as file:
                json.dump(existing_entries, file, ensure_ascii=False, indent=4)
            print("\n Data saved to 'data/output.json'")
        else:
            print("\n️ Duplicate entry found. Skipped saving.")
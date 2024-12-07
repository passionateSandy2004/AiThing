import google.generativeai as genai
import os 

# Gen AI Configuration
genai.configure(api_key="AIzaSyA3xtb9-icFxB0DqHL5zoaoQjWj48eSxqo")
model = genai.GenerativeModel("gemini-1.5-flash")
def MakeWords(i):
    response = model.generate_content(f"give a 1000 word paragraph specfiying the all the domain focus of the given startup idea only in words a single paragraph don not make points , type of fund required, what type capital they want to raise with their investor, and other things the startup idea wants to explain to their investors. idea:{i}. so that with these words i can make contextual search using webscrapping bot through all my investors i want . output template [Software and other domains foucsed on, type of fund required, other things the startup idea wants to explain to their investors ]")
    response= response.text
    return response 

import json
def load_json(file):
    with open(file, 'r') as file:
        records = json.load(file)
        return records
def find_relevant_records(input_description, top_n=5):
    # Preprocess the input description into lowercase words for matching
    input_words = set(MakeWords(input_description).lower().split())
    
    # Create a list to store matching results
    matches = []
    
    # Iterate through each record
    file=os.path.join(os.getcwd(),"scrape.json")
    records=load_json(file)
    for record in records:
        record_description = record.get("scrape description", "").lower()
        record_words = set(record_description.split())
        
        # Calculate the number of matching words
        match_count = len(input_words.intersection(record_words))
        
        if match_count > 0:
            matches.append({"#": record["#"], "match_count": match_count})
    
    # Sort results by match count in descending order
    matches = sorted(matches, key=lambda x: x["match_count"], reverse=True)
    
    # Return the top N matches by #
    return [match["#"] for match in matches[:top_n]]
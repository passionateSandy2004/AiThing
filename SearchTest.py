import os
import json
import re
import google.generativeai as genai

# Gen AI Configuration
genai.configure(api_key="AIzaSyA3xtb9-icFxB0DqHL5zoaoQjWj48eSxqo")
model = genai.GenerativeModel("gemini-1.5-flash")


def tokenize(text):
    """Faster tokenization by splitting words."""
    return text.lower().split()



def make_words(description):
    """Use the generative model to process the description."""
    response = model.generate_content(
        f"""Software and other domains focused on: AI, machine learning, data-driven decision-making. 
        Type of fund required: Venture capital, angel investment, seed funding. 
        Other things the startup idea wants to explain to their investors: Scalability, potential market size, competitive advantage. for the startup idea {description}"""
    )
    return tokenize(response.text)


def find_relevant_records(input_description, json_file=os.path.join(os.getcwd(),"scrape.json"), top_n=5):
    """Find the most relevant records from a JSON file by matching words in descriptions."""
    input_words = set(make_words(input_description))

    matches = []  # Store matching results

    # Load the entire JSON array (since it's not NDJSON)
    with open(json_file, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)  # Load the entire JSON array
            for record in data:
                record_description = record.get("scrape description", "")
                record_words = set(tokenize(record_description))
                
                # Count the matching words
                intersection = input_words.intersection(record_words)
                match_count = len(intersection)

                if match_count > 0:
                    matches.append((record["#"], match_count))

        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
        except Exception as e:
            print("Error:", e)

    # Sort results by match count in descending order
    matches.sort(key=lambda x: x[1], reverse=True)

    # Return only the top N matches (record # values)
    return [match[0] for match in matches[:top_n]]


# Example usage
if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "scrape.json")
    input_description = "Our startup focuses on AI-driven investor matching and advanced pitch deck automation."
    top_matches = find_relevant_records(input_description, file_path, top_n=5)
    print("Top Matches:", top_matches)

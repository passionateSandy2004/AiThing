import google.generativeai as genai
import re
import json 

# Gen AI Configuration
genai.configure(api_key="AIzaSyAnLVmAm9r4ZkiCW-TXCz8HAaff-IfvWn0")
model = genai.GenerativeModel("gemini-1.5-flash")

# Text-cleaner function
def clean_text_for_ppt(input_text):
    cleaned_text = re.sub(r'\s+', ' ', input_text.strip())
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    cleaned_text = cleaned_text.replace('\n', ' ')
    return cleaned_text
def answer(q):
    response = model.generate_content(q)
    response= response.text
    return response


def GenText2(input_idea, Blength,content_lenght):
    # JSON-based prompt for structured response
    prompt = f"""
    Based on the idea: "{input_idea}", generate the following details in JSON format:
    {{
        "introduction":"Brief explanation of the idea introduction in {Blength} words",
        "problem_statements": [
            {{
                "title": "Subtopic_of_problem_statement1",
                "description": "Actual problem statement 1 in {content_lenght} words"
            }},
            {{
                "title": "Subtopic_of_problem_statement2",
                "description": "Actual problem statement 2 in {content_lenght} words"
            }}
        ],
        "solutions": [
            {{
                "title": "Subtopic_of_solution1",
                "description": "Actual solution 1 in {content_lenght} words"
            }},
            {{
                "title": "Subtopic_of_solution2",
                "description": "Actual solution 2 in {content_lenght} words"
            }}
        ],
        "market_opportunities": [
            {{
                "title": "Topic of opportunity 1",
                "content": "Content for opportunity 1 in {content_lenght+25} words"
            }},
            {{
                "title": "Topic of opportunity 2",
                "content": "Content for opportunity 2 in {content_lenght+25} words"
            }},
            {{
                "title": "Topic of opportunity 3",
                "content": "Content for opportunity 3 in {content_lenght+25} words"
            }},
            {{
                "title": "Topic of opportunity 4",
                "content": "Content for opportunity 4 in {content_lenght+25} words"
            }}
        ],
        "business_model": "Brief explanation of the business model in {Blength} words."
    }}
    """
    
    # Get the response as a string
    response = answer(prompt)
    
    # Clean the response to remove `json` code formatting if present
    cleaned_response = response.strip().strip("```").strip("json").strip()

    # Attempt to parse the cleaned response into JSON
    try:
        response_json = json.loads(cleaned_response)
        
        # Extract data into the required dictionary format
        introduction=response_json["introduction"]
        problem_statements = response_json["problem_statements"]
        ps1t = problem_statements[0]["title"]
        ps1 = problem_statements[0]["description"]
        ps2t = problem_statements[1]["title"]
        ps2 = problem_statements[1]["description"]

        solutions = response_json["solutions"]
        s1t = solutions[0]["title"]
        s1 = solutions[0]["description"]
        s2t = solutions[1]["title"]
        s2 = solutions[1]["description"]

        market_opportunities = response_json["market_opportunities"]
        m1t = market_opportunities[0]["title"]
        m1 = market_opportunities[0]["content"]
        m2t = market_opportunities[1]["title"]
        m2 = market_opportunities[1]["content"]
        m3t = market_opportunities[2]["title"]
        m3 = market_opportunities[2]["content"]
        m4t = market_opportunities[3]["title"]
        m4 = market_opportunities[3]["content"]

        business_model = response_json["business_model"]

        # Return the formatted dictionary
        return {
            "ps1t": ps1t, "ps1": ps1, "ps2t": ps2t, "ps2": ps2,
            "s1t": s1t, "s1": s1, "s2t": s2t, "s2": s2,
            "m1t": m1t, "m1": m1, "m2t": m2t, "m2": m2,
            "m3t": m3t, "m3": m3, "m4t": m4t, "m4": m4,
            "bm": business_model, "introduction":introduction
        }

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        print(f"Cleaned Response: {cleaned_response}")
        return {}

    except KeyError as e:
        print(f"Missing key in JSON response: {e}")
        return {}

'''res=GenText2(
    "Our aim is to build a next level ai platform where startup founders can find their investors and make pitchdeck out of ai , the platform helps the founders to have ai search engine through the investors , here the problems like spam investors , outdateded vc database and unrelabile contact information are eliminated , the platform provides high quality data and connections to vc helpping founders rise fund. business model is a subscription based model where user pays to platform to use high quality ai feed to make pitch deck and find investors",
    30
)
print(res)'''

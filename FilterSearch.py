import google.generativeai as genai
import re

# Gen AI Configuration
genai.configure(api_key="AIzaSyAnLVmAm9r4ZkiCW-TXCz8HAaff-IfvWn0")
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_funding_recommendation(query):
    query_template = f"""
    For the given idea description: "{query}",

    Provide the recommended funding information in the following structured JSON format:
    {{
        "Explanation": give a 2 line explanation of what kind of fund focus ,fund stage , and fund type and why they need this,
        "FundFocus": "Select best-suggested Fund Focuses for the idea from the list below include all required fund focus",
        "FundStage": "Select one most recommended Fund Stage for the idea",
        "FundType": "Select one most recommended Fund Type for the idea"
    }}
    
    **Options**:
    - FundFocus: [FinTech, SaaS, Cryptocurrency / Blockchain, Advertising (AdTech), Big Data & Analytics, PropTech, Manufacturing, Artificial Intelligence & Machine Learning, Apps, Augmented & Virtual Reality, Developer Tools, AgTech (FarmTech), AudioTech, B2C, Beauty, B2B, BioTech, Black / African American, Cannabis, ClimateTech & Cleantech, Productivity Tools, CloudTech, Cloud Security, Construction Tech, Communications Infrastructure, Consumer, CPG, Consumer Internet, Creator Economy, CRM, Hardware, Cybersecurity, Wearables & Quantified Technology, Customer Service, D2C, DeepTech, Healthcare, Entertainment & Media, E-Commerce, EdTech, HR Tech, Energy, Enterprise, E-Sports (Gaming), Events, FemTech, Food and Beverage, RestaurantTech, Future of Work, GovTech, Impact Investing, Information Technology, Infrastructure, InsurTech, Internet, IoT (Internet of Things), Telecommunications, Mobile, Legal Tech, Life Science, Marketing (MarTech), Logistics, Marketplace, Meeting Software, Micro-Mobility, Network Security, Neuroscience, Oil & Gas, Travel, PaaS (Platforms), PetTech, Pharmaceuticals, Recruiting, RetailTech, Robotics, Sales Automation, Ridesharing, Sharing Economy, Social Media, Sports, Supply Chain Tech, Sustainability, Women-Founded, Transportation, SpaceTech, Software]

    - FundStage: ["Pre-Seed", "Seed", "Series A", "Series B", "Series C", "Series D"]

    - FundType: ["Venture", "Angel", "Accelerator", "Family Office", "Corporate VC"]
    
    Return only the JSON response with recommended values.
    """
    response = model.generate_content(query_template)
    response=response.text
    cleaned_response = response.strip().strip("```").strip("json").strip()
    return cleaned_response



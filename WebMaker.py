import google.generativeai as genai


def clean(out):
    out=out.replace("```html","")
    out=out[:out.find("```")]
    out=out.replace("class","className")
    return out
# Gen AI Configuration
genai.configure(api_key="AIzaSyA3xtb9-icFxB0DqHL5zoaoQjWj48eSxqo")
model = genai.GenerativeModel("gemini-1.5-flash")


def write_to_index_html(file_path, html_content):
    """
    Writes the provided HTML content to a given index.html file.

    Args:
        file_path (str): The path to the index.html file.
        html_content (str): The HTML content to write into the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def answer(q):
    response = model.generate_content(q)
    response= response.text
    return response

def makeBody(outputFile,d):
   q = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modern Business Portfolio</title>
        <script src="https://cdn.tailwindcss.com"></script>

    </head>
        <!-- Use Tailwind CSS to create a modern, responsive, and visually rich layout.
            The website should highlight the following business details:
            {d}
            Include sections like: 
            do not add image , use only professional theme and colors, every section should cover a full page 
            -nav bar section with ll the section pointing other sections
            - Hero section with a call to action covering first page fully
            - Services or offerings we make very clearly
            - About us with details and imagery from the google 
            - Testimonials or customer reviews
            - Contact details
            - Footer with social links -->
        {{body_code}} start from the body code
    </html>
    """
   code=answer(q)
   code=clean(code)
   write_to_index_html(outputFile,code)
   



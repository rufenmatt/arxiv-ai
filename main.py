from flask import Flask, render_template, request, jsonify, session, redirect
import requests
import feedparser
import openai
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

papers = []

@app.route('/')
def index():
    global papers

    if not papers:
        url = 'https://export.arxiv.org/api/query?search_query=all:machine%20learning&start=0&max_results=100'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.content
            feed = feedparser.parse(data)
            for entry in feed.entries:
                papers.append({
                    'title': entry.title,
                    'authors': entry.author,
                    'abstract': entry.summary,
                    'pdf_url': entry.links[1].href.replace('http://', 'https://')

                })
        else:
            return 'Error retrieving data from the API'

    # Convert the dictionary view object to a list
    papers = papers

    return render_template('index.html', papers=papers)

@app.route('/set-openai-key', methods=['POST'])
def set_openai_key():
    api_key = request.form['openai_key']

    openai.api_key = api_key
    # Make a test call to the OpenAI API
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt="test",
            max_tokens=5,
        )
    except openai.error.AuthenticationError:
        # The provided key is invalid
        error_message = 'Invalid API key'
        return render_template('index.html', error_message=error_message, papers=papers)
    else:
        # The provided key is valid
        # Continue with the rest of the Flask app logic
        session['openai_key'] = api_key
        return redirect('/')

@app.route('/paper/<int:paper_id>')
def paper(paper_id):
    paper = papers[paper_id]
    return render_template('paper.html', paper=paper)

@app.route('/generate-answer', methods=['POST'])
def generate_answer():
    openai.api_key = session.get('openai_key')

    # Get the prompt from the form data
    data = request.get_json()
    prompt = data['prompt']

    # Call the OpenAI API to generate an answer
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Extract the generated answer from the API response
    answer = response.choices[0].text.strip()

    # Return the answer to the browser
    return jsonify({'answer': answer})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)

from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Get the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "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")

@app.route("/", methods=["GET"])
def home():
    return "Nightbot ChatGPT API is running!"

@app.route("/ask", methods=["GET"])
def ask():
    q = request.args.get("q")  # Get the question from the URL parameter

    if not q:
        return "Error: No question provided.", 400  # Return an error if no question is given

    try:
        # Send the question to OpenAI's ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": q}],
            max_tokens=100  # Limit response length
        )

        # Extract the ChatGPT response
        reply = response["choices"][0]["message"]["content"]

        # Ensure the response is within Nightbot's 400-character limit
        if len(reply) > 400:
            reply = reply[:397] + "..."

        return reply  # Return the ChatGPT response

    except Exception as e:
        return f"Error: {str(e)}", 500  # Handle API errors

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Run the Flask app

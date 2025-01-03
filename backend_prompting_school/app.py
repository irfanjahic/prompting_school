from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from supabase import create_client, Client

import datetime
import jwt
import json
# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

with open('../config.json') as config_file:
    config = json.load(config_file)

openai_key = None #config['openai_key']
openai_organization = None #config['openai_organization']
openai_project = None #config['openai_project']
supabase_url = None #config['supabase_url']
supabase_key = None #config['supabase_key']
SECRET_KEY = None #config['secret_key'] # JWT secret key
supabase = None

with open('../config.json') as config_file:
        config = json.load(config_file)

openai_key = config['openai_key']
openai_organization = config['openai_organization']
openai_project = config['openai_project']
supabase_url = config['supabase_url']
supabase_key = config['supabase_key']
SECRET_KEY = config['secret_key'] # JWT secret key
supabase = create_client(supabase_url, supabase_key)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('input_text')
    # Process the input_text here

    openai_data(input_text)
    
    input_text = input_text.upper()
    input_text = input_text[::-1]
    
    result = f"Processed: {input_text}"
    return jsonify({'result': result})

def openai_data(input_text):
    print("OpenAI data processing.")
    client = OpenAI(
        api_key=openai_key,
        organization=openai_organization,
        project=openai_project
    )
    #client = OpenAI()

    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": "Say this is a test and this name:" + input_text,
        }],
        model="gpt-4o-mini",
    )

    #print(response)
    #print response text only from the llm.
    print(response.choices[0].message.content)
    return jsonify({'result': 'OpenAI data'})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = {
        'first_name': data['firstName'],
        'last_name': data['lastName'],
        'date_of_birth': data['dateOfBirth'],
        'email': data['email'],
        'password': data['password']
    }
    
    response = supabase.table("Users").insert(new_user).execute()
    #if response.error:
    #    return jsonify({'error': response.error.message}), 400
    return jsonify({'message': 'User registered successfully', 'data': response.data}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    
    try:
        response = supabase.table("Users").select().eq('email', email).eq('password', password).execute()
    except Exception as e:
        print("This exception occured: ", e)
        return jsonify({'error': str(e)}), 400
    
    if len(response.data) == 0:
        return jsonify({'error': 'Invalid email or password'}), 400

    # Generate JWT token
    token = jwt.encode({
        'user_id': response.data[0]['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'token': token}), 200

    #return jsonify({'message': 'User logged in successfully', 'data': response.data}), 200

def load_secrets():
    with open('../config.json') as config_file:
        config = json.load(config_file)
    print(openai_key)
    openai_key = config['openai_key']
    print(openai_key)
    openai_organization = config['openai_organization']
    openai_project = config['openai_project']
    supabase_url = config['supabase_url']
    supabase_key = config['supabase_key']
    SECRET_KEY = config['secret_key'] # JWT secret key

def initialize_database():
    pass
    #global supabase
    #supabase = create_client(supabase_url, supabase_key)

if __name__ == '__main__':
    #load_secrets()
    #initialize_database() # supabase
    app.run(debug=True)
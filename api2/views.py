from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo
from rest_framework.views import APIView
from rest_framework import status

class IndexView(APIView):
    def get(self, request):
        return Response({"message": "API Index"}, status=status.HTTP_200_OK)

# Connect to MongoDB
url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)
db = client['FormGenerator']  # Replace 'your_database_name' with the actual name of your MongoDB database

# Endpoint to retrieve forms from the forms collection
@api_view(['GET'])
def get_forms(request):
    # Assuming 'forms' is the collection for form information
    forms_collection = db['forms']

    # Retrieve all forms from the collection
    forms = list(forms_collection.find())

    # Format the forms data as needed
    formatted_forms = [
        {
            'form_id': str(form['_id']),
            'form_title': form['form_title'],
            'questions': form['components'],
            # Add more form details as needed
        }
        for form in forms
    ]

    return Response(formatted_forms)

# Endpoint to retrieve responses from the responses collection
@api_view(['GET'])
def get_responses(request, form_id):
    # Assuming 'responses' is the collection for responses
    responses_collection = db['responses']

    # Retrieve responses for the specified form ID
    responses = list(responses_collection.find({'form_id': form_id}))

    # Format the responses data as needed
    formatted_responses = [
        {
            'response_id': str(response['_id']),
            'form_id': response['form_id'],
            'responses': response['responses'],
            # Add more response details as needed
        }
        for response in responses
    ]

    return Response(formatted_responses)

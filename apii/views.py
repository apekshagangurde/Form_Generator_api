from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo
from django.http import Http404

url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['FormGenerator']  # Replace 'your_database_name' with the actual name of your MongoDB database

@api_view(['GET'])
def get_all_forms(request):
    try:
        # Assuming 'forms' is the collection for form information
        forms_collection = db['forms']

        # Retrieve all forms
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

    except Exception as e:
        # Handle the exception, log it, and return an error response
        print(f"An error occurred: {e}")
        return Response({'error': 'An error occurred while retrieving forms'}, status=500)

    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import Response
import pymongo
from django.shortcuts import get_object_or_404  # Import this if needed



# Connect to MongoDB
url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)
db = client['FormGenerator']  # Replace 'your_database_name' with the actual name of your MongoDB database

# Endpoint to create a new form in the form collection
@api_view(['POST'])
def create_form(request):
    try:
        form_data = request.data
        form_title = form_data.get('formTitle')
        components = form_data.get('components')

        # Assuming 'forms' is the collection for form information
        forms_collection = db['forms']

        # Create a new document in the forms collection for the new form
        form_document = {
            'form_title': form_title,
            'components': components if components else [],  # Ensure components is not None
            # Add more form details as needed
        }
        inserted_document = forms_collection.insert_one(form_document)

        return Response({'message': f'Form {form_title} created successfully with ID: {inserted_document.inserted_id}'})
    except Exception as e:
        return Response({'message': f'Error creating form: {str(e)}'}, status=500)


# Endpoint to add responses to the responses collection
@api_view(['POST'])
def add_responses(request):
    form_id = request.data.get('form_id')  # Get the form ID
    responses = request.data.get('responses')  # Get responses data from frontend

    # Assuming 'responses' is the collection for responses
    responses_collection = db['responses']

    # Insert responses into the collection
    responses_collection.insert_one({
        'form_id': form_id,
        'responses': responses,
    })

    return Response({'message': f'Responses added for Form ID: {form_id} successfully'})
from rest_framework.response import Response  # Add this import statement

def publish_form(request):
    try:
        form_data = request.data
        form_title = form_data.get('formTitle')
        components = form_data.get('components')

        # Assuming 'forms' is the collection for form information
        forms_collection = db['forms']

        # Create a new document in the forms collection for the new form
        form_document = {
            'form_title': form_title,
            'components': components if components else [],  # Ensure components is not None
            # Add more form details as needed
        }
        inserted_document = forms_collection.insert_one(form_document)

        form_id = str(inserted_document.inserted_id)  # Convert ObjectId to string

        # You can save the form_id to your Django model if needed
        # form_model = get_object_or_404(Form, id=form_id)
        # form_model.save()

        # Extract other data as needed and pass form_id and any other required data in the response
        response_data = {
            'message': f'Form {form_title} published successfully with ID: {form_id}',
            'formId': form_id,
            # Add other data as needed
        }

        return Response(response_data)  # Use Response from Django REST Framework
    except Exception as e:
        return Response({'message': f'Error publishing form: {str(e)}'}, status=500)

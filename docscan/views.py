from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .yoti_integration import YotiDocScanIntegration

class CreateYotiSessionView(APIView):
    def post(self, request):
        # Load SDK ID and PEM file path from environment variables
        client_sdk_id = config("SANDBOX_CLIENT_SDK_ID")
        pem_path = config("PEM_FILE_PATH")

        # Initialize YotiDocScanIntegration
        yoti_integration = YotiDocScanIntegration(
            client_sdk_id=client_sdk_id,
            pem_path=pem_path
        )

        # Create the Yoti session
        session_details = yoti_integration.create_session()

        # If session creation was successful, return both session_id and session_token
        if session_details:
            return Response({
                "session_id": session_details["session_id"],
                "session_token": session_details["session_token"]
            }, status=200)
        else:
            return Response({"error": "Failed to create session"}, status=500)

def verification_success(request):
    return HttpResponse("<h1>Verification Success</h1><p>Your document verification was successful!</p>")

# View for error page
def verification_error(request):
    return HttpResponse("<h1>Verification Failed</h1><p>There was an issue with your document verification. Please try again.</p>")

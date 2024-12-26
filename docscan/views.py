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












# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .yoti_integration import YotiDocScanIntegration

# class CreateYotiSessionView(APIView):
#     def post(self, request):
#         # user_tracking_id = request.data.get('user_tracking_id')
#         # if not user_tracking_id:
#         #     return Response({"error": "user_tracking_id is required"}, status=400)

#         # Initialize YotiDocScanIntegration with your Sandbox Client SDK ID and PEM file path
#         yoti_integration = YotiDocScanIntegration(
            
#             client_sdk_id="85fbd11e-55f8-4257-9226-4cd37f0a2aaa",  # Your sandbox SDK ID
#             pem_path="/home/ts/Desktop/yoti_app/yoti_integration/privateKey.pem"  # Your PEM file path
#         )
#         print(f"==>> yoti_integration: {yoti_integration}")


#         # Create the Yoti session
#         session_id = yoti_integration.create_session()
#         print(f"==>> session_id: {session_id}")
#         if session_id:
#             return Response({"session_id": session_id}, status=200)
#         else:
#             return Response({"error": "Failed to create session"}, status=500)

# View for success page
def verification_success(request):
    return HttpResponse("<h1>Verification Success</h1><p>Your document verification was successful!</p>")

# View for error page
def verification_error(request):
    return HttpResponse("<h1>Verification Failed</h1><p>There was an issue with your document verification. Please try again.</p>")

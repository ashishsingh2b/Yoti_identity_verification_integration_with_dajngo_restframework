from yoti_python_sdk.doc_scan import DocScanClient, SdkConfigBuilder, NotificationConfigBuilder, SessionSpecBuilder, RequestedDocumentAuthenticityCheckBuilder, RequestedFaceMatchCheckBuilder, RequestedLivenessCheckBuilder, RequestedTextExtractionTaskBuilder
from yoti_python_sdk.doc_scan.exception.doc_scan_exception import DocScanException
import logging

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

class YotiDocScanIntegration:
    def __init__(self, client_sdk_id, pem_path):
        # Initialize with sandbox SDK Key and PEM file
        self.client_sdk_id = client_sdk_id
        self.pem_path = pem_path
        self.doc_scan_client = DocScanClient(client_sdk_id, pem_path, api_url="https://api.yoti.com/sandbox/idverify/v1")

    def create_session(self, user_tracking_id=""):
        # Create configuration for SDK, notifications, and session
        sdk_config = (
            SdkConfigBuilder()
            .with_primary_colour("#2d9fff")
            .with_preset_issuing_country("GBR")
            .with_success_url("http://127.0.0.1:8000/api/verification-success/")
            .with_error_url("http://127.0.0.1:8000/api/verification-error/")
            .build()
        )

        notification_config = (
            NotificationConfigBuilder()
            .with_endpoint('https://yourdomain.example/idverify/updates')
            .with_auth_token('username:password')
            .for_resource_update()
            .for_task_completion()
            .for_check_completion()
            .for_session_completion()
            .build()
        )

        session_spec = (
            SessionSpecBuilder()
            .with_client_session_token_ttl(600)
            .with_resources_ttl(90000)
            .with_user_tracking_id(user_tracking_id)
            .with_requested_check(RequestedDocumentAuthenticityCheckBuilder().build())
            .with_requested_check(
                RequestedLivenessCheckBuilder()
                .with_liveness_type("STATIC")
                .with_max_retries(3)
                .build()
            )
            .with_requested_check(
                RequestedFaceMatchCheckBuilder().with_manual_check_fallback().build()
            )
            .with_requested_task(
                RequestedTextExtractionTaskBuilder().with_manual_check_fallback().build()
            )
            .with_sdk_config(sdk_config)
            .with_notifications(notification_config)
            .build()
        )

        try:
            # Try creating the session
            session = self.doc_scan_client.create_session(session_spec)
            
            # Capture session details (session_id and session_token)
            session_id = session.session_id
            session_token = session.client_session_token  # This is the correct attribute

            # Log the session details to confirm the token
            logging.debug(f"Session created: session_id={session_id}, session_token={session_token}")

            # Return both session_id and session_token
            return {
                "session_id": session_id,
                "session_token": session_token  # Now this should correctly return the token
            }
        except DocScanException as e:
            # Log or print error
            logging.error(f"Failed to create or retrieve Yoti session: {e}")
            return None






























# # yoti_integration.py

# from yoti_python_sdk.doc_scan import DocScanClient, SdkConfigBuilder, NotificationConfigBuilder, SessionSpecBuilder, RequestedDocumentAuthenticityCheckBuilder, RequestedFaceMatchCheckBuilder, RequestedLivenessCheckBuilder, RequestedTextExtractionTaskBuilder
# from yoti_python_sdk.doc_scan.exception.doc_scan_exception import DocScanException
# import logging

# # Enable logging for debugging
# logging.basicConfig(level=logging.DEBUG)
 

# class YotiDocScanIntegration:
#     def __init__(self, client_sdk_id, pem_path):
#         # Initialize with sandbox SDK Key and PEM file
#         self.client_sdk_id = client_sdk_id
#         self.pem_path = pem_path
#         self.doc_scan_client = DocScanClient(client_sdk_id, pem_path, api_url="https://api.yoti.com/sandbox/idverify/v1")

#     def create_session(self, user_tracking_id=""):
#         # Create configuration for SDK, notifications, and session
#         sdk_config = (
#             SdkConfigBuilder()
#             .with_primary_colour("#2d9fff")
#             .with_preset_issuing_country("GBR")
#             .with_success_url("http://127.0.0.1:8000/api/verification-success/")
#             .with_error_url("http://127.0.0.1:8000/api/verification-error/")
#             .build()
#         )

#         notification_config = (
#             NotificationConfigBuilder()
#             .with_endpoint('https://yourdomain.example/idverify/updates')
#             .with_auth_token('username:password')
#             .for_resource_update()
#             .for_task_completion()
#             .for_check_completion()
#             .for_session_completion()
#             .build()
#         )

#         # session_spec = (
#         #     SessionSpecBuilder()
#         #     .with_client_session_token_ttl(600)
#         #     .with_resources_ttl(90000)
#         #     .with_user_tracking_id(user_tracking_id)
#         #     .with_requested_check(RequestedDocumentAuthenticityCheckBuilder().build())
#         #     .with_requested_check(RequestedLivenessCheckBuilder().with_liveness_type("STATIC").build())
#         #     .with_requested_check(RequestedFaceMatchCheckBuilder().build())
#         #     .with_requested_task(RequestedTextExtractionTaskBuilder().build())
#         #     .with_sdk_config(sdk_config)
#         #     .with_notifications(notification_config)
#         #     .build()
#         # )
#         session_spec = (
#             SessionSpecBuilder()
#             .with_client_session_token_ttl(600)
#             .with_resources_ttl(90000)
#             # .with_user_tracking_id("")
#             .with_requested_check(RequestedDocumentAuthenticityCheckBuilder().build())
#             .with_requested_check(
#                 RequestedLivenessCheckBuilder()
#                 .with_liveness_type("STATIC")
#                 .with_max_retries(3)
#                 .build()
#             )
#             .with_requested_check(
#                 RequestedFaceMatchCheckBuilder().with_manual_check_fallback().build()
#             )
#             .with_requested_task(
#                 RequestedTextExtractionTaskBuilder().with_manual_check_fallback().build()
#             )
#             .with_sdk_config(sdk_config)
#             .with_notifications(notification_config)
#             .build()
#         )

#         try:
#             # Try creating the session
#             session = self.doc_scan_client.create_session(session_spec)
#             return session.session_id  # Return session ID if successful
#         except DocScanException as e:
#             # Log or print error
#             logging.error(f"Failed to create Yoti session: {e}")
#             return None
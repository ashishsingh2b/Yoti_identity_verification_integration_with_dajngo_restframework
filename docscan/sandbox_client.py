from yoti_python_sandbox.doc_scan.client import DocScanSandboxClient

# Your sandbox SDK ID and PEM file path
client_sdk_id = "85fbd11e-55f8-4257-9226-4cd37f0a2aaa"  # Replace with your sandbox SDK ID
pem_path = "/home/ts/Desktop/yoti_app/yoti_integration/privateKey.pem"  # Replace with your PEM file path

# Initialize the sandbox client
doc_scan_sandbox_client = DocScanSandboxClient(client_sdk_id, pem_path)

# Optionally, test the initialization by printing the client object or making an API call
print(f"Sandbox Client Initialized: {doc_scan_sandbox_client}")

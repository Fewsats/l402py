from .client import Client
from .hub_service import HubService
from .credentials import L402Credentials, CredentialsService, parse_http_402_response
from .preimage_provider import PreimageProvider
from .requests import Session

# Create the singleton instance
requests = Session()
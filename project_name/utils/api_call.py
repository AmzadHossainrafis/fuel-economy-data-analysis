#import requests
import json
import logging
import requests

logger = logging.getLogger(__name__)

def api_call(url, method, data=None, headers=None, params=None):
    """Make API call and return response

    Args:
        url (str): URL to make the API call
        method (str): HTTP method to use
        data (dict): Data to pass to the API call
        headers (dict): Headers to pass to the API call
        params (dict): Parameters to pass to the API call

    Returns:
        dict: Response from the API call
    """
    response = requests.request(method, url, data=data, headers=headers, params=params)
    #return json.loads(response.text)
    return {}
import json
import requests
import platform

def get_aws_metadata():
    try:
        # Request a token
        token = requests.put(
            'http://169.254.169.254/latest/api/token',
            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'},
            timeout=2
        )
        if token.status_code != 200:
            print(f"Error getting token, received status code: {token.status_code}")
            return {}

        # Use the token to request the instance metadata
        response = requests.get(
            'http://169.254.169.254/latest/dynamic/instance-identity/document',
            headers={'X-aws-ec2-metadata-token': token.text},
            timeout=2
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Received non-200 status code: {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        print("Error connecting to AWS metadata server:", str(e))
        return {}


def get_metadata():
    os_type = platform.system().lower()
    
    if os_type == "linux":
        aws_metadata = get_aws_metadata()
        if aws_metadata:
            return json.dumps(aws_metadata, indent=2)
        else:
            print("AWS metadata not found.")
            return {}
    else:
        print("This script is designed to be run on a Linux instance.")
        return {}
        
        
if __name__ == "__main__":
    metadata = get_metadata()
    print(metadata)
import requests
import json

def get_hash_checker_response(api_key, sha256):
    sha256 = sha256.strip()
    url = f"https://www.virustotal.com/api/v3/files/{sha256}"
    headers = {
        "x-apikey": api_key
    }
    
    response = requests.get(url, headers=headers)
    
    data = json.loads(response.content.decode())
    
    try:
        md5 = data["data"]["attributes"]["md5"]
        sha1 = data["data"]["attributes"]["sha1"]
        if data["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0:
            detect_result = "malicious"
        elif data["data"]["attributes"]["last_analysis_stats"]["suspicious"] > 0:
            detect_result = "Suspicious"
        else:
            detect_result = "Clean"
        
        return [sha256, md5, sha1, "",  detect_result]
    except KeyError:
        return ["error", "error", "error", "", "error"]
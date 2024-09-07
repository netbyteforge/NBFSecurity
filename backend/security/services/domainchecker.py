import requests
import json

url_domain = "https://www.virustotal.com/api/v3/domains/{}"

def get_domain_checker_response(api_key, domain):
    headers = {
        "x-apikey": api_key,
        "Accept": "application/json"
    }
    r = requests.get(url_domain.format(domain), headers=headers)
    response = json.loads(r.text)
    if "error" in response:
        result = response["error"]["message"]
    else:
        stats = response["data"]["attributes"]["last_analysis_stats"]
        if stats["malicious"] > 0:
            result = "MALICIOUS"
        elif stats["suspicious"] > 0:
            result = "SUSPICIOUS"
        else:
            result = "CLEAN"
    
    return result

import requests
import json

def get_ip_checker_response(api_key, ip):
    ip = ip.strip()
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'
    headers = {
        'x-apikey': api_key
    }
    params = {
        'include': 'whois,country'
    }
    
    response = requests.get(url, headers=headers, params=params)
    outs = json.loads(response.text)
    try:
        stats = outs["data"]["attributes"]["last_analysis_stats"]
        
        if response.status_code == 200:
            response_json = response.json()
            data = response.json()['data']
            reputation = data['attributes']['reputation']
            country = data['attributes']['country']
            if stats["malicious"] > 0:
                result = "MALICIOUS"
            elif stats["suspicious"] > 0:
                result = "SUSPICIOUS"
            else:
                result = "CLEAN"
            owner = response_json["data"]["attributes"]["as_owner"]
            return [ip, country, owner, result]
        elif response.status_code == 404:
            return [ip, 'Not found in VirusTotal database']
        else:
            return [ip, f'Request failed with status code {response.status_code}']
    except KeyError:
        return ["error", "error", "error", "error"]
import requests
import dns.resolver

def get_dns(domain):
    records = []
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for r in answers:
            records.append(str(r))
    except:
        pass
    return records

def get_headers(domain):
    try:
        r = requests.get(f"https://{domain}", timeout=5)
        return dict(r.headers)
    except:
        return {}

def run_recon(domain):
    data = {}
    data["dns"] = get_dns(domain)
    data["headers"] = get_headers(domain)
    return data
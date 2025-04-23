import os  
import re  
import requests  
from dotenv import load_dotenv  

load_dotenv()  

def analyze_email(email_text):  
    # Deteksi tautan  
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email_text)  
    suspicious_links = []  

    # Cek reputasi di VirusTotal  
    for link in links:  
        params = {  
            'apikey': os.getenv('VIRUSTOTAL_API_KEY'),  
            'resource': link  
        }  
        response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)  
        result = response.json()  

        if result.get('positives', 0) > 0:  
            suspicious_links.append(link)  

    return {  
        "suspicious_links": suspicious_links,  
        "total_detected": len(suspicious_links)  
    }  

if __name__ == "__main__":  
    email_contoh = "Halo, klik link ini: http://malicious-site.com/ atau http://google.com"  
    hasil = analyze_email(email_contoh)  
    print("🔍 Hasil Analisis Email:")  
    print(f"Tautan Mencurigakan: {hasil['suspicious_links']}")  
    print(f"Total Terdeteksi: {hasil['total_detected']}")  
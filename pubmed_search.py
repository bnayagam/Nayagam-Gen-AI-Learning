import requests

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

params = {
    "db": "pubmed",
    "term": "diabetes treatment",
    "retmax": 5,
    "retmode": "json"
}

response = requests.get(url, params=params)
data = response.json()

article_ids = data["esearchresult"]["idlist"]

print("Found article IDs:")
for article_id in article_ids:
    print(f"- {article_id}")
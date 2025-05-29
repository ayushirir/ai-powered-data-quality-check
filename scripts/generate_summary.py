import requests, os, json

def summarize(report):
    prompt = f"Summarize this data quality report: {json.dumps(report)}"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    test = {"null_percentage": {"fare": 2.5}, "duplicate_count": 4, "row_count": 1000}
    print(summarize(test))

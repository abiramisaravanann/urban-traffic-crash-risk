import requests

# 🌐 Public API Endpoint
url = "https://data.cityofchicago.org/resource/85ca-t3if.json"

# 🔹 Parameters
params = {
    "$limit": 10,                 # get 10 records
    "$order": "crash_date DESC"   # latest data first
}

try:
    # 🔥 API Call (no API key)
    response = requests.get(url, params=params, timeout=15)

    # ✅ Success check
    if response.status_code == 200:
        data = response.json()

        print("\n✅ Data fetched successfully!\n")

        for i, record in enumerate(data, start=1):
            print(f"--- Record {i} ---")

            print("Crash Date:", record.get("crash_date", "N/A"))
            print("Street Name:", record.get("street_name", "N/A"))
            print("Injury Severity:", record.get("most_severe_injury", "N/A"))
            print()

    else:
        print("❌ Error:", response.status_code)
        print(response.text)

except requests.exceptions.RequestException as e:
    print("🚫 API Request Failed:", e)
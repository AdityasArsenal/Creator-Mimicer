import http.client
import json

conn = http.client.HTTPSConnection("instagram-scraper-api2.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "730906c569msh05a6a01ee12bc70p1e9c21jsn4c0b66da6662",
    'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
}

conn.request("GET", "/v1.2/posts?username_or_id_or_url=mrbeast", headers=headers)

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))







# Establish the connection and get the data (you've already done this)
conn = http.client.HTTPSConnection("instagram-scraper-api2.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "730906c569msh05a6a01ee12bc70p1e9c21jsn4c0b66da6662",
    'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
}
conn.request("GET", "/v1.2/posts?username_or_id_or_url=mrbeast", headers=headers)

res = conn.getresponse()
data = res.read()

# Decode and parse the JSON response
json_data = data.decode("utf-8")
parsed_data = json.loads(json_data)  # Parse the string into a dictionary

# Print the parsed data to debug
print("Parsed Data: ", parsed_data)

# List to store video URLs
video_urls = []

# Assuming the posts are in the 'items' key (you might need to adjust this based on the actual JSON structure)
if "items" in parsed_data:  # Ensure the 'items' key exists
    for item in parsed_data["items"]:
        # Debug the item to understand its structure
        print("Item: ", item)

        # Check if the post is a video
        if item.get("is_video", False):
            # Extract the video URL
            url = item.get("progressive_download_url")
            if url:
                video_urls.append(url)

# Check if we found any video URLs
if video_urls:
    for url in video_urls:
        print("Video URL: ", url)
else:
    print("No video URLs found.")

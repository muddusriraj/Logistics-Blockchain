import time
import random
import requests

tokenid=123
# List of places to visit
places = ['Depot', 'Place 1', 'Place 2', 'Place 3', 'Place 4', 'Place 5']

# Function to generate random weather and road conditions
def mintNFT(truckid, data, name, PUTTOKENIDHERE, place):
    tokenid = PUTTOKENIDHERE
    url = "https://api.verbwire.com/v1/nft/mint/mintFromMetadata"
    
    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"chain\"\r\n\r\ngoerli\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tokenId\"\r\n\r\n{tokenid}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\n{data}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"contractAddress\"\r\n\r\n0xb7C0C23849Cea222648d37153f3A5F7ea9AA3176\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\nData Commited by Truck ID#{truckid} at Location: {place}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n{name}\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "accept": "application/json",
        "content-type": "multipart/form-data; boundary=---011000010111000001101001",
        "X-API-Key": "sk_live_a59f451a-cd88-481f-8940-66ea032854ec"
    }
    
    response = requests.post(url, data=payload, headers=headers)

    print(response.text)
    for sing in response.text.split(","):
        with open("C:/Users/Sriraj/Documents/nft_transaction_data.txt", "a") as f:
            f.write("\n" + sing)
def get_random_weather():
    weather_options = ['cloudy', 'windy', 'rainy', 'stormy']
    return random.choice(weather_options)

def get_random_road_conditions():
    road_conditions_options = ['good', 'poor']
    return random.choice(road_conditions_options)
    
data=[]
truckid=random.randint(10000000, 99999999)
tokenidlist=[]
# Function to simulate truck stopping at each place with random variables
def truck_simulation(shipments):
    boxes=shipments
    for place in places:
        temperature = random.uniform(15, 20)
        weather = get_random_weather()
        fuel_used = random.uniform(50, 100)
        box_dropped = round(random.uniform(10, 15))
        boxes-=box_dropped
        road_conditions = get_random_road_conditions()
        
        data = [f"Place: {place}", f"Boxes In Truck: {boxes}", f"Boxes Dumped: {box_dropped}", f"Temperature: {temperature:.1f}°C", f"Weather: {weather}", f"Fuel Used: {fuel_used:.2f} liters", f"Road Conditions: {road_conditions}"]
        tokenid=+1
        tokenidlist.append(tokenid)
        time.sleep(3)
        mintNFT(truckid, data, "TruckCommit", tokenid, place)
        # Simulate the truck's stop by sleeping for a fixed duration (e.g., 2 seconds)
    temperature = random.uniform(15, 20)
    weather = get_random_weather()
    fuel_used = random.uniform(50, 100)
    box_dropped = boxes
    boxes-=box_dropped
    road_conditions = get_random_road_conditions()
    data = ["Place: Final Stop", f"Boxes In Truck: {boxes}", f"Boxes Dumped: {box_dropped}", f"Temperature: {temperature:.1f}°C", f"Weather: {weather}", f"Fuel Used: {fuel_used:.2f} liters", f"Road Conditions: {road_conditions}"]
    mintNFT(truckid, data, "TruckCommit", tokenid, place)
    print(f"Truck has completed its route and returned to the Depot with {boxes} boxes left.")
    print("Token IDs: ")
    print(tokenidlist)

# Call the function to start the simulation
truck_simulation(100)

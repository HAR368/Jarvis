import asyncio
import os
import random
import time
from random import randint
from PIL import Image
import requests
from io import BytesIO
from dotenv import get_key
from time import sleep

# Load API Key
API_KEY = get_key('.env', 'HuggingFaceAPIKey')
if not API_KEY:
    raise ValueError("❌ HuggingFace API Key not found! Please check your .env file.")

API_URL = "https://api.airforce/v1/imagine2"  # Replace with actual API endpoint
headers = {"Authorization": f"Bearer {API_KEY}"}

# Ensure 'Data' folder exists
output_folder = "Data"
os.makedirs(output_folder, exist_ok=True)

# Function to open generated images
def open_images(prompt):
    folder_path = "Data"
    files = [f for f in os.listdir(folder_path) if f.startswith(prompt.replace(' ', '_')) and f.endswith(".png")]

    if not files:
        print(f"❌ No images found in {folder_path}.")
        return

    for image_file in files:
        image_path = os.path.join(folder_path, image_file)

        try:
            img = Image.open(image_path)
            print(f"✅ Opening image: {image_path}")
            img.show()
            sleep(1)

        except IOError:
            print(f"❌ Unable to open image: {image_path}")

# Function to send API requests asynchronously
async def query(prompt):
    params = {'prompt': prompt}
    try:
        response = await asyncio.to_thread(requests.get, API_URL, params=params)

        if response.status_code != 200:
            print(f"❌ API Error {response.status_code}: {response.text}")
            return None  # Return None instead of empty bytes to handle errors better
        
        return response.content  # Return the image content

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

# Function to generate images asynchronously
async def generate_images(prompt: str, num_images=4):
    tasks = []
    for _ in range(num_images):
        variation = random.choice(['high detail', 'vivid colors', 'wide angle', 'abstract style'])
        prompt_with_variation = f"{prompt}, {variation}"
        
        task = asyncio.create_task(query(prompt_with_variation))
        tasks.append(task)

    image_bytes_list = await asyncio.gather(*tasks)

    for i, image_bytes in enumerate(image_bytes_list):
        if image_bytes:  # Ensure image is valid before saving
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_path = os.path.join(output_folder, f"{prompt.replace(' ', '_')}_{timestamp}_{i + 1}.png")

            try:
                image = Image.open(BytesIO(image_bytes))
                image.save(file_path)
                print(f"✅ Image saved: {file_path}")

            except Exception as e:
                print(f"❌ Error saving image {i+1}: {e}")

# Wrapper function to handle event loop issues
def GenerateImages(prompt: str):
    loop = asyncio.get_event_loop()
    
    if loop.is_running():  # Prevent event loop conflicts
        loop.create_task(generate_images(prompt))
    else:
        asyncio.run(generate_images(prompt))

    open_images(prompt)

# Monitor ImageGeneration.data file for prompts
while True:
    try:
        with open(r"Frontend\Files\ImageGeneration.data", "r") as f:
            Data: str = f.read()

        Prompt, Status = Data.split(",")

        if Status.strip() == "True":
            print("Generating Images...")  
            GenerateImages(prompt=Prompt.strip())

            with open(r"Frontend\Files\ImageGeneration.data", "w") as f:
                f.write("False,False")
            break
        else:
            sleep(1)

    except Exception as e:
        print(f"❌ Error: {e}")  # Show error for debugging
        sleep(1)

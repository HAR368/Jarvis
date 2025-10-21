# from AppOpener import close, open as appopen
# from webbrowser import open as webopen #Import web browser functionality.
# from pywhatkit import search, playonyt #Import functions for Google search and YouTube playback.
# from dotenv import dotenv_values #Import doteny to manage environment variables.
# from bs4 import BeautifulSoup #Import BeautifulSoup for parsing HTML content.
# from rich import print  # Import rich for styled console output.
# from groq import Groq #Import Grog for Al chat functionalities.
# import webbrowser #Import webbrowser for opening URLs.
# import subprocess #Import subprocess for interacting with the system.
# import requests #Import requests for making HTTP requests.
# import keyboard #Import keyboard for keyboard-related actions.
# import asyncio #Import asyncin for asynchronous programming.
# import os #Import os for operating system functionalities. I

# #Load environment variables from the env file.
# env_vars = dotenv_values(".env")
# GroqAPIKey =env_vars.get("GroqAPIKey")

# #define css classes
# classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
#            "IZ6rdc", "05uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0e",
#            "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

# # Define a user-agent for making web requests.
# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# #Initialize the Grog client with the API key.
# client = Groq(api_key="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")

# #Predefined professional responses for user interactions.
# professional_responses = [
#      "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
#      "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
# ]
# #List to store chatbot messages.
# messages = []

# #System message to provide contest to the chathor.
# SystemChatBot =[{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letters, codes, application, essays, notes, songs, poems etc."}]

# # Function to perform a Google search.
# def GoogleSearch(Topic):
#     search (Topic) # Use pywhatkit's search function to perform a Google search.
#     return True # Indicate success.


# # Function to generate content using AI and save it to a file.
# def Content (Topic):
#     # Nested function to open a file in Notepad.
#     def OpenNotepad (File):
#         default_text_editor = 'notepad.exe' # Default text editor. I
#         subprocess.Popen([default_text_editor, File]) # Open the file in Notepad.

# # Nested function to generate content using the AI chatbot.
#     def ContentWriterAI (prompt):
#         messages.append({"role": "user", "content": f"{prompt}"}) # Add the user's prompt to messages.
    
#         completion = client.chat.completions.create(
#             model="mixtral-8x7b-32768", # Specify the AI model.
#             messages=SystemChatBot + messages, # Include system instructions and chat history.
#             max_tokens=2048, # Limit the maximum tokens in the response.
#             temperature=0.7, # Adjust response randomness.
#             top_p=1, # Use nucleus sampling for response diversity.
#             stream=True, # Enable streaming response. I
#             stop=None # Allow the model to determine stopping conditions.
#         )
#         Answer = " " # Initialize an empty string for the response.
    
#         # Process streamed response chunks.
#         for chunk in completion:
#             if chunk.choices[0].delta.content: # Check for content in the current chunk.
#                 Answer += chunk.choices[0].delta.content # Append the content to the answer.
    
#         Answer = Answer.replace("</s>", "") # Remove unwanted tokens from the response.
#         messages.append({"role": "assistant", "content": Answer}) # Add the AI's response to messages.
#         return Answer  
    
    
#     Topic: str = Topic.replace("Content", "") # Remove "Content" from the topic.
#     ContentByAI = ContentWriterAI(Topic) # Generate content using AI.
    
#     # Save the generated content to a text file.
#     with open(rf"Data\{Topic. lower().replace(' ','')}.txt", "w", encoding="utf-8") as file:
#         file.write(ContentByAI) # Write the content to the file.
#         file.close()

#     OpenNotepad (rf"Data\{Topic. lower().replace(' ','')}.txt") # Open the file in Notepad.
#     return True # Indicate success.


# # Function to search for a topic on YouTube.
# def YouTubeSearch(Topic):
#     Url4Search = f"https://www.youtube.com/results?search_query={Topic}" # Construct the Youtube search URL.
#     webbrowser.open(Url4Search) # Open the search URL in a web browser.
#     return True # Indicate success.

# # Function to play a video on YouTube.
# def PlayYoutube (query):
#     playonyt(query) # Use pywhatkit's playonyt function to play the video.
#     return True # Indicate success.

# # Function to ppen ap application or a relevant webpage.
# def OpenApp(app, sess=requests.session()):
#     try:
#         appopen(app, match_closest =True, output=True, throw_error=True) # Attempt to open the app.
#         return True # Indicate success.
    
#     except:
#         # Nested function to extract links from HTML content.
#         def extract_links(html):
#             if html is None:
#                 return [ ]
#             soup = BeautifulSoup(html, 'html.parser') # Parse the HTML content.
#             links = soup.find_all('a', {'jsname': 'UWckNb'}) # Find relevant links.
#             return [link.get('href') for link in links] # Return. the links.
    
    
#         # Nested function to perform a Google search and retrieve HTML.
#         def search_google(query):
#             url = f"https://www.google.com/search?q={query}" # Construct the Google search URL.
#             headers = {"User-Agent": useragent} # Use the predefined user-agent.
#             response = sess.get(url, headers=headers) # Perform the GET request.
            
#             if response.status_code == 200:
#                 return response.text # Return the HTML content.
#             else:
#                 print("Failed to retrieve search results.") # Print an error message.
#                 return None

#         html = search_google(app) # Perform the Google search.
        
#         if html:
#             link = extract_links(html)[0] # Extract the first link from the search results.
#             webopen(link) # Open the link in a web browser.
#         return True # Indicate success. I


# # Function to close an application.
# def CloseApp(app):
    
#     if "chrome" in app:
#         pass # Skip if the app is Chrome.
#     elif "vs code" in app:
#         pass
#     elif "python file" in app:
#         pass
#     else:
#         try:
#             close(app, match_closest =True, output=True, throw_error=True) # Attempt to close the app.
#             return True # Indicate success.
#         except:
#             return False # Indicate failure.

# # Function to execute system-level commands.
# def System(command):
    
#     # Nested function to mute the system volume.
#     def mute():
#         keyboard.press_and_release("volume mute") # Simulate the mute key press.
        
#     # Nested function to unmute the system volume.
#     def unmute():
#         keyboard.press_and_release("volume mute") # Simulate the unmute key press,
        
#     def volume_up():
#         keyboard.press_and_release("volume up") # Simulate the volume up key press.

#     # Nesten fonction to decrease the system volume.
#     def volume_down():
#         keyboard.press_and_release("volume down") # Simulate the volume down key press.
    
#     #Еxecute the soprooriace command.
#     if command == "mute":
#         mute()
#     elif command == "unmute":
#         unmute()
#     elif command == "volume up":
#         volume_up()
#     elif command == "volume down":
#         volume_down()
    
#     return True #Indicate success.

# #Asynchronous function to translare and execute user commands.
# async def TranslateAndExecute(commands: list[str]):

#     funcs = [] #List to store asunchronous tasks.
    
#     for command in commands:
        
#         if command.startswith("open "): # Handle "open" commands.
            
#             if "open it" in command: # Ignore "open it" commands.
#                 pass
            
#             if "open file" == command: # Ignore "open file" commands.
#                 pass
            
#             else:
#                 fun = asyncio.to_thread (OpenApp, command.removeprefix("open ")) # Schedule app opening.
#                 funcs.append(fun)
        
#         elif command.startswith("general"): # Placeholder for general commands.
#             pass

#         elif command.startswith("realtime "): # Placeholder for real-time commands.
#             pass
        
#         elif command.startswith("close"): # Handle "close" commands.
#             fun = asyncio.to_thread (CloseApp, command.removeprefix("close")) # Schedule app closing.
#             funcs.append(fun)

#         elif command.startswith("play "): # Handle "play" commands.
#             fun = asyncio.to_thread (PlayYoutube, command.removeprefix("play ")) # Schedule YouTube playback.
#             funcs.append(fun) 
            
#         elif command.startswith("content"): #Handle "content" commands.
#             fun = asyncio.to_thread (Content, command.removeprefix("content")) # Schedule content creation.
#             funcs.append(fun)
        
#         elif command.startswith("google search "): # Handle Google search commands.
#             fun = asyncio.to_thread (GoogleSearch, command.removeprefix("google search ")) # Schedule Google search.
#             funcs.append(fun)

#         elif command.startswith("youtube search "): # Handle YouTube search commands
#             fun = asyncio.to_thread (YouTubeSearch, command.removeprefix("youtube search ")) # Schedule YouTube search.
#             funcs.append(fun)
        
#         elif command.startswith("system"): #Handle system commands.
#             fun = asyncio.to_thread (System, command.removeprefix("system")) #Schedule system command.
#             funcs.append(fun)
#         else:
#             print("No Function Found. For (command}") #Print an error for unrecognized commands.
        
#     results = await asyncio.gather(*funcs) # Execute all tasks concurrently.

#     for result in results: # Process the results.
#         if isinstance(result, str): 
#             yield result
#         else:
#             yield result

# #Asynchronous function to automate command execution.
# async def Automation (commands: list[str]):
#     async for result in TranslateAndExecute(commands): # Translate and execute commands.
#         pass
#     return True # Indicate success.     

# if __name__ == "__main__":
#     asyncio.run(Automation(["open instagram", "open facebook", "open telegram", "play people", 'content song for me']))
  






from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os
import pyautogui
import cv2
import psutil
import speech_recognition as sr

# Load environment variables
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Initialize AI Client
client = Groq(api_key=GroqAPIKey)
messages = []

# Dictionary of popular websites
websites = {
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "whatsapp": "https://web.whatsapp.com",
    "twitter": "https://www.twitter.com",
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "linkedin": "https://www.linkedin.com",
    "gmail": "https://mail.google.com",
    "reddit": "https://www.reddit.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://stackoverflow.com",
    "tiktok": "https://www.tiktok.com",
    "snapchat": "https://www.snapchat.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.com",
    "ebay": "https://www.ebay.com",
    "discord": "https://www.discord.com",
    "zoom": "https://zoom.us",
    "skype": "https://www.skype.com",
    "microsoft": "https://www.microsoft.com",
    "apple": "https://www.apple.com",
    "spotify": "https://www.spotify.com",
    "soundcloud": "https://www.soundcloud.com",
    "telegram": "https://web.telegram.org",
    "yahoo": "https://www.yahoo.com",
    "bing": "https://www.bing.com",
    "wikipedia": "https://www.wikipedia.org",
    "adobe": "https://www.adobe.com",
    "dropbox": "https://www.dropbox.com",
    "paypal": "https://www.paypal.com",
    "quora": "https://www.quora.com",
    "canva": "https://www.canva.com",
    "figma": "https://www.figma.com",
    "medium": "https://www.medium.com",
    "coursera": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "khanacademy": "https://www.khanacademy.org",
    "weather": "https://www.weather.com",
    "cnn": "https://www.cnn.com",
    "bbc": "https://www.bbc.com",
    "nytimes": "https://www.nytimes.com",
    "forbes": "https://www.forbes.com",
    "bloomberg": "https://www.bloomberg.com",
    "nationalgeographic": "https://www.nationalgeographic.com"
}


# Define CSS classes
classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta", 
           "IZ6rdc", "05uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0e", 
           "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

# Define a user-agent
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# System message for chatbot
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'AI Assistant')}, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems, etc."}]

# Function to perform a Google search
def GoogleSearch(Topic):
    search(Topic)
    return True

# Function to generate content using AI
def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])
    
    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": prompt})
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )
        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        
        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer  
    
    Topic = Topic.replace("Content", "")
    ContentByAI = ContentWriterAI(Topic)
    file_path = rf"Data\{Topic.lower().replace(' ', '')}.txt"
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(ContentByAI)
    
    OpenNotepad(file_path)
    return True

# Function to search for a topic on YouTube
def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

# Function to play a video on YouTube
def PlayYoutube(video):
    playonyt(video)
    return True

# Function to take a photo using the webcam
def ClickPhoto():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("photo.jpg", frame)
        print("Photo saved as 'photo.jpg'")
    cam.release()

# Function to take a screenshot
def ClickScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot saved as 'screenshot.png'")


# Function to open an application or website
def OpenApp(app):
    try:
        success = appopen(app, match_closest=False, output=True, throw_error=False)
        if success:
            return True
        else:
            raise Exception("App not found")
    except:
        if app.lower() in websites:
            print(f"Application '{app}' not found. Opening website instead...")
            webopen(websites[app.lower()])
            return True
        else:
            print(f"Application '{app}' not found. No known website available.")
            return False


# Function to check if a Python script is running
def is_python_script_running():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if process.info['cmdline'] and any(arg.endswith('.py') for arg in process.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False


# Function to close the active browser tab, but not if a .py file is running
def CloseWebsite():
    if is_python_script_running():
        print("A Python script is currently running. Browser tab will not be closed.")
        return False
    try:
        pyautogui.hotkey('ctrl', 'w')
        print("Browser tab closed successfully.")
        return True
    except Exception as e:
        print(f"Error closing website: {e}")
        return False


# # Function to close an application
# def CloseApp(app):
#     protected_apps = ["chrome", "code", "vs code", "visual studio code", "python"]
    
#     if any(protected in app.lower() for protected in protected_apps):
#         print(f"Cannot close '{app}'. It is protected.")
#         return False
    
#     try:
#         close(app, match_closest=True, output=True, throw_error=False)
#         print(f"'{app}' closed successfully.")
#         return True
#     except:
#         print(f"Could not close '{app}'. App not found.")
#         return False


def CloseApp(app_name):
    app_mapping = {
        "word": "WINWORD.EXE",
        "excel": "EXCEL.EXE",
        "powerpoint": "POWERPNT.EXE",
        "notepad": "notepad.exe",
        "chrome": "chrome.exe",
        "firefox": "firefox.exe",
        "edge": "msedge.exe",
    }

    # Prevent VS Code or Python from being closed
    protected_apps = ["Code.exe", "python.exe", "cmd.exe"]

    if app_name.lower() in app_mapping:
        process_name = app_mapping[app_name.lower()]
    else:
        process_name = app_name + ".exe"  # Default assumption

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if process.info['name'].lower() == process_name.lower():
                if process.info['name'] in protected_apps:
                    print(f"❌ Protected app '{process.info['name']}' will NOT be closed.")
                    continue  # Skip protected apps
                os.system(f"taskkill /F /PID {process.info['pid']}")
                print(f"✅ Closed {process.info['name']}")
        except Exception as e:
            print(f"Error closing {app_name}: {e}")



# Function to confirm shutdown, restart, or sleep
def ConfirmAndExecute(action):
    confirmation = input(f"Are you sure you want to {action}? (yes/no): ")
    if confirmation.lower() == "yes":
        if action == "shutdown":
            os.system("shutdown /s /t 2")
        elif action == "restart":
            os.system("shutdown /r /t 2")
        elif action == "sleep":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        print(f"System {action} initiated!")
    else:
        print(f"{action.capitalize()} canceled.")


def CloseAppSafely(app_name):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            if process.info['name'] in ["Code.exe", "python.exe"]:  # Prevent closing VS Code & Python
                print(f"❌ Skipping protected app: {process.info['name']}")
                continue
            try:
                process.terminate()  # Graceful termination
                print(f"✅ Closed {process.info['name']}")
            except Exception as e:
                print(f"Error closing {process.info['name']}: {e}")



# Function to process commands asynchronously
async def TranslateAndExecute(commands: list[str]):
    funcs = []
    for command in commands:
        if command.startswith("open "):
            funcs.append(asyncio.to_thread(OpenApp, command.removeprefix("open ")))

        elif command.startswith("close "):
            app_or_site = command.removeprefix("close ")
            if app_or_site.lower() in websites:
                funcs.append(asyncio.to_thread(CloseWebsite))
            else:
                funcs.append(asyncio.to_thread(CloseApp, app_or_site))

        elif command.startswith("play "):
            funcs.append(asyncio.to_thread(PlayYoutube, command.removeprefix("play ")))

        elif command.startswith("google search "):
            funcs.append(asyncio.to_thread(GoogleSearch, command.removeprefix("google search ")))

        elif command == "click photo":
            funcs.append(asyncio.to_thread(ClickPhoto))

        elif command == "click screenshot":
            funcs.append(asyncio.to_thread(ClickScreenshot))

        elif command in ["shutdown", "restart", "sleep"]:
            funcs.append(asyncio.to_thread(ConfirmAndExecute, command))

        else:
            print(f"No function found for {command}")
    
    results = await asyncio.gather(*funcs)
    for result in results:
        yield result

# Asynchronous function to automate command execution
async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    return True

if __name__ == "__main__":
    asyncio.run(Automation(["take screenshot", "open excel","click photo", "open facebook", "sleep"]))

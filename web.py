import webbrowser
import time
import random
while True:
    sites = random.choice(['google.com','facebook.com','karthikdreams','youtube'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    break
    seconds = random.randrange(5,20)
    time.sleep(seconds)

    
    
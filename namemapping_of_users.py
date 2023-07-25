import time
from plyer import notification
import instaloader

# Dictionary to map real Instagram usernames to custom names
username_mapping = {
    "sambrina345": "Samundra2200",    
    # Add more entries as needed
}

def get_custom_name(username):
    # Look up the custom name for the given username in the mapping dictionary
    return username_mapping.get(username, username)

def check_for_story(username, login, password):
    L = instaloader.Instaloader()

    try:
        L.login(login, password)
        profile = instaloader.Profile.from_username(L.context, username)
        stories = L.get_stories(userids=[profile.userid])
        if stories:
            custom_name = get_custom_name(username)
            notification_title = f"{custom_name} uploaded a story!"
            notification_message = "Check it out now."
            notification.notify(title=notification_title, message=notification_message, timeout=10)
        else:
            print(f"No new stories found for {username}.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' not found.")
    except instaloader.exceptions.ConnectionException:
        print("Failed to connect to Instagram. Check your internet connection.")
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid login credentials. Please check your username and password.")

if __name__ == "__main__":
    favorite_instagram_users = ["username"] #username of the profile you want to follow about their story
    your_instagram_login = "your Instagram login" # your Instagram login credentials
    your_instagram_password = "your Instagram password" # your your Instagram password
    check_interval = 60 * 5 # Check for new stories every 5 minutes. Time for example 60*5=300sec meaning 5 minutes.

    while True:
        for username in favorite_instagram_users:
            check_for_story(username, your_instagram_login, your_instagram_password)
        time.sleep(check_interval)

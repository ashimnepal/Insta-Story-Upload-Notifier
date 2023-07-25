import time
from plyer import notification
import instaloader

def check_for_story(username, login, password):
    L = instaloader.Instaloader()
    try:
        L.login(login, password)
        profile = instaloader.Profile.from_username(L.context, username)
        stories = L.get_stories(userids=[profile.userid])
        if stories:
            notification_title = f"{username} uploaded a story!"
            notification_message = "Check it out now."
            notification.notify(title=notification_title, message=notification_message, timeout=10)
        else:
            print("No new stories found.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' not found.")
    except instaloader.exceptions.ConnectionException:
        print("Failed to connect to Instagram. Check your internet connection.")
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid login credentials. Please check your username and password.")

if __name__ == "__main__":
    favorite_instagram_user = "Instagram username"  # Replace with the Instagram username you want to follow
    your_instagram_login = "your Instagram login"  # Replace with your Instagram login
    your_instagram_password = "your Instagram password"  # Replace with your Instagram password
    check_interval = 60 * 5  # Check for new stories every 5 minutes. Time for example 60*5=300sec meaning 5 minutes.

    while True:
        check_for_story(favorite_instagram_user, your_instagram_login, your_instagram_password)
        time.sleep(check_interval)

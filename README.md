# Insta-Story-Upload-Notifier

It's a good place to include a brief description of your project, installation instructions, usage examples, and other relevant details.

Here's a basic `Readme.md` template you can use for your repository:

```markdown
# Instagram Story Notification

This Python script monitors multiple favorite Instagram users and sends notifications when any of them upload a story.

## Features

- Supports monitoring multiple Instagram users for story updates.
- Allows you to set custom names for the Instagram users to be displayed in notifications.

## Prerequisites

- Python (version 3.10)



## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/instagram-story-notification.git
```

2. Install the required Python libraries:

```bash
pip install instaloader plyer
```

## Usage

1. Open the `instagram_story_notification.py` file and modify the following variables:
   - `favorite_instagram_users`: Add the real Instagram usernames you want to monitor.
   - `your_instagram_login`: Replace with your Instagram login.
   - `your_instagram_password`: Replace with your Instagram password.

2. Save the changes to the file.

3. Run the script:

```bash
python instagram_story_notification.py
```

The script will check for new stories from the specified Instagram users every 5 minutes (adjust the interval as needed).

## Custom Names

You can customize the display names of the Instagram users in the notifications. Modify the `username_mapping` dictionary in the script to map the real usernames to your desired custom names.

```python
# Dictionary to map real Instagram usernames to custom names
username_mapping = {
    "real_username_1": "Custom Name 1",
    "real_username_2": "Custom Name 2",
    "real_username_3": "Custom Name 3",
    # Add more entries as needed
}
```

## Disclaimer

This script uses the Instagram Graph API for monitoring story updates. Make sure to comply with Instagram's terms of service and usage limits.


```

Replace the placeholders (e.g., `your_username`) with your actual GitHub username and adjust the Python library versions based on the requirements of your project.

After creating the `Readme.md` file, you can add, commit, and push it to your GitHub repository using Git commands. The contents of the `Readme.md` will be displayed on your repository's main page on GitHub.

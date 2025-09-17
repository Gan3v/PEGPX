
# Webhook Management Tool (PEGPX)

This Python script, `PEGPX.py`, provides a set of utilities for managing and interacting with Discord webhooks. You can perform various tasks such as sending messages, editing webhook names, deleting webhooks, and more—all through a simple terminal interface.

> **Note:** This tool is intended for educational purposes only. Misuse of this tool could lead to violations of Discord's terms of service.

## Features

- **Webhook Management:**
  - Save, select, and manage your webhooks.
  - Add new webhooks and store them for future use.

- **Core Webhook Functions:**
  - **Change Webhook Name:** Change the name of a webhook.
  - **Spam Webhook:** Send repeated messages to a webhook.
  - **Mass Spam:** Send messages in parallel using threads.
  - **Send Embed:** Send rich embeds with customizable title, description, and color.
  - **Send File:** Upload files to webhooks.
  - **Webhook Info:** Retrieve details of a webhook (e.g., name, channel ID).
  - **Clone Webhook:** Copy a webhook's settings (name and avatar) to another webhook.
  - **Delete Webhook:** Permanently delete a webhook.

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.x
- `requests` (used for making HTTP requests)
- `colorama` (used for adding color to the terminal output)

You can install the required Python packages using `pip`:

pip install requests colorama

How to Use

    Clone or Download the Repository:

    Clone this repository using Git or download it as a ZIP file.

git clone https://github.com/yourusername/webhook-management.git

Run the Script:

Navigate to the directory containing the script and run the PEGPX.py file:

    python PEGPX.py

    Interface:

    Once the script is running, you'll be presented with a text-based menu in the terminal. Here’s a quick rundown of what you can do:

        Select a Webhook: You can either choose from a list of saved webhooks or enter a new one manually.

        Change Webhook Name: Modify the name of an existing webhook.

        Spam Webhook: Send a message repeatedly to the selected webhook.

        Send Embed: Send a custom embed (rich content) to the webhook.

        Send File: Upload a file to the webhook.

        View Webhook Info: Get details about the webhook.

        Mass Spam: Send messages using multiple threads for a more intense spamming effect.

        Clone Webhook: Copy settings (name and avatar) from one webhook to another.

        Delete Webhook: Permanently remove a webhook.

        Save Webhook: Store your webhook URL for future use.

        Exit: Exit the script.

    After selecting an option, follow the on-screen prompts to perform your desired action.

Example Usage

$ python PEGPX.py

Once the program is running, select a webhook or enter one manually. After that, choose one of the actions from the menu (e.g., change the webhook name, send an embed, etc.).
How It Works

This script interacts with Discord's webhook API, allowing you to perform various actions on a webhook URL.

    Webhook URLs: Webhook URLs are used to send data to Discord channels. They can be created by anyone with permission to manage a channel.

    Threads: When spamming messages or using mass spam, threads are used to send multiple requests in parallel, increasing the number of messages sent in a short time.

The program uses requests for handling HTTP requests and colorama for colorful terminal output.
Security and Disclaimer

    Use Responsibly: This tool should only be used for legitimate and ethical purposes. Misuse (e.g., spamming or flooding webhooks) can result in account suspension or banning.

    Webhook URLs: Always ensure you have permission to use the webhooks you're interacting with.

Contributing

Feel free to open issues or create pull requests to improve this tool! Here are some ways you can contribute:

    Fix bugs or suggest improvements.

    Add new features.

    Enhance the user interface or terminal output.

License

This project is open-source and available under the MIT License.
Acknowledgements

    Thanks to colorama for providing terminal color features.

    Special thanks to Discord API for making webhooks so powerful and easy to use.

Created by b4for3 | Made with ❤️

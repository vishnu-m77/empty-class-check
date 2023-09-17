# empty-class-check

## Description
This tool automates checking for an empty space in a class. Run the code on a device until a space opens for the class. This tool uses a Discord Webhook URL to send an automated message on a Discord channel. The suggestion is to create a private channel in Discord. Create a new Webhook by going to channel settings -> Integrations -> Create Webhook. Copy the link to the `params.json` file.

## Motivation
I was trying to get into ECON 212 for Fall 2023 and the class was full. Instead of spending my time all day checking for an empty space on the Schedule of Classes website, I wrote this script which checks for an empty space. The code ran for 3 days before I get a message saying that there was an empty space in the class. I am successfully enrolled in the class thanks to this script.

## Parameters
- `DISCORD_WEBHOOK_URL` : The link for the Discord Webhook
- `course_name` : Ensure that this matches the dropdown options on the Schedule of Classes website.
- `course_num` : The code number for the course

## Remarks
Feel free to add more features to this project and make it more useful!


# NTCSC Discord Bot Code Setup Guide
1. Pull code from GitHub repository (https://github.com/NoahBlack012/ntcscDiscordBot)
2. Go to discord developer portal (https://discord.com/developers/applications)
3. Click new application
4. Go to bot tab 
    1. Click add bot
5. Go to OAuth2/URL generator
    1. Click bot checkbox
    2. Click administrator checkbox under bot permissions
    3. Copy link at bottom of page
6. Paste link copied into new tab and add bot to test server (You must create your own server on discord)
7. Open code pulled from GitHub repository in code editor 
    1. Open bot.py file 
    2. Go back to discord developer portal/bot tab and press reset token then copy token
    3. Paste copied token in the place of YOUR_TOKEN_HERE on the final line of the file
8. To run bot: Run bot.py and run commands in the server you added the bot to

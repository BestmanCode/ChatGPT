# ChatGPT <img src="https://github.com/acheong08/ChatGPT/blob/main/logo.png?raw=true" width="7%"></img>

[![PyPi](https://img.shields.io/pypi/v/revChatGPT.svg)](https://pypi.python.org/pypi/revChatGPT)
[![Downloads](https://static.pepy.tech/badge/revchatgpt)](https://pypi.python.org/pypi/revChatGPT)

Reverse Engineered ChatGPT API by OpenAI. Extensible for chatbots etc.

> ## Support my work
> Make a pull request and fix my bad code. <br>
> or <br>
> <a href="https://www.buymeacoffee.com/acheong08" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-black.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

> ## Other notes
> - There is a 60 requests per minute rate limit on the public proxy server which is costing me $5 per day to run
> - I am using a total of 5 servers and a load balancer to handle around 500GB of traffic per day
> - I will begin selling access to private servers without the rate limits in the coming days
>   - All proceeds from this will be used to fund the public server.
>   - After the first few purchases which will cover the cost of the existing servers, I will begin adding more servers to the public load balancer with the proceeds and start to lower the public rate limits
>   - Leave a comment under this Twitter thread if you have any thoughts on this: https://twitter.com/GodlyIgnorance/status/1629839371682865152
> - I have 18 days before I run out of credit to run the public servers

# V1 Standard ChatGPT
> ## Update 2023/02/14 9:00 PM GMT+8: It is working. Use this.

## Installation
`pip3 install revChatGPT`

## Configuration

1. Create account on [OpenAI's ChatGPT](https://chat.openai.com/)
2. Save your email and password

### Authentication method: (Choose 1)
#### Email/Password
Not supported for Google/Microsoft accounts
```json
{
  "email": "email",
  "password": "your password"
}
```
#### Session token
Comes from cookies on chat.openai.com as "__Secure-next-auth.session-token"

```json
{
  "session_token": "..."
}
```
#### Access token
https://chat.openai.com/api/auth/session
```json
{
  "access_token": "<access_token>"
}
```

#### Optional configuration:

```json
{
  "conversation_id": "UUID...",
  "parent_id": "UUID...",
  "proxy": "...",
  "paid": false
}
```

3. Save this as `$HOME/.config/revChatGPT/config.json`
4. If you are using Windows, you will need to create an environment variable named ```HOME``` and set it to your home profile for the script to be able to locate the config.json file.

## Usage

### Command line

`python3 -m revChatGPT.V1`

```
!help - Show this message
!reset - Forget the current conversation
!config - Show the current configuration
!rollback x - Rollback the conversation (x being the number of messages to rollback)
!exit - Exit this program
```

### Developer API

#### Basic example (streamed):
```python
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "<your email>",
  "password": "<your password>"
})

print("Chatbot: ")
prev_text = ""
for data in chatbot.ask(
    "Hello world",
):
    message = data["message"][len(prev_text) :]
    print(message, end="", flush=True)
    prev_text = data["message"]
print()
```

#### Basic example (single result):

```python
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "<your email>",
  "password": "<your password>"
})

prompt = "how many beaches does portugal have?"
response = ""

for data in chatbot.ask(
  prompt
):
    response = data["message"]

print(response)
```
#### All API methods
Refer to the [wiki](https://github.com/acheong08/ChatGPT/wiki/V1) for advanced developer usage.


> ## V2 Fast ChatGPT API is dead (broken by OpenAI)



# Awesome ChatGPT

[My list](https://github.com/stars/acheong08/lists/awesome-chatgpt)

If you have a cool project you want added to the list, open an issue.

# Disclaimers

This is not an official OpenAI product. This is a personal project and is not affiliated with OpenAI in any way. Don't sue me

# Credits

- [virtualharby](https://twitter.com/virtualharby) - Memes for emotional support
- [All contributors](https://github.com/acheong08/ChatGPT/graphs/contributors) - Pull requests

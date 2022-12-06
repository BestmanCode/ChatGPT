from revChatGPT.revChatGPT import Chatbot
import json
from sys import argv
import textwrap


def get_input(prompt):
    # prompt for input
    lines = []
    print(prompt, end="")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Join the lines, separated by newlines, and print the result
    user_input = "\n".join(lines)
    # print(user_input)
    return user_input


if __name__ == "__main__":
    print("""
    ChatGPT - A command-line interface to OpenAI's ChatGPT (https://chat.openai.com/chat)
    Repo: github.com/acheong08/ChatGPT
    """)
    print("Type '!help' to show commands")
    print("Press enter twice to submit your question.\n")
    with open("config.json", "r") as f:
        config = json.load(f)
    chatbot = Chatbot(config)

    while True:
        prompt = get_input("\nYou:\n")
        if prompt.startswith("!"):
            if prompt == "!help":
                print("""
                !help - Show this message
                !reset - Forget the current conversation
                !refresh - Refresh the session authentication
                !rollback - Rollback the conversation by 1 message
                !config - Show the current configuration
                !exit - Exit the program
                """)
                continue
            elif prompt == "!reset":
                chatbot.reset_chat()
                print("Chat session reset.")
                continue
            elif prompt == "!refresh":
                chatbot.refresh_session()
                print("Session refreshed.\n")
                continue
            elif prompt == "!rollback":
                chatbot.rollback_conversation()
                print("Chat session rolled back.")
                continue
            elif prompt == "!config":
                print(json.dumps(config, indent=4))
                continue
            elif prompt == "!exit":
                break

        if '--text' not in argv:
            messages = []
            lines_printed = 0

            try:
                print("Chatbot: ")
                formatted_parts = []
                for message in chatbot.get_chat_response(prompt, output="stream"):
                    # Split the message by newlines
                    message_parts = message['message'].split('\n')

                    # Wrap each part separately
                    formatted_parts = []
                    for part in message_parts:
                        formatted_parts.extend(textwrap.wrap(part, width=80))
                        for formatted_line in formatted_parts:
                            if (len(formatted_parts) > lines_printed+1):
                                print(formatted_parts[lines_printed])
                                lines_printed += 1
                print(formatted_parts[lines_printed])
            except Exception as e:
                print("Something went wrong!")
                print(e)
                continue
        else:
            try:
                print("Chatbot: ")
                print(chatbot.get_chat_response(prompt)['message'])
            except Exception as e:
                print("Something went wrong!")
                print(e)
                continue

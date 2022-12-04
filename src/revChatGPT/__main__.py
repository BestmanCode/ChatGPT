from revChatGPT.revChatGPT import Chatbot
import json

def get_input(prompt):
  # prompt for input
  lines = []
  print(prompt,end="")
  while True:
      line = input()
      if line == "":
          break
      lines.append(line)

  # Join the lines, separated by newlines, and print the result
  user_input = "\n".join(lines)
  #print(user_input)
  return user_input

if __name__ == "__main__":
    print("""
    ChatGPT - A command-line interface to OpenAI's ChatGPT (https://chat.openai.com/chat)
    Repo: github.com/acheong08/ChatGPT
    """)
    print("Type '!exit' to exit")
    print("Press enter twice to submit your question.\n")
    with open("config.json", "r") as f:
            config = json.load(f)
    chatbot = Chatbot(config)
    import subprocess
    from subprocess import Popen
    import sys

    while True:
        prompt = get_input("You: ")
        if prompt == "!exit":
            break
        try:
            print("Please wait for ChatGPT to formulate its full response...")
            response = chatbot.get_chat_response(prompt)
        except Exception as e:
            print("Something went wrong!")
            print(e)
            continue
        # Erase the "Please wait" line when done waiting
        sys.stdout.write("\033[F\033[K")

        print("\n")
        print("Chatbot:", response['message'])
        print("\n")

        arguments=list(sys.argv)
        del arguments[0]

        if len(arguments)>1:
            try:
                process.terminate()
            except NameError:
                print("")

            # Use `python3 ./revChatGPT.py say -v Samantha -r 600` to make a Mac speak the output
            # using the Samantha voice at 600 words per minute (about 3x)
            # or `python3 ./revChatGPT.py espeak -v en -s 600` to do something similar using espeak (untested)
            arguments.append('"' + response['message'] + '"')
            process = Popen(arguments)

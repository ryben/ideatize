import os

from openai import OpenAI


class Agent:

    def __init__(self, role: str, instructions: str, capabilities, alias=""):
        self.role = role
        self.instructions = instructions
        self.capabilities = capabilities
        self.alias = alias

    def start(self):

        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        # Step 1: Create an Assistant
        my_assistant = client.beta.assistants.create(
            model="gpt-4-1106-preview",
            instructions=self.instructions,
            name=self.alias
        )

        # Step 2: Create a Thread
        my_thread = client.beta.threads.create()

        # Step 3: Add a Message to a Thread
        my_thread_message = client.beta.threads.messages.create(
            thread_id=my_thread.id,
            role="user",
            content=self.instructions,
        )

        # Step 4: Run the Assistant
        my_run = client.beta.threads.runs.create(
            thread_id=my_thread.id,
            assistant_id=my_assistant.id,
            instructions="follow instructions"
        )

        # Step 5: Periodically retrieve the Run to check on its status to see if it has moved to completed
        while my_run.status != "completed":
            keep_retrieving_run = client.beta.threads.runs.retrieve(
                thread_id=my_thread.id,
                run_id=my_run.id
            )
            print(f"Run status: {keep_retrieving_run.status}")

            if keep_retrieving_run.status == "completed":
                print("\n")
                break

        # Step 6: Retrieve the Messages added by the Assistant to the Thread
        all_messages = client.beta.threads.messages.list(
            thread_id=my_thread.id
        )

        print("------------------------------------------------------------ \n")

        print(f"User: {my_thread_message.content[0].text.value}")
        print(f"Assistant: {all_messages.data[0].content[0].text.value}")

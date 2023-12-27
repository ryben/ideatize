import os

from openai import OpenAI

from skills.BaseTask import BaseTask


class LLM(BaseTask):
    def __init__(self):
        super().__init__()

    def execute(self, inputs):
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        instructions = self.details
        input_key = list(inputs.keys())[0]
        input_value = list(inputs.values())[0]
        instructions = instructions.replace("{" + input_key + "}", input_value)

        # Step 1: Create an Assistant
        my_assistant = client.beta.assistants.create(
            model="gpt-4-1106-preview",
            instructions="",
            name="Rey"
        )

        # Step 2: Create a Thread
        my_thread = client.beta.threads.create()

        print(f"Running instructions: {instructions}")

        # Step 3: Add a Message to a Thread
        my_thread_message = client.beta.threads.messages.create(
            thread_id=my_thread.id,
            role="user",
            content=instructions,
        )

        # Step 4: Run the Assistant
        my_run = client.beta.threads.runs.create(
            thread_id=my_thread.id,
            assistant_id=my_assistant.id,
            instructions=""
        )

        prev_status = ""
        # Step 5: Periodically retrieve the Run to check on its status to see if it has moved to completed
        while my_run.status != "completed":
            keep_retrieving_run = client.beta.threads.runs.retrieve(
                thread_id=my_thread.id,
                run_id=my_run.id
            )

            if prev_status != keep_retrieving_run.status:
                prev_status = keep_retrieving_run.status
                print(f"Run status: {prev_status} ", end=" ")
            else:
                print(f".", end="")

            if keep_retrieving_run.status == "completed":
                print("\n")
                break

        # Step 6: Retrieve the Messages added by the Assistant to the Thread
        all_messages = client.beta.threads.messages.list(
            thread_id=my_thread.id
        )

        print("------------------------------------------------------------ \n")

        print(f"User: {my_thread_message.content[0].text.value}")

        output = f"Assistant: {all_messages.data[0].content[0].text.value}"
        print(output)

        return output

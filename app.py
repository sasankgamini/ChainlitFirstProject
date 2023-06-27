import chainlit as cl

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()

#enter "chainlit run app.py -w" in terminal to run application. 
#the -w is to enable auto-reloading so you don't need to restart server any time you make changes

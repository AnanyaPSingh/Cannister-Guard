# File: agent-fetchai/agent.py

import re
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

# Import the logic from Developer B's file
from logic import get_canister_status_message
from message_logger import log_incoming, log_outgoing

# --- Agent Configuration ---
AGENT_SEED = "canister_guard_agent_secret_seed_phrase__make_this_unique2"
agent = Agent(name="canister_guard_agent", seed=AGENT_SEED, mailbox=True)
fund_agent_if_low(agent.wallet.address())

class Message(Model):
    text: str

# Regex to find an ICP canister ID in a string of text
CANISTER_ID_REGEX = r'([a-z0-9]{5}-){4,}[a-z0-9]{3}'

@agent.on_message(model=Message)
async def handle_message(ctx: Context, sender: str, msg: Message):
    # Enhanced logging for message tracking
    print(f"\n📨 MESSAGE RECEIVED:")
    print(f"   From: {sender}")
    print(f"   Content: {msg.text}")
    print(f"   Time: {ctx.storage.get('timestamp', 'N/A')}")
    print("-" * 50)
    
    # Log incoming message
    log_incoming(sender, msg.text)
    
    ctx.logger.info(f"Received message from {sender}: {msg.text}")

    # Step 1: Parse the user's input to find a canister ID
    match = re.search(CANISTER_ID_REGEX, msg.text)

    if not match:
        # UNHAPPY PATH 1: No Canister ID found in the message
        ctx.logger.info("No canister ID found in message.")
        error_message = (
            "I couldn't find a valid canister ID in your message. "
            "Please include a valid ICP canister ID (e.g., 'uxrrr-q7777-77774-qaaaq-cai') "
            "in your request."
        )
        
        print(f"❌ ERROR RESPONSE:")
        print(f"   To: {sender}")
        print(f"   Content: {error_message}")
        print("-" * 50)
        
        # Log outgoing error message
        log_outgoing(sender, error_message, status="error")
        
        await ctx.send(sender, Message(text=error_message))
        return

    target_canister_id = match.group(0)

    # Step 2: Try to get the status, handling any potential errors
    try:
        ctx.logger.info(f"Found canister ID: {target_canister_id}. Getting status...")

        # Call the logic function to get the canister status
        # This will automatically fetch from the local backend canister
        reply_text = get_canister_status_message()

        print(f"✅ SUCCESS RESPONSE:")
        print(f"   To: {sender}")
        print(f"   Content: {reply_text}")
        print("-" * 50)

        # Log outgoing success message
        log_outgoing(sender, reply_text, status="success")

        await ctx.send(sender, Message(text=reply_text))

    except Exception as e:
        # UNHAPPY PATH 2: The logic function failed for some reason
        ctx.logger.error(f"An error occurred while getting status: {e}")
        error_message = (
            f"Sorry, an unexpected error occurred while checking the canister status. "
            f"Please make sure the backend is running locally and try again."
        )
        
        print(f"❌ ERROR RESPONSE:")
        print(f"   To: {sender}")
        print(f"   Content: {error_message}")
        print("-" * 50)
        
        # Log outgoing error message
        log_outgoing(sender, error_message, status="error")
        
        await ctx.send(sender, Message(text=error_message))

if __name__ == "__main__":
    print(f"🚀 CanisterGuard Agent Starting...")
    print(f"Agent address: {agent.address}")
    print(f"Agent name: {agent.name}")
    print(f"Ready to receive messages!")
    print(f"Send a message with a canister ID to get status information.")
    print(f"Example: 'Check status of uxrrr-q7777-77774-qaaaq-cai'")
    print("-" * 50)
    agent.run()

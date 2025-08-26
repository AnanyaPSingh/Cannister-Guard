import asyncio
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

# Define the address of the agent you want to test
TARGET_AGENT_ADDRESS = "agent1q09ygn5sjry43z85zzkqyqlehftsza6hlmdzquxwyfyytgnxjnrfcvwdq2h"

# Define a message model that both agents understand
class Message(Model):
    text: str

# Create the sender agent
sender_agent = Agent(
    name="test_sender",
    seed="test_sender_seed",
    port=8001,
    endpoint="wss://agents.fetch.ai/testnet"  # Local testing
)


fund_agent_if_low(sender_agent.wallet.address())

# When the sender agent starts, send a message to the target agent
@sender_agent.on_event("startup")
async def send_test_message(ctx: Context):
    test_message_text = "Hey agent, what is the status of the canister qhbym-qaaaa-aaaaa-aaafq-cai?"
    ctx.logger.info(f"Sending message to {TARGET_AGENT_ADDRESS}: '{test_message_text}'")

    # Send message to target agent
    await ctx.send(TARGET_AGENT_ADDRESS, Message(text=test_message_text))

# Also handle replies (if the main agent responds)
@sender_agent.on_message(model=Message)
async def handle_reply(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Got reply from {sender}: {msg.text}")

if __name__ == "__main__":
    # Run the sender agent
    sender_agent.run()

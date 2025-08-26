# File: agent-fetchai/agent.py

import re
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

# Import the logic function (mock or real implementation)
from logic import get_canister_status_message

# --- Agent Configuration ---
AGENT_SEED = "canister_guard_agent_secret_seed_phrase__make_this_unique"
agent = Agent(
    name="canister_guard_agent",
    seed=AGENT_SEED,
    port=8000,
    endpoint="wss://agents.fetch.ai/testnet"  # Local testing
)


# Fund the agent if it has low balance (testnet faucet)
fund_agent_if_low(agent.wallet.address())

# --- Message Schema ---
class Message(Model):
    text: str

# Regex to match ICP canister IDs
CANISTER_ID_REGEX = r'([a-z0-9]{5}-){4,}[a-z0-9]{3}'

# --- Message Handler ---
@agent.on_message(model=Message)
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"📩 Received message from {sender}: {msg.text}")

    # Step 1: Look for a canister ID in the text
    match = re.search(CANISTER_ID_REGEX, msg.text)
    if not match:
        ctx.logger.info("❌ No canister ID found in message.")
        error_message = "I couldn't find a valid canister ID in your message. Please include the full ID."
        await ctx.send(sender, Message(text=error_message))
        return

    target_canister_id = match.group(0)

    # Step 2: Try to fetch status
    try:
        ctx.logger.info(f"🔍 Found canister ID: {target_canister_id}. Fetching status...")

        # Call Developer B’s logic (mock or real)
        reply_text = get_canister_status_message(target_canister_id)

        await ctx.send(sender, Message(text=reply_text))

    except Exception as e:
        ctx.logger.error(f"⚠️ Error while getting canister status: {e}")
        error_message = f"Sorry, an error occurred while checking {target_canister_id[:5]}.... Please try again later."
        await ctx.send(sender, Message(text=error_message))

# --- Run Agent ---
if __name__ == "__main__":
    print(f"🚀 Agent started! Address: {agent.address}")
    agent.run()

#!/usr/bin/env python3
"""
Check Agent Status and Registration
Diagnostic script to verify agent connectivity and registration
"""

from uagents import Agent
from uagents.setup import fund_agent_if_low

def check_agent_registration():
    """Check if the agent is properly registered"""
    
    # Create the same agent instance
    AGENT_SEED = "canister_guard_agent_secret_seed_phrase__make_this_unique2"
    agent = Agent(name="canister_guard_agent", seed=AGENT_SEED, mailbox=True)
    
    print("🔍 Agent Status Check")
    print("=" * 50)
    print(f"Agent Address: {agent.address}")
    print(f"Agent Name: {agent.name}")
    print(f"Agent Seed: {AGENT_SEED}")
    print(f"Mailbox Enabled: True (configured)")
    
    # Check if agent has funds
    try:
        fund_agent_if_low(agent.wallet.address())
        print("✅ Agent wallet funded")
    except Exception as e:
        print(f"❌ Agent funding issue: {e}")
    
    print("\n🌐 AgentVerse Visibility:")
    print("1. Go to: https://agentverse.ai")
    print("2. Search for your agent address:")
    print(f"   {agent.address}")
    print("3. Or use the direct inspector URL:")
    print(f"   https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8000&address={agent.address}")
    
    print("\n📋 Troubleshooting Steps:")
    print("1. ✅ Make sure the agent is running: python3 agent.py")
    print("2. ⏳ Wait 2-3 minutes for registration to propagate")
    print("3. 🔍 Check AgentVerse at: https://agentverse.ai")
    print("4. 🔗 Try the direct inspector URL from agent logs")
    print("5. 🌐 Ensure you have internet connectivity")
    print("6. 🔄 Restart the agent if needed")
    
    print("\n💡 Common Issues:")
    print("- Agent needs time to register (2-3 minutes)")
    print("- AgentVerse cache might need refresh")
    print("- Network connectivity issues")
    print("- Agent not running or crashed")

if __name__ == "__main__":
    check_agent_registration()

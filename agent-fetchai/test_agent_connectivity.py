#!/usr/bin/env python3
"""
Test Agent Connectivity
Simple test to verify agent is working properly
"""

import asyncio
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class TestMessage(Model):
    text: str

def test_agent_basic():
    """Test basic agent functionality"""
    print("🧪 Testing Agent Basic Functionality...")
    
    # Create agent
    AGENT_SEED = "canister_guard_agent_secret_seed_phrase__make_this_unique2"
    agent = Agent(name="canister_guard_agent", seed=AGENT_SEED, mailbox=True)
    
    print(f"✅ Agent created successfully")
    print(f"   Address: {agent.address}")
    print(f"   Name: {agent.name}")
    
    # Test funding
    try:
        fund_agent_if_low(agent.wallet.address())
        print("✅ Agent wallet funded")
    except Exception as e:
        print(f"❌ Funding issue: {e}")
    
    print("\n🎯 Next Steps:")
    print("1. Run: python3 agent.py")
    print("2. Wait 2-3 minutes")
    print("3. Check: https://agentverse.ai")
    print("4. Search for your agent address")

if __name__ == "__main__":
    test_agent_basic()

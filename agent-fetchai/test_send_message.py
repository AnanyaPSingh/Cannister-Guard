#!/usr/bin/env python3
"""
Test Send Message to Agent
Programmatically send test messages to the CanisterGuard agent
"""

import asyncio
import aiohttp
import json
from uagents import Agent, Context, Model

class Message(Model):
    text: str

async def send_test_message():
    """Send a test message to the agent"""
    
    # Agent details
    agent_address = "agent1qf45f8r9727vznytkmsg9n5my7mg0uc9l47q7k5cz228eq34pqvlvv0nceh"
    local_url = "http://127.0.0.1:8000"
    
    # Test message
    test_message = Message(text="Check status of uxrrr-q7777-77774-qaaaq-cai")
    
    print("🧪 Sending Test Message to Agent...")
    print(f"Agent Address: {agent_address}")
    print(f"Message: {test_message.text}")
    print("-" * 50)
    
    try:
        # Send message via local HTTP endpoint
        async with aiohttp.ClientSession() as session:
            payload = {
                "message": {
                    "text": test_message.text
                },
                "sender": "test_user"
            }
            
            async with session.post(f"{local_url}/submit", json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    print("✅ Message sent successfully!")
                    print(f"Response: {result}")
                else:
                    print(f"❌ Failed to send message: {response.status}")
                    print(await response.text())
                    
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        print("\n💡 Make sure:")
        print("1. The agent is running: python3 agent.py")
        print("2. The agent is accessible at: http://127.0.0.1:8000")
        print("3. Try using AgentVerse instead: https://agentverse.ai")

def show_manual_instructions():
    """Show manual instructions for testing"""
    print("\n📋 Manual Testing Instructions:")
    print("=" * 50)
    print("1. Make sure agent is running:")
    print("   source myenv/bin/activate && python3 agent.py")
    print()
    print("2. Open AgentVerse in browser:")
    print("   https://agentverse.ai")
    print()
    print("3. Search for your agent:")
    print("   agent1qf45f8r9727vznytkmsg9n5my7mg0uc9l47q7k5cz228eq34pqvlvv0nceh")
    print()
    print("4. Send this message:")
    print("   Check status of uxrrr-q7777-77774-qaaaq-cai")
    print()
    print("5. Or use direct inspector URL:")
    print("   https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8000&address=agent1qf45f8r9727vznytkmsg9n5my7mg0uc9l47q7k5cz228eq34pqvlvv0nceh")

if __name__ == "__main__":
    print("🚀 CanisterGuard Agent Message Testing")
    print("=" * 50)
    
    # Show manual instructions
    show_manual_instructions()
    
    # Try programmatic sending
    print("\n🤖 Attempting Programmatic Message Sending...")
    asyncio.run(send_test_message())

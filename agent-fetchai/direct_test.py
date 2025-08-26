#!/usr/bin/env python3
"""
Direct Test of CanisterGuard Agent
Test the agent logic directly without web interface
"""

from logic import get_canister_status_message
import re

def test_agent_logic():
    """Test the agent logic directly"""
    print("🧪 Direct Agent Logic Test")
    print("=" * 50)
    
    # Test cases
    test_messages = [
        "Check status of uxrrr-q7777-77774-qaaaq-cai",
        "How is my canister uxrrr-q7777-77774-qaaaq-cai doing?",
        "Get status for uxrrr-q7777-77774-qaaaq-cai",
        "Invalid message without canister ID",
        "Check status of invalid-canister-id"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n📝 Test {i}: {message}")
        print("-" * 40)
        
        # Extract canister ID using the same regex as the agent
        canister_id_regex = r'([a-z0-9]{5}-){4,}[a-z0-9]{3}'
        match = re.search(canister_id_regex, message)
        
        if match:
            canister_id = match.group(0)
            print(f"✅ Found canister ID: {canister_id}")
            
            try:
                # Call the logic function directly
                response = get_canister_status_message()
                print(f"✅ Response: {response}")
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print("❌ No valid canister ID found")
            print("Expected format: xxxxx-xxxxx-xxxxx-xxxxx-xxxxx-xxx")

def show_agent_status():
    """Show current agent status"""
    print("\n🔍 Agent Status Check")
    print("=" * 50)
    
    # Check if agent process is running
    import subprocess
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'python3 agent.py' in result.stdout:
            print("✅ Agent process is running")
        else:
            print("❌ Agent process not found")
    except:
        print("❌ Could not check agent process")
    
    # Check local server
    import requests
    try:
        response = requests.get('http://127.0.0.1:8000', timeout=5)
        print(f"✅ Local server responding: {response.status_code}")
    except:
        print("❌ Local server not accessible")
    
    print("\n💡 Alternative Testing Methods:")
    print("1. Test logic directly (this script)")
    print("2. Use AgentVerse (may take time to appear)")
    print("3. Check agent logs for registration status")

if __name__ == "__main__":
    show_agent_status()
    test_agent_logic()
    
    print("\n🎯 For Hackathon Demo:")
    print("1. Show this direct test working")
    print("2. Explain the agent architecture")
    print("3. Demonstrate the backend integration")
    print("4. Show the message logging system")

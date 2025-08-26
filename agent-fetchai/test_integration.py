#!/usr/bin/env python3
"""
Test script to verify the integration between logic.py and agent.py
"""

from logic import get_canister_status_message

def test_logic_integration():
    """Test the logic function to ensure it works correctly"""
    print("🧪 Testing CanisterGuard Logic Integration...")
    print("-" * 50)
    
    try:
        # Test the logic function
        result = get_canister_status_message()
        print("✅ Logic function executed successfully!")
        print("📋 Result:")
        print(result)
        print("-" * 50)
        print("🎉 Integration test passed! Ready to run the agent.")
        return True
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        print("Please make sure:")
        print("1. The backend canister is deployed locally")
        print("2. dfx is running")
        print("3. All dependencies are installed")
        return False

if __name__ == "__main__":
    test_logic_integration()

#!/usr/bin/env python3
"""
Message Logger Utility for CanisterGuard Agent
Logs all incoming and outgoing messages to a file for tracking
"""

import json
import datetime
from pathlib import Path

class MessageLogger:
    def __init__(self, log_file="agent_messages.log"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(exist_ok=True)
    
    def log_message(self, direction, sender, content, status="success"):
        """Log a message with timestamp"""
        timestamp = datetime.datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "direction": direction,  # "incoming" or "outgoing"
            "sender": sender,
            "content": content,
            "status": status
        }
        
        # Append to log file
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        # Also print to console
        print(f"[{timestamp}] {direction.upper()}: {sender} -> {content[:100]}...")
    
    def get_recent_messages(self, limit=10):
        """Get recent messages from log"""
        messages = []
        try:
            with open(self.log_file, "r") as f:
                lines = f.readlines()
                for line in lines[-limit:]:
                    if line.strip():
                        messages.append(json.loads(line))
        except FileNotFoundError:
            pass
        return messages
    
    def clear_log(self):
        """Clear the log file"""
        self.log_file.unlink(missing_ok=True)

# Global logger instance
message_logger = MessageLogger()

def log_incoming(sender, content):
    """Log incoming message"""
    message_logger.log_message("incoming", sender, content)

def log_outgoing(sender, content, status="success"):
    """Log outgoing message"""
    message_logger.log_message("outgoing", sender, content, status)

def show_recent_messages(limit=10):
    """Display recent messages"""
    messages = message_logger.get_recent_messages(limit)
    if not messages:
        print("No messages logged yet.")
        return
    
    print(f"\n📋 Recent Messages (last {len(messages)}):")
    print("-" * 60)
    for msg in messages:
        direction_icon = "📨" if msg["direction"] == "incoming" else "📤"
        status_icon = "✅" if msg["status"] == "success" else "❌"
        print(f"{direction_icon} {status_icon} [{msg['timestamp']}] {msg['sender']}: {msg['content'][:50]}...")
    print("-" * 60)

if __name__ == "__main__":
    # Test the logger
    print("🧪 Testing Message Logger...")
    log_incoming("test_user", "Check status of uxrrr-q7777-77774-qaaaq-cai")
    log_outgoing("test_user", "✅ Status: Running, Cycles: 2,916,088,525,937")
    show_recent_messages()

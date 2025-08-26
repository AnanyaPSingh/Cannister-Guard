#!/usr/bin/env python3
"""
View Message History for CanisterGuard Agent
Simple utility to view recent messages and logs
"""

from message_logger import show_recent_messages
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="View CanisterGuard Agent Messages")
    parser.add_argument("--limit", "-l", type=int, default=10, 
                       help="Number of recent messages to show (default: 10)")
    parser.add_argument("--clear", "-c", action="store_true",
                       help="Clear the message log")
    parser.add_argument("--file", "-f", action="store_true",
                       help="Show the raw log file content")
    
    args = parser.parse_args()
    
    if args.clear:
        from message_logger import message_logger
        message_logger.clear_log()
        print("🗑️ Message log cleared!")
        return
    
    if args.file:
        log_file = "agent_messages.log"
        if os.path.exists(log_file):
            print(f"📄 Raw log file content ({log_file}):")
            print("-" * 60)
            with open(log_file, "r") as f:
                print(f.read())
        else:
            print("📄 No log file found yet.")
        return
    
    # Show recent messages
    show_recent_messages(args.limit)

if __name__ == "__main__":
    main()

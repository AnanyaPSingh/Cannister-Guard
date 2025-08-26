# CanisterGuard Agent (Fetch.ai uAgent)

This directory contains the AI agent implementation for CanisterGuard, built using Fetch.ai's uAgents framework.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Backend canister deployed locally (see `../backend-icp/`)
- dfx running locally

### Setup

1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Test the integration:**
```bash
python3 test_integration.py
```

4. **Run the agent:**
```bash
python3 agent.py
```

## 📁 File Structure

- `agent.py` - Main uAgent implementation with message handling
- `logic.py` - Core logic for fetching canister status
- `test_integration.py` - Integration test script
- `message_logger.py` - Message tracking and logging utility
- `view_messages.py` - View message history and logs
- `requirements.txt` - Python dependencies

## 🔧 How It Works

1. **User Input**: Agent receives messages containing canister IDs
2. **Parsing**: Regex extracts canister ID from user message
3. **Status Fetching**: Calls local ICP canister via dfx
4. **Response**: Returns formatted status information

## 🧪 Testing

Run the integration test to verify everything works:
```bash
python3 test_integration.py
```

## 📨 Message Tracking

The agent automatically logs all incoming and outgoing messages. You can view them using:

```bash
# View recent messages
python3 view_messages.py

# View more messages
python3 view_messages.py --limit 20

# View raw log file
python3 view_messages.py --file

# Clear message log
python3 view_messages.py --clear
```

**Message logs are saved to `agent_messages.log` for persistent tracking.**

## 📝 Usage Examples

The agent can handle messages like:
- "Check status of uxrrr-q7777-77774-qaaaq-cai"
- "How is my canister doing? uxrrr-q7777-77774-qaaaq-cai"
- "Get status for uxrrr-q7777-77774-qaaaq-cai"

## 🔗 Integration

This agent integrates with:
- **Backend**: `../backend-icp/canister_guard/` (ICP canister)
- **Logic**: `logic.py` (Status fetching and formatting)

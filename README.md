# CanisterGuard - NextGen Agents Hackathon Project

## 🚀 Project Overview

**CanisterGuard** is an AI-powered chatbot dashboard for blockchain applications (canisters) on the Internet Computer. Developers can simply ask in plain English, "Hey, how's my app doing?" and the AI assistant (Fetch.ai uAgent) will call our ICP canister to get live health stats and report back instantly.

## 🏗️ Project Architecture

```
CanisterGuard/
├── backend-icp/          # ICP Canister Backend (Developer A)
│   └── canister_guard/   # Motoko canister for status queries
└── agent-fetchai/        # AI Agent Logic (Developers B & C)
    ├── logic.py          # Core status logic (Developer B)
    └── agent.py          # Main agent & I/O handling (Developer C)
```

## 📊 Current Progress

### ✅ **Developer A - COMPLETED** 
- [x] Created GitHub repository structure
- [x] Set up ICP canister project with `dfx`
- [x] Implemented Motoko backend with `get_status` function
- [x] Deployed canister to Internet Computer mainnet
- [x] Tested canister functionality

**Backend Status:** ✅ **READY FOR INTEGRATION**

**Canister ID:** `[TO BE ADDED AFTER DEPLOYMENT]`

**Key Features Implemented:**
- `get_status(canisterIdText: Text)` function
- Returns canister cycles, memory size, and status
- Handles running/stopping/stopped states
- Proper error handling for invalid canister IDs

### 🔄 **Developer B - IN PROGRESS**
**Role:** Agent Logic Lead
**Task:** Implement `get_canister_status_message()` function in `agent-fetchai/logic.py`

**Next Steps:**
1. Clone repository and navigate to `agent-fetchai/`
2. Set up Python virtual environment
3. Install `uagents` dependency
4. Create `logic.py` with mock data implementation
5. Test function output formatting

### 🔄 **Developer C - PENDING**
**Role:** Agent I/O & Reliability Lead  
**Task:** Implement main agent in `agent-fetchai/agent.py`

**Next Steps:**
1. Wait for Developer B to complete `logic.py`
2. Clone repository and navigate to `agent-fetchai/`
3. Set up Python virtual environment
4. Install `uagents` and `ic-py` dependencies
5. Create `agent.py` with regex parsing and error handling
6. Integrate with Developer B's logic function

## 🛠️ Technical Stack

### Backend (ICP)
- **Language:** Motoko
- **Framework:** DFX (Internet Computer SDK)
- **Network:** Internet Computer Mainnet
- **Key Dependencies:** `mo:base/Principal`, `mo:base/Text`

### Agent (Fetch.ai)
- **Language:** Python 3.x
- **Framework:** uAgents
- **Key Dependencies:** `uagents`, `ic-py`
- **Environment:** Python virtual environment

## 🚀 Getting Started

### For Developer B (Agent Logic)
```bash
# Clone the repository
git clone [REPOSITORY_URL]
cd nextgen-canister-guard/agent-fetchai

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install uagents

# Create logic.py and implement get_canister_status_message()
```

### For Developer C (Agent I/O)
```bash
# Clone the repository
git clone [REPOSITORY_URL]
cd nextgen-canister-guard/agent-fetchai

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install uagents ic-py

# Create agent.py and implement main agent logic
```

## 🔗 Integration Points

### Backend → Agent Integration
- **Canister ID:** `[TO BE ADDED]`
- **Function:** `get_status(canisterIdText: Text)`
- **Response Format:** 
  ```motoko
  type CanisterStatus = {
      cycles: Nat;
      memory_size: Nat;
      status: Text;
  };
  ```

### Agent Logic Flow
1. User sends message with canister ID
2. Agent parses canister ID using regex
3. Agent calls `get_canister_status_message(canister_id)`
4. Logic function formats response for user
5. Agent sends formatted message back to user

## 🧪 Testing

### Backend Testing
```bash
cd backend-icp/canister_guard
dfx canister call --network ic [CANISTER_ID] get_status '("qhbym-qaaaa-aaaaa-aaafq-cai")'
```

### Agent Testing
```bash
cd agent-fetchai
python3 logic.py  # Test logic function
python3 agent.py  # Test full agent (after integration)
```

## 📝 Development Notes

- **Time Remaining:** < 8 hours
- **Priority:** Complete agent integration before real canister calls
- **Mock Data:** Use mock data initially, integrate real canister calls later
- **Error Handling:** Implement comprehensive error handling for all edge cases

## 🤝 Team Communication

- **Repository:** [GitHub URL]
- **Canister ID:** [To be shared by Developer A]
- **Integration Status:** Backend ready, awaiting agent completion

---

**Last Updated:** [Current Date]
**Status:** Backend Complete ✅ | Agent Development In Progress 🔄

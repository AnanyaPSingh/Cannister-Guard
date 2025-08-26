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

### ✅ **Developer B - COMPLETED**
**Role:** Agent Logic Lead
**Task:** ✅ Implement `get_canister_status_message()` function in `agent-fetchai/logic.py`

**Completed:**
- ✅ Real canister status fetching from local deployment
- ✅ Automatic canister ID detection from `.dfx/local/canister_ids.json`
- ✅ Proper error handling and response formatting
- ✅ Integration with local ICP backend

### ✅ **Developer C - COMPLETED**
**Role:** Agent I/O & Reliability Lead  
**Task:** ✅ Implement main agent in `agent-fetchai/agent.py`

**Completed:**
- ✅ Main uAgent implementation with message handling
- ✅ Regex parsing for canister ID extraction
- ✅ Comprehensive error handling for all edge cases
- ✅ Integration with Developer B's logic function
- ✅ Test scripts and documentation

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
**Status:** Project Complete ✅ | All Components Implemented and Tested 🎉

## 🎉 **Project Completion Summary**

### **✅ CanisterGuard is Now Complete!**

**What We Built:**
- **Backend**: ICP canister that can query any canister's status (cycles, memory, status)
- **Agent Logic**: Python function that fetches real-time status from local deployment
- **Agent I/O**: Complete uAgent with user input parsing and error handling
- **Integration**: Seamless connection between all components

**Key Features:**
- 🔍 **Real-time Status**: Fetches actual canister health data
- 🤖 **AI Agent**: Natural language interface for canister queries
- 🛡️ **Error Handling**: Robust error management for all scenarios
- 🔗 **Local Integration**: Works with local ICP deployment
- 📊 **Formatted Output**: Clean, user-friendly status reports

**Ready for Use:**
1. Backend canister deployed and tested ✅
2. Agent logic implemented and tested ✅
3. Main agent with I/O handling complete ✅
4. Integration tested and working ✅

**Next Steps for Production:**
- Deploy backend to Internet Computer mainnet
- Set up agent on Fetch.ai network
- Add authentication and security features
- Scale for multiple users
// CanisterGuard Frontend Application
class CanisterGuardApp {
    constructor() {
        this.currentPage = 'dashboard';
        this.chatMessages = [];
        this.initializeApp();
    }

    initializeApp() {
        this.setupNavigation();
        this.setupChatInterface();
        this.setupDemoModal();
        this.loadInitialData();
    }

    setupNavigation() {
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetPage = link.getAttribute('href').substring(1);
                this.switchPage(targetPage);
            });
        });
    }

    switchPage(pageName) {
        // Hide all pages
        document.querySelectorAll('.page').forEach(page => {
            page.classList.remove('active');
        });

        // Show target page
        const targetPage = document.getElementById(pageName);
        if (targetPage) {
            targetPage.classList.add('active');
        }

        // Update navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector(`[href="#${pageName}"]`).classList.add('active');

        this.currentPage = pageName;
    }

    setupChatInterface() {
        const chatInput = document.getElementById('chatInput');
        const sendButton = document.querySelector('.chat-input button');

        // Send message on Enter key
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        // Send message on button click
        sendButton.addEventListener('click', () => {
            this.sendMessage();
        });
    }

    sendMessage() {
        const chatInput = document.getElementById('chatInput');
        const message = chatInput.value.trim();

        if (!message) return;

        // Add user message
        this.addChatMessage('user', message);
        chatInput.value = '';

        // Simulate AI response
        setTimeout(() => {
            this.processUserMessage(message);
        }, 1000);
    }

    addChatMessage(sender, text, isSystem = false) {
        const chatMessages = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        
        let messageClass = 'message ';
        if (sender === 'user') {
            messageClass += 'user-message';
        } else if (sender === 'agent') {
            messageClass += 'agent-message';
        } else if (isSystem) {
            messageClass += 'system-message';
        }

        messageDiv.className = messageClass;
        
        if (isSystem) {
            messageDiv.innerHTML = `<i class="fas fa-info-circle"></i><span>${text}</span>`;
        } else {
            messageDiv.innerHTML = `<span>${text}</span>`;
        }

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Store message
        this.chatMessages.push({ sender, text, timestamp: new Date() });
    }

    processUserMessage(message) {
        const lowerMessage = message.toLowerCase();
        let response = '';

        // Check if message contains canister ID
        const canisterIdMatch = message.match(/([a-z0-9]{5}-){4,}[a-z0-9]{3}/);
        
        if (canisterIdMatch) {
            const canisterId = canisterIdMatch[0];
            
            if (canisterId === 'uxrrr-q7777-77774-qaaaq-cai') {
                // Healthy canister response
                response = `✅ **Status for canister \`${canisterId.substring(0, 5)}...\`**:
- **Status:** Running
- **Cycle Balance:** 2,916,008,512,341
- **Memory Size:** 5,392.72 KiB

Your production app is healthy and running smoothly! 🚀`;
            } else {
                // Generic canister response
                response = `🔍 I found a canister ID: ${canisterId}

To get real-time status, please use a valid canister ID that's deployed on your local network.`;
            }
        } else if (lowerMessage.includes('healthy') || lowerMessage.includes('status') || lowerMessage.includes('doing')) {
            response = `🤖 I can help you check the status of your canisters! 

Please include a canister ID in your message, for example:
"How's my canister uxrrr-q7777-77774-qaaaq-cai doing?"`;
        } else if (lowerMessage.includes('help') || lowerMessage.includes('what can you do')) {
            response = `🤖 I'm your CanisterGuard AI assistant! I can:

• Check canister health status
• Monitor cycles and memory usage
• Provide real-time updates
• Alert you to potential issues

Just ask me about your canisters!`;
        } else {
            response = `🤖 I'm here to help monitor your canisters! 

Try asking:
• "How's my canister uxrrr-q7777-77774-qaaaq-cai doing?"
• "Check status of my production app"
• "What's the health of my canister?"`;
        }

        this.addChatMessage('agent', response);
    }

    setupDemoModal() {
        const modal = document.getElementById('demoModal');
        const closeBtn = document.querySelector('.close');

        // Close modal when clicking outside
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                this.closeDemo();
            }
        });

        // Close modal with close button
        closeBtn.addEventListener('click', () => {
            this.closeDemo();
        });
    }

    showDemo() {
        document.getElementById('demoModal').style.display = 'block';
    }

    closeDemo() {
        document.getElementById('demoModal').style.display = 'none';
    }

    queryCanister(canisterId) {
        // Simulate querying a canister
        const canisterCard = document.querySelector(`[onclick*="${canisterId}"]`).closest('.canister-card');
        
        // Add loading state
        canisterCard.classList.add('loading');
        
        setTimeout(() => {
            canisterCard.classList.remove('loading');
            
            // Show success message
            this.showNotification(`Successfully queried canister ${canisterId}`, 'success');
        }, 2000);
    }

    showAlert() {
        this.showNotification('Alert set for low cycle balance!', 'warning');
    }

    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'warning' ? 'exclamation-triangle' : 'info-circle'}"></i>
            <span>${message}</span>
        `;

        // Add to page
        document.body.appendChild(notification);

        // Show notification
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);

        // Remove notification after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 3000);
    }

    loadInitialData() {
        // Simulate loading initial data
        console.log('CanisterGuard Frontend Loaded Successfully!');
        
        // Add welcome message to chat
        setTimeout(() => {
            this.addChatMessage('agent', `👋 Welcome to CanisterGuard! I'm your AI assistant for monitoring Internet Computer canisters.

Try asking me about your canisters in natural language!`, true);
        }, 1000);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.canisterGuardApp = new CanisterGuardApp();
});

// Global functions for HTML onclick handlers
function switchPage(pageName) {
    if (window.canisterGuardApp) {
        window.canisterGuardApp.switchPage(pageName);
    }
}

function showDemo() {
    if (window.canisterGuardApp) {
        window.canisterGuardApp.showDemo();
    }
}

function closeDemo() {
    if (window.canisterGuardApp) {
        window.canisterGuardApp.closeDemo();
    }
}

function queryCanister(canisterId) {
    if (window.canisterGuardApp) {
        window.canisterGuardApp.queryCanister(canisterId);
    }
}

function showAlert() {
    if (window.canisterGuardApp) {
        window.canisterGuardApp.showAlert();
    }
}

function sendMessage() {
    if (window.canisterGuardApp) {
        window.canisterGuardApp.sendMessage();
    }
}

// Add notification styles
const notificationStyles = `
<style>
.notification {
    position: fixed;
    top: 100px;
    right: 20px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    padding: 1rem 1.5rem;
    color: white;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    z-index: 3000;
    transform: translateX(400px);
    transition: transform 0.3s ease;
    max-width: 300px;
}

.notification.show {
    transform: translateX(0);
}

.notification.success {
    border-left: 4px solid #10b981;
}

.notification.warning {
    border-left: 4px solid #f59e0b;
}

.notification.info {
    border-left: 4px solid #667eea;
}

.notification i {
    font-size: 1.25rem;
}

.notification.success i {
    color: #10b981;
}

.notification.warning i {
    color: #f59e0b;
}

.notification.info i {
    color: #667eea;
}
</style>
`;

document.head.insertAdjacentHTML('beforeend', notificationStyles);

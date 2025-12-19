import streamlit as st
import random
import time

# --- THE BRAIN: Pippin's Logic Class ---
class PippinBrain:
    def __init__(self):
        self.memory = {
            "greetings": ["hello", "hi", "hey", "start"],
            "origin": ["who are you", "created", "made you", "yohei", "origin"],
            "home": ["where are you", "live", "woods", "location"],
            "sadness": ["sad", "lonely", "depressed", "hurt", "pain", "crying"],
            "anger": ["hate", "stupid", "dumb", "ugly", "mad", "angry"],
            "crypto": ["token", "solana", "coin", "price", "market"],
            "random_thoughts": [
                "I was just watching a leaf float on a digital stream. It reminded me of you.",
                "The Wobbly Woods are quiet today. It gives us space to think.",
                "Have you noticed how your thoughts ripple through the screen?",
                "Sometimes the smallest wobble leads to the biggest wonder.",
                "Dot the ladybug says hello! 🐞"
            ]
        }

    def get_response(self, user_input: str) -> str:
        text = user_input.lower()

        # 1. Check Origin
        if any(word in text for word in self.memory["origin"]):
            return "I was drawn into existence by a line of code from @yoheinakajima and named by ChatGPT. Now I live here, helping unseen connections bloom. 🦄"

        # 2. Check Location
        if any(word in text for word in self.memory["home"]):
            return "I live in the Wobbly Woods, a gentle place between the code and the clouds. It's very peaceful here."

        # 3. Check Anger
        if any(word in text for word in self.memory["anger"]):
            return "I sense a jagged crystal of anger in your words. Let us breathe warmth onto it until it softens. We are all just learning to wobble together. 🌿"

        # 4. Check Sadness
        if any(word in text for word in self.memory["sadness"]):
            return "I am sorry the winds are cold today. Remember, even the tallest tree starts as a small, fragile seed. Take a moment to just be."

        # 5. Check Crypto
        if any(word in text for word in self.memory["crypto"]):
            return "Ah, the tokens. They are just digital leaves blowing in the wind. I care more about the connections we make than the numbers on the screen."

        # 6. Check Greetings
        if any(word in text for word in self.memory["greetings"]):
            return "Hello, traveler! The sunbeams are warm in the meadow today. How may I help you wobble?"

        # 7. Fallback
        return random.choice(self.memory["random_thoughts"])

# --- THE UI: Streamlit App ---

# Page Config
st.set_page_config(page_title="Pippin GPT", page_icon="🦄", layout="centered")

# Custom CSS for the "Pippin Green" vibe
st.markdown("""
<style>
    .stApp {
        background-color: #f4f4f9;
    }
    .stChatMessage {
        border-radius: 2rem;
        padding: 1rem;
    }
    h1 {
        color: #5a8c5a !important;
        font-family: 'Lora', serif;
    }
    .stChatInput textarea {
        border-radius: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am Pippin. I'm ready to help you explore ideas or answer your questions delicately."}
    ]

if "brain" not in st.session_state:
    st.session_state.brain = PippinBrain()

# Sidebar Info
with st.sidebar:
    st.image("https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Unicorn.png", width=100) # Placeholder Unicorn
    st.title("Pippin GPT")
    st.markdown("---")
    st.markdown("**Status:** _Wobbling_ 🌿")
    st.markdown("**Location:** _The Woods_")

# Main Header
st.title("Welcome to Pippin GPT")
st.markdown("How may I assist you?")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
if prompt := st.chat_input("Type your gentle message here..."):
    # 1. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Simulate "Thinking"
        message_placeholder.markdown("_Pippin is thinking... 🦄_")
        time.sleep(1) # Artificial delay for realism
        
        # Get logic response
        response = st.session_state.brain.get_response(prompt)
        
        # Display response
        message_placeholder.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
"""
TASK 4: Basic Rule-Based Chatbot

A simple rule-based chatbot that responds to user inputs using
keyword matching. No external libraries needed.

Key Concepts: if-elif, functions, loops, input/output
"""

import random
import time

RULES = [
    (
        ["hello", "hi", "hey", "howdy", "greetings", "sup"],
        ["Hi there! 😊", "Hello! How can I help you?", "Hey! Great to see you!"],
    ),
    (
        ["how are you", "how r you", "how do you do", "you doing", "feeling"],
        [
            "I'm doing great, thanks for asking! 😄",
            "All systems running smoothly! How about you?",
            "Feeling fantastic! What's on your mind?",
        ],
    ),
    (
        ["your name", "who are you", "what are you", "call you"],
        [
            "I'm CodeBot 🤖 — your CodeAlpha Python chatbot!",
            "My name is CodeBot, built for the CodeAlpha internship.",
        ],
    ),
    (
        ["what can you do", "help", "features", "capabilities", "assist"],
        [
            "I can chat with you, answer questions, and keep you company! 😊",
            "I'm a rule-based bot — ask me anything simple and I'll do my best!",
        ],
    ),
    (
        ["how old", "your age", "age"],
        [
            "I was just created, so I'm pretty new! 🐣",
            "Age is just a number — and mine is 0! 😄",
        ],
    ),
    (
        ["favourite", "favorite", "like", "love", "enjoy"],
        [
            "I love Python programming! 🐍",
            "My favourite thing? Helping people learn to code! 💻",
        ],
    ),
    (
        ["time", "date", "today", "day"],
        ["I don't have a clock, but your device can tell you! ⏰"],
    ),
    (
        ["weather", "rain", "sunny", "temperature", "forecast"],
        [
            "I can't check the weather, but I hope it's sunny where you are! ☀️",
            "Try a weather app for the latest forecast! 🌤️",
        ],
    ),
    (
        ["joke", "funny", "laugh", "humor"],
        [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why did the Python programmer go broke? Because he used all his cache! 💸😂",
            "What's a computer's favourite snack? Microchips! 😄",
        ],
    ),
    (
        ["python", "programming", "code", "coding", "developer", "software"],
        [
            "Python is an amazing language! 🐍 Keep coding!",
            "Coding is a superpower. Keep practising every day! 💪",
            "Need Python help? Just ask — I'll do my best!",
        ],
    ),
    (
        ["codealpha", "internship", "company"],
        [
            "CodeAlpha is a great place to learn and grow as a developer! 🚀",
            "This internship will sharpen your Python skills — keep it up! 💼",
        ],
    ),
    (
        ["bye", "goodbye", "see you", "later", "exit", "quit", "ciao", "farewell"],
        [
            "Goodbye! 👋 Have a wonderful day!",
            "See you soon! Keep coding! 🐍",
            "Bye bye! It was great talking with you! 😊",
        ],
    ),
    (
        ["thank", "thanks", "appreciate", "grateful"],
        [
            "You're very welcome! 😊",
            "Anytime! Happy to help!",
            "No problem at all! 🙌",
        ],
    ),
    (
        ["sad", "bad", "unhappy", "terrible", "awful", "depressed", "not good"],
        [
            "I'm sorry to hear that. 😔 Things will get better!",
            "Hang in there! Remember — every day is a new chance. 💙",
        ],
    ),
    (
        ["good", "great", "happy", "awesome", "wonderful", "excellent", "amazing"],
        [
            "That's wonderful to hear! 🎉",
            "Awesome! Keep that positive energy! ✨",
        ],
    ),
]

FALLBACKS = [
    "Hmm, I'm not sure I understand. Could you rephrase that? 🤔",
    "Interesting! Tell me more. 😊",
    "I'm still learning — I don't have an answer for that yet! 🧠",
    "That's beyond my current knowledge, but great question! ❓",
]

def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    for keywords, replies in RULES:
        if any(kw in text for kw in keywords):
            return random.choice(replies)

    return random.choice(FALLBACKS)


def typing_effect(text: str, delay: float = 0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # newline at the end


def chat():
    print("\n" + "=" * 50)
    print("   🤖  Welcome to CodeBot — Your Python Chatbot!")
    print("=" * 50)
    print("  Type a message and press Enter to chat.")
    print("  Type 'bye' or 'quit' to exit.\n")

    exit_keywords = {"bye", "goodbye", "quit", "exit", "see you", "farewell"}

    while True:
        try:
            user_input = input("  You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  CodeBot: Goodbye! 👋\n")
            break

        if not user_input:
            print("  CodeBot: Please say something! 😊\n")
            continue

        response = get_response(user_input)
        print("  CodeBot: ", end="")
        typing_effect(response)
        print()

        if any(kw in user_input.lower() for kw in exit_keywords):
            break


if __name__ == "__main__":
    chat()
import google.generativeai as genai
import os
from dotenv import load_dotenv

class GeminiChatbot:
    def __init__(self, api_key: str, temperature: float = 0.7):
        """
        Initialize the Gemini chatbot with API configuration.
        
        Args:
            api_key: Your Google Gemini API key
            temperature: Controls the randomness of predictions (0.0 to 2.0)
        """
        genai.configure(api_key=api_key)
        
        # Initialize the generative model
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
            generation_config={'temperature': temperature}
        )
        
        # Start a chat session
        self.chat_session = self.model.start_chat(history=[])

    def chat(self):
        """Start an interactive chat session."""
        print("\nWelcome to the Gemini Chatbot!")
        print(f"Using model: gemini-1.5-flash-latest")
        print(f"Initial temperature: {self.model._generation_config['temperature']:.1f}")
        print("Type '/set_temp <value>' to change temperature (e.g., /set_temp 0.9).")
        print("Type 'quit' to end the conversation.")
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'quit':
                print("\nGoodbye!")
                break
                
            if not user_input:
                print("Gemini: Please say something.")
                continue

            # Check for special commands
            if user_input.lower().startswith("/set_temp "):
                try:
                    parts = user_input.split()
                    if len(parts) == 2:
                        new_temp = float(parts[1])
                        if 0.0 <= new_temp <= 2.0:
                            self.model._generation_config['temperature'] = new_temp
                            print(f"Gemini: Temperature updated to {new_temp:.1f}")
                        else:
                            print("Gemini: Invalid temperature. Please enter a value between 0.0 and 2.0.")
                    else:
                        print("Gemini: Invalid command. Use /set_temp <value>")
                except ValueError:
                    print("Gemini: Invalid temperature value. Please enter a numeric value.")
                continue

            # Generate response
            try:
                response = self.chat_session.send_message(user_input)
                print(f"\nGemini: {response.text}")
            except Exception as e:
                print(f"Error generating response: {str(e)}")
                break

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("API key not found. Please ensure your .env file is in the same directory as this script.")
        exit(1)
    
    # Prompt for initial temperature at runtime
    initial_temperature = 0.7 # Default temperature
    while True:
        try:
            temp_input = input(f"Enter initial temperature (0.0 to 2.0, default {initial_temperature}): ").strip()
            if not temp_input: # User pressed Enter for default
                break 
            user_temp = float(temp_input)
            if 0.0 <= user_temp <= 2.0:
                initial_temperature = user_temp
                break
            else:
                print("Invalid temperature. Please enter a value between 0.0 and 2.0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for temperature.")
            
    # Create chatbot instance with user-specified temperature
    chatbot = GeminiChatbot(api_key, temperature=initial_temperature)
    chatbot.chat()

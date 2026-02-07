TalentScout AI: Agentic Hiring Assistant

TalentScout AI is a conversational Gen AI application designed to automate the initial phases of technical recruitment. Unlike traditional keyword-based ATS systems, this tool uses a "Candidate-First" approach, dynamically discovering a candidate's tech stack and generating real-time technical assessments through natural dialogue.

🚀 Key Features
Active Tech-Stack Discovery: Moves beyond static resume parsing by engaging candidates in a multi-turn conversation to identify their core competencies.

Adaptive Technical Screening: Dynamically generates targeted technical questions based on the candidate's specific frameworks and languages.

Zero-Dependency Logic: Built using the native Google Gen AI SDK rather than high-level abstractions like LangChain, ensuring full control over prompt orchestration and minimal latency.

Strict Behavioral Guardrails: System-level instructions ensure the agent remains professional and refuses off-topic queries.

🛠️ Tech Stack
LLM: Google Gemini 2.0 Flash (via google-genai)

Backend: Python 3.x

Web Framework: Streamlit (for real-time chat interface)

Environment Management: python-dotenv for secure API handling

📂 Project Structure

TalentScout/
├── app.py              # Streamlit UI and Session State management
├── llm_helper.py       # Core LLM orchestration and Gemini API integration
├── .env                # Private API keys (not included in repo)
├── .env.example        # Template for environment variables
├── .gitignore          # Rules to exclude venv, logs, and sensitive data
└── requirements.txt    # Project dependencies


⚙️ Installation & Setup

1.Clone the Repository

git clone https://github.com/your-username/TalentScout.git
cd TalentScout

2.Create a virtual Enviroment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3.Install Dependencies

pip install -r requirements.txt


4.Configure Environment Variables

Create a .env file in the root directory.
Add your Gemini API Key:

GEMINI_API_KEY=your_actual_api_key_here


5.Run the Application

streamlit run app.py

🧠 Strategic Approach 
This project demonstrates a deep understanding of Generative AI Orchestration:

Context Management: Uses Streamlit's session_state to maintain chat history across reruns.

System Instructions: Leverages native Gemini system prompts to enforce a strict four-step recruitment process.

Error Handling: Implements robust error catching during API calls to ensure a seamless candidate experience
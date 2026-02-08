# 🤖 TalentScout AI: Agentic Technical Recruiter

**TalentScout AI** is a conversational Gen AI application designed to automate technical pre-screening. Built with **Gemini 2.0 Flash**, it conducts dynamic "Tech-Stack Discovery" through dialogue rather than passive resume parsing, ensuring a more accurate and interactive candidate evaluation.

## 🚀 Key Features
- **Adaptive Technical Screening**: Dynamically generates targeted technical questions based on the candidate's self-identified tech stack.
- **Active Discovery Flow**: No resume required. The agent follows a strict process to gather info and audit skills in real-time.
- **Vanilla Python Implementation**: Built using the native **Google Gen AI SDK** for maximum control over prompt orchestration and minimal latency.
- **Professional Guardrails**: Includes strict behavioral instructions to maintain a recruiting persona and refuse off-topic queries.

## 🛠️ Tech Stack
- **LLM**: Google Gemini 2.0 Flash (`gemini-2.0-flash`)
- **Web Interface**: Streamlit
- **Environment Management**: Python-dotenv
- **Orchestration**: Direct Native SDK integration (No LangChain)

## 📂 Project Structure
```text
TalentScout/
├── app.py              # Streamlit UI & Chat Logic
├── llm_helper.py       # Gemini API Integration & Prompt Engineering
├── .env.example        # Template for Gemini API Key
├── .gitignore          # Rules for excluded files (venv, .env, __pycache__)
└── requirements.txt    # Project dependencies
```

##⚙️ Installation & Setup

**1.Clone the Repository**

```
git clone https://github.com/your-username/TalentScout.git

cd TalentScout
```
**2.Create a virtual Enviroment**
```
python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

```
**3.Install Dependencies**
```
pip install -r requirements.txt
```

**4.Configure Environment Variables**
Create a .env file in the root directory.
```
Add your Gemini API Key:

GEMINI_API_KEY=your_actual_api_key_here
```

**5.Run the Application**
```
streamlit run app.py

```
Error Handling: Implements robust error catching during API calls to ensure a seamless candidate experience

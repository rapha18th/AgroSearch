## To run the app locally

### clone the repo

### create a virtual environment

### `pip install - r requirements.txt`

### `streamlit run app.py`

```mermaid
graph TD
    subgraph Client Side (Browser)
        A1["<b>User Interface</b><br/>React + Vite + Tailwind<br/><i>Provides all user views, forms, and reports.</i>"]
        A2["<b>User Actions</b><br/>(Upload, Start/End Session)<br/><i>Triggers API calls via the API Client.</i>"]
        A3["<b>Unified API Client (api.ts)</b><br/><i>Manages all secure communication with the backend.</i>"]
        A4["<b>ElevenLabs React SDK</b><br/><i>Handles the real-time, low-latency voice connection.</i>"]

        A1 --> A2
        A2 --> A3
        A2 --> A4
    end

    subgraph Backend
        C1["<b>Flask Backend</b><br/><i>Hosts all API endpoints and business logic.</i>"]
        C2["<b>Firebase Admin SDK</b><br/><i>Verifies user tokens and manages all database operations.</i>"]
        C3["<b>AI Orchestration Logic</b><br/><i>Manages multi-step Gemini prompts for context and analysis.</i>"]

        C1 --> C2
        C1 --> C3
    end

    subgraph Cloud & External Services
        D1["<b>Firebase Authentication</b><br/><i>Securely handles user sign-in and identity management.</i>"]
        D2["<b>Firebase Realtime Database</b><br/><i>Stores all application data (profiles, projects, sessions).</i>"]
        D4["<b>Google Gemini API</b><br/><i>The engine for summarization, classification, and feedback generation.</i>"]
        D6["<b>ElevenLabs Conversational AI API</b><br/><i>Provides the real-time, multi-voice panel(Eric, Daniel and Rachel) AI agent.</i>"]
    end

    A3 -- "Sends API Requests" --> C1
    A1 -- "Handles Auth Flow" --> D1
    A4 -- "Streams Audio" --> D6
    C2 -- "Verifies Tokens" --> D1
    C2 -- "Reads/Writes Data" --> D2
    C3 -- "Sends Prompts" --> D4

    %% --- Styling ---
    %% Frontend
    style A1 fill:#2E7D32,stroke:#fff,color:#fff
    style A2 fill:#66BB6A,stroke:#fff,color:#fff
    style A3 fill:#388E3C,stroke:#fff,color:#fff
    style A4 fill:#1B5E20,stroke:#fff,color:#fff

    %% Backend
    style C1 fill:#FFB300,stroke:#333,color:#333
    style C2 fill:#FF8F00,stroke:#333,color:#333
    style C3 fill:#FF6F00,stroke:#333,color:#333

    %% Firebase
    style D1 fill:#FFA000,stroke:#fff,color:#fff
    style D2 fill:#F57C00,stroke:#fff,color:#fff

    %% Google Gemini
    style D4 fill:#4285F4,stroke:#fff,color:#fff

    %% ElevenLabs
    style D6 fill:#000000,stroke:#fff,color:#fff
```

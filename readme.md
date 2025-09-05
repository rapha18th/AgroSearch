## To run the app locally

### clone the repo

### create a virtual environment

### `pip install - r requirements.txt`

### `streamlit run app.py`

flowchart TD
  subgraph Client_Side_[Client Side (Browser)]
    A1["User Interface\nReact + Vite + Tailwind\nProvides all user views, forms, and reports."]
    A2["User Actions\n(Upload, Start/End Session)\nTriggers API calls via the API Client."]
    A3["Unified API Client (api.ts)\nManages all secure communication with the backend."]
    A4["ElevenLabs React SDK\nHandles the real-time, low-latency voice connection."]
    A1 --> A2
    A2 --> A3
    A2 --> A4
  end

  subgraph Backend
    C1["Flask Backend\nHosts all API endpoints and business logic."]
    C2["Firebase Admin SDK\nVerifies user tokens and manages all database operations."]
    C3["AI Orchestration Logic\nManages multi-step Gemini prompts for context and analysis."]
    C1 --> C2
    C1 --> C3
  end

  subgraph Cloud_and_External_Services[Cloud & External Services]
    D1["Firebase Authentication\nSecurely handles user sign-in and identity management."]
    D2["Firebase Realtime Database\nStores application data (profiles, projects, sessions)."]
    D4["Google Gemini API\nEngine for summarization, classification, and feedback generation."]
    D6["ElevenLabs Conversational AI API\nReal-time, multi-voice panel (Eric, Daniel, Rachel)."]
  end

  A3 -- Sends API Requests --> C1
  A1 -- Handles Auth Flow --> D1
  A4 -- Streams Audio --> D6
  C2 -- Verifies Tokens --> D1
  C2 -- Reads/Writes Data --> D2
  C3 -- Sends Prompts --> D4

  %% Styles
  classDef frontend fill:#2E7D32,stroke:#fff,color:#fff;
  classDef backend fill:#FFB300,stroke:#333,color:#333;
  classDef firebase fill:#F57C00,stroke:#fff,color:#fff;
  classDef google fill:#4285F4,stroke:#fff,color:#fff;
  classDef eleven fill:#000,stroke:#fff,color:#fff;

  class A1,A2,A3,A4 frontend;
  class C1,C2,C3 backend;
  class D1,D2 firebase;
  class D4 google;
  class D6 eleven;

## To run the app locally

### clone the repo

### create a virtual environment

### `pip install - r requirements.txt`

### `streamlit run app.py`

graph TD
    %% --- Client Side (Browser) ---
    subgraph "Client Side (Browser)"
        A1[User Interface - React + Vite + Tailwind]
        A2[User Actions (Upload Document, Start/End Session)]
        A3[Unified API Client (api.ts)]
        A4[ElevenLabs React SDK]

        A1 --> A2
        A2 --> A3
        A2 --> A4
    end

    %% --- Backend ---
    subgraph "Backend"
        C1[Flask Backend]
        C2[Firebase Admin SDK (Auth & DB Logic)]
        C3[AI Orchestration Logic (Context & Analysis)]

        C1 --> C2
        C1 --> C3
    end

    %% --- Cloud & External Services ---
    subgraph "Cloud & External Services"
        D1[Firebase Authentication]
        D2[Firebase Realtime Database]
        D4[Google Gemini API]
        D6[ElevenLabs Conversational AI API]
    end

    %% --- Cross Connections ---
    A3 --> C1
    A1 --> D1
    A4 --> D6
    C2 --> D1
    C2 --> D2
    C3 --> D4

    %% --- Styling ---
    style A1 fill:#2E7D32,stroke:#fff,stroke-width:2px,color:#fff
    style C1 fill:#FFC107,stroke:#333,stroke-width:2px,color:#333
    style D4 fill:#4285F4,stroke:#fff,stroke-width:2px,color:#fff
    style D6 fill:#000,stroke:#fff,stroke-width:2px,color:#fff
    style D1 fill:#FFA000,stroke:#fff,stroke-width:2px,color:#fff
    style D2 fill:#F57C00,stroke:#fff,stroke-width:2px,color:#fff

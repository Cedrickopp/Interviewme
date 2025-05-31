# AI Interview Agent – "My AI Avatar"

A personal interview agent that serves as a digital twin, representing my skillset, experiences, and projects. Recruiters can ask questions through a web interface and receive responses as if they were speaking directly with me – without requiring my physical presence.

## Objectives

* Web application allowing users to interview my AI avatar (based on my profile, projects, etc.)
* GPT-based response generation through Python Cloud Functions
* Simple, frictionless access for recruiters
* Cost-effective, secure, modular & scalable architecture

## Tech Stack (Updated May 2025)

| Area           | Tool / Service                                                                                    | Status      |
| -------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| Frontend       | **Vue 3** (Composition API)                                                                       | ✅ chosen    |
| Styling        | Bootstrap 5                                                                                       | ✅ chosen    |
| Interactivity  | Vue with `fetch` for backend communication                                                         | ✅ planned   |
| Backend        | Firebase Cloud Functions (Python, Gen2)                                                           | ✅ planned   |
| Database       | Cloud Firestore                                                                                   | ✅ planned   |
| Hosting        | Firebase Hosting                                                                                  | ✅ planned   |
| Security       | Rate limiting & IP-based protection                                                               | ✅ planned   |
| LLM API        | OpenAI (via Python SDK)                                                                           | ✅ planned   |
| Secrets Mgmt   | Google Cloud Secrets Manager                                                                      | ✅ recommended |

## Security Strategy

To ensure a smooth experience for recruiters while protecting the system:

### For Recruiters
- No login required
- Direct access to the interview interface
- Rate limiting per IP address (100 requests/hour)
- Automatic blocking after limit exceeded
- Simple re-authentication if needed

### For Admin (You)
- Firebase Auth with Google Sign-in
- Full access to system configuration
- Monitoring of usage and costs
- Ability to adjust rate limits

### Protection Measures
- IP-based rate limiting
- Request timeout limits
- Cost monitoring and alerts
- DDoS protection through Firebase
- Automatic blocking of suspicious activity

##  Roadmap (MVP v0.1)

###  Setup Phase

* [x] Configure Firebase project & Cloud Firestore
* [x] Set up Firebase Hosting for Vue frontend
* [x] Configure Cloud Functions (Python 3.10+) via `gcloud` CLI
* [x] Store OpenAI API Key in Google Cloud Secrets Manager

### Backend (Agent Logic)

* [ ] Create data structure in Firestore (`profile`, `faq`, `session_logs`)
* [ ] System Prompt Template + dynamic User Prompt
* [ ] Python Cloud Function: OpenAI call with guardrails
* [ ] Token limits, timeout, logging & basic filtering
* [ ] Test function with mock data

### Frontend (Vue 3)

* [ ] Initialize Vue CLI project (`vite` or `vue-cli`)
* [ ] Bootstrap integration (Vue-compatible via CDN or package)
* [ ] Chat component with question form, loading indicator & response display
* [ ] Rate limit indicator & user feedback
* [ ] "About me" page (static CV, projects)

### Security & Hosting

* [ ] Implement IP-based rate limiting
* [ ] Set up cost monitoring and alerts
* [ ] Configure request timeout limits
* [ ] Deployment via Firebase Hosting (CI optional)

## Current Setup

### Firebase Configuration
- Project initialized with Firestore, Storage, Functions, and Hosting
- Admin-only Firestore security rules implemented
- Local emulators configured for development
- Emulator ports:
  - UI: localhost:4000
  - Functions: localhost:5001
  - Firestore: localhost:8080
  - Hosting: localhost:5000
  - Storage: localhost:9199

## Open Questions

* **Profile Structure**: JSON vs Markdown vs Firestore document – how to maintain content?
* **Session Storage?** Store past questions/answers?
* **Cost Management?** Budget or limit API usage (tokens)?
* **Improve Agent Understanding?** Later use embeddings & vector database?
* **Rate Limits?** What are the optimal limits for different types of users?

## Local Development

### Setup

```bash
# Firebase CLI
npm install -g firebase-tools
firebase login
firebase init

# Google Cloud SDK for Python Functions
https://cloud.google.com/sdk/docs/install

# Local Emulation
firebase emulators:start
```

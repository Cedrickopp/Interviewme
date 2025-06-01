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
| Backend        | Firebase Cloud Functions (Python, Gen2)                                                           | ✅ chosen   |
| Database       | Cloud Firestore                                                                                   | ✅ planned   |
| Hosting        | Firebase Hosting                                                                                  | ✅ planned   |
| Security       | Rate limiting & IP-based protection                                                               | ✅ planned   |
| LLM API        | OpenAI (via Python SDK)                                                                           | ✅ chosen  |
| Secrets Mgmt   | Google Cloud Secrets Manager                                                                      | ✅ chosen  |

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

## OpenAI API Key & Google Secret Manager Setup

### 1. Create an OpenAI API Key
- Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
- Click "Create new secret key" and copy the key (starts with `sk-...`)

### 2. Store the Key in Google Secret Manager
- Go to [Google Cloud Secret Manager](https://console.cloud.google.com/security/secret-manager)
- Click "Create Secret"
- Name: `openai-api-key` (or your preferred name)
- Value: **Paste the API key as plain text (no quotes)**
- Click "Create"

### 3. Grant Access to Your Service Account
- Go to [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- Find your service account (e.g., `interviewme-ad529@appspot.gserviceaccount.com`)
- Click on it, go to "Permissions" or "Edit"
- Add the role: **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`)

### 4. Download Service Account Key (for local dev)
- In the Service Account page, go to "Keys" > "Add Key" > "Create new key" > JSON
- Download the key file

### 5. Set Environment Variable for Local Development
- In your terminal, run:
  ```powershell
  $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Path\To\Your\service-account-key.json"
  ```
- Or set it permanently in your system environment variables

### 6. Update Your Function Code
- Hardcode the `project_id` and `secret_id` in your function (safe, not sensitive)
- Do **not** hardcode the API key itself

## Local Development with Firebase Emulator

### 1. Activate the Python virtual environment in `functions/`:
```powershell
.\functions\venv\Scripts\Activate.ps1
```

### 2. Install dependencies:
```powershell
pip install -r functions/requirements.txt
```

### 3. Start the emulator (functions only):
```powershell
firebase emulators:start --only functions
```

### 4. Test your function
- The emulator will show a local URL, e.g.:
  `http://localhost:5001/<your-project-id>/us-central1/test_openai_connection`
- Use your browser or `curl` to test:
  ```sh
  curl http://localhost:5001/<your-project-id>/us-central1/test_openai_connection
  ```

## Troubleshooting

- **403 Permission Denied:**
  - Make sure the service account has the `Secret Manager Secret Accessor` role
  - Make sure the Secret Manager API is enabled
- **Connection error / ECONNRESET:**
  - Check your internet connection
  - Check OpenAI status: https://status.openai.com/
  - Try a different network (e.g., mobile hotspot)
  - Make sure your API key is valid and active
- **DefaultCredentialsError:**
  - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to your service account key
- **API key not working:**
  - Double-check the secret value in Secret Manager matches your working OpenAI key

## Open Questions

* **Profile Structure**: JSON vs Markdown vs Firestore document – how to maintain content?
* **Session Storage?** Store past questions/answers?
* **Cost Management?** Budget or limit API usage (tokens)?
* **Improve Agent Understanding?** Later use embeddings & vector database?
* **Rate Limits?** What are the optimal limits for different types of users?

---

**For any issues, check the emulator logs and the troubleshooting section above.**

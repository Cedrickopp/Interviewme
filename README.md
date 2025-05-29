# 🧠 AI Interview Agent – "My AI Avatar"

A personal interview agent that serves as a digital twin, representing my skillset, experiences, and projects. Recruiters can ask questions through a web interface and receive responses as if they were speaking directly with me – without requiring my physical presence.

## 🚀 Objectives

* Web application allowing users to interview my AI avatar (based on my profile, projects, etc.)
* GPT-based response generation through Python Cloud Functions
* Admin-only access (initially), with future authentication system for external users
* Cost-effective, secure, modular & scalable architecture

## 🧱 Tech Stack (Updated May 2025)

| Area           | Tool / Service                                                                                    | Status      |
| -------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| Frontend       | **Vue 3** (Composition API)                                                                       | ✅ chosen    |
| Styling        | Bootstrap 5                                                                                       | ✅ chosen    |
| Interactivity  | Vue with `fetch` for backend communication                                                         | ✅ planned   |
| Backend        | Firebase Cloud Functions (Python, Gen2)                                                           | ✅ planned   |
| Database       | Cloud Firestore                                                                                   | ✅ planned   |
| Hosting        | Firebase Hosting                                                                                  | ✅ planned   |
| Auth (now)     | Firebase Auth – Admin-only                                                                        | ✅ planned   |
| Auth (later)   | [Clerk](https://clerk.dev), [Auth0](https://auth0.com), [Supabase Auth](https://supabase.com/auth) | 🔲 open     |
| LLM API        | OpenAI (via Python SDK)                                                                           | ✅ planned   |
| Secrets Mgmt   | Google Cloud Secrets Manager                                                                      | ✅ recommended |

## 🔐 Authentication Proposal (Future)

When you want to enable public user login or provide agents for others, here are three **modern authentication systems** to choose from:

| Option            | Advantages                                                           | Disadvantages                      |
| ----------------- | -------------------------------------------------------------------- | ---------------------------------- |
| **Clerk.dev**     | Super easy Vue integration, Google/Apple/Email, GDPR-compliant       | Monthly costs after limit         |
| **Auth0**         | Widely used in enterprise, many providers                            | Slightly heavy for small projects  |
| **Supabase Auth** | Open Source, Email Magic Link, OAuth ready                           | Less polished UI than Clerk/Auth0  |

📌 **Recommendation:** For future scaling: **Clerk** – good mix of UX, pricing, and Vue compatibility.

## 🛣️ Roadmap (MVP v0.1)

### 🔹 Setup Phase

* [ ] Configure Firebase project & Cloud Firestore
* [ ] Set up Firebase Hosting for Vue frontend
* [ ] Configure Cloud Functions (Python 3.10+) via `gcloud` CLI
* [ ] Store OpenAI API Key in Google Cloud Secrets Manager

### 🔹 Backend (Agent Logic)

* [ ] Create data structure in Firestore (`profile`, `faq`, `session_logs`)
* [ ] System Prompt Template + dynamic User Prompt
* [ ] Python Cloud Function: OpenAI call with guardrails
* [ ] Token limits, timeout, logging & basic filtering
* [ ] Test function with mock data

### 🔹 Frontend (Vue 3)

* [ ] Initialize Vue CLI project (`vite` or `vue-cli`)
* [ ] Bootstrap integration (Vue-compatible via CDN or package)
* [ ] Chat component with question form, loading indicator & response display
* [ ] Auth guard for admin access
* [ ] "About me" page (static CV, projects)

### 🔹 Auth & Hosting

* [ ] Firebase Auth for admin with Google login
* [ ] Define "admin" role in Firestore or via claims
* [ ] Login component & protected routes
* [ ] Deployment via Firebase Hosting (CI optional)

## ❓ Open Questions

* **Profile Structure**: JSON vs Markdown vs Firestore document – how to maintain content?
* **Session Storage?** Store past questions/answers?
* **Cost Management?** Budget or limit API usage (tokens)?
* **Improve Agent Understanding?** Later use embeddings & vector database?
* **Public Access?** Make agent accessible to recruiters without login or via invitation?

## 🧑‍💻 Local Development

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

## 🔮 Ideas for v0.2+

* CV upload via Admin UI with automatic analysis
* Job posting matching (later)
* Agent feedback mode
* Versioned profile (e.g., different variants for roles)
* External candidate agent service (multi-user) 
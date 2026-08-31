# worthy

**Live app:** [worthy-tracker.streamlit.app](https://worthy-tracker.streamlit.app/)

An easier way to decide what earns its place in your monthly budget.

## What it does

`worthy` is a subscription tracker that goes a step further than just logging what you pay for. Alongside each subscription, it uses AI to generate a short "worth keeping?" verdict based on how recently you've actually used it, so you're not just seeing a list, you're getting a nudge on what might be worth cancelling.

## Features

- Add a subscription through a simple form: name, cost, renewal date, category, and last used date
- Browse a curated dropdown of common subscription services and categories, rather than typing free text
- See all saved subscriptions listed in one place
- Get an AI-powered "worth keeping?" verdict shown alongside each subscription


## Tech stack

- **Python** — core language
- **PostgreSQL** — data storage (cloud-hosted)
- **Streamlit** — web interface
- **Groq API** (Llama/GPT-OSS models) — AI reasoning
- **pytest** — testing
- **python-dotenv** — environment variable handling
- **GitHub Actions** — continuous integration

## Project structure

```
worthy/
├── models/
│   └── subscription.py      # Subscription class
├── services/
│   ├── db.py                 # database connection, save, and retrieve logic
│   └── ai.py                 # Groq AI verdict logic
├── tests/
│   ├── test_subscription.py
│   ├── test_db.py
│   └── test_ai.py
├── .github/
│   └── workflows/
│       └── tests.yml         # CI pipeline: runs pytest on every push
├── app.py                    # Streamlit interface
├── config.py
└── requirements.txt
```

## Running locally

1. Clone the repo and install dependencies: `pip install -r requirements.txt`
2. Set up a PostgreSQL database and create the `subscriptions` table (see `services/db.py` for the schema).
3. Create a `.env` file with:
   \`\`\`
   DB_HOST=your_host
   DB_PORT=5432
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_NAME=your_database
   GROQ_API_KEY=your_groq_key
   \`\`\`
4. Run the app: `streamlit run app.py`

## Running tests

\`\`\`
pytest
\`\`\`

Tests also run automatically on every push via GitHub Actions, using a temporary PostgreSQL instance spun up specifically for the test run.

## Why I built it

This project was built as part of my portfolio with a deliberate focus on doing the fundamentals well: clean, simple, test-driven code over unnecessary complexity. Along the way, it also became a real lesson in adapting a working setup, migrating the database from local MySQL to a cloud-hosted PostgreSQL instance to get the app properly live and deployable.

## License

MIT
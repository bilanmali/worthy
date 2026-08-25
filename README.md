# worthy

A calmer way to decide what earns its place in your monthly budget.

## What it does

`worthy` is a subscription tracker that goes a step further than just logging what you pay for. Alongside each subscription, it uses AI to generate a short "worth keeping?" verdict based on how recently you've actually used it — so you're not just seeing a list, you're getting a nudge on what might be worth cancelling.

## Features

- Add subscriptions with cost, renewal date, category, and last used date
- View all saved subscriptions in one place
- AI-generated verdict on whether each subscription still earns its keep, powered by Groq
- UK date formatting throughout
- Built with test-driven development — every core function has a test written before the code

## Tech stack

- **Python** — core language
- **MySQL** — data storage
- **Streamlit** — web interface
- **Groq API** (Llama/GPT-OSS models) — AI reasoning
- **pytest** — testing
- **python-dotenv** — environment variable handling

## Project structure
worthy/
├── models/
│ └── subscription.py # Subscription class
├── services/
│ ├── db.py # database connection, save, and retrieve logic
│ └── ai.py # Groq AI verdict logic
├── tests/
│ ├── test_subscription.py
│ ├── test_db.py
│ └── test_ai.py
├── app.py # Streamlit interface
├── config.py
└── requirements.txt



## Running locally

1. Clone the repo and install dependencies:
   pip install -r requirements.txt

2. Set up a MySQL database called `worthy` and create the `subscriptions` table (see `services/db.py` for the schema).
3. Create a `.env` file with:
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=your_password
    DB_NAME=worthy
    GROQ_API_KEY=your_groq_key

4. Run the app:
   streamlit run app.py


## Running tests
pytest


## Why I built it

This project was built as part of my portfolio with a deliberate focus on doing the fundamentals well: clean, simple, test-driven code over unnecessary complexity.

## License

MIT
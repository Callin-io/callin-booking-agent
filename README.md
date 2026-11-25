# Callin.io booking agent (Task Caller)

A minimal, working example that places one real outbound phone call with the [Callin.io](https://callin.io) Python SDK (`pip install callin`) and a "Task Caller" voice agent.

The SDK starts a one-contact campaign, passes `objective`, `context`, `language` and `name` as dynamic variables, and can wait for the status, summary and transcript. This is the same public API as in [Callin-io/callin-agents](https://github.com/Callin-io/callin-agents) (package `callin` 0.1.2). No unofficial endpoints.

## Get your API key

You need a Callin.io account, an API key, an outbound agent with a phone number, and available minutes. New accounts start with **30 free minutes**.

1. Create an account at [app.callin.io/signup](https://app.callin.io/signup).
2. Sign in at [app.callin.io](https://app.callin.io). Click your name at the bottom of the left sidebar → **Profile** → **API Keys**. If it says "No API key found", click **Regenerate Key** and copy the key. Regenerating immediately invalidates the previous key. Docs: [API reference](https://support.callin.io/api-reference/introduction).
3. Create an **outbound** voice agent and assign it a phone number. Paste the prompt in `prompt.md` into the agent (the official Task Caller template). The agent's id is `CALLIN_AGENT_ID`.
4. Copy `.env.example` to `.env` and fill in `CALLIN_API_KEY`, `CALLIN_AGENT_ID`, and `BOOKING_PHONE` (an E.164 number **you are allowed to call**, typically your own phone).

There is no public deep link to the API Keys tab; it lives inside the logged-in app.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

set -a && source .env && set +a
python book.py
```

`book.py` calls:

```python
from callin import Callin

result = Callin().place_call(
    "+390111234567",  # BOOKING_PHONE
    objective="Book a table for 2 tomorrow at 20:30 under the name Rossi",
    context="Party of 2. Name: Rossi. Prefer indoor seating if asked.",
    language="it",
    contact_name="Rossi",
    wait=True,
)
print(result.status, result.summary)
```

Use only numbers the callee has agreed you may call, or public business numbers. No unsolicited marketing, no emergency numbers, no payment card data. The agent states that it is an AI.

Pricing: $0.16 per minute, all inclusive, no monthly fee. See [callin.io/pricing](https://callin.io/pricing).

## License

MIT. © Replacing Humans LLC (Callin.io).

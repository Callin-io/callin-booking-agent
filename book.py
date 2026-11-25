"""Place one outbound booking call with the Callin.io Python SDK.

Verified against callin 0.1.2 (Callin-io/callin-agents, python/src/callin/client.py):

    Callin(api_key=None, agent_id=None, base_url=..., timeout=30.0)
        # api_key  <- CALLIN_API_KEY
        # agent_id <- CALLIN_AGENT_ID

    Callin.place_call(to, objective, *, context="", language="", agent_id=None,
                      contact_name="", variables=None, wait=False,
                      timeout_seconds=600, poll_seconds=10) -> CallResult

`to` must be E.164 (start with "+"). With wait=True the call blocks until it
ends and, when the link is certain, returns summary and transcript.
"""

import os
import sys

from callin import Callin

TO = os.environ.get("BOOKING_PHONE", "").strip()
if not TO:
    sys.exit("Set BOOKING_PHONE to an E.164 number you are allowed to call, e.g. +390111234567")

client = Callin()  # reads CALLIN_API_KEY and CALLIN_AGENT_ID from the environment
result = client.place_call(
    TO,
    objective="Book a table for 2 tomorrow at 20:30 under the name Rossi",
    context="Party of 2. Name: Rossi. Prefer indoor seating if asked.",
    language="it",
    contact_name="Rossi",
    wait=True,
)

print("status:", result.status)
print("campaign_id:", result.campaign_id)
print("call_id:", result.call_id)
print("match:", result.match)
print("summary:", result.summary or "(empty — not linked with certainty, or not ready yet)")
if result.transcript:
    print("--- transcript ---")
    print(result.transcript)

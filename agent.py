from hindsight_client import Hindsight

# Connect to Hindsight Cloud
client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key="hsk_b57e9081118bdc0771d38091805d4829_98fac594e3d896e3"
)

bank = "support-agent"

print("\n=== DAY 1: Customer contacts support for the first time ===\n")

# Store customer interaction in long-term memory
client.retain(
    bank_id=bank,
    content=(
        "Customer Priya Sharma reported that her app crashes every time "
        "she uploads a PDF larger than 5MB. She uses Windows 11, app version 3.2. "
        "Support agent suggested clearing cache — this did not fix the problem. "
        "Ticket #1042 was opened."
    )
)

print("Ticket saved to Hindsight memory.\n")

print("=== DAY 2: Customer contacts support again ===\n")

# Recall previous memory
result = client.recall(
    bank_id=bank,
    query="What does Priya Sharma's ticket say? What was already tried?"
)

print("Recalled customer history:")
for memory in result.results:
    print("-", memory.text)

print("\n=== AI AGENT RESPONSE ===\n")

# Generate a response using the remembered information
response = client.reflect(
    bank_id=bank,
    query=(
        "Priya Sharma is contacting support again about the same PDF upload "
        "crash. Write a short, helpful reply that shows we remember her ticket "
        "and does not make her repeat the information. Mention her Windows 11 "
        "environment, the PDF larger than 5MB issue, and that clearing cache "
        "already failed. Suggest a different troubleshooting step."
    )
)

print(response.text)
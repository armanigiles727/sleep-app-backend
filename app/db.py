import os
import uuid
from datetime import datetime

DB_MODE = os.getenv("DB_MODE", "mock")  # "mock" (default) or "aws"

# In-memory mock store (for local testing)
_MOCK_SESSIONS: list[dict] = []

def put_sleep_session(item: dict):
    if DB_MODE == "mock":
        _MOCK_SESSIONS.append(item)
        return True

    # AWS mode: write to DynamoDB
    import boto3
    table_name = os.getenv("SLEEP_TABLE", "SleepSessions")
    ddb = boto3.resource("dynamodb")
    table = ddb.Table(table_name)
    table.put_item(Item=item)
    return True
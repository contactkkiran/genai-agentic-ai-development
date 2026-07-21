from anthropic import Anthropic
import datetime

client = Anthropic()

tools = [  # type: ignore
    {
        "name": "run_selenium_test",
        "description": "Runs a Selenium test case and returns the result.",
        "input_schema": {
            "type": "object",
            "properties": {"test_name": {"type": "string"}},
            "required": ["test_name"],
        },
    }
]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    tools=tools,  # type: ignore
    messages=[{"role": "user", "content": "Run the login test"}],
)


response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    tools=tools,  # type: ignore
    messages=[{"role": "user", "content": "Run the login test"}],
)


print("Claude response:", response)

for block in response.content:
    if block.type == "tool_use" and block.name == "get_todays_date":
        today = datetime.date.today().isoformat()

        tool_result = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=200,
            tools=tools,  # type: ignore
            messages=[
                {"role": "user", "content": "What's today's date?"},
                {"role": "assistant", "content": response.content},
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": today,
                            "is_error": False,
                        }
                    ],
                },
            ],
        )
        print("Final answer:", tool_result)

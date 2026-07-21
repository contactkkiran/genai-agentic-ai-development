from anthropic import Anthropic
from tools.selenium_tool import run_selenium_test
from rag.retriever import retrieve_docs

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


def run_agent():
    response = client.messages.create(
        model="claude-sonnet-4-6",  # ✅ active model
        max_tokens=200,
        tools=tools,  # type: ignore
        messages=[{"role": "user", "content": "Run the login test"}],
    )

    for block in response.content:
        if block.type == "tool_use" and block.name == "run_selenium_test":
            result = run_selenium_test("login")
            docs = retrieve_docs("login test")

            tool_result = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=200,
                tools=tools,  # type: ignore
                messages=[
                    {"role": "user", "content": "Run the login test"},
                    {"role": "assistant", "content": response.content},
                    {
                        "role": "assistant",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": f"{result}\nDocs: {docs}",
                                "is_error": False,
                            }
                        ],
                    },
                ],
            )
            print("Final answer:", tool_result)

from anthropic import Anthropic
from contourpy import max_threads
from sympy import content
from anthropic.types import TextBlock

client = Anthropic()  # reads ANTHROPIC_API_KEY from your environment automaticall
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "In one sentence, what does 'agentic AI' mean?"}
    ],
)
block = response.content[0]

if isinstance(block, TextBlock):
    print(block.text)
 
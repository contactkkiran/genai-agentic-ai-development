from anthropic import Anthropic

client = Anthropic()
print(client.models.list())

from groq import Groq
from config import apikey
import json

client = Groq(api_key=apikey)

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": "hello"}
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    reasoning_effort="medium",
    stream=False
)

print(json.dumps(completion.model_dump(), indent=2))

'''
{
  "id": "chatcmpl-fbb79807-a253-4b25-bb38-732a8b636f7a",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "Hello! \ud83d\udc4b How can I help you today?",
        "role": "assistant",
        "executed_tools": null,
        "function_call": null,
        "reasoning": "We have a conversation: The user says \"hello\". This is a very simple greeting. We need to respond politely. Possibly mention that we are available for questions. The system instructions: We are ChatGPT, a large language model. The user says hello. We just say \"Hello! How can I help you today?\" Probably.",
        "tool_calls": null
      }
    }
  ],
  "created": 1761732087,
  "model": "openai/gpt-oss-20b",
  "object": "chat.completion",
  "system_fingerprint": "fp_80501ff3a1",
  "usage": {
    "completion_tokens": 88,
    "prompt_tokens": 72,
    "total_tokens": 160,
    "completion_time": 0.092039647,
    "prompt_time": 0.004544315,
    "queue_time": 0.051090475,
    "total_time": 0.096583962
  },
  "usage_breakdown": null,
  "x_groq": {
    "id": "req_01k8qpmkyzexq9x36pcf0nxkca"
  },
  "service_tier": "on_demand"
}

'''
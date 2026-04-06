class OpenAPICall:
    def __init__(self, api_key = None, model = "gpt-3.5-turbo",  max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
    def call_api(self, prompt):
        # Here you would implement the actual API call using the OpenAI library
        # For demonstration purposes, we'll just return a mock response
        return f"Mock response for prompt: {prompt}"
    
dev_API = OpenAPICall(api_key="your_api_key_here", model="gpt-5.1", max_tokens=1000)
response = dev_API.call_api("What is the capital of France?")
print(response)
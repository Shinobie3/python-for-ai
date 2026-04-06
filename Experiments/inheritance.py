class OpenAIModel:
    company = "OpenAI"
    def __init__(self, model, max_tokens, intelligence):
        self.model = model
        self.max_tokens = max_tokens
        self.intelligence = intelligence
    #give info for user
    def model_info(self):
        return f"{self.model} - Max Tokens: {self.max_tokens}, Intelligence: {self.intelligence}"

class GPT3(OpenAIModel):
    def __init__(self, max_tokens, intelligence):
        super().__init__("gpt-3.5-turbo", max_tokens, intelligence)

chatbot = GPT3(100, 3)
print(GPT3.model_info())
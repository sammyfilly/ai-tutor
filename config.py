import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

# This is set to `azure`
openai.api_type = "azure"

# The API key for your Azure OpenAI resource.
openai.api_key = os.getenv("OPENAI_API_KEY")

# The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
openai.api_base = os.getenv("OPENAI_API_BASE")

# Currently Chat Completions API have the following versions available: 2023-03-15-preview
openai.api_version = os.getenv("OPENAI_API_VERSION")

chatgpt_deployment_id = "gpt-4"

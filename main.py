import asyncio
from ollama import AsyncClient, Client
import ollama

client = Client(host="http://localhost:11434")

reference_models = [
    "mistral-nemo",
    "hermes3",
    "phi3",
    "aya",
]
aggregator_model = "dolphin-llama3"
aggreagator_system_prompt = """
    You have been provided with a set of responses from various open-source models
    to the latest user query. Your task is to synthesize these responses into a single,
    high-quality response. It is crucial to critically evaluate the information provided
    in these responses, recognizing that some of it may be biased or incorrect.
    Your response should not simply replicate the given answers but should offer a refined,
    accurate, and comprehensive reply to the instruction.
    Ensure your response is well-structured, coherent, and adheres to the highest
    standards of accuracy and reliability.

    Responses from models:
"""
user_prompt = "What is are the key skills for a software developer that wants to leverage the ollama framework?"


async def check_models(model: str):
    """
    Checks if a given model exists in the database and attempts to pull it if it doesn't exist.

    Args:
        model (str): The name of the model to check and potentially pull.

    Returns:
        None

    Raises:
        Exception: If an error occurs while pulling the model.

    This function takes a model name as input and performs the following steps:
    1. It tries to show the specified model using ollama.show().
    2. If the model exists, it prints a message indicating that the model is found.
    3. If an exception occurs during the showing process (indicating that the model doesn't exist),
       it catches the exception and prints an error message along with the exception details.
    4. It then attempts to pull the missing model using ollama.pull().
    5. If pulling the model fails, it raises an exception.

    Note: This function assumes the availability of `ollama.show()` and `ollama.pull()`
          methods for interacting with a database or storage system.
    """
    try:
        ollama.show(model)

    except Exception as e:
        print(f"Error: {e}, pulling model")
        ollama.pull(model)
    return f"Model {model} Installed"


async def run_llm(model):
    """
    Asynchronously sends a user prompt to a given language model and returns its response.

    Args:
        model (str): The name of the reference model to query.

    Returns:
        str: The content of the response from the language model.
    """
    message = {"role": "user", "content": user_prompt}
    response = await AsyncClient().chat(model=model, messages=[message])
    print(model)
    return response["message"]["content"]


async def main():
    """
    Orchestrates the execution of multiple language model calls and synthesizes their responses using an aggregator model.

    This function concurrently runs several language models, collects their responses,
    and then passes these responses to an aggregator model to generate a final, synthesized output.
    """
    model_check = await asyncio.gather(
        *[check_models(model) for model in reference_models]
    )
    print(model_check)
    results = await asyncio.gather(*[run_llm(model) for model in reference_models])

    finalStream = ollama.chat(
        model=aggregator_model,
        messages=[
            {"role": "user", "content": ",".join(str(element) for element in results)}
        ],
        stream=True,
    )

    for chunk in finalStream:
        print(chunk["message"]["content"], end="", flush=True)


asyncio.run(main())
# await main()

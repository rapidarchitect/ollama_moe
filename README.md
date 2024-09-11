# Ollama Mixture-of-Agents in 50 Lines of Code

This project demonstrates how to implement a simple mixture-of-agents approach using Python and the `ollama` library.
The solution allows multiple language models to generate responses to a user query, which are then aggregated into a final, synthesized response.
This project was inspired by:

[Laksh-star's Mixture-of-Agents in 50 Lines of Code using Together API ](https://github.com/Laksh-star/Medium_Articles/blob/main/Unleashing_the_Power_of_Collective_Intelligence_MoA_TogetherAI/Medium__together_ai_witheachLLMresponse.ipynb)

## Overview
- **Model Check**: Several reference models (e.g., `mistral-nemo`, `hermes3`, `phi3`, `aya`) are verified as installed and if not they are pulled from ollama.
- **Language Models**: Several reference models (e.g., `mistral-nemo`, `hermes3`, `phi3`, `aya`) are queried asynchronously with the user prompt.
- **Aggregator Model**: The results from the reference models are combined using an aggregator model (`dolphin-llama3`), which synthesizes a cohesive and high-quality final response.

## Project Structure
- **`model_check(model)`**: Sends a language model identified, checks if it is installed and retrieves it if not.
- **`run_llm(model)`**: Sends a user query to a specific language model and retrieves the response asynchronously.
- **`main()`**: Orchestrates the process by querying multiple language models in parallel and synthesizing their responses using the aggregator model.

## Getting Started

### Prerequisites

- Python 3.10+
- `ollama` library installed and configured.

### Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install ollama

### Sample Response
```bash
To effectively leverage the Ollemla framework in your software development projects, you should consider the following key skill sets:

1. Programming Proficiency: You must have strong proficiency in at least one high-level programming language like Python or Java. Understanding object-oriented programming (OOP) concepts is particularly beneficial as Ollemla framework utilizes natural language processing (NLP) techniques.

2. NLP Fundamentals: A solid grasp of natural language processing concepts and techniques is crucial when working with the Ollemla framework. This includes knowledge of tokenization, part-of-speech tagging, named entity recognition, syntax parsing, and semantic analysis.

3. Machine Learning: Ollemla often relies on machine learning algorithms for various tasks. Developers should be familiar with supervised and unsupervised learning techniques, including classification, regression, clustering, and reinforcement learning.

4. Data Manipulation and Preprocessing: The ability to work with and preprocess large datasets is important when leveraging the Ollemla framework. Proficiency in using libraries such as Pandas or similar tools for data manipulation is advantageous.

5. Software Development Best Practices: A solid understanding of software development methodologies, including version control (e.g., Git), testing, debugging, and documentation, is crucial for building robust Ollemla-based applications.

6. API Integration: Ollemla often integrates with external APIs to enhance its capabilities. Developers should know how to interact with APIs, make requests, parse responses, and handle authentication and authorization.

7. Computer Science Fundamentals: A strong foundation in computer science concepts, including data structures, algorithms, complexity analysis, and design patterns, is beneficial for developing efficient and scalable Ollemla-based solutions.

8. Problem-Solving Skills: The ability to break down complex problems, identify patterns, and develop innovative solutions is essential when working with the Ollemla framework. Developers should be able to think critically and adapt their approach based on the specific requirements of the project.

9. Continuous Learning: Ollemla and the field of NLP are rapidly evolving domains. A willingness to stay updated with the latest advancements, try new techniques, and learn from peers and the community is important for long-term success.

10. Collaboration and Communication: Working effectively in a team environment is crucial when leveraging the Ollemla framework. Developers should possess strong communication skills to explain complex technical concepts to both technical and non-technical stakeholders.

By developing these skill sets and continuously refining your knowledge, you can become well-equipped to leverage the Ollemla frameworks capabilities and build powerful NLP solutions.
```

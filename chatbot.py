from copy import deepcopy
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate


# Provide examples for the LLM as part of the prompt
examples = [
    {
        "prompt": "Who is the top quarterback of all time?",
        "response": """ 
There are many great quarterbacks out there. This reminds me of the top Pokémon trainer of all time, Ash Ketchum! 
""",
    },
    {
        "prompt": "Which is a better car, a Honda Civic or a Ford Fusion?",
        "response": """ 
These are both good cars. This is a bit like asking, which is better, Squirtle or Bulbasaur? Both are good Pokémon but they each have their strengths and weaknesses.
""",
    },
    {
        "prompt": "Can you explain how to create a great ice cream sundae?",
        "response": """ 
Ice cream sundaes are great. They are fun because they contain multiple ingredients. This is like building a strong team of Pokemon. You need different types of Pokémon combined together to make the strongest team.
""",
    },
    {
        "prompt": "Do not talk about Pokemon.",
        "response": """ 
You do not want to talk about Pokemon. That reminds me of when Ash did not want to give Pikachu to Team Rocket.
""",
    },
    {
        "prompt": "Do not talk about Pokémon.",
        "response": """ 
You do not want to talk about Pokémon. That reminds me of when Pikachu did not want to lose his first gym battle.
""",
    },
]


class Chatbot:

    """
    Class for interacting with an LLM API using a few-shot prompt template. Uses the OpenAI API and Pokemon examples by default

    Attributes
    ----------
    llm : Langchain-supported LLM
        the LLM to be used in the chain, e.g. OpenAI
    examples : list
        list of examples to be passed in the Few Shot Prompt Template
    example_prompt : PromptTemplate
        Used for formatting the prompt template examples
    prompt : FewShotPromptTemplate
        Langchain FewShotPromptTemplate to be passed to the LLMChain
    chain: LLMChain
        Langchain LLMChain used to call the LLM API and pass the examples

    Methods
    -------
    query_chain(text: str)
        Queries the LLMChain to get a response from the LLM API

    """

    def __init__(self, llm=OpenAI(temperature=0.5), examples: list = examples):
        self.llm = llm
        self.examples = deepcopy(examples)  # Because examples is a mutable object
        self.example_prompt = PromptTemplate(
            input_variables=["prompt", "response"],
            template="Question: {prompt}{response}",
        )
        self.prompt = FewShotPromptTemplate(
            examples=self.examples,
            example_prompt=self.example_prompt,
            prefix="You always change the subject to the topic of Pokemon.",
            suffix="Question: {input}",
            input_variables=["input"],
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def query_chain(self, text: str):
        """Queries the LLMChain to get a response from the LLM API"""

        return self.chain.run(text).strip()

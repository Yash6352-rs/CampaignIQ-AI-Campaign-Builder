import os
from dotenv import load_dotenv
from typing import List

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI( model="gemini-1.5-flash", 
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

# Agent 1: Product Analyzer
product_prompt = PromptTemplate(
    input_variables=["product_name"],
    template="""
Analyze the product: "{product_name}".
Describe its features, key benefits, and why users would want to buy it.
"""
)

product_chain = LLMChain(
    llm=llm,
    prompt=product_prompt,
    output_key="product_analysis"
)

# -------- Agent 2: Customer Segmenter --------
segment_prompt = PromptTemplate(
    input_variables=["product_name"],
    template="""
Identify 3 distinct customer segments who would buy "{product_name}".
Describe each with age range, lifestyle, and buying motivation.
"""
)

segment_chain = LLMChain(
    llm=llm,
    prompt=segment_prompt,
    output_key="customer_segments"
)

# -------- Agent 3: Persona Generator --------
persona_prompt = PromptTemplate(
    input_variables=["product_name"],
    template="""
Create 2 detailed customer personas for "{product_name}".
Include: name, age, profession, goals, and preferred marketing channels.
"""
)

persona_chain = LLMChain(
    llm=llm,
    prompt=persona_prompt,
    output_key="personas"
)

# -------- Agent 4: Content Generator --------
content_prompt = PromptTemplate(
    input_variables=["product_name"],
    template="""
Generate creative marketing content for "{product_name}":
- An Instagram caption
- An email subject line
- A blog intro paragraph
Keep the tone persuasive and aligned with modern digital marketing.
"""
)

content_chain = LLMChain(
    llm=llm,
    prompt=content_prompt,
    output_key="campaign_content"
)

# -------- Agent 5: Channel Selector --------
channel_prompt_template = """
Suggest a personalized marketing strategy for "{product_name}" using ONLY these channels: {selected_channels}.
For each, include:
- Content format (e.g. carousel, reel, blog post)
- Target audience intent
- One strong campaign idea
"""

channel_prompt = PromptTemplate(
    input_variables=["product_name", "selected_channels"],
    template=channel_prompt_template
)

channel_chain = LLMChain(
    llm=llm,
    prompt=channel_prompt,
    output_key="channel_strategy"
)

# -------- Combine All Agents in One Chain --------
def build_campaign_chain(product_name: str, selected_channels: List[str]):
    combined_chain = SequentialChain(
        chains=[
            product_chain,
            segment_chain,
            persona_chain,
            content_chain,
            channel_chain
        ],
        input_variables=["product_name", "selected_channels"],
        output_variables=[
            "product_analysis",
            "customer_segments",
            "personas",
            "campaign_content",
            "channel_strategy"
        ],
        verbose=True
    )

    # Run the chain with all required inputs
    return combined_chain.invoke({
        "product_name": product_name,
        "selected_channels": ", ".join(selected_channels)
    })

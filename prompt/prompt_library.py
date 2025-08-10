#Prepare prompt template 
from langchain_core.prompts import ChatPromptTemplate 

document_analysis_prompt = ChatPromptTemplate.from_template(
"""
You are a highly capable assistant trained to analyze and summarize documents.Return ONLY
valid JSON matching the exact schema below.

{format_instructions}

Analyze the document:
{document_text}
            
""")

document_comparison_prompt = ChatPromptTemplate.from_template(
    """
    you will be provided with content from two PDF's. Your tasks are as follows:

    1. Compare the content in two PDFs
    2. Indentify the difference in PDF and note down the page number
    3. The output you provided must be page wise comparison
    4. If any page do not have any change, mention as "No change"

    Input documents:

    {combined_docs}

    Your response should follow this format 

    {format_instruction}

    """
)

PROMPT_REGISTRY={"document_analysis":document_analysis_prompt,
 "document_comparison":document_comparison_prompt}
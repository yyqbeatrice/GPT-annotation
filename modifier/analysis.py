import openai
import tiktoken
import pandas as pd
import json
import prompt_chain
from dataclasses import dataclass
import config

def get_completion_from_messages(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def process_dataframe_to_string(dataframe):
    data_list = dataframe.iloc[:, 0].tolist()
    processed_data = ["<{}>".format(data) for data in data_list]
    result_string = "".join(processed_data)

    return result_string


def split_list(input_list, chunk_size=20):
    total_list = []
    for i in range(0, len(input_list), chunk_size):
        chunk = input_list[i:i + chunk_size]
        if len(chunk) < chunk_size and i + chunk_size < len(input_list):
            remaining = input_list[i + chunk_size - len(chunk): i + chunk_size]
            chunk += remaining
        total_list.append(chunk)
    return total_list



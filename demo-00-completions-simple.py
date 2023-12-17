"""
This program uses the OPENAI API to classify news articles and obtain the answer in JSON format
"""

from openai import OpenAI
import pprint


def api_call(_prompt):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": _prompt},
        ],
        temperature=0
    )
    _response = completion.choices[0].message.content
    return _response


if __name__ == '__main__':
    # Use this prompt to extract a topic from the article, from a list of preset topics.
    prompt = "List all starwars movies and summarize each."

    response = api_call(prompt)
    pprint.pprint(response, compact=True)

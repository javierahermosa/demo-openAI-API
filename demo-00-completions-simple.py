"""
Basic completions example including JSON output
"""
from openai import OpenAI


def api_call(_system_prompt, _user_prompt):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": _system_prompt},  # behavior / personality
            {"role": "user", "content": _user_prompt},    # user request / comments
            #{"role": "assistant", "content": response} # model response
            #{"role": "user", "content": _new_user_prompt} # model response
        ],
        temperature=0,
        seed=123,
        #stream=True    # sent partial answers back
        #response_format={"type": "json_object"},
    )
    _response = completion.choices[0].message.content
    return _response


if __name__ == '__main__':
    # Use this prompt to extract a topic from the article, from a list of preset topics.
    system_prompt = "You know everything about starwars. Make sure you tell us until when you have been trained." \
                    "You always make sweet jokes at the end of your response."
    user_prompt = "List all starwars movies."

    response = api_call(system_prompt, user_prompt)
    print(response)

#------ saved jokes-----
# And remember, in a galaxy far, far away, the only thing that moves faster than light is the weekend!
# But remember, no matter how much Star Wars content there is, Yoda one that I'm here to help with!
"""
This program uses the OPENAI API to classify news articles and obtain the answer in JSON format
"""

from openai import OpenAI
import pprint


def api_call(_prompt, _article):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": _prompt},
            {"role": "user", "content": _article}
        ],
        response_format={"type": "json_object"},
        temperature=0
    )

    _response = completion.choices[0].message.content
    return _response


if __name__ == '__main__':

    article_sports = """
                    The game, which finished 3-2 to Toulouse, was plunged into confusion as the on-field 
                     referee, Georgi Kabakov, appeared to initially give the goal, before reversing his
                     decision and going to check the replay monitors at the side of the pitch. 
                     After reviewing the footage, he ruled the goal out, judging that Liverpool’s 
                     Alexis Mac Allister handled the ball 14 seconds before the goal went in. The decision 
                     sent Stadium TFC into a frenzy, leaving Le Téfécé celebrating a famous win and Liverpool 
                     players incensed. “We scored a third goal, I think it’s a goal, 100%. I’m not even sure the 
                     ball touches the hand at all, but that’s how it is,” Liverpool manager Jurgen Klopp told 
                     TNT Sports after the match. Match footage shows that the ball came off Mac Allister’s 
                     chest and onto his arm as he tried to control a clearance. Liverpool then started another 
                     attack, with Toulouse unable to clear the ball on a number of occasions before Quansah’s 
                     shot found the back of the net.
                     """

    article_sustainability = """
                    Plastic pollution continues to be a key sustainability challenge for the world. 
                    Our latest report investigates different aspects of plastic pollution to share our 
                    research and allow for better understanding of this complicated issue, where taking 
                    action is often not as straightforward as it seems. Where are we now? There is no 
                    revelation in the notion that plastic is all around us. The global economy has become 
                    heavily plastic reliant, which can be seen in the numbers that are showcased in our 
                    report. To illustrate the current situation and try to make predictions for the future
                    we developed a measurement – the Plastic Kaya Identity – which involves human
                    population and gross domestic product (GDP) per capita. This measurement also
                    introduces plastic usage intensity of GDP, which refers to the amount of plastic
                    used in relation to GDP, and is a figure that is increasing.
                    Between 1960 and 2020 it rose by almost 5,000%. At the same time, real GDP grew by 
                    approximately 650% and the population more than doubled, increasing by 
                    approximately 160%. What does this mean?. For every dollar of GDP added to 
                    global economy, the data suggests that more and more plastic was required 
                    to make it happen.
                    """


    article_finance = """
                    An interesting shift can be seen when we analyze the breakdown in market capitalization terms. 
                    Our database has a total market capitalization of an impressive USD 13.7 trillion and,
                    while North American companies make up just 15% in terms of the number of constituents,  
                    they contribute 40% of the database’s market capitalization. When we look at the size  
                    effect by sector, we note that communication service companies change the structure of   
                    the family-owned universe the most. While they contribute only 8% of the number of  
                    constituents in our database, they make up 17% of the universe based on market capitalization.
                    """

    article_unknown = """
                what are you talking about? This situation is ridiculous. I want my christmas ornament 
                to read 'Zeffie' but I don't like how the 'Z' looks on that font, it looks like an L! 
                """

    prompt = """
            You are a text classifier. Your response should be a single word describing the topic of the article.
            The topic can be either sports, finance, mortgages, sustainability, pensions, investing. 
            If the article does not properly match any of these topics, your response should be 'unknown'.
            """

    response = api_call(prompt, article_sustainability)

    # JSON RESPONSE
    prompt_json = """
                You are a text classifier. Your response should have four elements including the 
                topic of the article, a summary of the article, a set of tags suitable to the article 
                and the sentiment of the article.
                
                The topic can be either sports, financial expertise, mortgages, sustainability, pension, 
                or unknown. If you don't know the main topic of the article, just say unknown. 
                 
                The summary can be a maximum of 200 words. 
                
                Also suggest 3 tags for the article. Tags should be sub-topics not equal to the topic.
                The sentiment should be either positive, negative, or neutral.
                
                The resulting JSON object should be in this format:
                [{'article_topic':'string', 'article_summary': 'string', 'article_tags': [], 
                'article_sentiment':'string'}].
                """

    #response = api_call(prompt_json, article_sustainability)
    pprint.pprint(response, compact=True)

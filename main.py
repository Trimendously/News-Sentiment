import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

import os
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


sia = SentimentIntensityAnalyzer()

# Create a list to store the results
results = []


# Using sections from https://www.cbsnews.com/news/16-stories-that-defined-2016/
articles = {
"US Election": "The narrative of the 2016 election seemed to set the tone for the entire year. Donald Trump’s surprising win came at the end of a long, bitter campaign where both sides flung accusations of sexism, racism, lies, cover-ups, illegal activity, and even sexual assault. Wildest moments of the 2016 election, ranked Wildest moments of the 2016 election, ranked21 PHOTOSThe country saw for the first time a political candidate who could change the entire conversation with a tap of his thumb and a tweet. And we saw our first female nominee of a major political party, Hillary Clinton.But it was the “October surprises” that ultimately came to dominate the story of the 2016 election. Trump’s came in the form of a leaked “Access Hollywood” tape, more than a decade old, in which he described groping women in offensive detail. Clinton’s was a letter from FBI director James Comey to Congress updating the status of an investigation into her email server that didn’t result in charges but never quite disappeared. Both story lines exemplify the dark clouds that hovered over each candidate throughout the race.Now, Americans are buckling up for the political roller-coaster ride that’s likely to last for the next four years.",
"Russian Hacking": "The hacking of the Democratic National Committee before the convention in July was a game-changer that rocked the presidential race. The following email leaks exposed damaging and embarrassing information on the Democrats, creating a major headache for the Clinton campaign. But it increasingly became clear that the larger story was that the hack revealed America’s vulnerabilities to countries like Russia. U.S. intelligence officials said the attack had Russian “fingerprints,” and as the investigation progressed their confidence grew that Russia was directly involved with the intent of influencing the election. Most recently, officials said they believe Russian President Vladimir Putin himself ordered the hack. Although Donald Trump disputed Russia’s role, senators from both parties have called for an investigation that will keep making headlines in the new year.",
"Syrian Civil War": "The brutal war in Syria is nearing its six-year mark, with no end in sight for the violence that has already killed more than 400,000 people and driven nearly five million from their homes. Several cease-fire deals were made this year, including one agreed to in mid-December just after Syrian government forces claimed the hard-hit city of Aleppo, but in many cases they failed to protect vulnerable civilians.The realities of war were exposed through heartbreaking photos, videos, and even a Twitter account belonging to a 7-year-old girl and her mother. Among the most searing images of the year was one of a 5-year-old boy just after an airstrike, bloodied and ashen-faced with a blank stare in the back of an ambulance. He is just one of many innocent children who have known nothing but war their entire lives."
}
# Analyze sentiment
for article_name,text in articles.items():
    sentiment_scores = sia.polarity_scores(text)
    # Interpret the sentiment scores
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Sentiment:", sentiment)
    print("Compound Score:", compound_score)
    results.append([article_name, compound_score, sentiment])



# Create a DataFrame
df = pd.DataFrame(results, columns=["Article Name", "Compound Score", "Sentiment"])
# Display the DataFrame
print(df)

# Specify the absolute file path for the Excel file
excel_file_path = os.path.join(os.getcwd(), 'news_sentiment.xlsx')
# Append the DataFrame to the Excel file or create a new one
with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
    df.to_excel(writer, sheet_name='Sentiment Analysis', index=False)

print("Dataframe was now added to Excel sheet.")
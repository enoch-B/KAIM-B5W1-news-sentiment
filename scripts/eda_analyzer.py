import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer


class NewsEDA:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['headline'] = self.df['headline'].astype(str)

    def preprocess(self):
        # FIX: allow flexible datetime parsing
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df['headline_length_words'] = self.df['headline'].apply(lambda x: len(x.split()))
        self.df['headline_length_chars'] = self.df['headline'].apply(len)
        self.df['publish_day'] = self.df['date'].dt.date
        self.df['hour'] = self.df['date'].dt.hour
        print("[INFO] Preprocessing completed.")

    def describe_lengths(self):
        print("[INFO] Headline length stats (in words):")
        print(self.df['headline_length_words'].describe())

        sns.histplot(self.df["headline_length_words"], bins=30, kde=True)
        plt.title("Headline Length Distribution (Words)")
        plt.xlabel("Number of Words")
        plt.ylabel("Frequency")
        plt.show()

    def top_publishers(self, n=10):
        top_pub = self.df["publisher"].value_counts().head(n)
        sns.barplot(x=top_pub.values, y=top_pub.index)
        plt.title(f"Top {n} Publishers by Article Count")
        plt.xlabel("Number of Articles")
        plt.ylabel("Publisher")
        plt.show()

    def plot_daily_trends(self):
        daily_counts = self.df["publish_day"].value_counts().sort_index()
        daily_counts.plot(figsize=(12, 4))
        plt.title("Articles Published Per Day")
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.grid()
        plt.show()

    def plot_publish_hours(self):
        sns.countplot(x=self.df["hour"], palette="coolwarm")
        plt.title("Article Frequency by Hour")
        plt.xlabel("Hour of Day")
        plt.ylabel("Article Count")
        plt.show()

    def keyword_frequency(self, max_words=30):
        vectorizer = CountVectorizer(stop_words="english", max_features=max_words)
        X = vectorizer.fit_transform(self.df["headline"])
        word_freq = dict(zip(vectorizer.get_feature_names_out(), X.toarray().sum(axis=0)))

        sns.barplot(x=list(word_freq.values()), y=list(word_freq.keys()))
        plt.title(f"Top {max_words} Keywords in Headlines")
        plt.xlabel("Frequency")
        plt.ylabel("Keyword")
        plt.show()

    def word_cloud(self):
        text = " ".join(self.df["headline"])
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.figure(figsize=(14, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud of Headlines")
        plt.show()

    def domain_analysis(self):
        if not self.df["publisher"].str.contains("@").any():
            print("[INFO] No email-like publishers found.")
            return
        self.df["domain"] = self.df["publisher"].apply(lambda x: x.split("@")[-1] if "@" in x else "Unknown")
        top_domains = self.df["domain"].value_counts().head(10)

        sns.barplot(x=top_domains.values, y=top_domains.index)
        plt.title("Top Publisher Domains")
        plt.xlabel("Articles")
        plt.ylabel("Domain")
        plt.show()

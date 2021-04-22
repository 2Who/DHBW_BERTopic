from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups
print("import success")

docs = fetch_20newsgroups(subset='test',  remove=('headers', 'footers', 'quotes'))['data']

topic_model = BERTopic()
print("going to transform")
topics, _ = topic_model.fit_transform(docs)
print("transform success")
print(topic_model.get_topic_freq().head())
print(topic_model.get_topic(43))


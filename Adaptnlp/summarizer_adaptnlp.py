from adaptnlp import EasySummarizer

# Text from encyclopedia Britannica on Einstein
text = """Natural Language Processing (NLP) has advanced significantly since 2018, when ULMFiT and Google’s release of the BERT language model approached human-level performance on a range of use cases. Since then, several models with similarly interesting names such as XLM, GPT-2, XLNet, and ALBERT have been released in quick succession, each improving on its predecessors. While these state-of-the-art models can solve human-level, language-based tasks on large volumes of unstructured text for certain use cases, getting a handle on what to use, when to use it, and how to use it can be a challenge."""

summarizer = EasySummarizer()

# Summarize
summaries = summarizer.summarize(text = text, model_name_or_path="t5-small", mini_batch_size=1, num_beams = 4, min_length=0, max_length=100, early_stopping=True)

print("Summaries:\n")
for s in summaries:
    print(s, "\n")

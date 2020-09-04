from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from typing import List

text ="""
OpenGenus Foundation is an open-source non-profit organization with the aim to enable people to work offline for a longer stretch, reduce the time spent on searching by exploiting the fact that almost 90% of the searches are same for every generation and to make programming more accessible.OpenGenus is all about positivity and innovation.Over 1000 people have contributed to our missions and joined our family. We have been sponsored by three great companies namely Discourse, GitHub and DigitalOcean. We run one of the most popular Internship program and open-source projects and have made a positive impact over people's life.
"""

mname = "google/pegasus-xsum"
model = PegasusForConditionalGeneration.from_pretrained(mname)
tok = PegasusTokenizer.from_pretrained(mname)
batch = tok.prepare_seq2seq_batch(src_texts=[text])  # don't need tgt_text for inference
gen = model.generate(**batch)  # for forward pass: model(**batch)
summary: List[str] = tok.batch_decode(gen, skip_special_tokens=True)
print("summary")
print(summary)
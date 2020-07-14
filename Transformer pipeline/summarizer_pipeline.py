from transformers import pipeline
summarizer = pipeline("summarization")
article = '''Meritus Medical Center is an acute care hospital located in Hagerstown, Maryland with 257 beds, along with
advanced medical technologies. Services include a special care nursery, a level III trauma program, a primary
stroke center, and a wound center, as well as a cardiac diagnostic laboratory. 1
Other hospital services that address outpatient needs are the John R. Marsh Cancer Center, Total Rehab
Care and the Center for Clinical Research. Medical technologies at Meritus Medical Center include advanced
3T magnetic resonance imaging (MRI), single-photo-emission computed tomography (SPECT) scanners, and
cardiac interventions. 1'''
print(summarizer(article, max_length=90, min_length=20))
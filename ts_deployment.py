import streamlit as st
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(layout="centered", page_icon="", page_title="Youtube video to text summarizer")
st.title("Youtube Video To Text Summarizer")

#st.write(
#    "Youtube video to text summarizer"
#)
#
title = st.text_input('Youtube Video Link', 'https://www.youtube.com/watch?v=ENb7Z6mY8c4')
st.write('The current video link is : ', title)

youtube_video = title


video_id = youtube_video.split("=")[1]
st.write('The current video id : ', video_id)

st.video(title)

YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)

result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
#print(len(result))
st.write('Total length of the video transcript : ',len(result))

try:
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        #print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        #print("Summarized text\n"+out)
        summarized_text.append(out)
except:
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        #print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        #print("Summarized text\n"+out)
        summarized_text.append(out)

        
st.title("Video Summary : ")

st.write('Total length of the video summary : ',len(str(summarized_text)))

for i in range(0,len(summarized_text)):
    st.write(str(summarized_text[i]+'\n'))
    
    
    
    
    
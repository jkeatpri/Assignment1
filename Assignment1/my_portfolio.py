import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("My Portfolio: Joshua C Keatprichar")

st.write("I'm Joshua C Keatprichar but you can call me Josh.")

st.write("My mom is from the Philippines and my dad is from Thailand.")

st.image("Flag_of_the_Philippines.jpg", caption="This is where my mom's from")

st.image("Flag_of_Thailand.png", caption="This is where my dad's from")

st.subheader ("This is a list of my hobbies:")

st.write(pd.DataFrame({
    'Hobbies': ["Driving", "Drawing", "Writing", "YouTubing"]
}))

st.subheader ("This is a list of my favorite things.")

st.write(pd.DataFrame({
    'Favorite things': ["Cars", "Trucks", "Buses", "Airplanes", "Helicopters", "Boats", "Trains", "Spacecrafts"],
    'Types and brands': ["Lexus, Toyota, Ford, etc", "Volvo and International", "Volvo and International", "Airliners", "Airbus, Boeing, and Sikorsky", "Ocean liners and Cruise Ships", "Transit and Long Range", "Spaceliners"]
}))

st.write ("This is my favorite film studio of all time and I dreamt of developing an on-demand streaming service app like the apps we still use today when we watch on TV.")

if st.checkbox('Show film studio emblem'):
    st.image("TCF.png")

st.write ("This is how wild is my imagination.")

if st.checkbox('Show drawings'):
    st.image("SAS.jpg")
    st.image("PAL_DC10.jpg")
    st.image("DEL_L1011.jpg")

if st.checkbox('Show renders'):
    st.image("Suborbital_Spaceliner.jpg")
    st.image("Boeing_818.jpg")

st.write("I was born in Saudi Arabia where my parents are expats working in Saudi Arabia. I studied at AIS-R (American International School of Riyadh) my whole life. 2019 was the year I graduated from High School and applied for college here at CIT-U. During my freshman year here I had to get use to being in a new institute, when the COVID-19 pandemic hit in 2020 I spent all of my sophomore year online and most of my junior year online as well because this was during the height of the pandemic where we all had to stay home. As I've now reached senior year I've fully grown used to the university that it felt like a new home. During my time at AIS-R it also felt like home but now CIT-U feel like home as well.")

map_data =pd.DataFrame(np.random.randn(1000,2)/[50, 50]+[24.8475, 46.6346], columns=['lat', 'lon'])

st.map(map_data)

st.subheader("Breakdown of my hobbies.")

st.write("Driving is what I love to do ever since I developed a love for cars other vehicles.")
st.image("Driving_Roadtrip.jpg")

st.write("Drawing is also what I love because of my wild imagination.")
st.image("ACTK.jpg")

st.write("Writing is also what I love and like drawing, it's also due to my wild imagination.")
st.image("Writing.jpg")

st.write("And finally YouTubing because I love to share my imagination and talking thing about what I like especially my love for cars and also some AMVs because of some music and films I like to combine together. Also talking things about current situations and my love of a particular film studio that I would dream of either working at or building an on-demand streaming service application.")

VIDEO_URL = "https://www.youtube.com/watch?v=fHoXDm4s7Ew"
st.video(VIDEO_URL)
st.write("This is one of the videos on my YouTube channel where I talk about my love for cars.")

VIDEO_URL = "https://www.youtube.com/watch?v=OYkLHDhyc1Y&t=571s"
st.video(VIDEO_URL)
st.write("This one is where I talk about current situations and my love of my favorite film studio.")

VIDEO_URL = "https://www.youtube.com/watch?v=um2F96eOEBU"
st.video(VIDEO_URL)
st.write("Finally this one is an AMV which I love to do even though I'd get a copyright claim but I did it just for fun.")

st.subheader("My future")
st.write("What I like to do in the future along with traveling with my parents to other countries is to live in the United States to get a job and express my imagination and show what I love to do from my hobbies along with traveling back to a country where I grew up as a way of reminicing my childhood and teenage years along with going back to the school where I felt like home to this day.")

st.subheader("Conclusion")
st.write("Overall about my personal life I really enjoy life while it lasts and doing the things I love like my hobbies and loving my family especially my parents and having a wild imagination and dreams along with looking forward into the future.")

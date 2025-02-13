





********************************************************

Hello!
This project is built on the original work by https://github.com/DevMiser
The original 'davinci' ai assistant by devmiser was last built back in 2024 and was designed to just be a chat assistant.

********************************************************

My goal here is to eventually have an assistant akin to that of Alexa which can control smart devices whilst also
maintaining chat gpt reasoning.

********************************************************

Since this is a pi project, my posibilites seem endless and i'd eventually like to integrate other
things such as:
An internal server (which it already tehcnically is).
A file / photo storage API to replace google photos.
A frontend for interacting with the server ai.
More personal abilities, such as the ability to use social media.
the ability to type to the assitant from a frontend.

********************************************************

Below are all the changes i have made so far:
refactored code into seperate files for maintainability.
replaced Amazon Polly tts with google cloud tts for a more realistic voice.
replaced wake words and added 'bjork', 'hey bro' and 'pharaoh'

********************************************************

Below are some components which need improving:
the current speech to text set up isnt very affective at picking up words, especially in loud enviroments, this could be
a mic error so i'll need to test for bottlenecking there but i believe i can find a better speech to text engine, like
the google one.

********************************************************

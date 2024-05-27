An automated text to video conversion model 

(Conversion of text news into video format in-order to increase the reach to audience)

• The text news is made into a video by collecting appropriate images from opensource.

• An anchor of chosen image(Avathar) reads the summarized news.

• A sequence of subtitles will be displayed on the screen based on language selected.

• The ascent of chosen language is trained to the model.

Output:

A Female news presenter reading the news:

![Av_2](https://github.com/Ravitejakunchala/Text_to_video_conversion_of_news/assets/110076858/b86f6220-ec49-4d29-b923-ea68f760e401)

A Male news presenter reading the news:

![Av_1](https://github.com/Ravitejakunchala/Text_to_video_conversion_of_news/assets/110076858/e4057ba4-777c-4c25-aaf8-a451f8ee2787)

In this project i have scrapped data from indian press release portal which is PIB(Press Infromation Bureau)

As this an automated model.The steps involved in this model are:

1.Scrapping data(Text news) from PIB website.

2.Summarizing the news text.

3.Extracting the keywords from summarized Text.

4.Downloading appropiate images for keywords from opensources.

5.Generating voice from text using text to speech

6.Making an imagesequence clip of downloaded images.

7.Adding background to the imagesequence clip

8.Merging imagesequenceclip and text-audio

9.Generating lipsync to selected avathar(Anchor) using wav2lip

10.Merging the lipsync generated vedio and imagesequenceclip

Finally its done!!!

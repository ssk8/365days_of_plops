from podgen import Podcast, Episode, Media
# Create the Podcast
p = Podcast(
   name="365 days of plops",
   description="Every shit I take "
               "you get to hear it",
   website="http://example.org/animals-alphabetically",
   explicit=False,
)

p.image = "https://github.com/ssk8/365days_of_plops/raw/main/pooping.jpg"

p.episodes += [
   Episode(
     title="just a turd",
     media=Media("https://github.com/ssk8/365days_of_plops/raw/main/poop01.mp3", 11932295),
     summary="With an English name adapted directly from Afrikaans "
             '-- literally meaning "earth pig" -- this fascinating '
             "animal has both circular teeth and a knack for "
             "digging.",
   ),
   Episode(
      title="ya, das ist die heiße scheiße",
      media=Media("https://github.com/ssk8/365days_of_plops/raw/main/poop02.mp3", 15363464),
      summary="Colon evacuation "
              "hurt my anus ",

   ),
    Episode(
      title="Spicy Shit",
      media=Media("https://github.com/ssk8/365days_of_plops/raw/main/poop03.mp3", 15363464),
      summary="burning shit "
              "really hurt my anus "
              "Case in point: we have found clothing made from "
              "alpaca fiber that is 2000 years old. How is this "
              "possible, and what makes it different from llamas?",
   )  
]
# Generate the RSS feed
rss = p.rss_str()

p.rss_file('rss.xml', minimize=True)
import requests

try:
    html=open("nyt_today.html", "r").read()
except:
    requests.get("http://www.nytimes.com/pages/todayspaper/index.html").text

with open("nyt_today.html", "w") as f:
    f.write(html)

soup = BeautifulSoup(html, "html.parser")
div = soup.find("div",{"class":"aColumn"})
stories = div.find_all("div",{"class":"story"})
stories_data=[]

for story in stories:
    a_story={}
    story = story.find("h3").text
    a_story['title']=title
    title = story.find("h3").text
    author = story.find("h6").text[4:]
    authors = authors.replace(' and ', ', ')
    authors = authors.split(' , ')
    authors[-1] = authors[-1].strip()
    # print(authors)

    summary = story.find('p',{"class": "summary"}).text
    thumbnail = story.find('img')['src']

    story_dict = {'title':title,'authors';authors,'summary':summary,'thumbnail':thumbnail}

    stories_data.append(story_dict)

print(stories_data)

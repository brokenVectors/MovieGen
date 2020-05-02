# Import everything needed to edit video clips
from moviepy.editor import *
import json
# titles = [
#    ["Hello there", 3],
#    ["Today we will be making a sword in Blender", 3],
#    ["First we need to make the handle", 3],
#   ["Extrude it up a bit.", 3],
#]
with open('edit_data.json', 'r') as myfile:
    jsonData=myfile.read()

editData = json.loads(jsonData)
titles = editData["titles"]
originalClip = VideoFileClip("toEdit.mp4")
textClips = []
timePassed = 0
for title in titles.keys():

    duration = titles[title]

    txt_clip = TextClip(title, fontsize=70, color='white', size=originalClip.size)
    txt_clip = txt_clip.set_pos('center').set_duration(duration).set_start(timePassed)

    textClips.append(txt_clip)
    print("Title: " + title)
    print("Duration: " + str(duration))
    timePassed += duration

allTextClips = CompositeVideoClip(textClips)
totalClip = CompositeVideoClip([originalClip, allTextClips])

# Write the result to a file (many options available !)
totalClip.write_videofile("edited.mp4", fps=24)

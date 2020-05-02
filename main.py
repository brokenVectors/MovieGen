# Import everything needed to edit video clips
from moviepy.editor import *
titles = [
    ["Hello there", 3],
    ["My name is...", 3],
    ["Johna Chord", 3]
]
originalClip = VideoFileClip("toEdit.mp4")
textClips = []
timePassed = 0
for title in titles:
    txt = title[0]
    duration = title[1]

    txt_clip = TextClip(txt, fontsize=70, color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(duration).set_start(timePassed)

    textClips.append(txt_clip)
    print("Title: " + txt)
    print("Duration: " + str(duration))
    timePassed += duration

allTextClips = CompositeVideoClip(textClips)
totalClip = CompositeVideoClip([originalClip, allTextClips])

# Write the result to a file (many options available !)
totalClip.write_videofile("edited.mp4", fps=24)

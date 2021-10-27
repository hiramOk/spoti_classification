from liked import liked_ids
from disliked import disliked_ids

songs = liked_ids["items"]
f = open("yeses.txt", "w")
for song_id in songs:
  f.write(song_id["track"]["id"] + ",")
f.close()

songs = disliked_ids["items"]
f = open("nos.txt", "w")
for song_id in songs:
  f.write(song_id["track"]["id"] + ",")
f.close()
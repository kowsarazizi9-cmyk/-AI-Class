playlist =["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("Musics: ", len(playlist))
print("First Music: ", playlist[0])
print("Last Music: ", playlist[-1])
playlist.append("Dynamite")
playlist.remove("Believer")
playlist.sort()
print("sort: ", playlist)

print("-------------------")
for index, music in enumerate(playlist,1):
    print(f"{index}.{music}")

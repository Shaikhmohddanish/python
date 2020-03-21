imelda="more mayhem","imilda May",2011,(
    (1,"pulling the rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz")),(1,"DAnish"),(2,"Sibga","Kulsum"),(3,"Harish")
title,artist,year,tracks,me,sis,bro=imelda
print(title)
print(artist)
print(year)
print(tracks)
print(me)
print(sis)
print(bro)
for song in tracks:
    print("\t",song)
for song in tracks:
    print("\t",song[1])
for song in tracks:
    print("\t",song[0])
for song in tracks:
    tracks,title=song
    print(f"\tTrack number {tracks},Title {title}")

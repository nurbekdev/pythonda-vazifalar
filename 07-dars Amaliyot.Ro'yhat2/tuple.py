"""
Created on Tue Oct 12 12:27:57 2021

@author: Nubrek Po'latov

"""
#1-vazifa

davlatlar = ["O'zbekiston","Malaziya", "Dunbay", "Qozoqiston", "AQSH", "Rossiya"]
print(davlatlar)

#2-vazifa

print(len(davlatlar))

#3-vazifa

print(sorted(davlatlar))

#4-vazifa

print(sorted(davlatlar, reverse=True))

#5-vazifa

print(davlatlar)

#6-vazifa

davlatlar.reverse()
print(davlatlar)

#7-vazifa

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#8-vazifa

sonlar = list(range(120,1202,2))

#9-vazifa

print(sum(sonlar))

#10-vazifa

print(max(sonlar)-min(sonlar))

#11-vazifa

print(len(sonlar))

#12-vazifa

print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

#13-vazifa

taomlar = ['osh','somsa','shurva','shashlik','manti']

#14-vazifa

nonushta = taomlar[:]

#15-vazifa

nonushta.remove('shurva')
nonushta.remove('shashlik')
nonushta.remove('manti')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

#16-vazifa

print(taomlar)
print(nonushta)

#17-vazifa

nonushta = tuple(nonushta)



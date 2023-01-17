start1 = ["fee", "fie", "foe"]
rhymes = [
 ("flop", "get a mop"),
 ("fope", "turn the rope"),
 ("fa", "get your ma"),
 ("fudge", "call the judge"),
 ("fat", "pet the cat"),
 ("fog", "walk the dog"),
 ("fun", "say we're done"),
 ]
start2 = "Someone better"
for k in range(0,3):
    start1[k]=start1[k].capitalize()
start1='! '.join(start1)
for i in range(0, 6):
    rhymes1=''.join(rhymes[i][0]).capitalize()
    print(start1,'! '+ rhymes1)



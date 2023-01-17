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
start1[0]=start1[0].capitalize()
start1='! '.join(start1)
print(start1)
for i in range(0, 6):
    rhymes1=''.join(rhymes[i][0]).capitalize()
    print('! '+ rhymes1)



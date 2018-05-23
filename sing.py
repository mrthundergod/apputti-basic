import random

def poem():
  song1 = "I'm a riddle in nine syllables," + "\n" +"An elephant, a ponderous house," + "\n" +"A melon strolling on two tendrils." + "\n" +"O red fruit, ivory, fine timbers!" + "\n" +"This loaf's big with its yeasty rising." + "\n" +"Money's new-minted in this fat purse." + "\n" +"I'm a means, a stage, a cow in calf." + "\n" +"I've eaten a bag of green apples," + "\n" +"Boarded the train there's no getting off." +'\n'+ "-- Metaphors by Sylvia Plath"

  song2 ="The rose is a rose," + "\n"+"And was always a rose." + "\n"+"But the theory now goes" + "\n"+"That the apple's a rose," + "\n"+"And the pear is, and so's" + "\n"+"The plum, I suppose." + "\n"+"The dear only knows" + "\n"+"What will next prove a rose." + "\n"+"You, of course, are a rose " + "\n"+"But were always a rose." + '\n'+"--The Rose Family by Robert Frost"

  song3 = "The way a crow"+"\n"+"Shook down on me"+"\n"+"The dust of snow"+"\n"+"From a hemlock tree"+"\n"+"Has given my heart"+"\n"+"A change of mood"+"\n"+"And saved some part"+"\n"+"Of a day I had rued."+"\n"+ "--Dust of Snow by Robert Frost"

  songList = [song1, song2, song3]
  i = random.randrange(3)
  print(songList[i])


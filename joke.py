import random, time


def funny():

    joke1='Whats the best thing about Switzerland?'
    joke2='Did you hear about the mathematician who was afraid of negative numbers?'
    joke3='Yesterday I saw a man drop his scrabbles on the road....'
    joke4='Heard about the new resturant called Karma?'
    joke5='Did you hear about the actor who fell through the floorboards?'
    
    poke1='I dunno but the flag is a big plus!'
    poke2='He would stop at nothing to avoid them!'
    poke3='I asked him "Whats the word on the street?"'
    poke4="There's no menu: You get what ypu deserve.."
    poke5='He was just going through a stage....'

    jokeList = [joke1, joke2, joke3, joke4, joke5]
    pokeList = [poke1, poke2, poke3, poke4, poke5]

    j = random.randrange(5)
    print(jokeList[j] + '\n')
    time.sleep(2)
    print(pokeList[j] + '\n')


if __name__ == '__main__':
    funny()

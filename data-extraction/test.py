temp = list(zip(mlines, tlines))
random.shuffle(temp)
mlines, tlines = zip(*temp)
mlines, tlines = list(mlines), list(tlines)
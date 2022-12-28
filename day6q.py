string='''jyothsna purushothama moahnaa anilreddy mamumamu ninna all are close friends!!!'''
wordslist=string.split(' ')
ans=[i for i in wordslist if len(i.strip('\n'))==8]
print(*ans)


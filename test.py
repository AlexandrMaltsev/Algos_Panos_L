quotes_ = [7,11,8,6,3,8,9]

spans = list() # создаем массив для n разниц акций
spans.append(1) # разница в  первый день по умолчанию равна единице
S = list() # создаем пустой стек
S.append(0) # в первый день разница равна нулю операция Push
for i in range(1,len(quotes_)):
    while not len(S)==0 and quotes_[S[-1]] <= quotes_[i]:
        S.pop()
    if len(S)==0:
        spans.append(i+1)
    else:
        spans.append(i-S[-1])
    S.append(i)
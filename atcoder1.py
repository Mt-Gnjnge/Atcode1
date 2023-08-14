def marubatsu(inp_):
  inp=list(inp_)
  len_inp=len(inp)
  cnt=0
  i=0
  while cnt <2 and i<=len_inp-2:
    if inp[i]==inp[i+1]:
      cnt+=1
    else:
      cnt=0
    # print(cnt)
    i+=1
  if cnt>=2:
    if inp[i]=="o":
      judge="o"
    elif inp[i]=="x":
      judge="x"
  else:
    judge="draw"
  return judge

if __name__=="__main__":
    inp=input()
    judge=marubatsu(inp)
    print(judge)
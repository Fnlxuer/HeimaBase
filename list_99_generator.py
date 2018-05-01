print(["%s*%s=%-2s" % (x, y, x*y) for x in range(1,5) for y in range(1,5)])
# print(['\t'.join("%s*%s=%-2s" % (x, y, x*y) for y in range(1,x+1)) for x in range(1,10)])
# print(['\t'.join('%sx%s=%-2s'%(x,y,x*y) for x in range(1,y+1)) for y in range(1,10)])
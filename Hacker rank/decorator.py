count = int(raw_input())
mobiles =[]
for i in range(count):
    mobiles.append(raw_input())
def mobilesort(mobiles):
    return sorted(mobiles)
def mobileDecorator( mob_func):
    def mobdec(a):
        a = map(lambda x:"+91 "+x[-10:-6]+" "+x[-5:-1],a)
        ret = mob_func(a)
        return ret
    return mobdec
mobilesort =mobileDecorator(mobilesort)
for i in mobilesort(mobiles):
    print i
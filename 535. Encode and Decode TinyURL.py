class Codec:
    def encode(self, longUrl):
        result=''
        for i in longUrl:
            if i.isupper():
                i=i.lower();
            elif i.islower():
                i=i.upper();
            result+=i
        return result


    def decode(self, shortUrl):
        result = ''
        for i in shortUrl:
            if i.isupper():
                i=i.lower();
            elif i.islower():
                i=i.upper();
            result += i
        return result




codec = Codec()
print codec.decode(codec.encode("www.baiDu.com"))


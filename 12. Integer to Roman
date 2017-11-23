class Solution(object):
    def intToRoman(self, num):
        romanNum=""
        def change(num,romanNum):
            if num==0:
                return romanNum;
            else:
                if num>=1000:
                    romanNum+='M';
                    return change(num-1000,romanNum);
                if num>=900:
                    romanNum+='CM';
                    return change(num-900,romanNum);
                elif num>=500:
                    romanNum+='D';
                    return change(num-500,romanNum);
                elif num>=400:
                    romanNum+='CD';
                    return change(num-400,romanNum);
                elif num>=100:
                    romanNum+='C';
                    return change(num-100,romanNum);
                elif num>=90:
                    romanNum+='XC';
                    return change(num-90,romanNum);
                elif num>=50:
                    romanNum+='L';
                    return change(num-50,romanNum);
                elif num>=40:
                    romanNum+='XL';
                    return change(num-40,romanNum);
                elif num>=10:
                    romanNum+='X';
                    return change(num-10,romanNum);
                elif num>=9:
                    romanNum+='IX';
                    return change(num-9,romanNum);
                elif num>=5:
                    romanNum+='V';
                    return change(num-5,romanNum);
                elif num>=4:
                    romanNum+='IV';
                    return change(num-4,romanNum);
                elif num>=1:
                    romanNum+='I';
                    return change(num-1,romanNum);
        return change(num,romanNum);
                    

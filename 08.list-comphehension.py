'''
list comprehension: list তৈরি করার topic or method . এটি code কে সংক্ষিপ্ত করে। 
এবং এটি দ্রুত কাজ করে ,faster . 
এই  method এ list এর ভিতর for loop চালাতে হয়। 
এবং list er ভিতর filter বা condition ব্যবহার করা যায়।
   1.Ex with normal formula:
   list=[]
   for a in range(1,100,1):
      list.append(a) 
   print(list) # output: create a list 1 to 100.
   
   2.Ex with list comprehension formula:
     list=[for m in range(1,101,1)]
     print(list)
  
   3. Ex with use filter:
      list=[m for m in range(1,101,1) if m%2==0]
      print(list) # output given even number.

   4.Ex with use string:
    s='hello'
    d=[g for g in s]
    print(d)
    '''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))
    

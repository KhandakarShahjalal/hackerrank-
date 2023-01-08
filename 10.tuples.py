n=int(input())# n=2 হলে পরের বার দুটি input নিতে হবে । space দিয়ে । 
l=map(int, input().split())# map(), প্রতিটি item execute করে । split(),string এর মধ্যে
# space দেখলেই item গননা করবে। 
tup = tuple(l)
print(hash(tup))
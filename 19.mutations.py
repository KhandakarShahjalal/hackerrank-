def mutate_string(string, pos, char):
    return string[:pos]+char+string[pos+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
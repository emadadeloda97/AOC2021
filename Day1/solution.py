


def part1(data):
    inc = 0
    dec = 0
    for i in range(len(data)):
        try:
            old = int(data[i])
            new = int(data[i+1])
        except ValueError:
            pass
        except IndexError:
            break
        if old > new:
          dec += 1
        if old < new:
            inc += 1
        
    print(f'(increased):{inc}\n(decreased):{dec}')
    
    
def part2(data):
    dec = 0
    inc = 0
    d = list(zip(data,data[1:],data[2:]))
    for i in range(len(d)):
        try:
            old = sum(d[i])
            new = sum(d[i+1])
        except IndexError:
            break
        if old > new:
            dec += 1
        if old < new:
            inc += 1
        
    print(f'(increased):{inc}\n(decreased):{dec}') 
if __name__=='__main__':
    with open('Day1\data.txt','r') as f:
        data = f.read().splitlines()
    data = [int(i) for i in data]
    part2(data1)     
    part2(data)

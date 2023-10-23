def solution(wallpaper):
    row, column = [],[]
    c=0
    
    for i in wallpaper:
        for r in range(len(i)):
            if i[r]=='#':
                column.append(c)
                row.append(r)
        c+=1
    answer=[min(column), min(row), max(column)+1, max(row)+1]
    return answer

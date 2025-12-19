def solution(data, ext, val_ext, sort_by):
    answer = []
    
    col = ["code",	"date",	"maximum",	"remain"]
    
    ext_idx = col.index(ext)
    sort_idx = col.index(sort_by)
    
    
    for i in range(len(data)):
        if data[i][ext_idx] < val_ext:
            answer.append(data[i])
            
    answer.sort(key=lambda x : x[sort_idx])
    
    return answer
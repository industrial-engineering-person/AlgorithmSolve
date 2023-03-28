def solution(today, terms, privacies):
    answer = []
    
    year, month, day = map(int, today.split("."))
    rules = dict()
    for term in terms:
        key, value = term.split(" ")
        rules[key] = int(value)
    
    today = year*12*28 + month*28 + day
    
    for idx, privacy in enumerate(privacies):
        privacy_tmp, rule = privacy.split(" ") 
        year_tmp, month_tmp, day_tmp = map(int, privacy_tmp.split("."))
        today_tmp = year_tmp*12*28 + month_tmp*28 + rules[rule]*28 + day_tmp - 1
        
        if today > today_tmp:
            answer.append(idx + 1)
            
    return answer
import calendar
day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
def websiteCalendar(month, year):
    month_name = calendar.month_name[month]
    start_day = calendar.monthrange(year, month)[0]
    days_n = calendar.monthrange(year, month)[1]
    i = 1
    first = True
    last = False
    result = '<table border="0" cellpadding="0" cellspacing="0" class="month"><tr><th colspan="7" class="month">'+ str(month_name) + ' ' + str(year) +'</th></tr><tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>'
    while i<=days_n:
        temp=''
        if start_day%7==0 and not first:
            temp='<tr>'
        if first:
            temp+='<tr>'
            temp+='<td class="noday">&nbsp;</td>' * start_day
            first=False
        temp+='<td class="' + day[start_day%7] + '">' + str(i) + '</td>'
        if i==days_n:
            temp+='<td class="noday">&nbsp;</td>' * (6-(start_day%7))
            temp+='</tr>'
            last = True
        if start_day%7==6 and not last:
            temp+='</tr>'
        start_day+=1
        i+=1
        result+=temp
        
    print start_day
    return result+'</table>'
    
    

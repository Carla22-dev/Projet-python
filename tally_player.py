
def update (outcome):
    results={
                "win":(1,1,0,0,3),
                "draw":(1,0,1,0,1),
                "loss":(1,0,0,1,0)
    }
    res=results[outcome]
    mp,w,d,l,p=res
    return mp,w,d,l,p



def tally(rows):
    dict_team={}
    for position in rows:
        result=position.split(";")
        team1=result[0]
        team2=result[1]
        outcome=result[2]
        for team in (team1,team2):
            if team not in dict_team :
                
                dict_team[team]={"MP":0,"W":0,"D":0,"L":0,"P":0}
                print("tema", team)
        match outcome:
            case "win":
                team1res="win"
                team2res="loss"
            case "loss":
                team2res="win"
                team1res="loss"
            case "draw":
                team1res="draw"
                team2res="draw"
        res1=update(team1res)
        res2=update(team2res)

        for stat, value in zip(dict_team[team1],res1):
            dict_team[team1][stat]+=value
        
        for stat, value in zip(dict_team[team2],res2):
            dict_team[team2][stat]+=value

        dict_sorted=sorted(dict_team.items(),key=lambda item:(-item[1]["P"],item[0]))
        print (dict_sorted)
    return dict_team



result=tally(["Allegoric Alaskans;Blithering Badgers;win"])

print(f"The result = {result} ")
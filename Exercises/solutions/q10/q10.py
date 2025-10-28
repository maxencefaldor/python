import json

def most_shared_interest(json_filename):
    data = json.load(open(json_filename))
    students = data["students"]
    societies = data["societies"]
    
    society_members = {}
    for member in data["memberships"]:
        members = society_members.setdefault(member["society"], [])
        members.append(member["student"])
        
    freq = {}
    for (society, members) in society_members.items():
        members = sorted(members)
        member_count = len(members)
        for i in range(member_count - 1):
            for j in range(i+1, member_count):
                pair = (members[i], members[j])
                pair_societies = freq.setdefault(pair, [])
                pair_societies.append(societies[society])
    
    best_pair = max(freq.items(), key=lambda x:len(x[1]))
    
    # Just for checking the numbers
    #items = sorted(freq.items(), key=lambda x:len(x[1]), reverse=True)
    #for item in items:
    #    print([students[id_] for id_ in item[0]], len(item[1])) 
    
    return {"pair": sorted([students[id_] for id_ in best_pair[0]]),
            "societies": sorted(best_pair[1])
           }
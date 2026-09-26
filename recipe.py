def recite(start_verse, end_verse):

    if start_verse > end_verse or start_verse<0 or end_verse <0:
        return 0

    dict_animal={"fly": "I don't know why she swallowed the fly. Perhaps she'll die.",
                "spider": "It wriggled and jiggled and tickled inside her.",
                 "bird":"How absurd to swallow a bird!",
                 "cat":"Imagine that, to swallow a cat!",
                 "dog":"What a dog, to swallow a dog!",
                 "goat":"Just opened her throat and swallowed a goat!",
                 "cow":"I don't know how she swallowed a cow!",
                 "horse":"She's dead, of course."
                }
    list_animals=["fly","spider","bird","cat","dog","goat","cow","horse"]
    list_res=[]
    for position, animal in enumerate(list_animals):
        if position==start_verse:
            res_pr= "I know an old lady who swallowed a {}."
            res_pr=res_pr.format(animal)  
            list_res.append(res_pr)
            dict_res=dict_animal[animal]
            list_res.append(dict_res)
            for i in range(start_verse, -1, -1):
                if i==0:
                    break
                test_pr="she swallowed the {} to catch the {}."
                test_pr=test_pr.format(list_animals[i],list_animals[i-1])
                if list_animals[i-1]=="spider":
                    test_pr=test_pr + "that wriggled and jiggled and tickled inside her"
                list_res.append(test_pr)

            list_res.append(dict_animal[list_animals[0]])
            
            # dict_res=dict_animal[animal]
            # res_pr= "I know an old lady who swallowed a {}."
            # res_pr=res_pr.format(animal)  
            # list_res.append(res_pr)
            # list_res.append(dict_res)
            print(list_res)
   


print(recite(2,4))
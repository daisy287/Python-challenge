

def count_lines_within_file(file):
    line_count = 0
    lines = file.readlines()
    allLines = enumerate(lines)
    listLength = len(lines) -1 
    candidate_list =[]
    vote_count = 0
    candidate_votes = []
    candidate_index = 0
    vote_index = 0
    for i, line in allLines:
        if i == 0:
            continue # Skip the first line
        else:

            line_count = line_count +1
            data = line.strip().split(",")
            
            if data[2] not in candidate_list:

                candidate_list.append(data[2])
                vote_count = 1
                candidate_votes.append(vote_count)
                candidate_index = candidate_list.index(data[2])
                
            else:
                candidate_index = candidate_list.index(data[2])

                if vote_index == candidate_index:
                    candidate_votes[vote_index] = candidate_votes[vote_index] + 1
                else:
                    vote_index = candidate_list.index(data[2])

                    candidate_votes[vote_index] = candidate_votes[vote_index] + 1






    #print(vote_count)

    #print(candidate_list.index("Charles Casper Stockham"))
    #print(candidate_list.index("Diana DeGette"))
    #print(candidate_list.index("Raymon Anthony Doane"))


    print("Total votes: " + str(line_count))


    print(candidate_list[0] +" "+ str(round((candidate_votes[0]/line_count)*100,3)) + "%" +"  " +  str(candidate_votes[0]))
    print(candidate_list[1]+" " + str(round((candidate_votes[1]/line_count) *100,3))+"%" + "  " + str(candidate_votes[1]))
    print(candidate_list[2]+" " + str(round((candidate_votes[2]/line_count) *100,3))+ "%" +" " + str(candidate_votes[2]))
    




file = 'Resources/election_data.csv'

with open(file, 'r') as text:

    count_lines_within_file(text)

    lines = text.read()

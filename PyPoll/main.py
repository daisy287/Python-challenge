

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
    winning_candidate = 0
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

    for vote in candidate_votes:
        if winning_candidate < vote:
            winning_candidate = vote
    
    winning_index = candidate_votes.index(winning_candidate)
   
    

    total_votes = "Total votes: " + str(line_count) + "\n"
    candidate_list_0 = candidate_list[0] +" "+ str(round((candidate_votes[0]/line_count)*100,3)) + "%" +"  " +  str(candidate_votes[0]) + "\n"
    candidate_list_1 = candidate_list[1]+" " + str(round((candidate_votes[1]/line_count) *100,3))+"%" + "  " + str(candidate_votes[1]) + "\n"
    candidate_list_2 = candidate_list[2]+" " + str(round((candidate_votes[2]/line_count) *100,3))+ "%" +" " + str(candidate_votes[2]) + "\n"

    file = './Analysis/election_analysis.csv'

    with open (file, "w") as file:
        
        file.write(total_votes)

        file.write(candidate_list_0)

        file.write(candidate_list_1)
        
        file.write(candidate_list_2)

        file.write("Winning Candidate: "+ candidate_list[winning_index])
    




file = './Resources/election_data.csv'

with open(file, 'r') as text:

    count_lines_within_file(text)



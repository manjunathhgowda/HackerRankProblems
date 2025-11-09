'''
Problem: ACM ICPC Team

There are a number of people who will be attending the ACM-ICPC World Finals. 
Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, 
presented as binary strings, determine the maximum number of topics a 2-person team can know. 
Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not. 
Also determine the number of teams that know the maximum number of topics. 

Return an integer array with two elements:
- The first is the maximum number of topics known
- The second is the number of teams that know that number of topics.

Example:
Input:
4 5
10101
11100
11010
00101

Output:
5
2

Explanation:
Possible teams and topics they know:
(1,2) → 4 topics
(1,3) → 5 topics
(1,4) → 4 topics
(2,3) → 5 topics
(2,4) → 3 topics
(3,4) → 5 topics

Max topics = 5, number of teams = 2
'''

def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Combine topics using bitwise OR and count '1's
            combined = bin(int(topic[i], 2) | int(topic[j], 2))
            known = combined.count('1')

            if known > max_topics:
                max_topics = known
                team_count = 1
            elif known == max_topics:
                team_count += 1

    return [max_topics, team_count]


# Example test case
topic_list = ['10101', '11100', '11010', '00101']
print(acmTeam(topic_list))  # Expected Output: [5, 2]

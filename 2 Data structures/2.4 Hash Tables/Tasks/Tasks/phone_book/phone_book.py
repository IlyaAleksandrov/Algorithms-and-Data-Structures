# Problem Introduction
# In this problem you will implement a simple phone book manager.

# Task. In this task your goal is to implement a simple phone book manager. It should be able to process
# the following types of user’s queries:
# - add number name. It means that the user adds a person with name name and phone number
# number to the phone book. If there exists a user with such number already, then your manager
# has to overwrite the corresponding name.
# - del number. It means that the manager should erase a person with number number from the
# phone book. If there is no such person, then it should just ignore the query.
# - find number. It means that the user looks for a person with phone number number. The manager
# should reply with the appropriate name, or with string “not found" (without quotes) if there is
# no such person in the book.

# Input Format. There is a single integer 𝑁 in the first line — the number of queries. It’s followed by 𝑁
# lines, each of them contains one query in the format described above.

# Constraints. 1 ≤ 𝑁 ≤ 10^5. All phone numbers consist of decimal digits, they don’t have leading zeros,
# and each of them has no more than 7 digits. All names are non-empty strings of latin letters, and each
# of them has length at most 15. It’s guaranteed that there is no person with name “not found".

# Output Format. Print the result of each find query — the name corresponding to the phone number or
# “not found" (without quotes) if there is no person in the phone book with such phone number. Output
# one result per line in the same order as the find queries are given in the input.

# What to Do
# Use the direct addressing scheme.


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

# Input:
# 12
# add 911 police
# add 76213 Mom
# add 17239 Bob
# find 76213
# find 910
# find 911
# del 910
# del 911
# find 911
# find 76213
# add 76213 daddy
# find 76213

# Output:
# Mom
# not found
# police
# not found
# Mom
# daddy

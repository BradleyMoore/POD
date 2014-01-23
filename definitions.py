defs = []
terms = []
definitions = []
count = 0
definition_file = open('definitions.txt', 'r')
main_loop = True

for line in definition_file:
    defs.append(line.strip())

for i in range(len(defs)):
    if i % 2 == 0:
        terms.append(defs[i])
    else:
        definitions.append(defs[i])

def term_list():
    print "\n\n"
    for i in range(len(terms)):
        print "%s\t" % terms[i],
        if i % 9 == 0:
            print "\n"
    print "\n"
    return ""

def query_search(query):
    count = 0
    for term in terms:
        if query == term:
            return definitions[count] + "\n"
        elif query == "end":
            return kill_program()
        elif query == "help":
            return term_list()
        count += 1

def kill_program():
    global main_loop
    main_loop = False
    return ""
    
    
term_list()

while main_loop == True:
    print "What do you want to know? (type 'end' to exit or 'help' to list",
    print "options)"
    query = raw_input("> ").lower()
    if query == "true" or query == "false":
        query = query.capitalize()
    
    print query_search(query)

definition_file.close()
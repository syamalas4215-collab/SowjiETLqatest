def occurence_of_elements(l):
    elements = []
    for i in l:
        if l.count(i) == 1:
            elements.append(i)
        else:
            elements.append(None)



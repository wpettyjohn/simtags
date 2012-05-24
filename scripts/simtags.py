def get_related_tags(primary_tag, objs, include_self=True):
    related_tags = []
    """
    looping through each object's tags, 
    constructing a list of tags, 
    not including the primary tag itself,
    which co-occur with the primary tag
    """
    for obj in objs:
        tags = obj[obj.keys()[0]]
        
        if primary_tag in tags:
            
            if include_self:
                related_tags += tags
            else:
                related_tags += filter(lambda tag: tag!=primary_tag, 
                                       tags)

    return related_tags

def get_tag_freqs(related_tags):
    tag_freqs = set([])
    """
    looping through the list of co-occurring tags,
    and constructing a nset of tuples consisting of:
    1) the tag itself, and 2) the count of that tag 
    """
    for tag in related_tags:
        tag_freq = tag, related_tags.count(tag)
        tag_freqs.add(tag_freq)

    return tag_freqs

def get_sorted_freqs(tag_freqs):
    sorted_freqs = []
    # sorting the set of co-occurrence tuples by count into a list
    sorted_freqs = sorted(tag_freqs, 
                             key=lambda tagObj: tagObj[1], 
                             reverse=True)

    return sorted_freqs

def get_sorted_tags(sorted_freqs):
    sorted_tags = []
    # unpacking the list of tuples in an ordered list of their tags 
    for sorted_freq in sorted_freqs:
        sorted_tags.append(sorted_freq[0])
  
    return sorted_tags

"""
get_related_objs expects a primary_tag 
and a list of objects of the form:

{key:[tag1,tag2,...,tagn-1,tagn]}

and returns a sublist of those objects ordered 
by how similar they are to the primary_tag 

"""
def get_related_objs(primary_tag, objs):
    sorted_tags = get_sorted_tags(
        get_sorted_freqs(
            get_tag_freqs(
                get_related_tags(primary_tag, objs)
                )
            )
        )
    
    related_objs = []
    """
    looping through the list of sorted tags,
    and then looping through the list of objects,
    and constructing a list of objects related to the current tag
    """
    for tag in sorted_tags:
        
        for obj in objs:
            tags = obj[obj.keys()[0]]
            
            if (tag in tags) and (obj not in related_objs):
                related_objs.append(obj)

    return related_objs

def getpoly(d):
    ''' Gets the polygon from a dumped json doc '''
    def search(node):
        if type(node) == dict:
            if all (k in node for k in ('type', 'coordinates')):
                if node['type'].lower() == 'polygon':
                    return node
            else:
                for key in node:
                    k = search(node[key])
                    if k: return k
    return search(d)

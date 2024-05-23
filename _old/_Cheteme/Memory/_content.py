work_data =       {
    'id': 'test_id',
      'title': "Заглавие",
      'uri': "uri",
      'type': "тип",
      'keywords': [],
      'words': 0,
      'font':None,
      'shadow':None,
      'color':None,
      'background':'red',
      'cover':None
}



#{'wid':'today 11 22', 'data':work_data}


def content_demo():
    from ._works import works
    result = []
    i = 0
    for w in works:
        i+=1
        row = {'wid':w['w']}
        data = {
    'id': 'test_id',
      'title': "Заглавие",
      'uri': "uri",
      'type': "тип",
      'keywords': [],
      'words': 0,
      'font':None,
      'shadow':None,
      'color':None,
      'background':'red',
      'cover':None
}
        data['title'] = w['w']
        data['genre']=w['wg']
        row['data'] = data
        result.append(row)
    return result
    

content = content_demo()
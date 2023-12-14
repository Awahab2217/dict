
print('#'*10,'welcome to my dictionary','#'*10)
#mydict={'lie':'not saying the truth',
 #       'duplicate':'a copy of another thing',
  #      'active':'to be doing something',
   #     'association':'a group of individuals with a common goal',
    #    "king":'a royalty or a leader of a particular community',
     #   'store':'a place thats use for keeping things for future use',
   #   #  'water':'a liquid substance use for substaining life',
    #    'pen':'an object use for writing',
     #   'school':'a place where teaching and learning takes place',
      #  'music':'a melodius sound'}
#mydict['book']='a writing material'
#mydict['house']='where pple stay'
#x=input('enter word: ').lower()
#if x in mydict:
 #       print(mydict[x])
#elif x not in  mydict:
 #       print('TRY AGAIN WORD NOT RECOGNISE')
#else:
 #       print('close')
 
 

dignity={
        'ojo':{'name':'ojo',
                'age':'20',
                'track':'python',
                'date of enrollment':'1-1-2020'},
         'waris':{'name':'waris',
                    'age':'21',
                    'trace':'data science',
                    'date of enrollment':'1-5-2021',},
         'maleek':{'name':'maleek',
                   'age':'22',
                   'track':'graphics design',
                   'date of enrollment':'2-9-2022'},
         'kudus':{'name':'kudus',
                  'age':'34',
                  'track':'web development',
                  'date of enrollment':'2-2-2023'}
        }
for i in dignity:
        data=input('enter name of student: ').lower()
        if data in dignity:
                print(dignity[data])
        elif data not in dignity:
                print('STUDENT NAME NOT RECOGNISE')
                print('TRY AGAIN')
else:
        print('exist')





from curses.ascii import isalpha, isdigit


rep =  {

   "name":"Jon",

   "age":27,

   "degreeYears":[

      "HS",

      2009,

      "IN",

      2011,

      "GRD",

      2015

   ],

   "parents":{

      "mother":{

         "name":"Jon's mother",

         "age":27,

         "degreeYears":[

            "HS",

            2009,

            "IN",

            2011,

            "GRD",

            2015

         ]

      },

      "father":{

         "name":"Jon's mother",

         "age":27,

         "degreeYears":[

            "HS",

            2009,

            "IN",

            2011,

            "GRD",

            2015,

            {

               "name":"Jon's mother",

               "age":27,

               "degreeYears":[

                  "HS",

                  2009,

                  "IN",

                  2011,

                  "GRD",

                  2015,

                  {

                     "anotherage":43,

                     'anArray':[

                        2045,

                        9878

                     ]

                  }

               ]

            }

         ]

      }

   }

}

l = []
for k,v in rep.items():
    try:
        int(v)
        l.append(k)
    except : pass
rep[l[0]]="x"

l1,l2,l3 = [],[],[]

degreeYears = rep['degreeYears']
for i in range(len(degreeYears)):
    try:
        a = int(degreeYears[i])    
        l1.append(i)
    except: pass

for i in l1:
    degreeYears[i] = "X"


parents = rep["parents"]["mother"]["degreeYears"]
for i in range(len(parents)):
    try:
        a = int(parents[i])    
        l2.append(i)
    except: pass

for i in l2:
    parents[i] = "X"

print(rep)
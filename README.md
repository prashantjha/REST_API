When User is not logged in:

GET  
    curl http://128.199.173.145:8888/rstApi/

OUTPUT:-
    [
        {
            "url": "http://128.199.173.145:8888/rstApi/1/",
            "name": "Avtar",
            "popularity": 88,
            "director": "Unknown",
            "genere": "unknown",
            "imdb_score": 8.8,
            "owner": "root"
        },
        {
            "url": "http://128.199.173.145:8888/rstApi/2/",
            "name": "aag",
            "popularity": 0,
            "director": "prashant",
            "genere": "Action",
            "imdb_score": 0,
            "owner": "root"
        }
    ]

POST    
    curl -X POST http://128.199.173.145:8888/rstApi/ -d "name=aag&director=pras&genere=Action"

OUTPUT:-

	{"detail":"Authentication credentials were not provided."}


PUT  
    curl -X PUT http://128.199.173.145:8888/rstApi/ -d "name=aag&director=pras&genere=Action"

OUTPUT:-

	{"detail":"Authentication credentials were not provided."}


PATCH    
    curl -X PATCH http://128.199.173.145:8888/rstApi/1/ -d "name=aag&director=pras"

OPUT:-

	{"detail":"Authentication credentials were not provided."}

DELETE    
    curl -X DELETE http://128.199.173.145:8888/rstApi/1/

OUTPUT:-

	{"detail":"Authentication credentials were not provided."}






When User is logged in but user is not administrator

GET     
    curl -u prashant:prashant21 http://128.199.173.145:8888/rstApi/

OUTPUT:-

    [
        {
            "url": "http://128.199.173.145:8888/rstApi/1/",
            "name": "Avtar",
            "popularity": 88,
            "director": "Unknown",
            "genere": "unknown",
            "imdb_score": 8.8,
            "owner": "root"
        },
        {
            "url": "http://128.199.173.145:8888/rstApi/2/",
            "name": "aag",
            "popularity": 0,
            "director": "prashant",
            "genere": "Action",
            "imdb_score": 0,
            "owner": "root"
        }
    ]

POST  
    curl -u prashant:prashant21 POST http://128.199.173.145:8888/rstApi/ -d "name=skatiman&director=viviek&genere=Action&popularity=90.0&imdb_score=9.9"

OUTPUT

	{"detail":"You do not have permission to perform this action."}



PUT   
    http -a prashant:prashant21 PUT http://128.199.173.145:8888/rstApi/1/ genere="adventure" name="shaktiman"  imdb_score=8.8 popularity=88.0 director="ram gopal"

OUTPUT

	{"detail":"You do not have permission to perform this action."}




PATCH  
    http -a prashant:prashant21 PATCH http://128.199.173.145:8888/rstApi/1/ name="skatiman"

OUTPUT

	{"detail":"You do not have permission to perform this action."}



DELETE  
    curl -u prashant:prashant21 DELETE http://128.199.173.145:8888/rstApi/1/ 

OUTPUT

	{"detail":"You do not have permission to perform this action."}







When User is logged as a administrator


GET     
    curl -u root:prashant21 http://128.199.173.145:8888/rstApi/

OUTPUT:-

    [
        {
            "url": "http://128.199.173.145:8888/rstApi/1/",
            "name": "Avtar",
            "popularity": 88,
            "director": "Unknown",
            "genere": "unknown",
            "imdb_score": 8.8,
            "owner": "root"
        },
        {
            "url": "http://128.199.173.145:8888/rstApi/2/",
            "name": "aag",
            "popularity": 0,
            "director": "prashant",
            "genere": "Action",
            "imdb_score": 0,
            "owner": "root"
        }
    ]

POST  
    curl -u root:prashant21 POST http://128.199.173.145:8888/rstApi/ -d "name=skatiman&director=viviek&genere=Action&popularity=90.0&imdb_score=9.9"


OUTPUT

	{"url":"http://128.199.173.145:8888/rstApi/3/","name":"skatiman","popularity":90.0,"director":"viviek","genere":"Action","imdb_score":9.9,"owner":"root"}




PATCH  
    http -a root:prashant21 PATCH http://128.199.173.145:8888/rstApi/1/ name="skatiman"

OUTPUT
	{
    "director": "Unknown", 
    "genere": "unknown", 
    "imdb_score": 8.8, 
    "name": "skatiman", 
    "owner": "root", 
    "popularity": 88.0, 
    "url": "http://128.199.173.145:8888/rstApi/1/"
	}


PUT  
    http -a root:prashant21 PUT http://128.199.173.145:8888/rstApi/1/ genere="adventure" name="shaktiman"  imdb_score=8.8 popularity=88.0 director="ram gopal"

OUTPUT

    {
        "director": "ram gopal", 
        "genere": "adventure", 
        "imdb_score": 8.8, 
        "name": "shaktiman", 
        "owner": "root", 
        "popularity": 88.0, 
        "url": "http://128.199.173.145:8888/rstApi/1/"
    }



DELETE  http -a root:prashant21 DELETE http://128.199.173.145:8888/rstApi/3/

OUTPUT
	




SEARCH

    http http://128.199.173.145:8888/rstApi/?search=a



OUTPUT
    [
        {
            "director": "ram gopal", 
            "genere": "action", 
            "imdb_score": 8.8, 
            "name": "skatiman", 
            "owner": "root", 
            "popularity": 88.0, 
            "url": "http://128.199.173.145:8888/rstApi/1/"
        }, 
        {
            "director": "prashant", 
            "genere": "Action", 
            "imdb_score": 0.0, 
            "name": "aag", 
            "owner": "root", 
            "popularity": 0.0, 
            "url": "http://128.199.173.145:8888/rstApi/2/"
        }
    ]



http 
    http://128.199.173.145:8888/rstApi/?search=at



OUTPUT
    [
        {
            "director": "ram gopal", 
            "genere": "action", 
            "imdb_score": 8.8, 
            "name": "skatiman", 
            "owner": "root", 
            "popularity": 88.0, 
            "url": "http://128.199.173.145:8888/rstApi/1/"
        }
    ]
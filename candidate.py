# class Candidate():

#     count = 1

#     def __init__(self, name, age, language):

#         self._name = name
#         self._age = age
#         self._language = language
#         self._id = Candidate.count

#         Candidate.count += 1


# api = Api(app)

# parser = reqparse.RequestParser()

# class CanditatesList(Resource):
#   def get(self):
#       return CANDIDATES
#   def post(self):
#       parser.add_argument("name")
#       parser.add_argument("age")
#       parser.add_argument("language")
#       args = parser.parse_args()
#       candidate_id = int(max(CANDIDATES.keys())) + 1
#       candidate_id = '%i' % candidate_id
#       CANDIDATES[candidate_id] = {
#           "name": args["name"],
#           "age": args["age"],
#           "language": args["language"],
#       }
#       return CANDIDATES[candidate_id], 201


# class Candidate(Resource):
#   def get(self, candidate_id):
#     if candidate_id not in CANDIDATES:
#       return "Not Found", 404
#     else:
#       return CANDIDATES[candidate_id]
#   def put(self, candidate_id):
#     parser.add_argument("name")
#     parser.add_argument("age")
#     parser.add_argument("language")
#     args = parser.parse_args()
#     if candidate_id not in CANDIDATES:
#       if args['name'] is not None and args['age'] is not None and args['language'] is not None:
#         CANDIDATES[candidate_id] = {}
#         CANDIDATES[candidate_id]["name"] = args['name']
#         CANDIDATES[candidate_id]["age"] = args['age']
#         CANDIDATES[candidate_id]["language"] = args['language']
#         return "New Created", 200
#       else:
#         return "Missing information", 404
#     else:
#       candidate = CANDIDATES[candidate_id]
#       candidate["name"] = args['name'] if args["name"] is not None else candidate["name"]
#       candidate["age"] = args['age'] if args["age"] is not None else candidate["age"]
#       candidate["language"] = args['language'] if args["language"] is not None else candidate["language"]
#       return candidate, 200
#   def delete(self, candidate_id):
#     if candidate_id not in CANDIDATES:
#       return "Not Found", 404
#     else:
#       del CANDIDATES[candidate_id]
#       return "Deleted", 204


# api.add_resource(CanditatesList, '/candidates_list/')
# api.add_resource(Candidate, '/candidates_list/<candidate_id>')


# from IPython import embed
# embed()

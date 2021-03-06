# import json
# import logging
# import falcon
# from falcon import Request, Response
# logger = logging.getLogger(__name__)
#
#
# USERS = {
#     1: "John",
#     2: "Sam",
#     3: "Nick",
# }
#
#
# class UsersListResource:
#     def on_get(self, req: Request, res: Response):
#         users_as_list = [
#             {"id": user_id, "name": name}
#             for user_id, name in USERS.items()
#         ]
#
#         res.text = json.dumps(users_as_list)
#
#     def on_post(self, req: Request, res: Response):
#         media: dict = req.get_media()
#         data: dict = json.loads(media["data"])
#
#         try:
#             user_id = int(data["id"])
#             user_name = data["name"]
#         except (ValueError, KeyError):
#             res.status = falcon.HTTP_400
#             result = {"message": "bad request, fields `id` (int) and `name` (str) required"}
#         else:
#             if user_id in USERS:
#                 res.status = falcon.HTTP_400
#                 result = {"message": f"user with id #{user_id} already exists!"}
#             else:
#                 USERS[user_id] = user_name
#                 res.status = falcon.HTTP_201
#                 result = {"id": user_id, "name": user_name}
#
#         # res.text = json.dumps({"message": "ok", "media": media, "data": data})
#         # res.media = {"message": "ok", "media": media, "data": data}
#         res.media = result
#
#
# class UserDetailsResource:
#     def on_get(self, req: Request, res: Response, user_id: str):
#         logger.info("process user request with user_id=%s",user_id)
#         try:
#             user_id = int(user_id)
#             name = USERS[user_id]
#         except ValueError:
#             res.status = falcon.HTTP_400
#             result = {"message": f"not valid id {user_id!r}"}
#         except KeyError:
#             res.status = falcon.HTTP_404
#             result = {"message": f"user #{user_id!r} not found"}
#         else:
#             result = {"id": user_id, "name": name}
#
#         res.text = json.dumps(result)
#
#     def on_delete(self, req: Request, res: Response, user_id: str):
#         try:
#             user_id = int(user_id)
#             name = USERS.pop(user_id)
#         except ValueError:
#             res.status = falcon.HTTP_400
#             result = {"message": f"not valid id {user_id!r}"}
#         except KeyError:
#             res.status = falcon.HTTP_404
#             result = {"message": f"user #{user_id!r} not found"}
#         else:
#             result = {"message": f"deleted user #{user_id} with name {name!r}"}
#
#         res.text = json.dumps(result)
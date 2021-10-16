from elasticsearch import Elasticsearch


class user:
    def __init__(self, phone):
        self.phone = phone
        self.id = ''
        self.infor = ''
        self.list_page = []
        self.list_group = []
        self.list_post = []
        self.list_pageId = []
        self.list_groupId = []
    count = 0
    es = Elasticsearch("http://103.74.122.196:9200")

    def get_user(self):
        res = self.es.search(index="dsminer_user_core", body={
            "query": {
                "match_phrase": {
                    "phone": self.phone
                }
            },
        })
        self.id = res["hits"]["hits"][0]['_source']['id']

            # print("user not found")
        self.infor = res["hits"]["hits"][0]['_source']
        try:
            self.list_pageId = res["hits"]["hits"][0]['_source']["pages"]
        except KeyError:
            self.list_pageId = []
        try:
            self.list_groupId = res["hits"]["hits"][0]['_source']["groups"]
        except KeyError:
            self.list_groupId = []

    def get_infor_page(self):
        for id in self.list_pageId:
            res = self.es.search(index="dsminer_page", body={
                "query": {
                    "match_phrase": {
                        "_id": id
                    }
                },
            })
            if res["hits"]["hits"]:
                self.list_page.append(res["hits"]["hits"][0]["_source"])

    def get_infor_group(self):
        for id in self.list_groupId:
            res = self.es.search(index="dsminer_group", body={
                "query": {
                    "match_phrase": {
                        "_id": id
                    }
                },
            })
            if res["hits"]["hits"]:
                self.list_group.append(res["hits"]["hits"][0]["_source"])

    def get_post(self):
        time_sleep = 2
        body = {
            'size': 10000,
            'query': {
                'bool': {
                    'must': [
                        {'bool': {
                            'should': [
                                {'match_phrase': {'userId': self.id}},
                            ]
                        }},
                        {'match_phrase': {
                            'docType': 'user_post'
                        }}
                    ]
                }
            },
            'track_total_hits': True,
            '_source': [
                'description',
                "message"
            ]
        }
        for month in range(8, 11):
            month = f'{month:02d}'
            for i in range(1, 31):
                day = i
                day = f'{day:02d}'
                index = f'dsminer_post_2021-{month}-{day}'
                try:
                    response = self.es.search(index=index, body=body)['hits']['hits']
                except:
                    continue
                for res in response:
                    self.list_post.append(res["_source"])

    def get_all(self):
        self.get_user()
        self.get_post()
        self.get_infor_group()
        self.get_infor_page()
        user = {
            # toàn bộ thông tin người dùng trong dsminer_user_core
            "infor": self.infor,
            # toàn bộ thông tin group của user
            "infor_group": self.list_group,
            # toàn bộ thông tin page của user
            "infor_page": self.list_page,
            # toàn bộ thông tin post trong vòng 1 tháng của user
            "infor_post": self.list_post
        }
        return user

# cong = user("100008618224799")
# cong.get_all()
# user = {
#     #toàn bộ thông tin người dùng trong dsminer_user_core
#     "infor" : cong.infor,
#     #toàn bộ thông tin group của user
#     "infor_group": cong.list_group,
#     #toàn bộ thông tin page của user
#     "infor_page": cong.list_page,
#     #toàn bộ thông tin post trong vòng 1 tháng của user
#     "infor_post": cong.list_post
# }
# # with open("user.txt"  , "w" , encoding= "utf8" ) as file:
# #     for group in cong.list_group:
# #         file.write(str(group))
# #     file.write('\n')
# #     for page in cong.list_page:
# #         file.write(str(page))
# #
# #     file.write('\n')
# #     for post in cong.list_post:
# #         file.write(str(post))
# with open("user.txt", "w", encoding="utf8") as file:
#     # json.dump(cong.list_page, file , ensure_ascii=False)
#     # json.dump(cong.list_group, file ,ensure_ascii=False)
#     json.dump(user, file, ensure_ascii=False)

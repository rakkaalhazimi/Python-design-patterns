from abc import abstractmethod, ABC



class DBClient(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def search(self):
        pass


class MySQLClient(DBClient):
    def __init__(self, user, pwd, host):
        self.client = self.connect(user, pwd, host)

    def connect(self, user, pwd, host):
        print(f"{self.__class__.__name__} connected to {host}")

    def search(self, query):
        print(f"Found data for {query}")


class MongoDBClient(DBClient):
    def __init__(self, user, pwd, host):
        self.client = self.connect(user, pwd, host)

    def connect(self, user, pwd, host):
        print(f"{self.__class__.__name__} connected to {host}")

    def search(self, query):
        print(f"Found data for {query}")


class ElasticSearchClient(DBClient):
    def __init__(self, user, pwd, host):
        self.client = self.connect(user, pwd, host)

    def connect(self, user, pwd, host):
        print(f"{self.__class__.__name__} connected to {host}")

    def search(self, query):
        print(f"Found data for {query}")



if __name__ == "__main__":
    user = "rakka"
    pwd = "rakka"
    host = "localhost:8200"

    mysql_client = MySQLClient(user=user, pwd=pwd, host=host)
    mongo_client = MongoDBClient(user=user, pwd=pwd, host=host)
    elastic_client = ElasticSearchClient(user=user, pwd=pwd, host=host)
class HttpMethodException(Exception):
    pass


class HttpVersionException(Exception):
    pass


class HTTP:
    BODY_METHODS = ("POST", "PUT", "PATCH")
    AVAILABLE_METHODS = ("GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "CONNECT", "OPTIONS", "TRACE")
    AVAILABLE_VERSIONS = (1.0, 1.1, 2, 3)

    def __init__(self):
        self.method: str | None = None
        self.url: str | None = None
        self.http_version: float | None = None
        self.headers: dict | None = {}
        self.body: str | None = None

    def http_generator(self, method: str, url: str, http_version: float, headers: dict, body: any = None) -> str:
        if method not in self.AVAILABLE_METHODS:
            raise HttpMethodException(f"{method} not available methods")
        if http_version not in self.AVAILABLE_VERSIONS:
            raise HttpVersionException(f"{http_version} not available versions")
        http_string = f"{method} {url} HTTP/{http_version}\n"
        for key in headers:
            http_string += f"{key}: {headers[key]}\n"
        if body and method in self.BODY_METHODS:
            http_string += f"\n{body}"
        return http_string

    def http_parser(self, http_string: str):
        http_strings_iterator = iter(http_string.split("\n"))
        self.method, self.url, http_version = next(http_strings_iterator).split()
        self.http_version = float(http_version.strip("HTTP/"))
        for headers_string in http_strings_iterator:
            if not headers_string:
                break
            key, value = headers_string.split(": ")
            self.headers[key] = value
        else:
            return
        body_string = ""
        for body_strings in http_strings_iterator:
            body_string += body_strings
        self.body = body_string


def test_http_generator():
    http = HTTP()
    method = "POST"
    url = "https://www.youtube.com/watch?v=s9oQRKsROF8&ab_channel=capybaross"
    http_version = 1.1
    headers = {"X-SID": "asfdsafdsdfsaf"}
    body = {"asdfsadf": "sadfsadfsda"}
    return http.http_generator(method, url, http_version, headers, body)


def test_http_parser():
    http = HTTP()
    http_string = "POST https://www.youtube.com/watch?v=s9oQRKsROF8&ab_channel=capybaross HTTP/1.1\n" \
                  "X-SID: asfdsafdsdfsaf\n" \
                  '\n{"asdfsadf": "sadfsadfsda"}'
    http.http_parser(http_string)
    assert http.method == "POST"
    assert http.url == "https://www.youtube.com/watch?v=s9oQRKsROF8&ab_channel=capybaross"
    assert http.http_version == 1.1
    assert http.headers == {"X-SID": "asfdsafdsdfsaf"}
    assert http.body == '{"asdfsadf": "sadfsadfsda"}'


if __name__ == "__main__":
    print(test_http_generator())
    test_http_parser()

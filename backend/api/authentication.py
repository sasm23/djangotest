from rest_framework.authentication import TokenAuthentication as BaseTokenAUth

class TokenAuthentication(BaseTokenAUth):
    keyword= 'Bearer'
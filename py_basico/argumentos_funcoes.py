class User:

    @staticmethod
    def get_by_email(email):
        u = db.users.find_one({ 'email': email })
        if u:
            return User(**u)
        return None

    def __init__(self, *args, **kwargs):
        self.nome = kwargs.get('nome', 'Lucas')

def fn(a, b, c='Lucas', *args, **kwargs):
    print(a, b, c, args, kwargs)


fn(1, 2, 3)
fn('a', 'b', 'c')

fn(a=1, b=2, c=3)
fn(c=3, a=3, b=1)

fn(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, um=1, dois=2, tres=3)

lista = [ 1, 2, 3, 4, 5, 6 ]

fn(lista[0], lista[1], lista[2])
fn(*lista)

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 2
}

fn(**dicionario)

fn(1, 2, 2)

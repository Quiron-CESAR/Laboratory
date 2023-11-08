from pydantic import BaseModel, EmailStr
from .Role import Role
from infra.entities.users import User


class UserAuth(BaseModel):
    email: EmailStr
    password: str

class Users(UserAuth):
    '''Classe para representar Users que vêm da API'''
    nome: str 
    contato: str
    role: Role = Role.USER


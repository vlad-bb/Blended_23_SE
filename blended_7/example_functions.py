def create_user(name: str, phone: str = None, age: int = None, discount: float = None,
                is_active: bool = False) -> dict[
                                           str:str] | None:  # parameters

    return {"name": name, "phone": phone, "age": age, "discount": discount, "is_active": is_active}


def create_client(*args, **kwargs):
    user_name = args[0]
    age = kwargs["age"]
    return f"{user_name} {age}"


if __name__ == "__main__":
    user = create_client()  # args
    create_user()
    print(user)

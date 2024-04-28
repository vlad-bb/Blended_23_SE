def retry_connect(attempt=1):
    def wrapper(func):
        def inner(question):

            for i in range(attempt):
                print(f"Attempt # {i}")
                answer, status = func(question)
                if status is True:
                    return answer
                else:
                    question = answer

        return inner

    return wrapper


@retry_connect(attempt=5)
def run_chat(question=None):
    if not question:
        question = input("Ask me: ")
    answer = hash(question)  # real connect to GPT
    if answer > 0:
        print(f"Answer is positive {answer}")
        return answer, True
    else:
        print(f"Answer is negative {answer}")
        return question, False


if __name__ == "__main__":
    run_chat(question=None)

def mix_color(color_1, color_2, osnova="water", discount=False):
    print(f"{color_1=}")
    print(f"{color_2=}")
    print(f"{osnova=}")
    result = ''
    if color_1.startswith("W_") and color_2.startswith("W_") and osnova == "water":  # якщо
        if discount is True:
            result = 'W_Gray'
        else:
            result = "Not possible to mix"
    elif color_1.startswith("O_") and color_2.startswith("O_") and osnova == "oil":  # або
        result = "O_Green"
    else:  # в усіх інших випадках
        result = "Forbiden to mix"

    return result


new_color = mix_color("W_White", 'W_Black', discount=True)
# # print(f"{new_color=}")
# new_color = mix_color("O_Blue", 'O_Yellow', osnova='water')
print(f"{new_color=}")

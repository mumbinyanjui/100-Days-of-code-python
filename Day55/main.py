def validate_number(function):
    def wrapper(number):
        ran_no = random.choice(range(1, 10))
        str = function(number)
        if number < ran_no:
            return str + "<h1>Too low!</h1><br>" \
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGlmN3ZmbWN6cDFxOTEyOGducTliYm05NWtjNTdiajQxZDlqbDZqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKJkUIgrWrJdOWA/giphy.gif'" \
            " width='700' />"
        elif number > ran_no:
            return str + "<h1>Too High!</h1><br>" \
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXBlMHRmbWpjaWtrNmRiNnU0dzN0cHdxb2dpYmM5Z2N4YjJldHJoayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J3AoXNNJPXBRu/giphy.gif'" \
            " width='700' />"
        else:
            return str + "<h1>You got it!</h1><br>" \
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXFqeDlzYXgzMWJ4MW5waXhzamZrbTFwcXFzZG41MTI3d211ajR3dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYB0aJJ0hQ230WI/giphy.gif'" \
            " width='700' />"
    return wrapper


@app.route("/<int:number>")
@validate_number
def check_number(number):
    return f"<h1>Your guess is : {number}</h1>"
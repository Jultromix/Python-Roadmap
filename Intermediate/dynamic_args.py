def newsapy_client(api_key, query, timout=30, retries=3):
    return f"News API: {query} con timout {timout}"


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timout {timeout}"


def ejemplo_args(api_key, *args):
    print(f"Api_key: {api_key} de tipo {type(api_key)}")
    print(f"Argumentos dinámicos {args} de tipo {type(args)}")


ejemplo_args("p1", "p2", "p3")
ejemplo_args("p1_1", "p1_2")
# ejemplo_args()


def dinamic_adder(*args):
    """funtion to add numbers"""
    try:
        print(f" Numbers to add {args} with result {sum(args)}")
    except TypeError:
        print("tipo de dato incorrecto, operación abortada, usa solo números")


dinamic_adder(1, 1)
dinamic_adder(1, 1, 3, 4, 5, 6, 7, 8, 9)
dinamic_adder(1, "1")
dinamic_adder(1, 2.3)


def dinamic_adder_compr(*args):
    """function to add numbers conditioning its type"""
    print(
        f"Numbers to add {args} with result {
            sum([x for x in args if isinstance(x, (float, int))])
        }"
    )


dinamic_adder_compr(1, 1)
dinamic_adder_compr(1, "1")

from input_functions import read_string, read_integer_in_range


def letter_label():
    title = str(input("Please enter your title (Mr, Mrs, Ms, Miss, Dr): "))
    first_name = str(input("Please enter your first name: "))
    last_name = str(input("Please enter your last name: "))
    h_u_number = str(input("Please enter the house or unit number: "))
    street_name = str(input("Please enter the street name: "))
    suburb = str(input("Please enter the suburb: "))
    post_code = read_integer_in_range("Please enter a postcode (0000 - 9999): ", 0, 9999)
    label = f"{title} {first_name} {last_name} \n{h_u_number} {street_name} \n{suburb} {post_code}"
    return(label)

def letter_content():
    subject = str(input("Please enter your message subject line: "))
    content = str(input("Please enter your message content: "))
    message = f"\nRE: {subject}\n\n{content}"
    return(message)

def full():
    label=letter_label()
    message=letter_content()
    output=f"{label}\n{message}"
    return(output)
def main():
    print(full())
if __name__ == "__main__":
    main()
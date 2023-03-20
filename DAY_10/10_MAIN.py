# Functions with Outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #print(f"{formatted_f_name} {formatted_l_name}")
    # Becomes the OUTPUT
    return f"{formatted_f_name} {formatted_l_name}"


#format_name("JEff", "DANieLs")
formatted_string = format_name("JEff", "DANielS")
print(formatted_string)

# "Return" becomes a signal for the function to finish

import pyfiglet
import termcolor

msg = input("What would you like to print? ")
color = input("What color? ")
results = pyfiglet.figlet_format(msg)
colored_ascii = termcolor.colored(results, color=color)
print(colored_ascii)


from random import randint

output=open("output.txt","w")

stuff = [n for n in range(2,260)]
stuff.reverse()

for n in stuff:
    output.write(f"""switch(FEAT_TRAINS,SELF,SW_TEST_LIMIT_{n-1},cargo_subtype){{0:SW_TEST_LIMIT_{n};return {randint(1,100)};}}
""")

x = lambda x : f"""\n{str(x)}:SW_TEST_LIMIT_{str(x)};"""

for n in stuff:
    output.write(f"""\n{str(n-1)}:SW_TEST_LIMIT_{str(n-1)};""")
    
print(x(3))
print(x(4))
# Slut

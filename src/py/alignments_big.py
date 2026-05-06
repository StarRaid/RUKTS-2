
import contextlib
import os

output=open("output_big.txt","w")

for n in range(0,12):
    output.write(f"""

template TEMPLATE_{12-n}_8_A(x,y){{
	[x*300,		y*50,	12,	40,		-5,		{-19-2*n},	ANIM]	// NORTH
	[x*300+16,	y*50,	34,	28,		{-24+2*n},	{-15-n},	ANIM]	// NORTH EAST
	[x*300+54,	y*50,	53,	22,		{-35+4*n},	-17,	ANIM]	// EAST
	[x*300+111,	y*50,	34,	28,		-16,		-19,	ANIM]	// SOUTH EAST
	[x*300+149,	y*50,	12,	40,		-5,		-27,	ANIM]	// SOUTH
	[x*300+165,	y*50,	34,	28,		-16,	-19,	ANIM]	// SOUTH WEST
	[x*300+203,	y*50,	53,	22,		-19,	-17,	ANIM]	// WEST
	[x*300+260,	y*50,	34,	28,		{-8-2*n},		{-15-n},	ANIM]	// NORTH WEST
}}
template TEMPLATE_{12-n}_8_B(x,y){{
	[x*300+149,	y*50,	12,	40,		-5,		{-19-2*n},	ANIM]	// NORTH
	[x*300+165,	y*50,	34,	28,		{-24+2*n},	{-15-n},	ANIM]	// NORTH EAST
	[x*300+203,	y*50,	53,	22,		{-35+4*n},	-17,	ANIM]	// EAST
	[x*300+260,	y*50,	34,	28,		-16,		-19,	ANIM]	// SOUTH EAST
	[x*300,		y*50,	12,	40,		-5,		-27,	ANIM]	// SOUTH
	[x*300+16,	y*50,	34,	28,		-16,	-19,	ANIM]	// SOUTH WEST
	[x*300+54,	y*50,	53,	22,		-19,	-17,	ANIM]	// WEST
	[x*300+111,	y*50,	34,	28,		{-8-2*n},		{-15-n},	ANIM]	// NORTH WEST
}}

template TEMPLATE_{12-n}_4(x,y){{
	[x*300,		y*50,	12,	40,		-5,		{-19-2*n},	ANIM]	// NORTH
	[x*300+16,	y*50,	34,	28,		{-24+2*n},	{-15-n},	ANIM]	// NORTH EAST
	[x*300+54,	y*50,	53,	22,		{-35+4*n},	-17,	ANIM]	// EAST
	[x*300+111,	y*50,	34,	28,		-16,		-19,	ANIM]	// SOUTH EAST
	[x*300,		y*50,	12,	40,		-5,		-27,	ANIM]	// SOUTH
	[x*300+16,	y*50,	34,	28,		-16,	-19,	ANIM]	// SOUTH WEST
	[x*300+54,	y*50,	53,	22,		-19,	-17,	ANIM]	// WEST
	[x*300+111,	y*50,	34,	28,		{-8-2*n},		{-15-n},	ANIM]	// NORTH WEST
}}

""")





# Slut

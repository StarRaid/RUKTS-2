
import contextlib
import os

output=open("output.txt","w")

for n in range(0,8):
    output.write(f"""

template TEMPLATE_{8-n}_8_A(x,y){{
	[x*250,		y*40,	12,	30,		-5,		{-17-2*n},	ANIM]	// NORTH	
	[x*250+16,	y*40,	26,	24,		{-16+2*n},	{-15-n},	ANIM]	// NORTH EAST
	[x*250+46,	y*40,	37,	22,		{-19+4*n},	-17,	ANIM]	// EAST
	[x*250+87,	y*40,	26,	24,		-8,		-15,	ANIM]	// SOUTH EAST
	[x*250+117,	y*40,	12,	30,		-5,		-17,	ANIM]	// SOUTH
	[x*250+133,	y*40,	26,	24,		-16,	-15,	ANIM]	// SOUTH WEST
	[x*250+163,	y*40,	37,	22,		-19,	-17,	ANIM]	// WEST
	[x*250+204,	y*40,	26,	24,		{-8-2*n},		{-15-n},	ANIM]	// NORTH WEST
}}
template TEMPLATE_{8-n}_8_B(x,y){{
	[x*250+117,	y*40,	12,	30,		-5,		{-17-2*n},	ANIM]	// NORTH	
	[x*250+133,	y*40,	26,	24,		{-16+2*n},	{-15-n},	ANIM]	// NORTH EAST
	[x*250+163,	y*40,	37,	22,		{-19+4*n},	-17,	ANIM]	// EAST
	[x*250+204,	y*40,	26,	24,		-8,		-15,	ANIM]	// SOUTH EAST
	[x*250,		y*40,	12,	30,		-5,		-17,	ANIM]	// SOUTH
	[x*250+16,	y*40,	26,	24,		-16,	-15,	ANIM]	// SOUTH WEST
	[x*250+46,	y*40,	37,	22,		-19,	-17,	ANIM]	// WEST
	[x*250+87,	y*40,	26,	24,		{-8-2*n},		{-15-n},	ANIM]	// NORTH WEST
}}

template TEMPLATE_{8-n}_4(x,y){{
	[x*250,		y*40,	12,	30,		-5,		{-17-2*n},	ANIM]	// NORTH	
	[x*250+16,	y*40,	26,	24,		{-16+2*n},	{-15-n},	ANIM]	// NORTH EAST
	[x*250+46,	y*40,	37,	22,		{-19+4*n},	-17,	ANIM]	// EAST
	[x*250+87,	y*40,	26,	24,		-8,		-15,	ANIM]	// SOUTH EAST
	[x*250,		y*40,	12,	30,		-5,		-17,	ANIM]	// SOUTH
	[x*250+16,	y*40,	26,	24,		-16,	-15,	ANIM]	// SOUTH WEST
	[x*250+46,	y*40,	37,	22,		-19,	-17,	ANIM]	// WEST
	[x*250+87,	y*40,	26,	24,		{-8-2*n},		{-15-n},	ANIM]	// NORTH WEST
}}

""")





# Slut

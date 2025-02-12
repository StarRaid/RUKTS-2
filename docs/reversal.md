
# Problem

For the reversal behaviour to work, we're going to have to work around the 255 switch limit before GRF starts reusing them.

## Breakdown

Each vehicle currently has many, many switches for graphics. Most notably, one switch for each livery to check if the vehicle is reversed. This alone will consume most of the 255 switch limit.
Our current reversal model also adss to the number of switches as there are separate switches for normal and advanced reversal behaviours.

What if we combined all this into one switch?

# Solution

Per vehicle ID, there can be one graphics switch, or one graphics switch per sprite stack layer (for things like the 37) with the following inputs, mapped as a bitmask with three bits:

( ( Is the parent vehicle reversed ) OR ( Is the parent vehicle reversed AND does the consist meet reversal behaviour requirements ), 
( getbits function for the cargo subtype of a specific vehicle ( if ( the parent vehicle reversed AND does the consist meet reversal requirements ) : return `position_in_consist_from_end`-`position_in_consist` ; else return `position_in_consist` ) )

Bit one checks if we need to output a reversed sprite or not.
Bits two and three select the livery from the cargo subtype.

## This switch can be referenced irregardless of where the vehicle is in the consist.
- If this switch is referenced by a non-reversed vehicle of the intended ID, it will always return its non reversed sprite of the correct livery (checking its own `cargo_subtype`).
- If this switch is referenced by a reversed vehicle of the intended ID, but is not in a consist that does not meet advanced reversal behaviour requirements, it will return its reversed sprite of the correct livery (checking its own `cargo_subtype`).
- If this switch is referenced by a reversed vehicle of any ID, and is in a consist that meets advanced reversal behaviour, it will return the correct livery of the vehicles equal (checking the `cargo_subtype` of the vehicle of the equivalent position at the opposite end of the consist (`position_in_consist_from_end`-`position_in_consist`)).

The function to check if the vehicle meets reversal behaviour requirements. It returns 1 if:

- All vehicles in the consist belong to a specific reversal group (use badges or callback info).
- The front and rear most vehicles are IDs that have cabs (use badges for this?)
 
Use OR to check for multiple groups if the vehicle belongs to multiple groups.

## Limitations

- Readability; This will be impossible for a human to interpret when viewing the finished NML file, so we must put an explanation and breakdown of how and why this thing works.
- We still don't know how *Global* sound and particle effect checks will fit into this.
- Any switches that change vehicle stats will be fine as they are generally defined next to the `item` block of the vehicle.
